import typing

from BaseClasses import Item
from .Names import ItemName


class KH2Item(Item):
    game: str = "Kingdom Hearts 2"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
   
    kh2id: int
    #Save+ mem addr
    memaddr: int
    #some items have bitmasks. if bitmask>0 bitor to give item else 
    #if kh2id is > than everything before it and < everything after than use write short
    #OR include a boolean
    bitmask: int = 0
    quantity: int = 1
    #if ability then 
    ability: bool = False
    event: bool = False


Reports_Table = {
    ItemName.SecretAnsemsReport1:  		ItemData(0x1320004,  226, 0x36C4 ,6),
    ItemName.SecretAnsemsReport2:  		ItemData(0x1320005,  227, 0x36C4 ,7),
    ItemName.SecretAnsemsReport3:  		ItemData(0x1320006,  228, 0x36C5 ,1),
    ItemName.SecretAnsemsReport4:  		ItemData(0x1320007,  229, 0x36C5 ,2),
    ItemName.SecretAnsemsReport5:  		ItemData(0x1320008,  230, 0x36C5 ,4),
    ItemName.SecretAnsemsReport6:  		ItemData(0x1320009,  231, 0x36C5 ,3),
    ItemName.SecretAnsemsReport7:  		ItemData(0x132000A,  232, 0x36C5 ,4),
    ItemName.SecretAnsemsReport8:  		ItemData(0x132000B,  233, 0x36C5 ,5),
    ItemName.SecretAnsemsReport9:  		ItemData(0x132000C,  234, 0x36C5 ,6),
    ItemName.SecretAnsemsReport10: 		ItemData(0x132000D,  235,0x36C5  ,7),
    ItemName.SecretAnsemsReport11: 		ItemData(0x132000E,  236, 0x36C6 ,0),
    ItemName.SecretAnsemsReport12: 		ItemData(0x132000F,  237, 0x36C6 ,1),
    ItemName.SecretAnsemsReport13: 		ItemData(0x1320010,  238, 0x36C6 ,2),
}

Progression_Table = {
    ItemName.ProofofConnection:     	ItemData(0x1320011,  593, 0x36B0 ),
    ItemName.ProofofNonexistence:   	ItemData(0x1320012,  594, 0x36B3 ),
    ItemName.ProofofPeace:          	ItemData(0x1320013,  595, 0x36B4 ),
    ItemName.PromiseCharm:          	ItemData(0x1320014,  524, 0x3694 ),
    ItemName.NamineSketches:        	ItemData(0x1320015,  368, 0x3642 ),
    #dummy 13
    ItemName.CastleKey:             	ItemData(0x1320016,  460, 0x365D ),
    ItemName.BattlefieldsofWar:     	ItemData(0x1320017,  54, 0x35AE ),
    ItemName.SwordoftheAncestor:    	ItemData(0x1320018,  55, 0x35AF ),
    ItemName.BeastsClaw:            	ItemData(0x1320019,  59, 0x35B3 ),
    ItemName.BoneFist:              	ItemData(0x132001A,  60, 0x35B4 ),
    ItemName.ProudFang:             	ItemData(0x132001B,  61, 0x35B5 ),
    ItemName.SkillandCrossbones:    	ItemData(0x132001C,  62, 0x35B6 ),
    ItemName.Scimitar:              	ItemData(0x132001E,  72, 0x35C0 ),
    ItemName.MembershipCard:        	ItemData(0x132001D,  369, 0x3643 ),
    ItemName.IceCream:              	ItemData(0x132001F,  375, 0x3649 ),
    ItemName.Picture:           		ItemData(0x1320020,  376, 0x364A ),
    ItemName.WaytotheDawn: 				ItemData(0x1320021,  73, 0x35C1 ),
    ItemName.IdentityDisk: 				ItemData(0x1320022,  74, 0x35C2 ),
    ItemName.Poster: 				    ItemData(0x1320023,  366, 0x3640 ),
    #This only needs to be one tornpage
    ItemName.TornPages: 				ItemData(0x1320024,  32, 0x3598),

}
Forms_Table = {
    ItemName.ValorForm: 				ItemData(0x1320025,  26, 0x36C0,1),
    ItemName.WisdomForm: 				ItemData(0x1320026,  27, 0x36C0,2),
    ItemName.LimitForm: 				ItemData(0x1320027,  563,0x36CA,3),
    ItemName.MasterForm: 				ItemData(0x1320028,  31, 0x36C0,6),
    ItemName.FinalForm: 				ItemData(0x1320029,  29, 0x36C0,4),
}
Magic_Table = {
    ItemName.FireElement: 				    ItemData(0x132002A,  21, 0x3594),
    ItemName.BlizzardElement: 				ItemData(0x132002B,  22, 0x3595),
    ItemName.ThunderElement: 				ItemData(0x132002C,  23, 0x3596),
    ItemName.CureElement: 				    ItemData(0x132002D,  24, 0x3597),
    ItemName.MagnetElement: 				ItemData(0x132002E,  87, 0x35CF),
    ItemName.ReflectElement: 				ItemData(0x132002F,  88, 0x35D0),
    ItemName.Genie: 				        ItemData(0x1320030,  159, 0x36C4,4),
    ItemName.PeterPan: 				        ItemData(0x1320031,  160, 0x36C4,5),
    ItemName.Stitch: 				        ItemData(0x1320032,  25, 0x36C0,0),
    ItemName.ChickenLittle: 				ItemData(0x1320033,  383, 0x36C0,3),
}                                                    
                                                     
