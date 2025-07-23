# Project Title

# OpenRA-Image-to-Map-Converter-Generator
A python script for conveting png black and white images to openra map.bin files


It is a simple script, but it was a real pain decripting the way OpenRa codes their bin files.

Instructions:

1. Take a black and white PNG image of the map you want to generate. white -> water, not-white -> basic terrain depending on type of map. Max dimensions 997 x 997 

2. Generate a valid map using OpenRa's map editor WITH THE SAME DIMENSIONS AS THE IMAGE 

3. Find the .oramap file inside the maps folder (C:/Users/<username>/AppData/Roaming/OpenRA/maps/ra for Red Alert mod on windows) 

4. Extract using winrar or whatever (.oramaps are just zip files) 

5. Eliminate the .oramap file so only the extracted folder remains 

6. Keep the file path. Now, follow the prompts


As an example, here is what I wanted to do:





![App Screenshot]([[https://drive.google.com/file/d/1bToaBHZzRBf9yawCHB-7bjC4GNF4O0Fz/view?usp=sharing](https://github.com/midex882/OpenRA-Image-to-Map-Converter-Generator/blob/main/input.png)](https://freeimage.host/i/FOmddCl))

And this is the result:

![App Screenshot]([[https://drive.google.com/file/d/1AgyNQ1PqzDJTj5w7Gq-eb59hmy_3ZNLV/view?usp=sharing](https://github.com/midex882/OpenRA-Image-to-Map-Converter-Generator/blob/main/result.png)](https://freeimage.host/i/FOmFK3N))

Good luck!
