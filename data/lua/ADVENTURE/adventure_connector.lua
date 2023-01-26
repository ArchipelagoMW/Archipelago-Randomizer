local socket = require("socket")
local json = require('json')
local math = require('math')

local STATE_OK = "Ok"
local STATE_TENTATIVELY_CONNECTED = "Tentatively Connected"
local STATE_INITIAL_CONNECTION_MADE = "Initial Connection Made"
local STATE_UNINITIALIZED = "Uninitialized"

local SCRIPT_VERSION = 1

local APItemValue = 0xA2
local APItemRam = 0xE7
local PlayerRoomAddr = 0x8A -- if in number room, we're not in play mode
local WinAddr = 0xDE -- if not 0 (I think if 0xff specifically), we won (and should update once, immediately)

-- If any of these are 2, that dragon ate the player (should send update immediately
-- once, and reset that when none of them are 2 again)

local DragonState = {0xA8, 0xAD, 0xB2}
local carryAddress = 0x9D

local nullObjectId = 0xAD
local ItemsReceived = nil
local sha256hash = nil
-- TODO: See how best to handle storage of collected foreign items, and resetting that after a restart/reload/whatever
local foreign_items = nil
local foreign_items_by_room = {}

local prev_player_room = 0
local prev_ap_room_index = nil

local pending_foreign_items_collected = {}
local rendering_foreign_item = nil

local inventory = {}
local next_inventory_item = nil

local input_button_address = 0xD7

local deathlink_rec = nil
local deathlink_send = false

local prevstate = ""
local curstate =  STATE_UNINITIALIZED
local atariSocket = nil
local frame = 0

local ItemIndex = 0

local u8 = nil
local wU8 = nil
local u16



u8 = memory.read_u8
wU8 = memory.write_u8
u16 = memory.read_u16_le
function uRangeRam(address, bytes)
	data = memory.read_bytes_as_array(address, bytes, "Main RAM")
	return data
end
function uRangeRom(address, bytes)
	data = memory.read_bytes_as_array(address+0xf000, bytes, "System Bus")
	return data
end
function uRangeAddress(address, bytes)
	data = memory.read_bytes_as_array(address, bytes, "System Bus")
	return data
end


function table.empty (self)
    for _, _ in pairs(self) do
        return false
    end
    return true
end

function slice (tbl, s, e)
    local pos, new = 1, {}
    for i = s + 1, e do
        new[pos] = tbl[i]
        pos = pos + 1
    end
    return new
end

function processBlock(block)
    if block == nil then
        return
    end
    local block_identified = 0
    local itemsBlock = block["items"]
    if itemsBlock ~= nil then
        block_identified = 1
	    ItemsReceived = itemsBlock
    end
   local apItemsBlock = block["foreign_items"]
   if apItemsBlock ~= nil then
        block_identified = 1
        print("got foreign items block")
        foreign_items = apItemsBlock
        for _, foreign_item in ipairs(foreign_items) do
            if foreign_items_by_room[foreign_item.room_id] == nil then
                foreign_items_by_room[foreign_item.room_id] = {}
            end
            table.insert(foreign_items_by_room[foreign_item.room_id], foreign_item)
        end
        print("foreign item table")
        print(foreign_items_by_room)
   end
   deathlink_rec = block["deathlink"]
   if( block_identified == 0 ) then
      print("unidentified block")
      print(block)
   end
end

function difference(a, b)
    local aa = {}
    for k,v in pairs(a) do aa[v]=true end
    for k,v in pairs(b) do aa[v]=nil end
    local ret = {}
    local n = 0
    for k,v in pairs(a) do
        if aa[v] then n=n+1 ret[n]=v end
    end
    return ret
end

function getAllRam()
    uRangeRAM(0,128);
    return data
end

local function arrayEqual(a1, a2)
  if #a1 ~= #a2 then
    return false
  end

  for i, v in ipairs(a1) do
    if v ~= a2[i] then
      return false
    end
  end

  return true
end

local function alive_mode()
    return (u8(PlayerRoomAddr) ~= 0x00 and u8(WinAddr) == 0x00)
end

local function generateLocationsChecked()
    list_of_locations = {}
    for s, f in pairs(pending_foreign_items_collected) do
        table.insert(list_of_locations, f.short_location_id + 118000000)
    end
    return list_of_locations
end

