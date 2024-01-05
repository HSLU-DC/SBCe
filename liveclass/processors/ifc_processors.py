import ifcopenshell as ios
import os

export_lst = []

def process_ifc_data(conf_lst):

    for c in conf_lst:
        source_folder  = c.source_folder
        source_file = c.source
        source_path = os.path.join(source_folder, source_file)
        check_file = os.path.isfile(source_path)
        if(check_file):
            print("File exists")
            ifc_file = ios.open(source_path)
            print(ifc_file.by_type(c.data))
        else:
            print("File " + source_path + " does not exist")
    return True