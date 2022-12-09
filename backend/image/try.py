import cv2
import pyocr
import sys
from PIL import Image
image = "moji.png"

img = cv2.imread(image)
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
res = tool.image_to_string(
    Image.open("moji.png")
    ,lang="eng")

print(res)