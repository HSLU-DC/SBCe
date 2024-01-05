from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("-c", "--config-level", help="Input the prefered Config Level", type=int, default=3)
arg_parser.add_argument("-p-ifc", "--path-ifc", help="IFC Path", type=str, default="./ARC_Modell_NEST_230328.ifc")
arg_parser.add_argument("-p-conf", "--path-conf", help="Config Path", type=str, default="./excel view/Konfigurator.xlsx")
arg_parser.add_argument("-p-parts", "--path-parts", help="Parts Path", type=str, default="./excel view/Bauteilliste_Elektro.xlsx")
arg_parser.add_argument("-p-out", "--path-out", help="Output Path", type=str, default="./out/")
arg_parser.add_argument("-w", "--web", help="Serve Web Page", action="store_true")
#arg_parser.add_argument("-m", "--matrix-path", help="Room Type Matrix Path", type=str, default="./naming.xlsx")

script_args = arg_parser.parse_args()

#   glb_out_path = "./output.ifc"
#   glb_ifc_path = "./ARC_Modell_NEST_230328.ifc"
#   glb_conf_path = "./excel_view/Konfigurator.xlsx"
#   glb_parts_path = "./excel_view/Bauteilliste_Elektro.xlsx"