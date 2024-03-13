# WaterMarker
Simple script to watermark a photo with the file name and date. 

## Description
This script takes photos in a folder, and will watermark them with the following information 
* File name
* Date

## Dependancies 
This code requries the use of 
* Pillow image processing `PIL`

this script will take number of folders containing images, and will watermark the photo with its filename. 
ie   -> working dir 
               -> folder 1
                       -> photo1.png
                       -> photo2.jpg
               -> folder 2 
                       -> image2.png
                       -> image92.jpg
               ....
               -> folder 9
                       -> photo4.png
                       -> photo6.jpg

How to use: 

1. Download script
2. Place photos in folders, in the script root dir
3. Follow the menu to select automatic date (ie, today's date) or manul date (ie, whatever date the user inputs).
   - The date shall follow the the format `DD MM YYYY`

## this script will NOT work on a folder of folders or standalong photos. All photos need to be in one folder. Multiple standalone folders are supported 



