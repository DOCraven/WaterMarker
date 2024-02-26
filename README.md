# WaterMarker
Simple script to watermark a photo with the file name and date. 

## Description
This script takes photos in a folder, and will watermark them with the following information 
* File name
* Date

The user can select which corner, colour and manually change the date as required. 

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
3. If you wish to use today's date, leave the variable `date_overide = False` uncommented and the `date_overide = datetime.datetime(2023, 8, 25)` commented out
4. If you wish to manually specify a date, comment out `date_overide = False` and uncomment `date_overide = datetime.datetime(2023, 8, 25)`, using the format `YYYY, M, D`

## this script will NOT work on a folder of folders or standalong photos. All photos need to be in one folder. Multiple standalone folders are supported 



