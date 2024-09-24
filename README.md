# WaterMarker
Simple script to watermark a photo with the file name and date. 

## Description
This script takes photos in a folder, and will watermark them with the following information 
* File name
* Date

## Dependancies 
This code requries the use of 
* Pillow image processing `PIL`
All dependencies are listed in `requirements.txt`

this script will take number of folders containing images, and will watermark the photo with its filename. 
ie   -> input directory 
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

1. Download script, including
2. Place photos in folders, in the `input` directory
3. - Follow the menu to select automatic date (ie, today's date) or manul date (ie, whatever date the user inputs).
   - The date shall follow the the format `DD MM YYYY`
4. The script will place watermarked photos in the `output` folder.
   - The `output` folder shall be created if it does not exist.  


## Notes ##
This script will show error logs via the command line. It may save an error log in `C\Windows\System32`. 

## this script will NOT work on a folder of folders or standalong photos. All photos need to be in a folder. Multiple standalone folders are supported,



