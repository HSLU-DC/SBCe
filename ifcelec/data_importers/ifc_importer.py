# ifc_importer.py
import ifcopenshell
import os
from dataclasses import dataclass

def read_source_ifc(source_path):
    print("\tReading IFC: " + source_path)
    check_file = os.path.isfile(source_path)

    if check_file:
        print("\tFile exists")
        print("\tReading room information")

        file = ifcopenshell.open(source_path)
        products = file.by_type("IfcProduct")
        spaces =[]
        for i in products:
            if i.is_a("IfcSpace"):
                spaces.append(i)

        room_list = []

        for room in spaces:
            values =ifcopenshell.util.element.get_psets(room, qtos_only=True)
            room_info = Room(
                name=room.get_info()["LongName"],
                site=getBuilding(room),
                story=getStorey(room),
                guid=room.get_info()["GlobalId"],
                area=values["BaseQuantities"]["NetFloorArea"],
                volume=values["BaseQuantities"]["GrossVolume"],
                windows=None,
                doors=None,
                other_openings=None
            )
            room_list.append(room_info)

    else:
        print("\033[1m" + "File does not exist!")
        exit()

    print("\tRoomlist from IFC imported\n")
    #print(room_list)
    return room_list

@dataclass
class Room:
    name: str
    area: float = None
    windows: list = None
    doors: list = None
    other_openings: list = None
    volume: float = None
    site: str = None
    story: str = None
    guid: str = None
    

def getStorey(ele):
    lev_name = ""

    if ele.is_a('IfcSpatialStructureElement'):
        lev_name = ele.Decomposes[0][4].Name
    else:
        lev_obj = ifcopenshell.util.element.get_container(ele)
        lev_name = lev_obj.Name

    return lev_name

def getBuilding(ele):

    building_name = ""

    if ele.is_a('IfcSpatialStructureElement'):
        lev_obj = ele.Decomposes[0][4]

    else:
        lev_obj = ifcopenshell.util.element.get_container(ele)

    building_obj = lev_obj.Decomposes[0][4]
    building_name = building_obj.Name

    return building_name


if __name__ == "__main__":
    read_source_ifc("./ARC_Modell_NEST_230328.ifc")
