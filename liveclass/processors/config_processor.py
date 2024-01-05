import pandas as pd 
import os

import helpers.data_helpers as hlp  # Import the helper functions

# Global variables:

conf_lst = []

#Start Function

def read_source_data():
    print("Start: Reading source data")

    source_folder = input("Please enter the path to the source folder:  ")
    if str(source_folder[-4] + source_folder[-3] + source_folder[-2] + source_folder[-1]) == "xlsx": 
        xls_file = source_folder
    else:
        xls_file_name = "Elementplan.xlsx"
        xls_file = os.path.join(source_folder, xls_file_name)
    print("Reading file: " + xls_file)
    check_file = os.path.isfile(xls_file)
    if check_file == True:
        print("File exists")
        xls_df = pd.read_excel(xls_file)
        print(xls_df)
        s_data_category = pd.read_excel(xls_file, sheet_name="Objektkatalog")
        s_data_attributes = pd.read_excel(xls_file, sheet_name="Attributsliste")
        col_count = len(s_data_category.columns)
        row_count = len(s_data_category.columns)  

        for index, row in s_data_category.iterrows():
            if col_count > 3:
                for gr in range(3, col_count): # Loop through the columns of the category sheet
                     attr_group_conf = s_data_category.iloc[index, gr] # Get the value of the current column
                     if str(attr_group_conf).lower() == "x": # Check if the value is "x"
                        current_attr_group = s_data_attributes[s_data_attributes["Gruppe"] == s_data_category.columns[gr]] # Filter the attributes for the current group
                        print(current_attr_group)  

                        prop_list = []

                        for _i, _r in current_attr_group.iterrows(): # Loop through the attributes of the current group

                            p_h = hlp.Prop_Holder(_r["Pset"], _r["Property"], _r["Gruppe"]) # Create a new property holder object
                            prop_list.append(p_h) # Add the property holder object to the list

                        _target_object = hlp.filterConfig(row["Branch"], conf_lst) # Check if the current object already exists in the configuration list

                        if _target_object != None:
                            print("Adding to Configuration: ")
                            print("Klasse: " + row["IfcClass"])

                            _target_object.prop_list.extend(prop_list) # Add the list of properties to the target object

                        else:
                            print("Creating new Configuration: ")
                            print("Klasse: " + row["IfcClass"])

                            d_h = hlp.Data_Holder(prop_list, row["Branch"], row["IfcClass"], row["Quelle"], source_folder) # Create a new data holder object
                            conf_lst.append(d_h) # Add the data holder object to the configuration list
                            
                        print("Finished Creating Configuration")
    else:
        print("File does not exist")
        exit()

    return conf_lst, source_folder




