from BaseClasses import Location, LocationProgressType

included_locations: dict[str, tuple[str, LocationProgressType]] = {}
"""Name: (region name, LocationProgressType)"""


def addlevels(maxlevel: int, logictype: int) -> dict[str, tuple[str, LocationProgressType]]:
    """Returns a dictionary with all level locations based on given options (maxlevel INCLUDED)."""
    locations: dict[str, tuple[str, LocationProgressType]] = {}

    # Level 1 is always directly accessible
    locations["Level 1"] = ("Menu", LocationProgressType.PRIORITY)
    locations["Level 1 Additional"] = ("Menu", LocationProgressType.DEFAULT)

    if logictype == 0 or logictype == 1:
        locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Level 2"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 3"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 4"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        locations["Level 5"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Level 6"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        locations["Level 7"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Level 8"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Level 9"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        locations["Level 10"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(11, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
    elif logictype == 2 or logictype == 3:
        phaselength = maxlevel//6
        l20phase = 20//phaselength
        if l20phase == 0:
            locations["Level 20 Additional"] = ("Menu", LocationProgressType.DEFAULT)
        elif l20phase == 1:
            locations["Level 20 Additional"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        else:
            locations["Level 20 Additional"] = (f"Levels with {min(l20phase, 5)} Buildings", LocationProgressType.DEFAULT)
        for x in range(2, phaselength):
            locations[f"Level {x}"] = ("Menu", LocationProgressType.DEFAULT)
        for x in range(phaselength, phaselength*2):
            locations[f"Level {x}"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        for x in range(phaselength*2, phaselength*3):
            locations[f"Level {x}"] = ("Levels with 2 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*3, phaselength*4):
            locations[f"Level {x}"] = ("Levels with 3 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*4, phaselength*5):
            locations[f"Level {x}"] = ("Levels with 4 Buildings", LocationProgressType.DEFAULT)
        for x in range(phaselength*5, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
    else:  # logictype == 4
        locations["Level 20 Additional"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        for x in range(2, maxlevel+1):
            locations[f"Level {x}"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)

    return locations


def addupgrades(finaltier: int, logictype: int) -> dict[str, tuple[str, LocationProgressType]]:
    """Returns a dictionary with all upgrade locations based on given options (finaltier INCLUDED)."""
    locations: dict[str, tuple[str, LocationProgressType]] = {}
    categories = ["Routing", "Extracting", "Shape Processing", "Color Processing"]

    for cat in categories:
        locations[f"{cat} Upgrade Tier II"] = ("Menu", LocationProgressType.PRIORITY)

    if logictype == 0:
        for cat in categories:
            locations[f"{cat} Upgrade Tier III"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        for cat in categories:
            locations[f"{cat} Upgrade Tier IV"] = ("Upgrades with 2 Buildings", LocationProgressType.DEFAULT)
        for x in range(5, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
    elif logictype == 1:
        for cat in categories:
            locations[f"{cat} Upgrade Tier III"] = ("Upgrades with 1 Building", LocationProgressType.DEFAULT)
        for x in range(4, 7):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = (f"Upgrades with {x-2} Buildings", LocationProgressType.DEFAULT)
        for x in range(7, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
    else: # logictype == 2
        for x in range(3, finaltier+1):
            for cat in categories:
                locations[f"{cat} Upgrade Tier {roman(x)}"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)

    return locations


def addachievements(include: bool, excludesoftlock: bool, excludelong: bool, excludeprogressive: bool,
                    maxlevel: int, levellogictype: int, finaltier: int, upgradelogictype: int,
                    goal: int) -> dict[str, tuple[str, LocationProgressType]]:
    """Returns a dictionary with all achievement locations based on given options."""
    locations: dict[str, tuple[str, LocationProgressType]] = {}
    phaselength = maxlevel//6
    l12phase = 12//phaselength
    l14phase = 14//phaselength
    l20phase = 20//phaselength
    l26phase = 26//phaselength
    l27phase = 27//phaselength
    l50phase = 50//phaselength
    l100phase = 100//phaselength

    if not include:
        return locations

    locations["Painter"] = ("Painted Shape Achievements", LocationProgressType.DEFAULT)
    locations["Cutter"] = ("Cut Shape Achievements", LocationProgressType.DEFAULT)
    locations["Rotater"] = ("Rotated Shape Achievements", LocationProgressType.DEFAULT)
    locations["Wait, they stack"] = ("Stacked Shape Achievements", LocationProgressType.DEFAULT)
    if levellogictype in [0, 1, 4]:
        locations["Wires"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
    else:
        if l20phase == 0:
            locations["Wires"] = ("Menu", LocationProgressType.DEFAULT)
        elif l20phase == 1:
            locations["Wires"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
        else:
            locations["Wires"] = (f"Levels with {min(l20phase, 5)} Buildings", LocationProgressType.DEFAULT)
    locations["Storage"] = ("Stored Shape Achievements", LocationProgressType.DEFAULT)
    if goal: # not goal == 0
        if levellogictype in [0, 1, 4]:
            locations["Freedom"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        else:
            if l26phase == 0:
                locations["Freedom"] = ("Menu", LocationProgressType.DEFAULT)
            elif l26phase == 1:
                locations["Freedom"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            else:
                locations["Freedom"] = (f"Levels with {min(l26phase, 5)} Buildings", LocationProgressType.DEFAULT)
    locations["The logo!"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["To the moon"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["It's piling up"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["I'll use it later"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Efficiency 1"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Preparing to launch"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["SpaceY"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Stack overflow"] = ("Stacked Shape Achievements", LocationProgressType.DEFAULT)
    locations["It's a mess"] = ("Menu", LocationProgressType.DEFAULT)
    if upgradelogictype == 1:
        locations["Faster"] = ("Upgrades with 3 Buildings", LocationProgressType.DEFAULT)
        locations["Even faster"] = ("Upgrades with 3 Buildings", LocationProgressType.DEFAULT)
    else:
        locations["Faster"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
        locations["Even faster"] = ("Upgrades with 5 Buildings", LocationProgressType.DEFAULT)
    locations["Get rid of them"] = ("Trashed Shape Achievements", LocationProgressType.DEFAULT)
    if goal > 1 or maxlevel > 50:
        if levellogictype in [0, 1, 4]:
            locations["Can't stop"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        else:
            if l50phase == 0:
                locations["Can't stop"] = ("Menu", LocationProgressType.DEFAULT)
            elif l50phase == 1:
                locations["Can't stop"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            else:
                locations["Can't stop"] = (f"Levels with {min(l50phase, 5)} Buildings", LocationProgressType.DEFAULT)
    if goal > 1 or maxlevel > 100:
        if levellogictype in [0, 1, 4]:
            locations["Is this the end?"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        else:
            if l100phase == 0:
                locations["Is this the end?"] = ("Menu", LocationProgressType.DEFAULT)
            elif l100phase == 1:
                locations["Is this the end?"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            else:
                locations["Is this the end?"] = (f"Levels with {min(l100phase, 5)} Buildings", LocationProgressType.DEFAULT)
    locations["Getting into it"] = ("Menu", LocationProgressType.DEFAULT)
    locations["Now it's easy"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Computer Guy"] = ("Wiring Achievements", LocationProgressType.DEFAULT)
    locations["Efficiency 2"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Branding specialist 1"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Branding specialist 2"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    if goal: # not goal == 0
        if levellogictype in [0, 1, 4]:
            locations["MAM (Make Anything Machine)"] = ("Levels with 5 Buildings", LocationProgressType.DEFAULT)
        else:
            if l27phase == 0:
                locations["MAM (Make Anything Machine)"] = ("Menu", LocationProgressType.DEFAULT)
            elif l27phase == 1:
                locations["MAM (Make Anything Machine)"] = ("Levels with 1 Building", LocationProgressType.DEFAULT)
            else:
                locations["MAM (Make Anything Machine)"] = (f"Levels with {min(l27phase, 5)} Buildings", LocationProgressType.DEFAULT)
    locations["Perfectionist"] = ("Menu", LocationProgressType.DEFAULT)
    locations["The next dimension"] = ("Wiring Achievements", LocationProgressType.DEFAULT)
    locations["Oops"] = ("Menu", LocationProgressType.DEFAULT)
    locations["Copy-Pasta"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["I've seen that before ..."] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["Memories from the past"] = ("All Buildings Shapes", LocationProgressType.DEFAULT)
    locations["I need trains"] = ("Menu", LocationProgressType.DEFAULT)
    locations["GPS"] = ("Menu", LocationProgressType.DEFAULT)

    if excludeprogressive:
        type = LocationProgressType.EXCLUDED
    else:
        type = LocationProgressType.DEFAULT

    if not excludesoftlock:
        if levellogictype in [0, 1, 4]:
            locations["Speedrun Master"] = ("Levels with 5 Buildings", type)
            locations["Speedrun Novice"] = ("Levels with 5 Buildings", type)
            locations["Not an idle game"] = ("Levels with 5 Buildings", type)
            locations["It's so slow"] = ("Levels with 5 Buildings", type)
            locations["King of Inefficiency"] = ("Levels with 5 Buildings", type)
        else:
            if l12phase == 0:
                locations["Speedrun Master"] = ("Menu", type)
                locations["Speedrun Novice"] = ("Menu", type)
                locations["Not an idle game"] = ("Menu", type)
                locations["It's so slow"] = ("Menu", type)
            elif l12phase == 1:
                locations["Speedrun Master"] = ("Levels with 1 Building", type)
                locations["Speedrun Novice"] = ("Levels with 1 Building", type)
                locations["Not an idle game"] = ("Levels with 1 Building", type)
                locations["It's so slow"] = ("Levels with 1 Building", type)
            else:
                locations["Speedrun Master"] = (f"Levels with {min(l12phase, 5)} Buildings", type)
                locations["Speedrun Novice"] = (f"Levels with {min(l12phase, 5)} Buildings", type)
                locations["Not an idle game"] = (f"Levels with {min(l12phase, 5)} Buildings", type)
                locations["It's so slow"] = (f"Levels with {min(l12phase, 5)} Buildings", type)
            if l14phase == 0:
                locations["King of Inefficiency"] = ("Menu", type)
            elif l14phase == 1:
                locations["King of Inefficiency"] = ("Levels with 1 Building", type)
            else:
                locations["King of Inefficiency"] = (f"Levels with {min(l14phase, 5)} Buildings", type)
        locations["A bit early?"] = ("All Buildings Shapes", type)

    if not excludelong:
        locations["It's been a long time"] = ("Menu", LocationProgressType.DEFAULT)
        locations["Addicted"] = ("Menu", LocationProgressType.DEFAULT)

    return locations


def roman(num: int) -> str:
    translate: set[tuple[int, str]] = {
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    }
    rom: str = ""
    for (key, val) in translate:
        while num > key:
            rom += val
    return rom


class ShapezLocation(Location):
    game = "Shapez"
