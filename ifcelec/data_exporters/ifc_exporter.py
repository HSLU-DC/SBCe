import ifcopenshell

def ifc_exporter(ifc_file, components_per_room, out_path, config_level):
    # Export IFC Data
    file = ifcopenshell.open(ifc_file)
    owner_history = file.by_type("IfcOwnerHistory")[0]
    products = file.by_type("IfcProduct")
    spaces =[]
    for i in products:
        if i.is_a("IfcSpace"):
            spaces.append(i)

    #spaces = file.by_type("IfcSpace")
    for space in spaces:
        room_name = space.get_info()["LongName"]
        for roomname in components_per_room[config_level]:
            #print(room_name, roomname)
            if roomname == room_name:
                for type, components in components_per_room[config_level][roomname].items():
                    component = components
                    try:
                        name = components['n']
                        if components['n']:
                            del component['n']
                    except:
                        pass
                    component = components
                    result = [f'{k}: {v}' for k, v in component.items()]
                    result_string = ', '.join(result)
                    #print(result_string)
                    property_values = [
                        file.createIfcPropertySingleValue(str(name), str(name), file.create_entity("IfcText", str(result_string)), None),
                    ]   
                    
                    property_set = file.createIfcPropertySet(space.GlobalId, owner_history, str(f"IFCELEC_{type}"), None, property_values)
                    file.createIfcRelDefinesByProperties(space.GlobalId, owner_history, None, None, [space], property_set)

    file.write(out_path + "output.ifc")