Movement_Table = {                                   
    #        const int ADDRESS_START = 0x2544;       
    #        const int ADDRESS_END = 0x25CC;
    #kh2.write_short(kh2.base_address + Save+ADDRESS_END, 0x05E)
    #For each abilit sent to sora -2 from address_end
    ItemName.HighJump: 				    ItemData(0x1320034,  94,  0x05E,0,1,True),
    ItemName.HighJump2: 				ItemData(0x1320035,  95,  0x05E,0,1,True),
    ItemName.HighJump3: 				ItemData(0x1320036,  96,  0x05E,0,1,True),
    ItemName.HighJump4: 				ItemData(0x1320037,  97,  0x05E,0,1,True),
                                                                        
    ItemName.QuickRun: 				    ItemData(0x1320038,  98,  0x062,0,1,True),
    ItemName.QuickRun2: 				ItemData(0x1320039,  99,  0x062,0,1,True),
    ItemName.QuickRun3: 				ItemData(0x132003A,  100, 0x062,0,1,True),
    ItemName.QuickRun4: 				ItemData(0x132003B,  101, 0x062,0,1,True),
                                                                        
    ItemName.AerialDodge: 				ItemData(0x132003C,  102, 0x066,0,1,True),
    ItemName.AerialDodge2: 				ItemData(0x132003D,  103, 0x066,0,1,True),
    ItemName.AerialDodge3: 				ItemData(0x132003E,  104, 0x066,0,1,True),
    ItemName.AerialDodge4: 				ItemData(0x132003F,  105, 0x066,0,1,True),
                                                                        
    ItemName.Glide: 				    ItemData(0x1320040,  106, 0x06A,0,1,True),
    ItemName.Glide2: 				    ItemData(0x1320041,  107, 0x06A,0,1,True),
    ItemName.Glide3: 				    ItemData(0x1320042,  108, 0x06A,0,1,True),
    ItemName.Glide4: 				    ItemData(0x1320043,  109, 0x06A,0,1,True),
                                                                        
    ItemName.DodgeRoll: 				ItemData(0x1320044,  564, 0x234,0,1,True ),
    ItemName.DodgeRoll2: 				ItemData(0x1320045,  565, 0x234,0,1,True ),
    ItemName.DodgeRoll3: 				ItemData(0x1320046,  566, 0x234,0,1,True ),
    ItemName.DodgeRoll4: 				ItemData(0x1320047,  567, 0x234,0,1,True ),
}

