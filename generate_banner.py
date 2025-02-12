from PIL import Image, ImageDraw, ImageFont
import requests
import datetime

# Define image size
WIDTH, HEIGHT = 1200, 400
background_color = (30, 30, 30)  # Dark background

# Create blank image
image = Image.new("RGB", (WIDTH, HEIGHT), background_color)
draw = ImageDraw.Draw(image)

# Load font (use a path to an existing .ttf file)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 60)

# Get current time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add text to image
text = f"Hello, Jheelam! {current_time}"
bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

draw.text(((WIDTH - text_width) / 2, (HEIGHT - text_height) / 2), text, font=font, fill="white")

# Save the banner
image.save("banner.png")
