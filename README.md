Birthday Postcard Generator

This Python script generates personalized birthday postcards by adding custom text to a background image.

Features
	Creates personalized birthday postcards with a custom name

	Adds multiple lines of text with beautiful styling

	Uses outline effects to make text more readable

	Automatically centers text on the image

	Saves the result as a JPG file


Requirements
- Python 3.7+

- Pillow library — install it with:

bash
pip install pillow

Installation
Clone this repository or download the script

Install the required dependencies:

pip install Pillow

Usage
Run the script from the command line with the recipient's name as an argument:
python birthday_postcard.py John

If no name is provided, it will default to "Friend":

python postcard.py Rob (any name)
The script will generate a file named postcard_for_[name].jpg in the same directory.

Customization
To customize the postcard:

- Replace happy_birthday.jpg with your own background image (keep the same filename)

- Adjust font sizes and positions by modifying the script parameters:

  font_big and font_small control text sizes

- The y variable controls vertical positioning

  color_text and color_outline control text colors

- Change the messages by editing the text1, text2, and text3 variables

Notes
The script expects a font file named "DancingScript-VariableFont_wght.ttf" in the same directory

You may need to adjust text positioning depending on your background image dimensions


License
This project is open source and available under the MIT License.