Keyblade_Table = {
    ItemName.Oathkeeper: 				ItemData(0x1320048,  42,  0x35A2),
    ItemName.Oblivion: 				    ItemData(0x1320049,  43,  0x35A3),
    ItemName.StarSeeker: 				ItemData(0x132004A,  480, 0x367B ),
    ItemName.HiddenDragon: 				ItemData(0x132004B,  481, 0x367C ),
    ItemName.HerosCrest: 				ItemData(0x132004C,  484, 0x367F ),
    ItemName.Monochrome: 				ItemData(0x132004D,  485, 0x3680 ),
    ItemName.FollowtheWind: 			ItemData(0x132004E,  486, 0x3681 ),
    ItemName.CircleofLife: 				ItemData(0x132004F,  487, 0x3682 ),
    ItemName.PhotonDebugger: 			ItemData(0x1320050,  488, 0x3683 ),
    ItemName.GullWing: 				    ItemData(0x1320051,  489, 0x3684 ),
    ItemName.RumblingRose: 				ItemData(0x1320052,  490, 0x3685 ),
    ItemName.GuardianSoul: 				ItemData(0x1320053,  491, 0x3686 ),
    ItemName.WishingLamp: 				ItemData(0x1320054,  492, 0x3687 ),
    ItemName.DecisivePumpkin: 			ItemData(0x1320055,  493, 0x3688 ),
    ItemName.SleepingLion: 				ItemData(0x1320056,  494, 0x3689 ),
    ItemName.SweetMemories: 			ItemData(0x1320057,  495, 0x368A ),
    ItemName.MysteriousAbyss: 			ItemData(0x1320058,  496, 0x368B ),
    ItemName.TwoBecomeOne: 				ItemData(0x1320059,  543, 0x3698 ),
    ItemName.FatalCrest: 				ItemData(0x132005A,  497, 0x368C ),
    ItemName.BondofFlame: 				ItemData(0x132005B,  498, 0x368D ),
    ItemName.Fenrir: 				    ItemData(0x132005C,  499, 0x368E ),
    ItemName.UltimaWeapon: 				ItemData(0x132005D,  500, 0x368F ),
    ItemName.WinnersProof: 				ItemData(0x132005E,  544, 0x3699 ),
    ItemName.Pureblood: 				ItemData(0x132005F,  71,  0x35BF ),
}
Staffs_Table = {
    ItemName.Centurion2: 				ItemData(0x1320060,  546, 0x369B ),
    ItemName.MeteorStaff: 				ItemData(0x1320061,  150, 0x35F1 ),
    ItemName.NobodyLance: 				ItemData(0x1320062,  155, 0x35F6 ),
    ItemName.PreciousMushroom: 			ItemData(0x1320063,  549, 0x369E ),
    ItemName.PreciousMushroom2: 		ItemData(0x1320064,  550, 0x369F ),
    ItemName.PremiumMushroom: 			ItemData(0x1320065,  551, 0x36A0 ),
    ItemName.RisingDragon: 				ItemData(0x1320066,  154, 0x35F5 ),
    ItemName.SaveTheQueen2: 			ItemData(0x1320067,  503, 0x3692 ),
    ItemName.ShamansRelic: 				ItemData(0x1320068,  156, 0x35F7 ),
}                                                
Shields_Table = {                                
    ItemName.AkashicRecord: 			ItemData(0x1320069,  146, 0x35ED ),
    ItemName.FrozenPride2: 				ItemData(0x132006A,  553, 0x36A2 ),
    ItemName.GenjiShield: 				ItemData(0x132006B,  145, 0x35EC ),
    ItemName.MajesticMushroom: 			ItemData(0x132006C,  556, 0x36A5 ),
    ItemName.MajesticMushroom2: 		ItemData(0x132006D,  557, 0x36A6 ),
    ItemName.NobodyGuard: 				ItemData(0x132006E,  147, 0x35EE ),
    ItemName.OgreShield: 				ItemData(0x132006F,  141, 0x35E8 ),
    ItemName.SaveTheKing2: 				ItemData(0x1320070,  504, 0x3693 ),
    ItemName.UltimateMushroom: 			ItemData(0x1320071,  558, 0x36A7 ),
}                                                                          
Accessory_Table = {                                                        
    ItemName.AbilityRing: 				ItemData(0x1320072,  8, 0x3587 ),  
    ItemName.EngineersRing: 			ItemData(0x1320073,  9, 0x3588 ),  
    ItemName.TechniciansRing: 			ItemData(0x1320074,  10, 0x3589 ), 
    ItemName.SkillRing: 				ItemData(0x1320075,  38, 0x359F ), 
    ItemName.SkillfulRing: 				ItemData(0x1320076,  39, 0x35A0 ), 
    ItemName.ExpertsRing: 				ItemData(0x1320077,  11, 0x358A ), 
    ItemName.MastersRing: 				ItemData(0x1320078,  34, 0x359B ),
    ItemName.CosmicRing: 				ItemData(0x1320079,  52, 0x35AD ),
    ItemName.ExecutivesRing: 			ItemData(0x132007A,  599, 0x36B5 ),
    ItemName.SardonyxRing: 				ItemData(0x132007B,  12, 0x358B ),
    ItemName.TourmalineRing: 			ItemData(0x132007C,  13, 0x358C ),
    ItemName.AquamarineRing: 			ItemData(0x132007D,  14, 0x358D ),
    ItemName.GarnetRing: 				ItemData(0x132007E,  15, 0x358E ),
    ItemName.DiamondRing: 				ItemData(0x132007F,  16, 0x358F ),
    ItemName.SilverRing: 				ItemData(0x1320080,  17, 0x3590 ),
    ItemName.GoldRing: 				    ItemData(0x1320081,  18, 0x3591 ),
    ItemName.PlatinumRing: 				ItemData(0x1320082,  19, 0x3592 ),
    ItemName.MythrilRing: 				ItemData(0x1320083,  20, 0x3593 ),
    ItemName.OrichalcumRing: 			ItemData(0x1320084,  28, 0x359A ),
    ItemName.SoldierEarring: 			ItemData(0x1320085,  40, 0x35A6 ),
    ItemName.FencerEarring: 			ItemData(0x1320086,  46, 0x35A7 ),
    ItemName.MageEarring: 				ItemData(0x1320087,  47, 0x35A8 ),
    ItemName.SlayerEarring: 			ItemData(0x1320088,  48, 0x35AC ),
    ItemName.Medal: 				    ItemData(0x1320089,  53, 0x35B2 ),
    ItemName.MoonAmulet: 				ItemData(0x132008A,  35, 0x359C ),
    ItemName.StarCharm: 				ItemData(0x132008B,  36, 0x359E ),
    ItemName.CosmicArts: 				ItemData(0x132008C,  56, 0x35B1 ),
    ItemName.ShadowArchive: 			ItemData(0x132008D,  57, 0x35B2 ),
    ItemName.ShadowArchive2: 			ItemData(0x132008E,  58, 0x35B7 ),
    ItemName.FullBloom: 				ItemData(0x132008F,  64, 0x35B9 ),
    ItemName.FullBloom2: 				ItemData(0x1320090,  66, 0x35BB ),
    ItemName.DrawRing: 				    ItemData(0x1320091,  65, 0x35BA ),
    ItemName.LuckyRing: 				ItemData(0x1320092,  63, 0x35B8 ),
}
Armor_Table = {
    ItemName.ElvenBandana: 				ItemData(0x1320093,  67, 0x35BC ),
    ItemName.DivineBandana: 			ItemData(0x1320094,  68, 0x35BD ),
    ItemName.ProtectBelt: 				ItemData(0x1320095,  78, 0x35C7 ),
    ItemName.GaiaBelt: 				    ItemData(0x1320096,  79, 0x35CA ),
    ItemName.PowerBand: 				ItemData(0x1320097,  69, 0x35BE ),
    ItemName.BusterBand: 				ItemData(0x1320098,  70, 0x35C6 ),
    ItemName.CosmicBelt: 				ItemData(0x1320099,  111, 0x35D1 ),
    ItemName.FireBangle: 				ItemData(0x132009A,  173, 0x35D7 ),
    ItemName.FiraBangle: 				ItemData(0x132009B,  174, 0x35D8 ),
    ItemName.FiragaBangle: 				ItemData(0x132009C,  197, 0x35D9 ),
    ItemName.FiragunBangle: 			ItemData(0x132009D,  284, 0x35DA ),
    ItemName.BlizzardArmlet: 			ItemData(0x132009E,  286, 0x35DC ),
    ItemName.BlizzaraArmlet: 			ItemData(0x132009F,  287, 0x35DD ),
    ItemName.BlizzagaArmlet: 			ItemData(0x13200A0,  288, 0x35DE ),
    ItemName.BlizzagunArmlet: 			ItemData(0x13200A1,  289, 0x35DF ),
    ItemName.ThunderTrinket: 			ItemData(0x13200A2,  291, 0x35E2 ),
    ItemName.ThundaraTrinket: 			ItemData(0x13200A3,  292, 0x35E3 ),
    ItemName.ThundagaTrinket: 			ItemData(0x13200A4,  293, 0x35E4 ),
    ItemName.ThundagunTrinket: 			ItemData(0x13200A5,  294, 0x35E5 ),
    ItemName.ShockCharm: 				ItemData(0x13200A6,  132, 0x35D2 ),
    ItemName.ShockCharm2: 				ItemData(0x13200A7,  133, 0x35D3 ),
    ItemName.ShadowAnklet: 				ItemData(0x13200A8,  296, 0x35F9 ),
    ItemName.DarkAnklet: 				ItemData(0x13200A9,  297, 0x35FB ),
    ItemName.MidnightAnklet: 			ItemData(0x13200AA,  298, 0x35FC ),
    ItemName.ChaosAnklet: 				ItemData(0x13200AB,  299, 0x35FD ),
    ItemName.ChampionBelt: 				ItemData(0x13200AC,  305, 0x3603 ),
    ItemName.AbasChain: 				ItemData(0x13200AD,  301, 0x35FF ),
    ItemName.AegisChain: 				ItemData(0x13200AE,  302, 0x3600 ),
    ItemName.Acrisius: 				    ItemData(0x13200AF,  303, 0x3601 ),
    ItemName.Acrisius2: 				ItemData(0x13200B0,  307, 0x3605 ),
    ItemName.CosmicChain: 				ItemData(0x13200B1,  308, 0x3606 ),
    ItemName.PetiteRibbon: 				ItemData(0x13200B2,  306, 0x3604 ),
    ItemName.Ribbon: 				    ItemData(0x13200B3,  304, 0x3602 ),
    ItemName.GrandRibbon: 				ItemData(0x13200B4,  157, 0x35D4 ),
}
Usefull_Table = {
    ItemName.MickyMunnyPouch : 			ItemData(0x13200B5,  535, 0x3695 ),
    ItemName.OletteMunnyPouch : 		ItemData(0x13200B6,  362, 0x363C ),
    ItemName.HadesCupTrophy: 			ItemData(0x13200B7,  537, 0x3696 ),
    ItemName.UnknownDisk: 				ItemData(0x13200B8,  462, 0x365F ),
    ItemName.OlympusStone: 				ItemData(0x13200B9,  370, 0x3644 ),
    ItemName.MaxHPUp: 				    ItemData(0x13200BA,  470, 0x3671 ),
    ItemName.MaxMPUp: 				    ItemData(0x13200BB,  471, 0x3672 ),
    ItemName.DriveGaugeUp: 				ItemData(0x13200BC,  472, 0x3673 ),
    ItemName.ArmorSlotUp: 				ItemData(0x13200BD,  473, 0x3674 ),
    ItemName.AccessorySlotUp: 			ItemData(0x13200BE,  474, 0x3675 ),
    ItemName.ItemSlotUp: 				ItemData(0x13200BF,  463, 0x3660 ),
}
SupportAbility_Table = {
    ItemName.Scan: 				        ItemData(0x13200C0,  138, 0x08A ,0,1,True),
    ItemName.Scan2: 				    ItemData(0x13200C1,  138, 0x08A ,0,1,True),
    ItemName.AerialRecovery: 			ItemData(0x13200C2,  158, 0x09E ,0,1,True),
    ItemName.ComboMaster: 				ItemData(0x13200C3,  539, 0x21B ,0,1,True),
    ItemName.ComboPlus: 				ItemData(0x13200C4,  162, 0x0A2 ,0,1,True),
    ItemName.ComboPlus2: 				ItemData(0x13200C5,  162, 0x0A2 ,0,1,True),
    ItemName.ComboPlus3: 				ItemData(0x13200C6,  162, 0x0A2 ,0,1,True),
    ItemName.AirComboPlus: 				ItemData(0x13200C7,  163, 0x0A3 ,0,1,True),
    ItemName.AirComboPlus2: 			ItemData(0x13200C8,  163, 0x0A3 ,0,1,True),
    ItemName.AirComboPlus3: 			ItemData(0x13200C9,  163, 0x0A3 ,0,1,True),
    ItemName.ComboBoost: 				ItemData(0x13200CA,  390, 0x186 ,0,1,True),
    ItemName.AirComboBoost: 			ItemData(0x13200CB,  391, 0x187 ,0,1,True),
    ItemName.ReactionBoost: 			ItemData(0x13200CC,  392, 0x188 ,0,1,True),
    ItemName.ReactionBoost2: 			ItemData(0x13200CD,  392, 0x188 ,0,1,True),
    ItemName.FinishingPlus: 			ItemData(0x13200CE,  393, 0x189 ,0,1,True),
    ItemName.FinishingPlus2: 			ItemData(0x13200CF,  393, 0x189 ,0,1,True),
    ItemName.NegativeCombo: 			ItemData(0x13200D0,  394, 0x18A ,0,1,True),
    ItemName.BerserkCharge: 			ItemData(0x13200D1,  395, 0x18B ,0,1,True),
    ItemName.DamageDrive: 				ItemData(0x13200D2,  396, 0x18C ,0,1,True),
    ItemName.DriveBoost: 				ItemData(0x13200D3,  397, 0x18D ,0,1,True),
    ItemName.FormBoost: 				ItemData(0x13200D4,  398, 0x18E ,0,1,True),
    ItemName.FormBoost2: 				ItemData(0x13200D5,  398, 0x18E ,0,1,True),
    ItemName.FormBoost3: 				ItemData(0x13200D6,  398, 0x18E ,0,1,True),
    ItemName.SummonBoost: 				ItemData(0x13200D7,  399, 0x18F ,0,1,True),
    ItemName.ExperienceBoost: 			ItemData(0x13200D8,  401, 0x191 ,0,1,True),
    ItemName.Draw: 				        ItemData(0x13200D9,  405, 0x195 ,0,1,True),
    ItemName.Draw2: 				    ItemData(0x13200DA,  405, 0x195 ,0,1,True),
    ItemName.Draw3: 				    ItemData(0x13200DB,  405, 0x195 ,0,1,True),
    ItemName.Jackpot: 				    ItemData(0x13200DC,  406, 0x196 ,0,1,True),
    ItemName.LuckyLucky: 				ItemData(0x13200DD,  407, 0x197 ,0,1,True),
    ItemName.LuckyLucky2: 				ItemData(0x13200DE,  407, 0x197 ,0,1,True),
    ItemName.LuckyLucky3: 				ItemData(0x13200DF,  407, 0x197 ,0,1,True),
    ItemName.DriveConverter: 			ItemData(0x13200E0,  540, 0x21C ,0,1,True),
    ItemName.FireBoost: 				ItemData(0x13200E1,  408, 0x198 ,0,1,True),
    ItemName.BlizzardBoost: 			ItemData(0x13200E2,  409, 0x199 ,0,1,True),
    ItemName.ThunderBoost: 				ItemData(0x13200E3,  410, 0x19A ,0,1,True),
    ItemName.ItemBoost: 				ItemData(0x13200E4,  411, 0x19B ,0,1,True),
    ItemName.MPRage: 				    ItemData(0x13200E5,  412, 0x19C ,0,1,True),
    ItemName.MPRage2: 				    ItemData(0x13200E6,  412, 0x19C ,0,1,True),
    ItemName.MPHaste: 				    ItemData(0x13200E7,  413, 0x19D ,0,1,True),
    ItemName.MPHaste2: 				    ItemData(0x13200E8,  413, 0x19D ,0,1,True),
    ItemName.MPHastera: 				ItemData(0x13200E9,  421, 0x1A5 ,0,1,True),
    ItemName.MPHastera2: 				ItemData(0x13200EA,  421, 0x1A5 ,0,1,True),
    ItemName.MPHastega: 				ItemData(0x13200EB,  422, 0x1A6 ,0,1,True),
    ItemName.Defender: 				    ItemData(0x13200EC,  414, 0x19E ,0,1,True),
    ItemName.DamageControl: 			ItemData(0x13200ED,  542, 0x21E ,0,1,True),
    ItemName.NoExperience: 				ItemData(0x13200EE,  404, 0x194 ,0,1,True),
    ItemName.NoExperience2: 			ItemData(0x13200EF,  404, 0x194 ,0,1,True),
    ItemName.LightDarkness: 			ItemData(0x13200F0,  541, 0x21D ,0,1,True),
}                                                
LvlAbility_Table = {                             
    ItemName.ComboBoost2: 				ItemData(0x13200F1,  390, 0x186 , 0,1,True ),
    ItemName.ExperienceBoost2: 			ItemData(0x13200F2,  401, 0x191 , 0,1,True ),
    ItemName.MagicLock: 				ItemData(0x13200F3,  403, 0x193 , 0,1,True ),
    ItemName.ReactionBoost3: 			ItemData(0x13200F4,  392, 0x188 , 0,1,True ),
    ItemName.ItemBoost2: 				ItemData(0x13200F5,  411, 0x19B , 0,1,True ),
    ItemName.LeafBracer: 				ItemData(0x13200F6,  402, 0x192 , 0,1,True ),
    ItemName.FireBoost2: 				ItemData(0x13200F7,  408, 0x198 , 0,1,True ),
    ItemName.DriveBoost2: 				ItemData(0x13200F8,  397, 0x18D , 0,1,True ),
    ItemName.Draw4: 				    ItemData(0x13200F9,  405, 0x195 , 0,1,True ),
    ItemName.CombinationBoost: 			ItemData(0x13200FA,  400, 0x190 , 0,1,True ),
    ItemName.DamageDrive: 				ItemData(0x13200FB,  396, 0x18C , 0,1,True ),
    ItemName.AirComboBoost2: 			ItemData(0x13200FC,  391, 0x187 , 0,1,True ),
    ItemName.BlizzardBoost2: 			ItemData(0x13200FD,  409, 0x199 , 0,1,True ),
    ItemName.DriveConverter2: 			ItemData(0x13200FE,  540, 0x21C , 0,1,True ),
    ItemName.NegativeCombo2: 			ItemData(0x13200FF,  394, 0x18A , 0,1,True ),
    ItemName.OnceMore: 				    ItemData(0x1320100,  416, 0x1A0 , 0,1,True ),
    ItemName.FinishingPlus3: 			ItemData(0x1320101,  393, 0x189 , 0,1,True ),
    ItemName.ThunderBoost2: 			ItemData(0x1320102,  410, 0x19A , 0,1,True ),
    ItemName.Defender2: 				ItemData(0x1320103,  414, 0x19E , 0,1,True ),
    ItemName.BerserkCharge2: 			ItemData(0x1320104,  395, 0x18B , 0,1,True ),
    ItemName.Jackpot2: 				    ItemData(0x1320105,  406, 0x196 , 0,1,True ),
    ItemName.SecondChance: 				ItemData(0x1320106,  415, 0x19F , 0,1,True ),
    ItemName.DamageControl2: 			ItemData(0x1320107,  542, 0x21E , 0,1,True ),
}
ActionAbility_Table = {
    ItemName.Guard: 				    ItemData(0x1320108,  82, 0x052  , 0,1,True ),                    
    ItemName.UpperSlash: 				ItemData(0x1320109,  137, 0x089 , 0,1,True ),              
    ItemName.HorizontalSlash: 			ItemData(0x132010A,  271, 0x10F , 0,1,True ),         
    ItemName.FinishingLeap: 			ItemData(0x132010B,  267, 0x10B , 0,1,True ),           
    ItemName.RetaliatingSlash: 			ItemData(0x132010C,  273, 0x111 , 0,1,True ),        
    ItemName.Slapshot: 				    ItemData(0x132010D,  262, 0x106 , 0,1,True ),                
    ItemName.DodgeSlash: 				ItemData(0x132010E,  263, 0x107 , 0,1,True ),              
    ItemName.FlashStep: 				ItemData(0x132010F,  559, 0x22F , 0,1,True ),               
    ItemName.SlideDash: 				ItemData(0x1320110,  264, 0x108 , 0,1,True ),               
    ItemName.VicinityBreak: 			ItemData(0x1320111,  562, 0x232 , 0,1,True ),           
    ItemName.GuardBreak: 				ItemData(0x1320112,  265, 0x109 , 0,1,True ),              
    ItemName.Explosion: 				ItemData(0x1320113,  266, 0x10A , 0,1,True ),               
    ItemName.AerialSweep: 				ItemData(0x1320114,  269, 0x10D , 0,1,True ),             
    ItemName.AerialDive: 				ItemData(0x1320115,  560, 0x230 , 0,1,True ),              
    ItemName.AerialSpiral: 				ItemData(0x1320116,  270, 0x10E , 0,1,True ),            
    ItemName.AerialFinish: 				ItemData(0x1320117,  272, 0x110 , 0,1,True ),            
    ItemName.MagnetBurst: 				ItemData(0x1320118,  561, 0x231 , 0,1,True ),             
    ItemName.Counterguard: 				ItemData(0x1320119,  268, 0x10C , 0,1,True ),            
    ItemName.AutoValor: 				ItemData(0x132011A,  385, 0x181 , 0,1,True ),               
    ItemName.AutoWisdom: 				ItemData(0x132011B,  386, 0x182 , 0,1,True ),              
    ItemName.AutoLimit: 				ItemData(0x132011C,  568, 0x238 , 0,1,True ),               
    ItemName.AutoMaster: 				ItemData(0x132011D,  387, 0x183 , 0,1,True ),              
    ItemName.AutoFinal: 				ItemData(0x132011E,  388, 0x184 , 0,1,True ),               
    ItemName.AutoSummon: 				ItemData(0x132011F,  389, 0x185 , 0,1,True ),              
    ItemName.TrinityLimit: 				ItemData(0x1320120,  198, 0x0C6,  0,1,True ),                   
}
Items_Table = {
    ItemName.Potion: 				    ItemData(0x1320121,  1, 0x3580 ),
    ItemName.HiPotion: 				    ItemData(0x1320122,  2, 0x3581 ),
    ItemName.Ether: 				    ItemData(0x1320123,  3, 0x3582 ),
    ItemName.Elixir: 				    ItemData(0x1320124,  4, 0x3583 ),
    ItemName.MegaPotion: 				ItemData(0x1320125,  5, 0x3584 ),
    ItemName.MegaEther: 				ItemData(0x1320126,  6, 0x3585 ),
    ItemName.Megalixir: 				ItemData(0x1320127,  7, 0x3586 ),
    ItemName.Tent: 				        ItemData(0x1320128,  131, 0x35E1 ),
    ItemName.DriveRecovery: 			ItemData(0x1320129,  274, 0x3664 ),
    ItemName.HighDriveRecovery: 		ItemData(0x132012A,  275, 0x3665 ),
    ItemName.PowerBoost: 				ItemData(0x132012B,  276, 0x3666 ),
    ItemName.MagicBoost: 				ItemData(0x132012C,  277, 0x3667 ),
    ItemName.DefenseBoost: 				ItemData(0x132012D,  278, 0x3668 ),
    ItemName.APBoost: 				    ItemData(0x132012E,  279, 0x3669 ),
}                                                

