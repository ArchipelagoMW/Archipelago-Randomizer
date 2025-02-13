from enum import Enum


class LocationName():
    ## Blue Mystery Datas
    # ACDC Area
    ACDC_1_Southwest_BMD = "ACDC 1 Southwest BMD"
    ACDC_1_Northeast_BMD = "ACDC 1 Northeast BMD"
    ACDC_2_Center_BMD = "ACDC 2 Center BMD"
    ACDC_2_North_BMD = "ACDC 2 North BMD"
    ACDC_3_Southwest_BMD = "ACDC 3 Southwest BMD"
    ACDC_3_Northeast_BMD = "ACDC 3 Northeast BMD"

    # SciLab Area
    SciLab_1_WWW_BMD = "SciLab 1 WWW BMD"
    SciLab_1_East_BMD = "SciLab 1 East BMD"
    SciLab_2_West_BMD = "SciLab 2 West BMD"
    SciLab_2_South_BMD = "SciLab 2 South BMD"

    # Yoka Area
    Yoka_1_North_BMD = "Yoka 1 North BMD"
    Yoka_1_WWW_BMD = "Yoka 1 WWW BMD"
    Yoka_2_Upper_BMD = "Yoka 2 Upper BMD"
    Yoka_2_Lower_BMD = "Yoka 2 Lower BMD"

    # Beach Area
    Beach_1_BMD = "Beach 1 BMD"
    Beach_2_West_BMD = "Beach 2 West BMD"
    Beach_2_East_BMD = "Beach 2 East BMD"

    # Undernet Area
    Undernet_1_South_BMD = "Undernet 1 South BMD"
    Undernet_1_WWW_BMD = "Undernet 1 WWW BMD"
    Undernet_2_Upper_BMD = "Undernet 2 Upper BMD"
    Undernet_2_Lower_BMD = "Undernet 2 Lower BMD"
    Undernet_3_South_BMD = "Undernet 3 South BMD"
    Undernet_3_Central_BMD = "Undernet 3 Central BMD"
    Undernet_4_Bottom_West_BMD = "Undernet 4 Bottom West BMD"
    Undernet_4_Top_Pillar_BMD = "Undernet 4 Top Pillar BMD"
    Undernet_4_Top_North_BMD = "Undernet 4 Top North BMD"
    Undernet_5_Upper_BMD = "Undernet 5 Upper BMD"
    Undernet_5_Lower_BMD = "Undernet 5 Lower BMD"
    Undernet_6_East_BMD = "Undernet 6 East BMD"
    Undernet_6_Central_BMD = "Undernet 6 Central BMD"
    Undernet_6_TV_BMD = "Undernet 6 TV BMD"
    Undernet_7_West_BMD = "Undernet 7 West BMD"
    Undernet_7_Northwest_BMD = "Undernet 7 Northwest BMD"
    Undernet_7_Northeast_BMD = "Undernet 7 Northeast BMD"

    # Secret Area
    Secret_1_South_BMD = "Secret 1 South BMD"
    Secret_1_Northeast_BMD = "Secret 1 Northeast BMD"
    Secret_1_Northwest_BMD = "Secret 1 Northwest BMD"
    Secret_2_Upper_BMD = "Secret 2 Upper BMD"
    Secret_2_Lower_BMD = "Secret 2 Lower BMD"
    Secret_2_Island_BMD = "Secret 2 Island BMD"
    Secret_3_South_BMD = "Secret 3 South BMD"
    Secret_3_Island_BMD = "Secret 3 Island BMD"
    Secret_3_BugFrag_BMD = "Secret 3 BugFrag BMD"

    # School Area
    School_1_Entrance_BMD = "School 1 Entrance BMD"
    School_1_North_Central_BMD = "School 1 North Central BMD"
    School_1_Far_West_BMD_2 = "School 1 Far West BMD 2"
    School_2_Entrance_BMD = "School 2 Entrance BMD"
    School_2_South_BMD = "School 2 South BMD"
    School_2_Mainframe_BMD = "School 2 Mainframe BMD"

    # Zoo Area
    Zoo_1_East_BMD = "Zoo 1 East BMD"
    Zoo_1_Central_BMD = "Zoo 1 Central BMD"
    Zoo_1_North_BMD = "Zoo 1 North BMD"
    Zoo_2_East_BMD = "Zoo 2 East BMD"
    Zoo_2_Central_BMD = "Zoo 2 Central BMD"
    Zoo_2_West_BMD = "Zoo 2 West BMD"
    Zoo_3_North_BMD = "Zoo 3 North BMD"
    Zoo_3_Central_BMD = "Zoo 3 Central BMD"
    Zoo_3_Path_BMD = "Zoo 3 Path BMD"
    Zoo_3_Northwest_BMD = "Zoo 3 Northwest BMD"
    Zoo_4_West_BMD = "Zoo 4 West BMD"
    Zoo_4_Northwest_BMD = "Zoo 4 Northwest BMD"
    Zoo_4_Southeast_BMD = "Zoo 4 Southeast BMD"

    # Hades Area
    Hades_South_BMD = "Hades South BMD"

    # Hospital Area
    Hospital_1_Center_BMD = "Hospital 1 Center BMD"
    Hospital_1_West_BMD = "Hospital 1 West BMD"
    Hospital_1_North_BMD = "Hospital 1 North BMD"
    Hospital_2_Southwest_BMD = "Hospital 2 Southwest BMD"
    Hospital_2_Central_BMD = "Hospital 2 Central BMD"
    Hospital_2_Island_BMD = "Hospital 2 Island BMD"
    Hospital_3_Central_BMD = "Hospital 3 Central BMD"
    Hospital_3_West_BMD = "Hospital 3 West BMD"
    Hospital_3_Northwest_BMD = "Hospital 3 Northwest BMD"
    Hospital_4_Central_BMD = "Hospital 4 Central BMD"
    Hospital_4_Southeast_BMD = "Hospital 4 Southeast BMD"
    Hospital_4_North_BMD = "Hospital 4 North BMD"
    Hospital_5_Southwest_BMD = "Hospital 5 Southwest BMD"
    Hospital_5_Northeast_BMD = "Hospital 5 Northeast BMD"
    Hospital_5_Island_BMD = "Hospital 5 Island BMD"

    # WWW Area
    WWW_1_Central_BMD = "WWW 1 Central BMD"
    WWW_1_West_BMD = "WWW 1 West BMD"
    WWW_1_East_BMD = "WWW 1 East BMD"
    WWW_2_East_BMD = "WWW 2 East BMD"
    WWW_2_Northwest_BMD = "WWW 2 Northwest BMD"
    WWW_3_East_BMD = "WWW 3 East BMD"
    WWW_3_North_BMD = "WWW 3 North BMD"
    WWW_4_Northwest_BMD = "WWW 4 Northwest BMD"
    WWW_4_Central_BMD = "WWW 4 Central BMD"

    # Misc Net Area
    ACDC_Dog_House_BMD = "ACDC Dog House BMD"
    ACDC_Lans_Security_Panel_BMD = "ACDC Lan's Security Panel BMD"
    ACDC_Yais_Phone_BMD = "ACDC Yai's Phone BMD"
    ACDC_NumberMan_Display_BMD = "ACDC NumberMan Display BMD"
    ACDC_Tank_BMD_1 = "ACDC Tank BMD 1"
    ACDC_Tank_BMD_2 = "ACDC Tank BMD 2"
    ACDC_School_Server_BMD_1 = "ACDC School Server BMD 1"
    ACDC_School_Server_BMD_2 = "ACDC School Server BMD 2"
    ACDC_School_Blackboard_BMD = "ACDC School Blackboard BMD"
    SciLab_Vending_Machine_BMD = "SciLab Vending Machine BMD"
    SciLab_Virus_Lab_Door_BMD_1 = "SciLab Virus Lab Door BMD 1"
    SciLab_Virus_Lab_Door_BMD_2 = "SciLab Virus Lab Door BMD 2"
    SciLab_Dads_Computer_BMD = "SciLab Dad's Computer BMD"
    Yoka_Armor_BMD = "Yoka Armor BMD"
    Yoka_TV_BMD = "Yoka TV BMD"
    Yoka_Hot_Spring_BMD = "Yoka Hot Spring BMD"
    Yoka_Ticket_Machine_BMD = "Yoka Ticket Machine BMD"
    Yoka_Giraffe_BMD = "Yoka Giraffe BMD"
    Yoka_Panda_BMD = "Yoka Panda BMD"
    Beach_Hospital_Bed_BMD = "Beach Hospital Bed BMD"
    Beach_TV_BMD = "Beach TV BMD"
    Beach_Vending_Machine_BMD = "Beach Vending Machine BMD"
    Beach_News_Van_BMD = "Beach News Van BMD"
    Beach_Battle_Console_BMD = "Beach Battle Console BMD"
    Beach_Security_System_BMD = "Beach Security System BMD"
    Beach_Broadcast_Computer_BMD = "Beach Broadcast Computer BMD"
    Hades_Gargoyle_BMD = "Hades Gargoyle BMD"
    WWW_Wall_BMD = "WWW Wall BMD"
    Mayls_HP_BMD = "Mayl's HP BMD"
    Yais_HP_BMD_1 = "Yai's HP BMD 1"
    Yais_HP_BMD_2 = "Yai's HP BMD 2"
    Dexs_HP_BMD_1 = "Dex's HP BMD 1"
    Dexs_HP_BMD_2 = "Dex's HP BMD 2"
    Tamakos_HP_BMD = "Tamako's HP BMD"

    # Story Item BMDs
    Undernet_7_Upper_BMD = "Undernet 7 Upper BMD"
    School_1_KeyDataA_BMD = "School 1 KeyDataA BMD"
    School_1_KeyDataB_BMD = "School 1 KeyDataB BMD"
    School_1_KeyDataC_BMD = "School 1 KeyDataC BMD"
    School_2_CodeC_BMD = "School 2 CodeC BMD"
    School_2_CodeA_BMD = "School 2 CodeA BMD"
    School_2_CodeB_BMD = "School 2 CodeB BMD"
    Hades_HadesKey_BMD = "Hades HadesKey BMD"
    WWW_1_South_BMD = "WWW 1 South BMD"
    WWW_2_West_BMD = "WWW 2 West BMD"
    WWW_3_South_BMD = "WWW 3 South BMD"
    WWW_4_East_BMD = "WWW 4 East BMD"

    ## Purple Mystery Data
    ACDC_1_PMD = "ACDC 1 PMD"
    Yoka_1_PMD = "Yoka 1 PMD"
    Beach_1_PMD = "Beach 1 PMD"
    Undernet_7_PMD = "Undernet 7 PMD"
    Mayls_HP_PMD = "Mayl's HP PMD"
    SciLab_Dads_Computer_PMD = "SciLab Dad's Computer PMD"
    Zoo_Panda_PMD = "Zoo Panda PMD"
    Beach_DNN_Security_Panel_PMD = "Beach DNN Security Panel PMD"
    Beach_DNN_Main_Console_PMD = "Beach DNN Main Console PMD"
    Tamakos_HP_PMD = "Tamako's HP PMD"

    ## Overworld Items
    Yoka_Mr_Quiz = "Yoka Mr Quiz"
    Yoka_Quiz_Master = "Yoka Quiz Master"
    Hospital_Quiz_Queen = "Hospital Quiz Queen"
    Hades_Quiz_King = "Hades Quiz King"
    ACDC_SonicWav_W_Trade = "ACDC SonicWav W Trade"
    ACDC_Bubbler_C_Trade = "ACDC Bubbler C Trade"
    ACDC_Recov120_S_Trade = "ACDC Recov120 S Trade"
    SciLab_Shake1_S_Trade = "SciLab Shake1 S Trade"
    Yoka_FireSwrd_P_Trade = "Yoka FireSwrd P Trade"
    Hospital_DynaWav_V_Trade = "Hospital DynaWav V Trade"
    Beach_DNN_WideSwrd_C_Trade = "Beach DNN WideSwrd C Trade"
    Beach_DNN_HoleMetr_H_Trade = "Beach DNN HoleMetr H Trade"
    Beach_DNN_Shadow_J_Trade = "Beach DNN Shadow J Trade"
    Hades_GrabBack_K_Trade = "Hades GrabBack K Trade"
    Comedian = "Comedian"
    Villain = "Villain"
    Mod_Tools_Guy = "Mod Tools Guy"
    ACDC_School_Desk = "ACDC School Desk"
    ACDC_Class_5B_Bookshelf = "ACDC Class 5B Bookshelf"
    SciLab_Garbage_Can = "SciLab Garbage Can"
    Yoka_Inn_Jars = "Yoka Inn Jars"
    Yoka_Zoo_Garbage = "Yoka Zoo Garbage"
    Beach_Department_Store = "Beach Department Store"
    Beach_Hospital_Plaque = "Beach Hospital Plaque"
    Beach_Hospital_Pink_Door = "Beach Hospital Pink Door"
    Beach_Hospital_Tree = "Beach Hospital Tree"
    Beach_Hospital_Hidden_Conversation = "Beach Hospital Hidden Conversation"
    Beach_Hospital_Girl = "Beach Hospital Girl"
    Beach_DNN_Kiosk = "Beach DNN Kiosk"
    Beach_DNN_Boxes = "Beach DNN Boxes"
    Beach_DNN_Poster = "Beach DNN Poster"
    Hades_Boat_Dock = "Hades Boat Dock"
    WWW_Control_Room_1_Screen = "WWW Control Room 1 Screen"
    WWW_Wilys_Desk = "WWW Wily's Desk"
    Undernet_4_Pillar_Prog = "Undernet 4 Pillar Prog"
    Serenade = "Serenade"

    ## Numberman Codes
    Numberman_Code_01 = "Numberman Code 01"
    Numberman_Code_02 = "Numberman Code 02"
    Numberman_Code_03 = "Numberman Code 03"
    Numberman_Code_04 = "Numberman Code 04"
    Numberman_Code_05 = "Numberman Code 05"
    Numberman_Code_06 = "Numberman Code 06"
    Numberman_Code_07 = "Numberman Code 07"
    Numberman_Code_08 = "Numberman Code 08"
    Numberman_Code_09 = "Numberman Code 09"
    Numberman_Code_10 = "Numberman Code 10"
    Numberman_Code_11 = "Numberman Code 11"
    Numberman_Code_12 = "Numberman Code 12"
    Numberman_Code_13 = "Numberman Code 13"
    Numberman_Code_14 = "Numberman Code 14"
    Numberman_Code_15 = "Numberman Code 15"
    Numberman_Code_16 = "Numberman Code 16"
    Numberman_Code_17 = "Numberman Code 17"
    Numberman_Code_18 = "Numberman Code 18"
    Numberman_Code_19 = "Numberman Code 19"
    Numberman_Code_20 = "Numberman Code 20"
    Numberman_Code_21 = "Numberman Code 21"
    Numberman_Code_22 = "Numberman Code 22"
    Numberman_Code_23 = "Numberman Code 23"
    Numberman_Code_24 = "Numberman Code 24"
    Numberman_Code_25 = "Numberman Code 25"
    Numberman_Code_26 = "Numberman Code 26"
    Numberman_Code_27 = "Numberman Code 27"
    Numberman_Code_28 = "Numberman Code 28"
    Numberman_Code_29 = "Numberman Code 29"
    Numberman_Code_30 = "Numberman Code 30"
    Numberman_Code_31 = "Numberman Code 31"

    ## Jobs
    Please_deliver_this = "Job: Please deliver this"
    My_Navi_is_sick = "Job: My Navi is sick"
    Help_me_with_my_son = "Job: Help me with my son!"
    Transmission_error = "Job: Transmission error"
    Chip_Prices = "Job: Chip Prices"
    Im_broke = "Job: I'm broke?!"
    Rare_chips_for_cheap = "Job: Rare chips for cheap!"
    Be_my_boyfriend = "Job: Be my boyfriend"
    Will_you_deliver = "Job: Will you deliver?"
    Look_for_friends = "Job: Look for friends (Tora)"
    Stuntmen_wanted = "Job: Stuntmen wanted! (Tora)"
    Riot_stopped = "Job: Riot stopped (Tora)"
    Gathering_Data = "Job: Gathering Data (Tora)"
    Somebody_please_help = "Job: Somebody, please help!"
    Looking_for_condor = "Job: Looking for condor"
    Help_with_rehab = "Job: Help with rehab"
    Help_with_rehab_bonus = "Job: Help with rehab bonus"
    Old_Master = "Job: Old Master"
    Catching_gang_members = "Job: Catching gang members"
    Please_adopt_a_virus = "Job: Please adopt a virus!"
    Legendary_Tomes = "Job: Legendary Tomes"
    Legendary_Tomes_Treasure = "Job: Legendary Tomes - Treasure"
    Hide_and_seek_First_Child = "Job: Hide and seek! First Child"
    Hide_and_seek_Second_Child = "Job: Hide and seek! Second Child"
    Hide_and_seek_Third_Child = "Job: Hide and seek! Third Child"
    Hide_and_seek_Fourth_Child = "Job: Hide and seek! Fourth Child"
    Hide_and_seek_Completion = "Job: Hide and seek! Completion"
    Finding_the_blue_Navi = "Job: Finding the blue Navi"
    Give_your_support = "Job: Give your support"
    Stamp_collecting = "Job: Stamp collecting"
    Help_with_a_will = "Job: Help with a will"

    Alpha_Defeated = "Alpha Defeated"

    ## Chocolates
    Chocolate_Shop_01 = "Chocolate Shop 01"
    Chocolate_Shop_02 = "Chocolate Shop 02"
    Chocolate_Shop_03 = "Chocolate Shop 03"
    Chocolate_Shop_04 = "Chocolate Shop 04"
    Chocolate_Shop_05 = "Chocolate Shop 05"
    Chocolate_Shop_06 = "Chocolate Shop 06"
    Chocolate_Shop_07 = "Chocolate Shop 07"
    Chocolate_Shop_08 = "Chocolate Shop 08"
    Chocolate_Shop_09 = "Chocolate Shop 09"
    Chocolate_Shop_10 = "Chocolate Shop 10"
    Chocolate_Shop_11 = "Chocolate Shop 11"
    Chocolate_Shop_12 = "Chocolate Shop 12"
    Chocolate_Shop_13 = "Chocolate Shop 13"
    Chocolate_Shop_14 = "Chocolate Shop 14"
    Chocolate_Shop_15 = "Chocolate Shop 15"
    Chocolate_Shop_16 = "Chocolate Shop 16"
    Chocolate_Shop_17 = "Chocolate Shop 17"
    Chocolate_Shop_18 = "Chocolate Shop 18"
    Chocolate_Shop_19 = "Chocolate Shop 19"
    Chocolate_Shop_20 = "Chocolate Shop 20"
    Chocolate_Shop_21 = "Chocolate Shop 21"
    Chocolate_Shop_22 = "Chocolate Shop 22"
    Chocolate_Shop_23 = "Chocolate Shop 23"
    Chocolate_Shop_24 = "Chocolate Shop 24"
    Chocolate_Shop_25 = "Chocolate Shop 25"
    Chocolate_Shop_26 = "Chocolate Shop 26"
    Chocolate_Shop_27 = "Chocolate Shop 27"
    Chocolate_Shop_28 = "Chocolate Shop 28"
    Chocolate_Shop_29 = "Chocolate Shop 29"
    Chocolate_Shop_30 = "Chocolate Shop 30"
    Chocolate_Shop_31 = "Chocolate Shop 31"
    Chocolate_Shop_32 = "Chocolate Shop 32"