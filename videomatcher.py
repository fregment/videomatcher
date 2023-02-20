import os
from PIL import Image
import pytesseract
from time import strftime
from time import gmtime

# Assuming the extrated frames of the analyzed video are in a subfolder called "frames"
DIRECTORY = "./frames"

# Assuming each frame is 3 seconds apart
SECONDS_PER_FRAME = 3

# Define the features to look for in the frames related to the observed task (e.g. "Exploring Results" has GUI elements (words) "FINISH EXPLORE" and "FINISH OUTCOME VIEW")
GUI_FEATURES = { "Exploring Results":["FINISH EXPLORE","FINISH OUTCOME VIEW"],
                    "Editing Constraints" : ["STRUCTURAL CONSTRAINTS"],
                    "Editing Loads":["STRUCTURAL LOADS","EDIT STRUCTURAL LOAD"],
                    "Setting Preserve Geometry":["PRESERVE GEOMETRY"],
                    "Setting Obstacle Geometry":["OBSTACLE GEOMETRY"],
                    "Editing Material Options":["STUDY MATERIALS"],
                    "Editing Manufacturing Options":["MANUFACTURING"],
                    "Pre-check warning":["Cannot Generate","Some important input is missing"],
                    "Pre-check ready confirmation":["Ready to Generate","The study setup has all the information required"],
                    "Using Previewer":["Preview:"],
                    "Starting Solver":["STUDIES OF THE ACTIVE DOCUMENT"],

                    "--web: Viewing Info Sheet":["Participants Info Sheet", "FSN", "Boundary Conditions"],
                    "--web: Visiting SearchEngine":["google.com","google","duckduckgo"],
                    "--web: Visiting YouTube":["youtube.com","youtube"],
                    "--web: Visiting Autodesk site / forums":["forums.autodesk.com","autodesk.com"],
                    "--web: Visiting reddit":["reddit","reddit.com"]
                    }

# Helper variables
seconds = 0
this_frame_found = {}
last_frame_found = {}

for key in GUI_FEATURES:
    this_frame_found[key] = False
    last_frame_found[key] = False


filenames = os.listdir(DIRECTORY)
sorted_filenames = filenames
sorted_filenames = sorted(filenames, key=lambda x: int(x.split('.')[0]) if x.endswith(".jpg") else 0)

print(f"Events found in {DIRECTORY}")
for filename in sorted_filenames:
    if filename.endswith(".jpg"):

        filepath = os.path.join(DIRECTORY, filename)
        # print(filepath)
        seconds += SECONDS_PER_FRAME
        time = strftime("%H:%M:%S", gmtime(seconds))

        ocr_res = pytesseract.image_to_string(filepath)

        for feature in GUI_FEATURES:
            search_terms = GUI_FEATURES[feature]

            this_frame_found[feature] = False
            if any(x in ocr_res for x in search_terms):
                # print(f"Found: {feature}")
                this_frame_found[feature] = True

            if last_frame_found[feature] is False and this_frame_found[feature] is True:
                timestamp = f"{time} \t\t{feature}"
                print(timestamp)
            last_frame_found[feature] = this_frame_found[feature]

# End of script