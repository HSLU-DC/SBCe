import pandas as pd
import os

# Ignore warnings
# import warnings
# warnings.simplefilter(action='ignore', category=UserWarning)

#Start Function

def read_component_data(source_path):

    components = {}

    print("\tReading Excel: " + source_path)
    check_file = os.path.isfile(source_path)
    if check_file == True:
        print("\tFile exists")
        print("\tImporting Components:")

        #Import all Lamps
        print("\t\tImporting Lamps")
        s_component_lights = pd.read_excel(source_path, sheet_name="Leuchten")
        lamps = []
        for i in range(2, len(s_component_lights.columns)):
            classification = s_component_lights.iloc[0, i]
            if classification == "na":
                pass
            else:
                #Read all Component information
                useability = s_component_lights.iloc[2, i]
                brand = s_component_lights.iloc[4, i]
                art_n = s_component_lights.iloc[8, i]
                power = s_component_lights.iloc[12, i]
                price = s_component_lights.iloc[28, i]
                attr = {
                    "n": i-1,
                    "classification": classification,
                    "useability": useability,
                    "brand": brand,
                    "art_n": art_n,
                    "power": power,
                    "price": price
                }
                lamps.append(attr)
        components["lamps"] = lamps

        #Import all Switches
        print("\t\tImporting Switches")
        s_component_switch = pd.read_excel(source_path, sheet_name="Taster_Schalter")
        switches = []
        for i in range(2, len(s_component_switch.columns)):
            classification = s_component_switch.iloc[1, i]
            if classification == "na":
                pass
            else:
                #Real all Component information
                useability = s_component_switch.iloc[0, i]
                brand = s_component_switch.iloc[3, i]
                art_n = s_component_switch.iloc[7, i]
                price = s_component_switch.iloc[9, i]
                attr = {
                    "n": i-1,
                    "classification": classification,
                    "useability": useability,
                    "brand": brand,
                    "art_n": art_n,
                    "price": price
                }
                switches.append(attr)
        components["switches"] = switches

        #Import all sensors
        print("\t\tImporting sensors")
        s_component_sensor = pd.read_excel(source_path, sheet_name="Sensoren")
        sensors = []
        for i in range(2, len(s_component_sensor.columns)):
            classification = s_component_sensor.iloc[2, i]
            if classification == "na":
                pass
            else:
                #Real all Component information
                useability = s_component_sensor.iloc[1, i]
                brand = s_component_sensor.iloc[4, i]
                art_n = s_component_sensor.iloc[6, i]
                price = s_component_sensor.iloc[9, i]
                attr = {
                    "n": i-1,
                    "classification": classification,
                    "useability": useability,
                    "brand": brand,
                    "art_n": art_n,
                    "price": price
                }
                sensors.append(attr)
        components["sensors"] = sensors

        #Import all plugs
        print("\t\tImporting Plugs")
        s_component_plugs = pd.read_excel(source_path, sheet_name="Steckdosen")
        plugs = []
        for i in range(2, len(s_component_plugs.columns)):
            classification = s_component_plugs.iloc[0, i]
            if classification == "na":
                pass
            else:
                #Real all Component information
                useability = s_component_plugs.iloc[3, i]
                brand = s_component_plugs.iloc[1, i]
                art_n = s_component_plugs.iloc[2, i]
                price = s_component_plugs.iloc[5, i]
                attr = {
                    "n": i-1,
                    "classification": classification,
                    "useability": useability,
                    "brand": brand,
                    "art_n": art_n,
                    "price": price
                }
                plugs.append(attr)
        components["plugs"] = plugs
                
    else:
        print("\033[1m" + "File does not exist!")
        exit()
    #print(components)
    print("\tComponents partially imported\n")
    return(components)
    
if __name__ == "__main__":
    read_component_data("./Praxismodul_DC_GEE/Bauteilliste_Elektro.xlsx")