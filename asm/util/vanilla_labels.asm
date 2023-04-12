.gba

; Variables
.definelabel PassageID, 0x3000002
.definelabel InPassageLevelID, 0x3000003
.definelabel CurrentRoomId, 0x3000024
.definelabel ucFlashLoop, 0x3000044
.definelabel ucTimeUp, 0x3000047
.definelabel EntityLeftOverStateList, 0x3000564
.definelabel CurrentEnemyData, 0x3000A24
.definelabel LevelStatusTable, 0x3000A68
.definelabel Scbuf_ucStatus, 0x3000BE0
.definelabel HasJewelPiece1, 0x3000C07
.definelabel HasJewelPiece2, 0x3000C08
.definelabel HasJewelPiece3, 0x3000C09
.definelabel HasJewelPiece4, 0x3000C0A
.definelabel HasCD, 0x3000C0B
.definelabel HasKeyzer, 0x3000C0C
.definelabel sGameSeq, 0x3000C3C
.definelabel GlobalTimer, 0x3000C41
.definelabel KeyPressContinuous, 0x3001844
.definelabel KeyPressPrevious, 0x3001846
.definelabel usTrg_KeyPress1Frame, 0x3001848
.definelabel Wario_ucReact, 0x3001898
.definelabel Wario_ucMiss, 0x300189C
.definelabel WarioHeart, 0x3001910
.definelabel usWarStopFlg, 0x30019F6

; Functions
.definelabel MainGameLoop, 0x80001CC
.definelabel m4aSongNumStart, 0x8001DA4
.definelabel WarioHitMain, 0x801009c
.definelabel EnemyChildSet, 0x801E328
.definelabel ChangeWarioReact_Fire, 0x801EA3C
.definelabel ChangeWarioReact_Fat, 0x801EA64
.definelabel ChangeWarioReact_Puffy, 0x801EADC
.definelabel ChangeWarioReact_Spring, 0x801EB04
.definelabel ChangeWarioReact_Frozen, 0x801EB54
.definelabel KillChildWhenParentDies, 0x80268DC
.definelabel EntityAI_Q_K5_Hip_COM_takarabako, 0x80292BC
.definelabel EntityAI_INITIAL_takara_kakera, 0x802932C
.definelabel TOptObjSet, 0x80766E8
.definelabel WarioCoinSet, 0x80768B8
.definelabel WarioVoiceSet, 0x8088620
.definelabel MiniRandomCreate, 0x8089B80
.definelabel modsi3, 0x8094ED0
.definelabel WarioChng_React, 0x82DECA0

; ROM data
.definelabel takara_Anm_00, 0x83B4BC8
.definelabel takara_Anm_01, 0x83B4BD8
.definelabel takara_Anm_02, 0x83B4C00
.definelabel takara_Anm_03, 0x83B4C10
.definelabel takara_Anm_04, 0x83B4C20
.definelabel takara_Anm_05, 0x83B4C30
.definelabel zako_takara_box_Anm_02, 0x83B4F34
.definelabel zako_takara_box_Anm_11, 0x83B5004
