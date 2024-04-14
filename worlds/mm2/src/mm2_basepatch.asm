norom
!headersize = 16

!controller_mirror = $23
!controller_flip = $27 ; only on first frame of input, used by crash man, etc
!current_stage = $2A
!received_stages = $8A
!completed_stages = $8B
!received_item_checks = $8C
!last_wily = $8D
!deathlink = $8F
!energylink_packet = $90
!received_weapons = $9A
!received_items = $9B
!current_weapon = $A9

!stage_completion = $0F70
!consumable_checks = $0F80

!CONTROLLER_SELECT = #$04
!CONTROLLER_SELECT_START = #$0C
!CONTROLLER_ALL_BUTTON = #$0F

!PpuControl_2000 = $2000
!PpuMask_2001 = $2001

!LOAD_BANK = $C000

macro org(address,bank)
    if <bank> == $0F
        org <address>-$C000+($4000*<bank>)+!headersize ; org sets the position in the output file to write to (in norom, at least)
        base <address> ; base sets the position that all labels are relative to - this is necessary so labels will still start from $8000, instead of $0000 or somewhere
    else
        org <address>-$8000+($4000*<bank>)+!headersize
        base <address>
    endif
endmacro

%org($8400, $08)
incbin "mm2font.dat"

%org($A900, $09)
incbin "mm2titlefont.dat"

%org($802B, $0D)
PatchFaceTiles:
    LDA !received_stages

%org($8072, $0D)
PatchFaceSprites:
    LDA !received_stages

%org($80CC, $0D)
CheckItemsForWily:
    LDA !received_items
    CMP #$07

%org($80D2, $0D)
LoadWily:
    JSR GoToMostRecentWily
    NOP

%org($80DC, $0D)
CheckAccessCodes:
    LDA !received_stages

%org($A315, $0D)
RemoveWeaponClear:
    NOP
    NOP
    NOP
    NOP

%org($BB74, $0D)
GetEquippedStage:
    JSR StageGetEquipped
    NOP #13

%org($BCF1, $0D)
GetEquippedItem:
    ADC #$07
    JSR ItemGetEquipped
    JSR LoadItemsColor
    NOP ; !!!! This is a load-bearing NOP. It gets branched to later in the function
    LDX $FF


%org($BB08, $0D)
WilyProgress:
    JSR StoreWilyProgress
    NOP

%org($805B, $0E)
InitalizeStartingRBM:
    LDA #$FF ; this does two things
    STA !received_stages ; we're overwriting clearing e-tanks and setting RBM available to none

%org($8066, $0E)
BlockStartupAutoWily:
    ; presumably this would be called from password?
    LDA #$00

%org($80A7, $0E)
StageLoad:
    JMP CleanWily5
    NOP

%org($8178, $0E)
Main1:
    JSR MainLoopHook
    NOP

%org($81DE, $0E)
Wily5Teleporter:
    LDA $99
    CMP #$01
    BCC SkipSpawn

%org($81F9, $0E)
SkipSpawn:
; just present to fix the branch, if we try to branch raw it'll get confused

%org($822D, $0E)
Main2:
    ; believe used in the wily 5 refights?
    JSR MainLoopHook
    NOP

%org($842F, $0E)
Wily5Hook:
    JMP Wily5Requirement
    NOP

%org($C10D, $0F)
Deathlink:
    JSR KillMegaMan

%org($C1BC, $0F)
RemoveETankLoss:
    NOP
    NOP

%org($C23C, $0F)
WriteStageComplete:
    ORA !completed_stages
    STA !completed_stages

%org($C243, $0F)
WriteReceiveItem:
    ORA !received_item_checks
    STA !received_item_checks

%org($C254, $0F)
BlockAutoWily:
    ; and this one is on return from stage?
    LDA #$00

%org($C261, $0F)
WilyStageCompletion:
    JSR StoreWilyStageCompletion
    NOP

%org($E5AC, $0F)
NullDeathlink:
    STA $8F ; we null his HP later in the process
    NOP

%org($E5D1, $0F)
EnergylinkHook:
    JSR Energylink
    NOP #2 ; comment this out to enable item giving their usual reward alongside EL

%org($E5E8, $0F)
ConsumableHook:
    JSR CheckConsumable

%org($F2E3, $0F)

