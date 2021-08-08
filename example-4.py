"""
Convert images to JPEG and resize them to match the upper bound.
"""

import os
import sys

from PIL import Image, UnidentifiedImageError

if len(sys.argv) != 3:
    print("Usage: 'example-4.py <directory-with-images> <max-side-pixels>'.")
    sys.exit()

raw_directory = sys.argv[1]
if not os.path.exists(raw_directory):
    print(f"Error: The directory '{raw_directory}' was not found.")
    sys.exit()

try:
    max_size = int(sys.argv[2])
except ValueError:
    print(f"Error: The size '{sys.argv[2]}' should be an integer.")
    sys.exit()

processed_directory = os.path.join(os.getcwd(), "processed")
if not os.path.exists(processed_directory):
    os.mkdir(processed_directory)

for file in os.listdir(raw_directory):
    try:
        with Image.open(os.path.join(raw_directory, file)) as image:
            name = os.path.splitext(file)[0] + ".jpg"
            path = os.path.join(processed_directory, name)
            rgb_image = image.convert("RGB")
            rgb_image.thumbnail((max_size, max_size), Image.LANCZOS)
            rgb_image.save(path, optimize=True, quality=95)
            print(f"The file '{file}' was saved as '{path}'.")
    except UnidentifiedImageError:
        print(f"Warning: The file '{file}' is not an image. Skipping...")
