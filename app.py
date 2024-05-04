from PIL import Image, ImageDraw, ImageFont

# Open the image file
image = Image.open("/home/vivalchemy/Pictures/wallpapers/sakuna.jpg")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define the text content, font, and color
text = "Sample Text"
font = ImageFont.truetype("/usr/share/fonts/TTF/Poppins/Poppins-Regular.ttf", 72)
text_color = "white"

# Calculate the position to place the text at the center of the image
text_width = draw.textlength(text, font=font)
image_width, image_height = image.size
text_x = (image_width - text_width) // 2
text_y = (image_height) // 2

# Draw the text onto the image
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save or display the modified image
image.show()