CheckConsumable:
    STA $0140, Y
    TXA
    PHA
    LDA $AD ; the consumable value
    CMP #$7C
    BPL .Store
    print "Consumables (replace 7a): ", hex(realbase())
    CMP #$76
    BMI .Store
    LDA #$00
    .Store:
    STA $AD
    LDA $2A
    ASL
    ASL
    TAX
    TYA
    .LoopHead:
    CMP #$08
    BMI .GetFlag
    INX
    SBC #$08
    BNE .LoopHead
    .GetFlag:
    TAY
    LDA #$01
    .Loop2Head:
    CPY #$00
    BEQ .Apply
    ASL
    DEY
    BNE .Loop2Head
    .Apply:
    ORA !consumable_checks, X
    STA !consumable_checks, X
    PLA
    TAX
    RTS

GoToMostRecentWily:
    LDA !controller_mirror
    CMP !CONTROLLER_SELECT_START
    BEQ .Default
    LDA !last_wily
    BNE .Store
    .Default:
    LDA #$08 ; wily stage 1
    .Store:
    STA !current_stage
    RTS

StoreWilyStageCompletion:
    LDA #$01
    STA !stage_completion, X
    INC !current_stage
    LDA !current_stage
    STA !last_wily
    RTS

ReturnToGameOver:
    LDA #$10
    STA !PpuControl_2000
    LDA #$06
    STA !PpuMask_2001
    JMP $C1BE ; specific code that loads game over

MainLoopHook:
    LDA !controller_mirror
    CMP !CONTROLLER_ALL_BUTTON
    BNE .Next
    JMP ReturnToGameOver
    .Next:
    LDA !deathlink
    CMP #$01
    BNE .Next2
    JMP $E5A8 ; this kills the Mega Man
    .Next2:
    print "Quickswap:", hex(realbase())
    LDA #$00 ; slot data, write in enable for quickswap
    CMP #$01
    BNE .Finally
    LDA !controller_flip
    AND !CONTROLLER_SELECT
    BEQ .Finally
    JMP Quickswap
    .Finally:
    LDA !controller_flip
    AND #$08 ; this is checking for menu
    RTS

StoreWilyProgress:
    STA !current_stage
    TXA
    PHA
    LDX !current_stage
    LDA #$01
    STA !stage_completion, X
    PLA
    TAX
    LDA #$17
    RTS

KillMegaMan:
    JSR $C051 ; this kills the mega man
    LDA #$00
    STA $06C0 ; set HP to zero so client can actually detect he died
    RTS

Wily5Requirement:
    LDA #$01
    LDX #$08
    LDY #$00
    .LoopHead:
    BIT $BC
    BEQ .Skip
    INY
    .Skip:
    DEX
    ASL
    CPX #$00
    BNE .LoopHead
    print "Wily 5 Requirement:", hex(realbase())
    CPY #$08
    BCS .SpawnTeleporter
    JMP $8450
    .SpawnTeleporter:
    LDA #$FF
    STA $BC
    LDA #$01
    STA $99
    JMP $8433

CleanWily5:
    LDA #$00
    STA $BC
    STA $99
    JMP $80AB

LoadString:
    STY $00
    ASL
    ASL
    ASL
    ASL
    TAY
    LDA $DB
    ADC #$00
    STA $C8
    LDA #$40
    STA $C9
    LDA #$F6
    CLC
    ADC $C8
    STA $CA
    LDA ($C9), Y
    STA $03B6
    TYA
    CLC
    ADC #$01
    TAY
    LDA $CA
    ADC #$00
    STA $CA
    LDA ($C9), Y
    STA $03B7
    TYA
    CLC
    ADC #$01
    TAY
    LDA $CA
    ADC #$00
    STA $CA
    STY $FE
    LDA #$0E
    STA $FD
    .LoopHead:
    JSR $BD34
    LDY $FE
    CPY #$40
    BNE .NotEqual
    LDA $0420
    BNE .Skip
    .NotEqual:
    LDA ($C9), Y
    .Skip:
    STA $03B8
    INC $47
    INC $03B7
    LDA $FE
    CLC
    ADC #$01
    STA $FE
    LDA $CA
    ADC #$00
    STA $CA
    DEC $FD
    BNE .LoopHead
    LDY $00
    JSR $C0AB
    RTS

StageGetEquipped:
    LDA !current_stage
    LDX #$00
    BCS LoadGetEquipped
ItemGetEquipped:
    LDX #$02
LoadGetEquipped:
    STX $DB
    ASL
    ASL
    PHA
    SEC
    JSR LoadString
    PLA
    ADC #$00
    PHA
    SEC
    JSR LoadString
    PLA
    ADC #$00
    PHA
    SEC
    JSR LoadString
    LDA #$00
    SEC
    JSR $BD3E
    PLA
    ADC #$00
    SEC
    JSR LoadString
    RTS

