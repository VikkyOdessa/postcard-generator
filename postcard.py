from PIL import Image, ImageDraw, ImageFont
import sys

# Get name from command-line argument
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "Friend"

# Load background image
image = Image.open('happy_birthday.jpg')
draw = ImageDraw.Draw(image)

# Load font
font_big = ImageFont.truetype("DancingScript-VariableFont_wght.ttf", 550)
font_small = ImageFont.truetype("DancingScript-VariableFont_wght.ttf", 380)

# Colors
color_text = "white"
color_outline = "black"

# Function to draw text with outline
def draw_text_with_outline(draw, position, text, font, text_color, outline_color, outline_width):
    x, y = position
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    draw.text(position, text, font=font, fill=text_color)

# Image size
img_width, img_height = image.size

# Initial Y position (near top)
y = 150

# First line (centered)
text1 = f"Dear {name},"
text1_bbox = draw.textbbox((0, 0), text1, font=font_big)
text1_width = text1_bbox[2] - text1_bbox[0]
text1_height = text1_bbox[3] - text1_bbox[1]
x1 = (img_width - text1_width) // 2
draw_text_with_outline(draw, (x1, y), text1, font_big, color_text, color_outline, 5)

# Second line
y += text1_height + 170
text2 = "Wishing you a wonderful day!"
text2_bbox = draw.textbbox((0, 0), text2, font=font_small)
text2_width = text2_bbox[2] - text2_bbox[0]
text2_height = text2_bbox[3] - text2_bbox[1]
x2 = (img_width - text2_width) // 2
draw_text_with_outline(draw, (x2, y), text2, font_small, color_text, color_outline, 3)

# Third line
y += text2_height + 100
text3 = "From, Your Family"
text3_bbox = draw.textbbox((0, 0), text3, font=font_small)
text3_width = text3_bbox[2] - text3_bbox[0]
text3_height = text3_bbox[3] - text3_bbox[1]
x3 = (img_width - text3_width) // 2
draw_text_with_outline(draw, (x3, y), text3, font_small, color_text, color_outline, 3)

# Save result
image.save(f"postcard_for_{name}.jpg")
print(f"Created postcard_for_{name}.jpg with CENTERED text near top!")



