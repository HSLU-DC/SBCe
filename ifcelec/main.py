import data_importers.excel_importer as e_imp
import data_importers.ifc_importer as i_imp
import data_importers.component_importer as c_imp
import data_importers.config_lvl as conf_lvl

import data_processors.roomtypes as roomtypes
import data_processors.components_per_room as cpr
import data_processors.costs as costs
import helpers.parser as parser
#import data_exporters.excel_exporter as e_exp
import data_exporters.ifc_exporter as i_exp
import data_exporters.excel_exporter as e_exp
import time

#Main Function
def main():
    start_time = time.time()
    # Global Variables
    glb_ifc_rooms = []
    glb_data_presets = []
    glb_components = []
    glb_user_conf = []
    glb_conf_lvl = 3
    glb_roomtypes = {}

    #Helper Functions
    #print(parser.script_args.path_conf)
    #print(str(type(parser.script_args.path_conf)))

    glb_ifc_path = parser.script_args.path_ifc
    glb_conf_path = parser.script_args.path_conf
    glb_parts_path = parser.script_args.path_parts
    glb_conf_lvl = parser.script_args.config_level
    glb_out_path = parser.script_args.path_out

    # Start Information
    start_information()

    # Import Excel Data
    print("- Importing Excel Data")
    glb_user_conf = e_imp.read_source_data(glb_conf_path)
    if glb_user_conf['config_lvl'] != 0:
        glb_conf_lvl = glb_user_conf['config_lvl']
    #print(glb_user_conf)

    # Import IFC Data
    print("- Importing IFC Data")
    glb_ifc_rooms = i_imp.read_source_ifc(glb_ifc_path)
    #print(glb_ifc_rooms)

    #Import Components
    print("- Importing Components")
    glb_components = c_imp.read_component_data(glb_parts_path)
    #print(glb_components)

    # Get Config Level
    if glb_conf_lvl == 0:
        print("- Getting Configuration Level")
        glb_conf_lvl = conf_lvl.get_config_lvl()

    #Get Roombook by Config Level
    print("- Getting Roombooks")
    glb_data_presets = e_imp.get_roombook(glb_conf_path)

    #Get Roomtype by Rooname
    print("- Getting Roomtype by Room name")
    glb_roomtypes = roomtypes.roomtypes(glb_ifc_rooms, glb_conf_path)

    #Get Needed Components by Roombook and Roomtype
    print("- Getting Needed Components by Roombook and Roomtype")
    glb_components_per_roomtype = cpr.get_needed_components_per_roomtype(glb_data_presets, glb_roomtypes)

    #Get Components by Room
    print("- Getting Components by Room")
    glb_components_per_room = cpr.get_components_for_components_per_roomtype(glb_components_per_roomtype, glb_components)

    #Calculate Costs
    print("- Calculating Costs\n")
    glb_total_costs = costs.total_costs(glb_components_per_room)
    glb_total_costs_per_room = costs.total_costs_per_room(glb_components_per_room)

    #Print Results
    print("- Printing Results")
    print("\n-----\n")
    print("Total Costs per Config Level: ")
    for lvl, cost in glb_total_costs.items():
        if cost == 0:
            print(f'\t Config Level {lvl}: No Components found')
            continue
        print(f'\t Config Level {lvl}: {cost} CHF')
    print("\nTotal Costs per Room: ")
    for config_level, roomconfigs in glb_total_costs_per_room.items():
        if glb_total_costs[config_level] == 0:
            print(f'\n\t Config Level {config_level}: No Components found')
            continue
        print(f'\n\t Config Level {config_level}: ')
        for room, cost in roomconfigs.items():
            if cost == 0:
                print(f'\t\t {room}: No Components found')
                continue
            print(f'\t\t {room}: {cost} CHF')
    print("\n-----\n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Script execution time: {elapsed_time} seconds")

    #Export IFC Data

    print("- Exporting IFC Data")
    i_exp.ifc_exporter(glb_ifc_path, glb_components_per_room, glb_out_path, glb_conf_lvl)

    #Export Excel Data
    #print("- Exporting Excel Data")
    #e_exp.excel_exporter(glb_ifc_path, glb_components_per_room, glb_out_path, glb_conf_lvl)


# Helper Functions
def start_information():
    print("----- \nWelcome to the Smart Home Configurator\n-----\n")


if __name__ == "__main__":
    main()