LoadItemsColor:
    LDA #$7D
    STA $FD
    LDA $0420
    AND #$0F
    ASL
    SEC
    ADC #$1A
    STA $FF
    RTS

Energylink:
    LSR $0420, X
    print "Energylink: ", hex(realbase())
    LDA #$00
    BEQ .ApplyDrop
    LDA $04E0, X
    BEQ .ApplyDrop ; This is a stage pickup, and not an enemy drop
    STY !energylink_packet
    SEC
    BCS .Return
    .ApplyDrop:
    STY $AD
    .Return:
    RTS


Quickswap:
    LDX #$0F
    .LoopHead:
    LDA $0420, X
    BMI .Return1 ; return if we have any weapon entities spawned
    DEX
    CPX #$01
    BNE .LoopHead
    LDX !current_weapon
    BNE .DoQuickswap
    LDX #$00
    .DoQuickswap:
    TYA
    PHA
    LDX !current_weapon
    INX
    CPX #$09
    BPL .Items
    LDA #$01
    .Loop2Head:
    DEX
    BEQ .FoundTarget
    ASL
    CPX #$00
    BNE .Loop2Head
    .FoundTarget:
    LDX !current_weapon
    INX
    .Loop3Head:
    PHA
    AND !received_weapons
    BNE .CanSwap
    PLA
    INX
    CPX #$09
    BPL .Items
    ASL
    BNE .Loop3Head
    .CanSwap:
    PLA
    SEC
    BCS .ApplySwap
    .Items:
    TXA
    PHA
    SEC
    SBC #$08
    TAX
    LDA #$01
    .Loop4Head:
    DEX
    BEQ .CheckItem
    ASL
    CPX #$00
    BNE .Loop4Head
    .CheckItem:
    TAY
    PLA
    TAX
    TYA
    .Loop5Head:
    PHA
    AND !received_items
    BNE .CanSwap
    PLA
    INX
    ASL
    BNE .Loop5Head
    LDX #$00
    SEC
    BCS .ApplySwap
    .Return1:
    RTS
    .ApplySwap: ; $F408 on old rom
    LDA #$0D
    JSR !LOAD_BANK
    ; this is a bunch of boiler plate to make the swap work
    LDA $B5
    PHA
    LDA $B6
    PHA
    LDA $B7
    PHA
    LDA $B8
    PHA
    LDA $B9
    PHA
    LDA $20
    PHA
    LDA $1F
    PHA
    ;but wait, there's more
    STX !current_weapon
    JSR $CC6C
    LDA $1A
    PHA
    LDX #$00
    .Loop6Head:
    STX $FD
    CLC
    LDA $52
    ADC $957F, X
    STA $08
    LDA $53
    ADC #$00
    STA $09
    LDA $08
    LSR $09
    ROR
    LSR $09
    ROR
    STA $08
    AND #$3F
    STA $1A
    CLC
    LDA $09
    ADC #$85
    STA $09
    LDA #$00
    STA $1B
    LDA $FD
    CMP #$08
    BCS .Past8
    LDX $A9
    LDA $9664, X
    TAY
    CPX #$09
    BCC .LessThanNine
    LDX #$00
    BEQ .Apply
    .LessThanNine:
    LDX #$05
    BNE .Apply
    .Past8:
    LDY #$90
    LDX #$00
    .Apply:
    JSR $C760
    JSR $C0AB ; iirc this is loading graphics?
    LDX $FD
    INX
    CPX #$0F
    BNE .Loop6Head
    STX $FD
    LDY #$90
    LDX #$00
    JSR $C760
    JSR $D2ED
    ; two sections redacted here, might need to look at what they actually do?
    PLA
    STA $1A
    PLA
    STA $1F
    PLA
    STA $20
    PLA
    STA $B9
    PLA
    STA $B8
    PLA
    STA $B7
    PLA
    STA $B6
    PLA
    STA $B5
    LDA #$00
    STA $AC
    STA $2C
    STA $0680
    STA $06A0
    LDA #$1A
    STA $0400
    LDA #$03
    STA $AA
    LDA #$30
    JSR $C051
    .Finally:
    LDA #$0E
    JSR !LOAD_BANK
    PLA
    TAY
    .Return:
    RTS

assert realbase() <= $03F650 ; This is the start of our text data, and we absolutely cannot go past this point (text takes too much room).

%org($F640, $0F)
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"
db $25, $4B, "PLACEHOLDER_L1"
db $25, $6B, "PLACEHOLDER_L2"
db $25, $8B, "PLACEHOLDER_L3"
db $25, $EB, "PLACEHOLDER_PL"

%org($FFB0, $0F)
db "MM2_BASEPATCH_ARCHI "