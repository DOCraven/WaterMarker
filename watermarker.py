from PIL import Image, ImageDraw, ImageFont, ExifTags
import os
import sys
import logging 
from datetime import datetime
from datetime import date

## VERSION ##
## 2.5.1 ##

## THIS USES A Virtual Environment (venv) called 'WaterScript'. 
    # to run this code in the venv, use the following steps 
    # 1. open terminal/cmd
    # 2. change directory ('cd .....) to this directory (ie, cd C:\Scratch\Watermarking Photos)
    #       a. much easier to just use the absolute path ()

## ADDING LIBRARIES via PIP ##
# to bypass pip not being in path, use the following code: 
#   C:\Users\[YOUR USERNAME]\AppData\Local\Programs\Python\Python312\python.exe -m pip install pillow
#   C:\Users\DCRAVEN\AppData\Local\Programs\Python\Python312\python.exe -m pip [pip command]


# this script will take number of folders containing images, and will watermark the photo with its filename and selected date. The photos need to be stored in the "input" folder of the root directory. 
#  ie   -> input
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
## CHANGE THIS TO CHANGE THE FONT COLOUR - DEFAULT IS RED 
user_font_colour = 'red'

####### FUNCTIONS #####################

def date_selector_menu (): 
    '''function to allow the user to input a date, or determine it automatically'''
    
    print('\nThis script shall automatically watermark photos with the file name and selected date.\n\n')
    while True:
        user_date_choice = input('Date Selection:\n================================================\n1 - Automatic (Today\'s Date)\n2 - Manual Date Selection (User Selection)\n\nSELECTION: ')

        #make a decision about the user input
        if user_date_choice == '1': #Automatic Date 
            print('Today\'s Date Chosen')
            auto_date = True
            return auto_date 
        
        elif user_date_choice == '2': #Manual date choice
            print('User Date Chosen.\n')
            auto_date = False
            return auto_date 
        
        else: #incorrect input
            print("\n\nERROR - PLEASE SELECT A CORRECT INPUT\n")

def date_determinator (auto_date = True): 
    """function to get date input, either automatically or manually"""
    #automatic Selection: 
    if auto_date: 
        ## choose todays date
        validated_date = date.today() #determine todays date
        return validated_date
    
    else: #manual selection 
        #user inputs date, and it is validated by the function below
        date_string = user_date_input_manual_validator() 
        #convert the string to type datestring
        validated_date = datetime.strptime(date_string, "%Y, %m, %d")
        return validated_date

def user_date_input_manual_validator(): 
    ''' receives and validates the users manual date input'''
    #literally stolen from ChatGPT here
    while True:
        #get user inut
        date_str = input('\nPlease choose a date in DD MM YYYY format (e.g., 02 10 2024): ')
        date_parts = date_str.split()

        #check that the date contains 3 components 
        if len(date_parts) != 3:
            print("\nPlease enter the date in the correct format.")
            continue
        
        #split those into individual components to validate indivudually 
        try:
            day = int(date_parts[0])
            month = int(date_parts[1])
            year = int(date_parts[2])

        #validate those components 
            if not (1000 <= year <= 9999) or not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError

            # Additional validation such as checking for valid days in each month
            # could be done here.

            break
        except ValueError:
            print("\nInvalid date. Please enter the date in the correct format.")

    # print("Date entered:", year, month, day) #for testing

    #combine the date into a single string to return
    date_combined = f"{year}, {month}, {day}"
    return date_combined

def name_input_menu():
    '''takes user name input'''
    return #nothing

def add_watermark_to_folder(input_folder, output_dir,  output_folder_root="output", output_folder_suffix="(watermarked)", date = date.today()):
    '''This function will add the watermark to the image'''
    #folder structure 
        # output = folder that holds the edited photos
        # (watermarked) = edited folders are appended with this, to determine status of watermarking 


    # Create the output root folder
    print('\n\nENCODING: This may take some time. Please be patient.')
    output_root = os.path.join(output_dir, output_folder_root)
    os.makedirs(output_root, exist_ok=True)

    # Get a list of all folders in the working directory
    folders = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

    #format the date into DD/MM/YY
    date_processed = date.strftime("%d/%m/%Y") 
    photographer_name = 'Taken by: D Craven' #TODO add in menu for another user to enter their name


    for folder in folders:
        # Create output folder with "(Edited)" suffix
        if folder == 'output': #so it ignores the output folder, otherwise it will copy the output folder to the output folder
            pass #do nothing
        elif folder == 'watermarking': #ignores the venv folder
            pass
        else:
            output_folder = os.path.join(output_root, f"{folder} {output_folder_suffix}") #look for output directory to put images in. 
            os.makedirs(output_folder, exist_ok=True)


        # Get a list of all files (photos) in the input folder
        files = os.listdir(os.path.join(input_folder, folder))

        for file in files:
            # Check if the file is an image (you can add more image formats if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Open the image
                image_path = os.path.join(input_folder, folder, file)
                img = Image.open(image_path)

                 # Save EXIF data if available
                exif_data = img.info.get('exif')

                # Get the base name of the file (without extension)
                file_name = os.path.splitext(file)[0]
                file_name_with_date = file_name + '\n' + date_processed + '\n' + photographer_name #slap the date below the file name, and my name under that
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


                # Add the watermark to the image with chosen color
                # file_name_with_date = '\n\nTaken By: D Craven'
                draw.text(position, file_name_with_date, font=font, fill=font_color)

                # Save the image with EXIF data
                output_path = os.path.join(output_folder, file)
                if exif_data:
                    img.save(output_path, exif=exif_data)  # Save with EXIF data
                else:
                    img.save(output_path)  # Save without EXIF if not available
    
    return #nothing 


def main(): 
    ''' script runs here'''
    ## STEP 1 ## - User auto or manual date selection 
    menu = date_selector_menu()

    ## STEP 2 ## - Date is determined and validated if required
    chosen_date = date_determinator(menu)

    ## STEP 3 ## - Watermark the photos
        #get the current working dir, to put photos in when done
    output_dir = os.getcwd()
        #get the current directory, and then look for the "input" folder. 

    # add the folder called "input" to the working directory. Photos to be processed live here    
    working_directory = os.path.join(os.getcwd(), 'input') #get working dir, add #input# to it. 
    ## TODO change output dir to ove level above. 
    # send everything to the function
    add_watermark_to_folder(working_directory, output_dir, date = chosen_date)



if __name__ == "__main__":
    # Change the working directory to the script's directory
    print('WaterMarker - The Water Marking Script\n\nCreated by David Craven\nhttps://github.com/DOCraven/WaterMarker\n\nVersion 2.5.0\n')
    
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_directory)

    print("Current Working Directory:", os.getcwd())

    
    #error catching and logging
    try: 
        main() #run the code
    except Exception as e: 
        logging.error("An error occurred: %s", e)  # Log the error message
        print("An error occurred. Please check error_log.txt for details.")
       
#let the user know the code has finished. 
finished = input('\n\nCode is completed.\nPress ENTER to close this window.') 
