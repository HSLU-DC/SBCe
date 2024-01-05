def get_config_lvl():
    x = 1
    while x == 1:
        glb_conf_lvl = (input("\tPlease enter the configuration level (1 - 4): "))
        try:
            glb_conf_lvl = int(glb_conf_lvl)
            if glb_conf_lvl >= 1 and glb_conf_lvl <= 4:
                x = 0
                print("\n")
            else:
                print("Invalid Input, try again")
        except:
            print("Invalid Input, try again")
    return glb_conf_lvl