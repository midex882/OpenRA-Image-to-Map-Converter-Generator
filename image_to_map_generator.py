import os
import random
from PIL import Image
import struct

# World map
MAP_WIDTH = 0
MAP_HEIGHT = 0

TILE_WATER = 0x01
TILE_GRASS = 0xFF
UNKNOWN_BYTE = 0x00


binary_data = 0


def convert_image_to_map(input_bin_path,image_path, output_path):
    print("Processing image...")
    

    with open(input_bin_path, "rb") as source_file:
        original_header = source_file.read(17)
        print(f"original header: {original_header}")
        file_size = os.path.getsize(input_bin_path)
        print(f"expected size: {file_size}")
        HEADER_MAP_WIDTH = int.from_bytes(original_header[1:3], byteorder='little')
        HEADER_MAP_HEIGHT = int.from_bytes(original_header[3:5], byteorder='little')

        MAP_WIDTH = HEADER_MAP_WIDTH-2
        MAP_HEIGHT = HEADER_MAP_HEIGHT-2

        print(f"Map hidth: {MAP_WIDTH} px")
        print(f"Map height: {MAP_HEIGHT} px")

        print(f"OpenRA adds A 1px border to the map, so real dimensions are: {HEADER_MAP_WIDTH} x {HEADER_MAP_HEIGHT} px")
    
    img = Image.open(image_path).convert('L')

    if img.size != (MAP_WIDTH, MAP_HEIGHT):
        raise ValueError(f"Image must be {MAP_WIDTH}x{MAP_HEIGHT}, got {img.size}")

   
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    img = img.rotate(90, expand=True)

    img.save("C:/Users/mid_ex882/Desktop/debug_input.png")

    
    with open(output_path, 'wb') as f:
        f.write(original_header)

        image_pixel_tracker = [0,0]
        print(image_pixel_tracker)
        for x in range(MAP_WIDTH+2):   
            for y in range(MAP_HEIGHT+2):
                if x == 0 or x == MAP_WIDTH+1 or y == 0 or y == MAP_HEIGHT+1:
                    tile_id = TILE_WATER
                    style = 0x00
                else:
                    pixel = img.getpixel((image_pixel_tracker[0], image_pixel_tracker[1]))
                    image_pixel_tracker[0] += 1
                    
                    if pixel >= 128:
                        tile_id = TILE_WATER
                        style = 0x00
                    else:
                        tile_id = TILE_GRASS
                        style = style = random.randint(0, 15)

                    
                    if image_pixel_tracker[0] == MAP_HEIGHT:
                        image_pixel_tracker[0] = 0
                        image_pixel_tracker[1] += 1
                        
                tile_data = struct.pack('BBB', tile_id, UNKNOWN_BYTE, style)
                f.write(tile_data)
                
            
        current_size = f.tell()
        padding_needed = file_size - current_size
        if padding_needed < 0:
            raise RuntimeError(f"Output exceeded target size: {current_size} > {file_size}")
        f.write(b'\x00' * padding_needed)
    print(f"Done. File written to {output_path} with size {current_size} bytes.")

print("Map converter. This code takes a black and white PNG image and converts it to a map.bin file for OpenRA.\n Instructions: \n1)Take a black and white PNG image of the map you want to generate. white -> water, not-white -> basic terrain depending on type of map. Max dimensions 997 x 997 \n2) Generate a valid map using OpenRa's map editor WITH THE SAME DIMENSIONS AS THE IMAGE \n3)Find the .oramap file inside the maps folder (C:/Users/<username>/AppData/Roaming/OpenRA/maps/ra for Red Alert mod on windows) \n4)Extract using winrar or whatever (.oramaps are just zip files) \n5)Eliminate the .oramap file so only the extracted folder remains \n6) Keep the file path. Now, follow the prompts\n")
input_bin_file_path = input("Enter the path to the .bin file inside the extracted folder: ")

if os.path.isfile(input_bin_file_path) and input_bin_file_path.lower().endswith(".bin"):

    input_image_file_path = input("Enter the path to the png image file: ")
    if os.path.isfile(input_image_file_path) and input_image_file_path.lower().endswith(".png"):
        print("Valid .bin file found. Sarting...")
        convert_image_to_map(
        input_bin_file_path,
        input_image_file_path,
        input_bin_file_path)
    else:
        print("No png image found at that path.")
else:
    print("No .bin file found at that path.")

