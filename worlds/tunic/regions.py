from typing import Dict, Set

tunic_regions: Dict[str, Set[str]] = {
    "Menu": {"Overworld"},
    "Overworld": {"Overworld Holy Cross", "East Forest", "Dark Tomb", "Beneath the Well", "West Garden",
                  "Ruined Atoll", "Eastern Vault Fortress", "Beneath the Vault", "Quarry Back", "Quarry", "Swamp",
                  "Spirit Arena"},
    "Overworld Holy Cross": set(),
    "East Forest": set(),
    "Dark Tomb": {"West Garden"},
    "Beneath the Well": set(),
    "West Garden": set(),
    "Ruined Atoll": {"Frog's Domain", "Library"},
    "Frog's Domain": set(),
    "Library": set(),
    "Eastern Vault Fortress": {"Beneath the Vault"},
    "Beneath the Vault": {"Eastern Vault Fortress"},
    "Quarry Back": {"Quarry"},
    "Quarry": {"Lower Quarry"},
    "Lower Quarry": {"Rooted Ziggurat"},
    "Rooted Ziggurat": set(),
    "Swamp": {"Cathedral"},
    "Cathedral": set(),
    "Spirit Arena": set()
}


tunic_ladder_regions: Dict[str, Set[str]] = {
    "Menu": {"Overworld"},
    "Overworld": {"Dark Tomb Front", "West Garden", "Ruined Atoll", "Beneath the Well", "Beneath the Well Back",
                  "Quarry", "Swamp", "Back of Swamp", "Spirit Arena", "Sealed Temple", "East Overworld",
                  "Upper Overworld", "Overworld Holy Cross", "East Forest", "Overworld Beach"},
    "Overworld Holy Cross": set(),
    "East Forest": {"Lower Forest"},
    "Lower Forest": set(),
    "East Overworld": {"East Forest", "Eastern Vault Fortress", "Beneath the Vault"},
    "Upper Overworld": {"Quarry Back", "Sealed Temple"},
    "Overworld Beach": {"West Garden", "Ruined Atoll"},
    "Dark Tomb Front": {"Dark Tomb"},
    "Dark Tomb": {"West Garden"},
    "Beneath the Well": {"Beneath the Well Back"},
    "Beneath the Well Back": {"Beneath the Well"},
    "West Garden": {"Overworld Beach"},
    "Ruined Atoll": {"Frog's Domain", "Library"},
    "Frog's Domain": set(),
    "Library": set(),
    "Eastern Vault Fortress": {"Beneath the Vault"},
    "Beneath the Vault": {"Eastern Vault Fortress"},
    "Quarry Back": {"Quarry"},
    "Quarry": {"Lower Quarry"},
    "Lower Quarry": {"Rooted Ziggurat"},
    "Rooted Ziggurat": set(),
    "Swamp": {"Swamp Middle"},
    "Swamp Middle": {"Cathedral"},
    "Cathedral": {"Back of Swamp"},
    "Back of Swamp": set(),
    "Spirit Arena": set(),
    "Sealed Temple": set()
}
