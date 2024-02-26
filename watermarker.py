from PIL import Image, ImageDraw, ImageFont
import os
import re
from datetime import date
import datetime


# this script will take number of folders containing images, and will watermark the photo with its filename. 
#  ie   -> working dir 
#                 -> folder 1
#                         -> photo1.png
#                         -> photo2.jpg
#                 -> folder 2 
#                         -> image2.png
#                         -> image92.jpg
#                 ....
#                 -> folder 9
#                         -> photo4.png
#                         -> photo6.jpg
# this script will NOT work on a folder of folders or standalong photos. All photos need to be in one folder. 

#variables
font_location = "C:/Windows/Fonts/arial.ttf"
## CHANGE THIS TO CHANGE THE FONT COLOUR - DEFAULT IS BLACK 
user_font_colour = 'red'
### TO MANUALLY CHANGE THE DATE, comment out line 27, and uncomment out line 28. Change the date using the format YYYY, M, D
date_overide = False
# date_overide = datetime.datetime(2023, 8, 25) #YYYY, M, D 

def add_watermark_to_folder(input_folder, output_folder_root="watermarked", output_folder_suffix="(watermarked)"):
    # Create the output root folder
    output_root = os.path.join(input_folder, output_folder_root)
    os.makedirs(output_root, exist_ok=True)

    # Get a list of all folders in the working directory
    folders = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

    #check for manual date selection 
    if not date_overide: #ie, date has been automatically selected
        #get todays date to watermark show the rough date of images were processed
        today = date.today() #get the date
        print('Date automatically determined!')
        
    else: #ie, the date has been automatically determined using datetime to be todays date
        today = date_overide
        print('Date manually determined!')

    
    date_processed = today.strftime("%d/%m/%Y") #format the date into DD/MM/YY


    for folder in folders:
        # Create output folder with "(Edited)" suffix
        if folder == 'watermarked': #so it ignores the output folder, otherwise it will copy the output folder to the output folder
            pass #do nothing
        else:
            output_folder = os.path.join(output_root, f"{folder} {output_folder_suffix}")
            os.makedirs(output_folder, exist_ok=True)




        # Get a list of all files (photos) in the input folder
        files = os.listdir(os.path.join(input_folder, folder))

        for file in files:
            # Check if the file is an image (you can add more image formats if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Open the image
                image_path = os.path.join(input_folder, folder, file)
                img = Image.open(image_path)

                # Get the base name of the file (without extension)
                file_name = os.path.splitext(file)[0]
                file_name_with_date = file_name + '\n' + date_processed #slap the date below the file name
                # Create a drawing object
                draw = ImageDraw.Draw(img)
                
                # Choose font and size (you may need to change the font path)
                font_path = font_location
                font_size = 128
                font = ImageFont.truetype(font_path, font_size)

                # Choose the position for the watermark (you can adjust this)
                position = (10, 10)

                # Set the font color to black
                font_color = user_font_colour 


                # Add the watermark to the image with black color
                draw.text(position, file_name_with_date, font=font, fill=font_color)

                # Save the image to the output folder
                output_path = os.path.join(output_folder, file)
                img.save(output_path)

if __name__ == "__main__":
    working_directory = os.getcwd()
    add_watermark_to_folder(working_directory)

print("\n\ncode completed\n\n")