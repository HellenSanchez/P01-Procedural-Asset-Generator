# P01-Procedural-Asset-Generator

A procedural chair generator built with Python, PySide6, and Autodesk Maya. Generates different chair designs based on customizable user parameters.

# GitHub Repository

https://github.com/HellenSanchez/P01-Procedural-Asset-Generator.git

# Features

- Adjustable seat, leg, cushion, and backrest dimensions.
- Customizable apron position.
- Procedural furniture generation based on user parameters.

# Challenge Features

- Added a QComboBox with multiple chair presets, including Floating Apron Chair, Wide Chair (Bench Style), Lounge Chair, and an additional Bed option.
- Added a custom group naming option that allows users to change the name of the generated object's group. When the checkbox is unchecked, the group name automatically returns to its original name, chair_GRP.
- Added a Reset button that restores all parameters and settings to the original chair configuration.

# How to Run

1. Place chair_generator.py in a folder that Maya can access.
2. Open Maya Script Editor.
3. Select the Python tab and run the following commands:

import chair_generator
import importlib

importlib.reload(chair_generator)

win = chair_generator.ChairGeneratorGUI()
win.show()

# Additional Note

- This project was developed using PySide6 instead of PySide2, following the version used in class.
