from PIL import Image, ImageDraw, ImageFont
import os
import re
from datetime import datetime
from datetime import date

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

####### FUNCTIONS #####################

def date_selector_menu (): 
    '''function to allow the user to input a date, or determine it automatically'''
    
    print('This script shall automatically watermark photos with the file name and selected date.\n\n')
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

def add_watermark_to_folder(input_folder, output_folder_root="watermarked", output_folder_suffix="(watermarked)", date = date.today()):
    '''This function will add the watermark to the image'''
    
    # Create the output root folder
    print('\nENCODING: This may take some time. Please be patient.')
    output_root = os.path.join(input_folder, output_folder_root)
    os.makedirs(output_root, exist_ok=True)

    # Get a list of all folders in the working directory
    folders = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

    #format the date into DD/MM/YY
    date_processed = date.strftime("%d/%m/%Y") 


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


                # Add the watermark to the image with chosen color
                draw.text(position, file_name_with_date, font=font, fill=font_color)

                # Save the image to the output folder
                output_path = os.path.join(output_folder, file)
                img.save(output_path)

def main(): 
    ''' script runs here'''
    ## STEP 1 ## - User auto or manual date selection 
    menu = date_selector_menu()

    ## STEP 2 ## - Date is determined and validated if required
    chosen_date = date_determinator(menu)

    ## STEP 3 ## - Watermark the photos
    working_directory = os.getcwd()
    add_watermark_to_folder(working_directory, date = chosen_date)



if __name__ == "__main__":
    main() #run the code
       
#let the user know the code has finished. 
finished = input('\n\nCode is completed.\nPress ENTER to close this window.') 
