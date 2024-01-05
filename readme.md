# Project Name

IFCelec   [![pipeline status](https://gitlab.casacaotica.ch/timo/ifcelec/badges/main/pipeline.svg)](https://gitlab.casacaotica.ch/timo/ifcelec/-/commits/main) [![Latest Release](https://gitlab.casacaotica.ch/timo/ifcelec/-/badges/release.svg)](https://gitlab.casacaotica.ch/timo/ifcelec/-/releases)


## Installation

Run:

<code>
pip install -r requirements.txt

python main.py-h
</code>


## Usage

Run this project usinf the code above. You can add parameters with the help given by running it with `-h` or `--help`

## Functionality

### `main.py`

This file is the main entry point of the project. It contains the following functions:

#### `main()`

This function uses all sub-modules to import all needed Information, correlate them and create the finished IFC file

##### Global Variables

<i>

- `var1` (Type): Description ov Variable: `Default Structure and Content (if applicable)`

</i>

- `glb_ifc_rooms` (Dict): All Room as defined in the IFC Files: `RoomNumber: RoomName`
- `glb_data_presets` (Dict(Dict)): Room Book per Config Level. List of Room Type Containing the Component Type and Amount: `{'Bathroom': {DSI40: 2}}`
- `glb_components` (Dict(List(Dict))): All Components as defined in the given Excel Sheet: `{'lamps': [{'n': 1, 'classification': 'DSI40', 'useability': 'Korridore/Wohnen', 'brand': 'Luxion', 'art_n': 'LUX-2183040-HS7-WM', 'power': 7, 'price': 66}]}`
- `glb_user_conf` (Dict): User Configuration as defined in Excel Sheet: `{'Canton': 'Zurich'}`
- `glb_conf_lvl` (Int): Configuration Level as chosen by user. `3`
- `glb_ifc_path` (Path): Input IFC File Path: `"./ARC_Modell_NEST_230328.ifc"`
- `glb_conf_path` (Path): User Configuration and RoomBooks Excel Sheet Path: `"./Konfigurator.xlsx"`
- `glb_parts_path` (Path): Components Excel Sheet Path: `"./Praxismodul_DC_GEE/Bauteilliste_Elektro.xlsx"`
- `glb_out_path` (Path): Output Path of IFC: `"./Output.ifc"`

### `other_file.py`

This file contains the following functions:

#### `function_name(arg1, arg2)`

This function does Y.

##### Parameters

- `arg1` (type): Description of arg1.
- `arg2` (type): Description of arg2.

##### Returns

- `return_value` (type): Description of return value.

## CI Status

The current status of the CI pipeline can be found at 
[![pipeline status](https://gitlab.casacaotica.ch/timo/ifcelec/badges/main/pipeline.svg)](https://gitlab.casacaotica.ch/timo/ifcelec/-/commits/main).