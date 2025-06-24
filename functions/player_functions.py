import os
import json
import time

player_config_tempate = {
    "money": 0,
    "last_update": time.time(),

    "buildings": {
        "Promotor klubu swingersów": {
            "quantity": 0,
            "cost": 800,
            "per_h": 18,
            "description": "Załatwia wejściówki, gumki i awantury małżeńskie w pakiecie.",
        },
        "Sklep Ropucha": {
            "quantity": 0,
            "cost": 1500,
            "per_h": 40,
            "description": "Oficjalny dystrybutor dziwnych zapachów i nielegalnych Vibovitów.",       
        },
        "Solarium Shalom": {
            "quantity": 0,
            "cost": 2500,
            "per_h": 65,
            "description": "Kiedyś palono ludzi dla idei. Teraz – dla 19.99 zł/h.”"
        },
        "Dom pogrzebowy 'Do piachu'": {
            "quantity": 0,
            "cost": 6000,
            "per_h": 170,
            "description": "Zakopią cię z klasą albo przynajmniej z plastikowym wieńcem z Biedronki."
        },
        "Labolatorium Czeskiej mety": {
            "quantity": 0,
            "cost": 15000,
            "per_h": 500,
            "description": "Zarobisz albo oślepniesz. Albo jedno i drugie."
        }
    }
}


def player_get_profit(player_id):

    player_data = player_get_data(player_id)
    profit_per_h = 0
    for key in player_data["buildings"]:
        if (player_data["buildings"][key]["quantity"] > 0):
            profit_per_h = profit_per_h + (player_data["buildings"][key]["per_h"] * player_data["buildings"][key]["quantity"])
    

    return profit_per_h


def player_get_data(player_id):
    with open(f"./data/players/{player_id}.json", "r") as file:
        return json.load(file)

def player_update_config(player_id):
    os.makedirs("./data/players", exist_ok=True)

    if (not os.path.exists(f"./data/players/{player_id}.json")):
        player_data = player_config_tempate

        with open(f"./data/players/{player_id}.json", "w") as file:
            json.dump(player_data, file,  indent= 4)
        
    

    with open(f"./data/players/{player_id}.json", "r") as file:
        player_data = json.load(file)
    
    updated = False
    for key in player_config_tempate:
        if (key not in player_data and key != "buildings"):
            player_data[key] = player_config_tempate[key]
            updated = True
        
        if (key == "buildings"):

            for key_building in player_config_tempate["buildings"]:

                if (key_building not in player_data["buildings"]):
                    player_data["buildings"][key_building] = player_config_tempate["buildings"][key_building]
                    updated = True
        

    if (updated):
        player_save_data(player_id, player_data)

def player_save_data(player_id, player_data):
    with open(f"./data/players/{player_id}.json", "w") as file:
        json.dump(player_data, file,  indent= 4)