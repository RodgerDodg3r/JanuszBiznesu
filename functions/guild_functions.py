import os
import json

config_template = {
    "bot_channel": 0,   
    "currency": "💵PLN"
}

def guild_get_data():
    with open("./data/config.json", "r") as file:
        guild_data = json.load(file)   
    
    return guild_data


def guild_data_save(data):
    with open("./data/config.json", "w") as file:
        json.dump(data, file, indent= 4)

def guild_update_config():
    os.makedirs("./data/", exist_ok=True)
    if (not os.path.exists("./data/config.json")):
        guild_data = config_template

        with open("./data/config.json", "w") as file:
            json.dump(guild_data, file,  indent= 4)
    

    with open("./data/config.json", "r") as file:
        guild_data = json.load(file)
    
    updated = False
    for key in config_template:
        if (key not in guild_data):
            guild_data[key] = config_template[key]
            updated = True
    


    if (updated):
        guild_data_save(guild_data)



guild_update_config()