def total_costs(glb_components_per_room):
    total_costs = {}
    #print(glb_components_per_room)
    for config_level, roomconfigs in glb_components_per_room.items():
        total_costs[config_level] = 0
        for room, roomconfig in roomconfigs.items():
            for type, component in roomconfig.items():
                if component['price'] == "na" or component['price'] == "-":
                    continue
                try:
                    total_costs[config_level] += (int(component['amount'] * int(component['price'])))
                except ValueError:
                    pass
    return total_costs

def total_costs_per_room(glb_components_per_room):
    total_costs_per_room = {}
    for config_level, roomconfigs in glb_components_per_room.items():
        total_costs_per_room[config_level] = {}
        for room, roomconfig in roomconfigs.items():
            total_costs_per_room[config_level][room] = 0
            for type, component in roomconfig.items():
                if component['price'] == "na" or component['price'] == "-":
                    continue
                try:
                    total_costs_per_room[config_level][room] += (int(component['amount'] * int(component['price'])))
                except ValueError:
                    pass
    return total_costs_per_room