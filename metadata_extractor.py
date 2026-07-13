from PIL import Image
from PIL.ExifTags import TAGS

# Open image
image = Image.open("sample.jpg.jpg")

# Get EXIF data
exif_data = image.getexif()

print("===== IMAGE METADATA =====")

if exif_data:
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
else:
    print("No EXIF metadata found.")