# These items cannot be in other games so these are done locally in kh2
DonaldAbility_Table = {
    ItemName.DonaldFire: 				ItemData(0x132012F,  165,0x111 ),
    ItemName.DonaldBlizzard: 			ItemData(0x1320130,  166,0x111 ),
    ItemName.DonaldThunder: 			ItemData(0x1320131,  167,0x111 ),
    ItemName.DonaldCure: 				ItemData(0x1320132,  168,0x111 ),
    ItemName.Fantasia: 				    ItemData(0x1320133,  199,0x111 ),
    ItemName.FlareForce: 				ItemData(0x1320134,  200,0x111 ),
    ItemName.DonaldMPRage: 				ItemData(0x1320135,  412,0x111 ),
    ItemName.DonaldJackpot: 			ItemData(0x1320136,  406,0x111 ),
    ItemName.DonaldLuckyLucky: 			ItemData(0x1320137,  407,0x111 ),
    ItemName.DonaldFireBoost: 			ItemData(0x1320138,  408,0x111 ),
    ItemName.DonaldBlizzardBoost: 		ItemData(0x1320139,  409,0x111 ),
    ItemName.DonaldThunderBoost: 		ItemData(0x132013A,  410,0x111 ),
    ItemName.DonaldFireBoost: 			ItemData(0x132013B,  408,0x111 ),
    ItemName.DonaldBlizzardBoost: 		ItemData(0x132013C,  409,0x111 ),
    ItemName.DonaldThunderBoost: 		ItemData(0x132013D,  410,0x111 ),
    ItemName.DonaldMPRage: 				ItemData(0x132013E,  412,0x111 ),
    ItemName.DonaldMPHastera: 			ItemData(0x132013F,  421,0x111 ),
    ItemName.DonaldAutoLimit: 			ItemData(0x1320140,  417,0x111 ),
    ItemName.DonaldHyperHealing: 		ItemData(0x1320141,  419,0x111 ),
    ItemName.DonaldAutoHealing: 		ItemData(0x1320142,  420,0x111 ),
    ItemName.DonaldMPHastega: 			ItemData(0x1320143,  422,0x111 ),
    ItemName.DonaldItemBoost: 			ItemData(0x1320144,  411,0x111 ),
    ItemName.DonaldDamageControl: 		ItemData(0x1320145,  542,0x111 ),
    ItemName.DonaldHyperHealing: 		ItemData(0x1320146,  419,0x111 ),
    ItemName.DonaldMPRage: 				ItemData(0x1320147,  412,0x111 ),
    ItemName.DonaldMPHaste: 			ItemData(0x1320148,  413,0x111 ),
    ItemName.DonaldMPHastera: 			ItemData(0x1320149,  421,0x111 ),
    ItemName.DonaldMPHastega: 			ItemData(0x132014A,  422,0x111 ),
    ItemName.DonaldMPHaste: 			ItemData(0x132014B,  413,0x111 ),
    ItemName.DonaldDamageControl: 		ItemData(0x132014C,  542,0x111 ),
    ItemName.DonaldMPHastera: 			ItemData(0x132014D,  421,0x111 ),
    ItemName.DonaldDraw: 				ItemData(0x132014E,  405,0x111 ),
}
GoofyAbility_Table = {
    ItemName.GoofyTornado: 				ItemData(0x132014F,  423,0x111 ),
    ItemName.GoofyTurbo: 				ItemData(0x1320150,  425,0x111 ),
    ItemName.GoofyBash: 				ItemData(0x1320151,  429,0x111 ),
    ItemName.TornadoFusion: 			ItemData(0x1320152,  201,0x111 ),
    ItemName.Teamwork: 				    ItemData(0x1320153,  202,0x111 ),
    ItemName.GoofyDraw: 				ItemData(0x1320154,  405,0x111 ),
    ItemName.GoofyJackpot: 				ItemData(0x1320155,  406,0x111 ),
    ItemName.GoofyLuckyLucky: 			ItemData(0x1320156,  407,0x111 ),
    ItemName.GoofyItemBoost: 			ItemData(0x1320157,  411,0x111 ),
    ItemName.GoofyMPRage: 				ItemData(0x1320158,  412,0x111 ),
    ItemName.GoofyDefender: 			ItemData(0x1320159,  414,0x111 ),
    ItemName.GoofyDamageControl: 		ItemData(0x132015A,  542,0x111 ),
    ItemName.GoofyAutoLimit: 			ItemData(0x132015B,  417,0x111 ),
    ItemName.GoofySecondChance: 		ItemData(0x132015C,  415,0x111 ),
    ItemName.GoofyOnceMore: 			ItemData(0x132015D,  416,0x111 ),
    ItemName.GoofyAutoChange: 			ItemData(0x132015E,  418,0x111 ),
    ItemName.GoofyHyperHealing: 		ItemData(0x132015F,  419,0x111 ),
    ItemName.GoofyAutoHealing: 			ItemData(0x1320160,  420,0x111 ),
    ItemName.GoofyDefender: 			ItemData(0x1320161,  414,0x111 ),
    ItemName.GoofyHyperHealing: 		ItemData(0x1320162,  419,0x111 ),
    ItemName.GoofyMPHaste: 				ItemData(0x1320163,  413,0x111 ),
    ItemName.GoofyMPHastera: 			ItemData(0x1320164,  421,0x111 ),
    ItemName.GoofyMPRage: 				ItemData(0x1320165,  412,0x111 ),
    ItemName.GoofyMPHastega: 			ItemData(0x1320166,  422,0x111 ),
    ItemName.GoofyItemBoost: 			ItemData(0x1320167,  411,0x111 ),
    ItemName.GoofyDamageControl: 		ItemData(0x1320168,  542,0x111 ),
    ItemName.GoofyProtect: 				ItemData(0x1320169,  596,0x111 ),
    ItemName.GoofyProtera: 				ItemData(0x132016A,  597,0x111 ),
    ItemName.GoofyProtega: 				ItemData(0x132016B,  598,0x111 ),
    ItemName.GoofyDamageControl: 		ItemData(0x132016C,  542,0x111 ),
    ItemName.GoofyProtect: 				ItemData(0x132016D,  596,0x111 ),
    ItemName.GoofyProtera: 				ItemData(0x132016E,  597,0x111 ),
    ItemName.GoofyProtega: 				ItemData(0x132016F,  598,0x111 ),
}

