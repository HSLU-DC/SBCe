import pandas as pd 
import os

# Ignore warnings
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

def conf_test(value):
    if str(value).lower() == "ja":
        return True
    else:
        return False

#Start Function

def read_source_data(source_path):

    print("\tReading Excel: " + source_path)
    check_file = os.path.isfile(source_path)
    if check_file == True:
        print("\tFile exists")
        print("\tReading user configuration")
        s_data_informationen = pd.read_excel(source_path, sheet_name="Infomationen")
        # Extract the information from the excel file
        # General Informartion
        canton = s_data_informationen.iloc[1, 2]
        district = s_data_informationen.iloc[2, 2]
        floors = s_data_informationen.iloc[3, 2]
        rooms = s_data_informationen.iloc[4, 2]
        persons = s_data_informationen.iloc[5, 2]
        energyefficiency = s_data_informationen.iloc[6, 2]
        config_lvl = s_data_informationen.iloc[7, 2]

        # Building Information
        useable_roof_lenght = s_data_informationen.iloc[0, 6]
        useable_roof_width = s_data_informationen.iloc[1, 6]
        useable_roof_area = useable_roof_width * useable_roof_lenght
        if s_data_informationen.iloc[2, 6] == "Flachdach":
            roof_form = "flat"
        else:
            roof_form = "angled"
        if s_data_informationen.iloc[0, 10] == "Sole/Wasser-Wärmepumpensystem":
            heating_warmwater = "sole"
        else:   
            heating_warmwater = "air"

        # Optional Information
        ventilation =  conf_test(s_data_informationen.iloc[0, 14])
        photovoltaic = conf_test(s_data_informationen.iloc[1, 14])
        lightning_protection = conf_test(s_data_informationen.iloc[2, 14])
        bas = conf_test(s_data_informationen.iloc[3, 14])
        type_bas = s_data_informationen.iloc[4, 14]
        e_mobility = conf_test(s_data_informationen.iloc[5, 14])
        smart_metering = conf_test(s_data_informationen.iloc[6, 14])
        smart_gardening = conf_test(s_data_informationen.iloc[7, 14])
        fire_alarm_system = conf_test(s_data_informationen.iloc[8, 14])
        burglar_alarm_system = conf_test(s_data_informationen.iloc[9, 14])
        geothermal_probes = conf_test(s_data_informationen.iloc[10, 14])
        Audiosystem = conf_test(s_data_informationen.iloc[11, 14])

        # Create a dictionary with the information
        user_information = {
            "canton": canton,
            "district": district,
            "floors": floors,
            "rooms": rooms,
            "persons": persons,
            "energyefficiency": energyefficiency,
            "config_lvl": config_lvl,
            "useable_roof_width": useable_roof_width,
            "useable_roof_lenght": useable_roof_lenght,
            "useable_roof_area": useable_roof_area,
            "roof_form": roof_form,
            "heating_warmwater": heating_warmwater,
            "ventilation": ventilation,
            "photovoltaic": photovoltaic,
            "lightning_protection": lightning_protection,
            "bas": bas,
            "type_bas": type_bas,
            "e_mobility": e_mobility,
            "smart_metering": smart_metering,
            "smart_gardening": smart_gardening,
            "fire_alarm_system": fire_alarm_system,
            "burglar_alarm_system": burglar_alarm_system,
            "geothermal_probes": geothermal_probes,
            "Audiosystem": Audiosystem
        }
        print("\tUser Information imported\n")

    else:
        print("\033[1m" + "File does not exist!")
        exit()

    return user_information

def get_roombook(source_path):
    roombooks = {}
    print("\tReading Excel: " + source_path)
    check_file = os.path.isfile(source_path)
    if check_file == True:
        print("\tFile exists")
        print("\tReading Roombooks")
        sheet = pd.read_excel(source_path, sheet_name="Raumaustattung")
        for config_level in range(0, 4):
            print("\t\tReading Roombook for config level " + str(config_level+1))
            conv_lvl = {}
            for room in range(1, 18):
                #print("\t\tReading Roombook for config level " + str(config_level+1) + ": " + str(sheet.iloc[4, config_level*17+11+room]))
                dict = []
                for i in range(7, sheet.shape[0]):
                    if str(sheet.iloc[i, 1]) != 'nan' and str(sheet.iloc[i, 1]) != "Total":
                        component = [
                            next((sheet.iloc[i - x, 2] for x in range(1, 10) if pd.isna(sheet.iloc[i - x, 1]) and not pd.isna(sheet.iloc[i - x, 2])), None),
                            sheet.iloc[i, 1],
                            sheet.iloc[i, 2]
                            #sheet.iloc[i, 3]
                        ]

                        if str(sheet.iloc[i, config_level*17+11+room]) != "nan":
                            dict.append((component, sheet.iloc[i, config_level*17+11+room]))
                conv_lvl[str(sheet.iloc[4, config_level*17+11+room])] = dict
            roombooks[config_level+1] = conv_lvl
    print("\tRoombooks imported" + "\n")
    return roombooks

if __name__ == "__main__":
    print(get_roombook("./Konfigurator.xlsx"))