function receive()
    l, e = atariSocket:receive()
    if e == 'closed' then
        if curstate == STATE_OK then
            print("Connection closed")
        end
        curstate = STATE_UNINITIALIZED
        return
    elseif e == 'timeout' then
        return
    elseif e ~= nil then
        print(e)
        curstate = STATE_UNINITIALIZED
        return
    end
    if l ~= nil then
        processBlock(json.decode(l))
    end
    -- Determine Message to send back

    newSha256 = memory.hash_region(0xF000, 0x1000, "System Bus")
    if (sha256hash ~= nil and sha256hash ~= newSha256) then
        print("ROM changed, quitting")
        curstate = STATE_UNINITIALIZED
        return
    end
    sha256hash = newSha256
    local retTable = {}
    retTable["scriptVersion"] = SCRIPT_VERSION
    retTable["romhash"] = sha256hash
    if alive_mode() then
        retTable["locations"] = generateLocationsChecked()
    end
    retTable["deathLink"] = deathlink_send
    deathlink_send = false
    msg = json.encode(retTable).."\n"
    local ret, error = atariSocket:send(msg)
    if ret == nil then
        print(error)
    elseif curstate == STATE_INITIAL_CONNECTION_MADE then
        curstate = STATE_TENTATIVELY_CONNECTED
    elseif curstate == STATE_TENTATIVELY_CONNECTED then
        print("Connected!")
        curstate = STATE_OK
    end
end

function main()
    memory.usememorydomain("System Bus")
    if (is23Or24Or25 or is26To28) == false then
        print("Must use a version of bizhawk 2.3.1 or higher")
        return
    end
    server, error = socket.bind('localhost', 17242)

    while true do
        frame = frame + 1
        if not (curstate == prevstate) then
            print("Current state: "..curstate)
            prevstate = curstate
        end
        if (alive_mode()) then
            local current_player_room = u8(PlayerRoomAddr)
            if (current_player_room ~= prev_player_room) then
                print("Room change "..current_player_room)
                memory.write_u8(APItemRam, 0xFF, "System Bus")
                prev_ap_room_index = 0
                prev_player_room = current_player_room
            end
            local carry_item = memory.read_u8(carryAddress, "System Bus")
            if (next_inventory_item ~= nil) then
                if ( carry_item == nullObjectId ) then
                    local input_value = memory.read_u8(input_button_address, "System Bus")
                    if( input_value >= 64 and input_value < 128 ) then -- high bit clear, second highest bit set
                        memory.write_u8(carryAddress, next_inventory_item)
                    end
                end
            end
            if( carry_item == APItemValue and rendering_foreign_item ~= nil ) then
                print("detected carry item")
                memory.write_u8(carryAddress, nullObjectId, "System Bus")
                memory.write_u8(APItemRam, 0xFF, "System Bus")
                pending_foreign_items_collected[rendering_foreign_item.short_location_id] = rendering_foreign_item
                for index, fi in pairs(foreign_items_by_room[rendering_foreign_item.room_id]) do
                    if( fi.short_location_id == rendering_foreign_item.short_location_id ) then
                        table.remove(foreign_items_by_room[rendering_foreign_item.room_id], index)
                        break
                    end
                end
            end

            rendering_foreign_item = nil
            if( foreign_items_by_room[current_player_room] ~= nil ) then
                if( foreign_items_by_room[current_player_room][prev_ap_room_index] ~= nil ) then
                    foreign_items_by_room[current_player_room][prev_ap_room_index].room_x = memory.read_u8(APItemRam + 1)
                    foreign_items_by_room[current_player_room][prev_ap_room_index].room_y = memory.read_u8(APItemRam + 2)
                end
                prev_ap_room_index = prev_ap_room_index + 1
                if( foreign_items_by_room[current_player_room][prev_ap_room_index] == nil ) then
                    prev_ap_room_index = 1
                end
                if( foreign_items_by_room[current_player_room][prev_ap_room_index] ~= nil ) then
                    memory.write_u8(APItemRam, current_player_room)
                    rendering_foreign_item = foreign_items_by_room[current_player_room][prev_ap_room_index]
                    memory.write_u8(APItemRam + 1, rendering_foreign_item.room_x)
                    memory.write_u8(APItemRam + 2, rendering_foreign_item.room_y)
                else
                    memory.write_u8(APItemRam, 0xFF, "System Bus")
                end
            end
        end
        if (curstate == STATE_OK) or (curstate == STATE_INITIAL_CONNECTION_MADE) or (curstate == STATE_TENTATIVELY_CONNECTED) then
            if (frame % 5 == 0) then
                receive()
                if alive_mode() then
                    --if deathlink_rec == true then
                    --    wU8(APDeathLinkAddress, 1)
                    --elseif u8(APDeathLinkAddress) == 3 then
                    --    wU8(APDeathLinkAddress, 0)
                    --    deathlink_send = true
                    --end
                    if ItemsReceived[ItemIndex + 1] ~= nil then
                        local static_id = ItemsReceived[ItemIndex + 1] - 118000000
                        inventory[static_id] = 1
                        if next_inventory_item == nil then
                            next_inventory_item = static_id
                        end
                    end
                end
            end
        elseif (curstate == STATE_UNINITIALIZED) then
            if  (frame % 60 == 0) then

                print("Waiting for client.")

                emu.frameadvance()
                server:settimeout(2)
                print("Attempting to connect")
                local client, timeout = server:accept()
                if timeout == nil then
                    curstate = STATE_INITIAL_CONNECTION_MADE
                    atariSocket = client
                    atariSocket:settimeout(0)
                end
            end
        end
        emu.frameadvance()
    end
end

main()
