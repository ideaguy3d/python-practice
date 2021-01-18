from pathlib import Path
import csv
import json
import os
import re
from collections import OrderedDict
import subprocess
import pprint
import pandas


pretty_print = pprint.PrettyPrinter(indent=4)

# Paths
ROOT_DIR = Path("/Users/jhernandez/Documents/Annotation_folder")
# Paths to source data
CSV_PATH = ROOT_DIR / "Bubbly_Report.csv"
VIDEO_DIR = Path("/Users/jhernandez/Box/Bubbly_Transperfect/Deliveries/20201229")
POSTER_DIR = Path("/Users/jhernandez/Box/P2_posters_full_info")
# Paths to generated data
CONFIG_DIR = ROOT_DIR / "config"
STATUS_PATH = ROOT_DIR / "status.csv"
ANNOTATION_DIR = ROOT_DIR / "annotations"
# Annotation tool binary
GT_TOOL_PATH = "/Users/jhernandez/Documents/Annotation_folder/ODTApps_Object3dGroundTruthTool.app/Contents/MacOS/ODTApps_Object3dGroundTruthTool"

# Status CSV Fields
STATUS_FIELDS = OrderedDict([
    ("video", "str"),
    ("poster", "str"),
    ("appcode", "str_list"),  # List of | separated strings
    ("poster_width_px", "int"),
    ("poster_height_px", "int"),
    ("appcode_width_px", "int_list"),  # List of | separated ints
    ("appcode_x_px", "int_list"),  # List of | separated ints
    ("appcode_y_px", "int_list"),  # List of | separated ints
    ("poster_width_meters", "float"),
    ("poster_height_meters", "float"),
    ("status", "str"),
    ("frames_processed", "int"),
    ("frames_tracked", "int"),
    ("frames_tracked_percent", "int"),  # % tracked out of processed frames
    ("notes", "str")
])

# Source CSV Column Names
VIDEO_COL = "Captured Video name"
POSTER_COL = "Poster Used (Copy/Paste the Name for file used)"
POSTER_WIDTH_COL = "Poster width (in millimeter accuracy)"
POSTER_HEIGHT_COL = "Poster height (in millimeter accuracy)"

print('\n\nEllo World ^_^/')

x = 5
print(f'\n x = {x} \n\n')

posters = []
for i in POSTER_DIR.iterdir():
    posters.append(i)

debug = 1

# end of file