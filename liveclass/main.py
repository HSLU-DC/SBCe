import processors.config_processor as config_p
import processors.ifc_processors as ifc_p
#Global Lists

glb_conf_lst = []
glb_conf_folder = ""


def start_func():
    print("Start der Hauptfunktion")

    # Step 1; Read Config File

    glb_conf_set = config_p.read_source_data()
    glb_conf_lst = glb_conf_set[0]
    glb_conf_folder = glb_conf_set[1]

    print(glb_conf_lst)
    print(glb_conf_folder)

    # Step 2; Read IFC File
    ifc_p.process_ifc_data(glb_conf_lst)
    

    # Step 3; Export data to Excel /Users/ftimo/Library/CloudStorage/OneDrive-HochschuleLuzern/Studium/Module/3. Semester/programming/ifcelec/liveclass/Elementplan.xlsx

if __name__ == "__main__":
    start_func()