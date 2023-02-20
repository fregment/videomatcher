# text recognition
from PIL import Image
import pytesseract
import re

ocr_res = pytesseract.image_to_string('autodesk_forum.jpg').lower()

print(ocr_res)

if any(x in ocr_res for x in ["autodesk","forums.autodesk.com"]):
    print("YES")
else:
    print("NO")



# if "autodesk" in res.lower() or "forums.autodesk.com" in res.lower():
#     print("Autodesk forum: Yes")
# else:
#     print("Autodesk forum: No")
#
#
# print("------")
#
# if "google" in res.lower() or "google.com" in res.lower():
#     print("Google: Yes")
# else:
#     print("Google: No")
#
# print("------")
#
# if "youtube.com" in res.lower():
#     print("YouTube: Yes")
# else:
#     print("YouTube: No")
#
# print("------")
#
# if "reddit" in res.lower():
#     print("Reddit: Yes")
# else:
#     print("Reddit: No")
#
# print("------")