Misc_Table = {
    ItemName.LuckyEmblem: 				ItemData(0x1320170,  1,0x111 ),
    ItemName.Victory: 				    ItemData(0x1320171,  1, True,0x111 ),
}   #itemname luckey emblem (0x1320172)    will be unused map

exclusionItem_table = {
    "Ability": {
        ItemName.Scan,
        ItemName.Scan2,
        ItemName.AerialRecovery,
        ItemName.ComboMaster,
        ItemName.ComboPlus,
        ItemName.ComboPlus2,
        ItemName.ComboPlus3,
        ItemName.AirComboPlus,
        ItemName.AirComboPlus2,
        ItemName.AirComboPlus3,
        ItemName.ComboBoost,
        ItemName.AirComboBoost,
        ItemName.ReactionBoost,
        ItemName.ReactionBoost2,
        ItemName.FinishingPlus,
        ItemName.FinishingPlus2,
        ItemName.NegativeCombo,
        ItemName.BerserkCharge,
        ItemName.DamageDrive,
        ItemName.DriveBoost,
        ItemName.FormBoost,
        ItemName.FormBoost2,
        ItemName.FormBoost3,
        ItemName.SummonBoost,
        ItemName.ExperienceBoost,
        ItemName.Draw,
        ItemName.Draw2,
        ItemName.Draw3,
        ItemName.Jackpot,
        ItemName.LuckyLucky,
        ItemName.LuckyLucky2,
        ItemName.LuckyLucky3,
        ItemName.DriveConverter,
        ItemName.FireBoost,
        ItemName.BlizzardBoost,
        ItemName.ThunderBoost,
        ItemName.ItemBoost,
        ItemName.MPRage,
        ItemName.MPRage2,
        ItemName.MPHaste,
        ItemName.MPHaste2,
        ItemName.MPHastera,
        ItemName.MPHastera2,
        ItemName.MPHastega,
        ItemName.Defender,
        ItemName.DamageControl,
        ItemName.NoExperience,
        ItemName.NoExperience2,
        ItemName.LightDarkness,
        ItemName.ComboBoost2,
        ItemName.ExperienceBoost2,
        ItemName.MagicLock,
        ItemName.ReactionBoost3,
        ItemName.ItemBoost2,
        ItemName.LeafBracer,
        ItemName.FireBoost2,
        ItemName.DriveBoost2,
        ItemName.Draw4,
        ItemName.CombinationBoost,
        ItemName.DamageDrive,
        ItemName.AirComboBoost2,
        ItemName.BlizzardBoost2,
        ItemName.DriveConverter2,
        ItemName.NegativeCombo2,
        ItemName.OnceMore,
        ItemName.FinishingPlus3,
        ItemName.ThunderBoost2,
        ItemName.Defender2,
        ItemName.BerserkCharge2,
        ItemName.Jackpot2,
        ItemName.SecondChance,
        ItemName.DamageControl2,
        ItemName.Guard,
        ItemName.UpperSlash,
        ItemName.HorizontalSlash,
        ItemName.FinishingLeap,
        ItemName.RetaliatingSlash,
        ItemName.Slapshot,
        ItemName.DodgeSlash,
        ItemName.FlashStep,
        ItemName.SlideDash,
        ItemName.VicinityBreak,
        ItemName.GuardBreak,
        ItemName.Explosion,
        ItemName.AerialSweep,
        ItemName.AerialDive,
        ItemName.AerialSpiral,
        ItemName.AerialFinish,
        ItemName.MagnetBurst,
        ItemName.Counterguard,
        ItemName.AutoValor,
        ItemName.AutoWisdom,
        ItemName.AutoLimit,
        ItemName.AutoMaster,
        ItemName.AutoFinal,
        ItemName.AutoSummon,
        ItemName.TrinityLimit,
        ItemName.HighJump,
        ItemName.HighJump2,
        ItemName.HighJump3,
        ItemName.HighJump4,
        ItemName.QuickRun,
        ItemName.QuickRun2,
        ItemName.QuickRun3,
        ItemName.QuickRun4,
        ItemName.AerialDodge,
        ItemName.AerialDodge2,
        ItemName.AerialDodge3,
        ItemName.AerialDodge4,
        ItemName.Glide,
        ItemName.Glide2,
        ItemName.Glide3,
        ItemName.Glide4,
        ItemName.DodgeRoll,
        ItemName.DodgeRoll2,
        ItemName.DodgeRoll3,
        ItemName.DodgeRoll4, 
    },
    "StatUps":{
        ItemName.MaxHPUp,
        ItemName.MaxMPUp,
        ItemName.DriveGaugeUp,
        },
    "Forms": {
        ItemName.ValorForm,
        ItemName.WisdomForm,
        ItemName.LimitForm,
        ItemName.MasterForm,
        ItemName.FinalForm,

    },
    "Schmovement": {
        ItemName.HighJump,
        ItemName.QuickRun,
        ItemName.DodgeRoll,
        ItemName.AerialDodge,
        ItemName.Glide,
    }
}
# Abilites that could be on keyblades
keybladeAbilities = [
    ItemName.Scan,
    ItemName.Scan2,
    ItemName.AerialRecovery,
    ItemName.ComboMaster,
    ItemName.ComboPlus,
    ItemName.ComboPlus2,
    ItemName.ComboPlus3,
    ItemName.AirComboPlus,
    ItemName.AirComboPlus2,
    ItemName.AirComboPlus3,
    ItemName.ComboBoost,
    ItemName.AirComboBoost,
    ItemName.ReactionBoost,
    ItemName.ReactionBoost2,
    ItemName.FinishingPlus,
    ItemName.FinishingPlus2,
    ItemName.NegativeCombo,
    ItemName.BerserkCharge,
    ItemName.DamageDrive,
    ItemName.DriveBoost,
    ItemName.FormBoost,
    ItemName.FormBoost2,
    ItemName.FormBoost3,
    ItemName.SummonBoost,
    ItemName.ExperienceBoost,
    ItemName.Draw,
    ItemName.Draw2,
    ItemName.Draw3,
    ItemName.Jackpot,
    ItemName.LuckyLucky,
    ItemName.LuckyLucky2,
    ItemName.LuckyLucky3,
    ItemName.DriveConverter,
    ItemName.FireBoost,
    ItemName.BlizzardBoost,
    ItemName.ThunderBoost,
    ItemName.ItemBoost,
    ItemName.MPRage,
    ItemName.MPRage2,
    ItemName.MPHaste,
    ItemName.MPHaste2,
    ItemName.MPHastera,
    ItemName.MPHastera2,
    ItemName.MPHastega,
    ItemName.Defender,
    ItemName.DamageControl,
    ItemName.NoExperience,
    ItemName.NoExperience2,
    ItemName.LightDarkness,
    ItemName.ComboBoost2,
    ItemName.ExperienceBoost2,
    ItemName.MagicLock,
    ItemName.ReactionBoost3,
    ItemName.ItemBoost2,
    ItemName.LeafBracer,
    ItemName.FireBoost2,
    ItemName.DriveBoost2,
    ItemName.Draw4,
    ItemName.CombinationBoost,
    ItemName.DamageDrive,
    ItemName.AirComboBoost2,
    ItemName.BlizzardBoost2,
    ItemName.DriveConverter2,
    ItemName.NegativeCombo2,
    ItemName.OnceMore,
    ItemName.FinishingPlus3,
    ItemName.ThunderBoost2,
    ItemName.Defender2,
    ItemName.BerserkCharge2,
    ItemName.Jackpot2,
    ItemName.SecondChance,
    ItemName.DamageControl2,
    ItemName.AutoValor,
    ItemName.AutoWisdom,
    ItemName.AutoLimit,
    ItemName.AutoMaster,
    ItemName.AutoFinal,
    ItemName.AutoSummon,
]
# donald abiltys that are only donalds
#these probably dont need to be here but it is simpiler.
donaldAbility = [
    ItemName.DonaldFire,
    ItemName.DonaldBlizzard,
    ItemName.DonaldThunder,
    ItemName.DonaldCure,
    ItemName.Fantasia,
    ItemName.FlareForce,
    ItemName.DonaldMPRage,
    ItemName.DonaldJackpot,
    ItemName.DonaldLuckyLucky,
    ItemName.DonaldFireBoost,
    ItemName.DonaldBlizzardBoost,
    ItemName.DonaldThunderBoost,
    ItemName.DonaldFireBoost,
    ItemName.DonaldBlizzardBoost,
    ItemName.DonaldThunderBoost,
    ItemName.DonaldMPRage,
    ItemName.DonaldMPHastera,
    ItemName.DonaldAutoLimit,
    ItemName.DonaldHyperHealing,
    ItemName.DonaldAutoHealing,
    ItemName.DonaldMPHastega,
    ItemName.DonaldItemBoost,
    ItemName.DonaldDamageControl,
    ItemName.DonaldHyperHealing,
    ItemName.DonaldMPRage,
    ItemName.DonaldMPHaste,
    ItemName.DonaldMPHastera,
    ItemName.DonaldMPHastega,
    ItemName.DonaldMPHaste,
    ItemName.DonaldDamageControl,
    ItemName.DonaldMPHastera,
    ItemName.DonaldDraw,
]
goofyAbility = [
    ItemName.GoofyTornado,
    ItemName.GoofyTurbo,
    ItemName.GoofyBash,
    ItemName.TornadoFusion,
    ItemName.Teamwork,
    ItemName.GoofyDraw,
    ItemName.GoofyJackpot,
    ItemName.GoofyLuckyLucky,
    ItemName.GoofyItemBoost,
    ItemName.GoofyMPRage,
    ItemName.GoofyDefender,
    ItemName.GoofyDamageControl,
    ItemName.GoofyAutoLimit,
    ItemName.GoofySecondChance,
    ItemName.GoofyOnceMore,
    ItemName.GoofyAutoChange,
    ItemName.GoofyHyperHealing,
    ItemName.GoofyAutoHealing,
    ItemName.GoofyDefender,
    ItemName.GoofyHyperHealing,
    ItemName.GoofyMPHaste,
    ItemName.GoofyMPHastera,
    ItemName.GoofyMPRage,
    ItemName.GoofyMPHastega,
    ItemName.GoofyItemBoost,
    ItemName.GoofyDamageControl,
    ItemName.GoofyProtect,
    ItemName.GoofyProtera,
    ItemName.GoofyProtega,
    ItemName.GoofyDamageControl,
    ItemName.GoofyProtect,
    ItemName.GoofyProtera,
    ItemName.GoofyProtega,
]


item_dictionary_table = {**Reports_Table,
                         **Progression_Table,
                         **Forms_Table,
                         **Magic_Table,
                         **Armor_Table,
                         **Movement_Table,
                         **Shields_Table,
                         **Keyblade_Table,
                         **Accessory_Table,
                         **Usefull_Table,
                         **SupportAbility_Table,
                         **LvlAbility_Table,
                         **ActionAbility_Table,
                         **Items_Table,
                         **Misc_Table,
                         **Items_Table,
                         **DonaldAbility_Table,
                         **GoofyAbility_Table,
                         }

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_dictionary_table.items() if
                                            data.code}
#lookup_kh2id_to_name: typing.Dict[int, str] = {data.kh2id: item_name for item_name, data in
#                                               item_dictionary_table.items() if data.kh2id}
