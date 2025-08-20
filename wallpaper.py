from PIL import Image, ImageDraw, ImageFont, ImageColor
import os
import platform

def get_font_path():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "cour.ttf")
    elif system == "Darwin":
        return "/System/Library/Fonts/Monaco.ttc"
    elif system == "Linux":
        return "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    else:
        return "cour.ttf"


for attempt in range(3):
    try:
        background_color = input('Enter background color: ').strip()
        if not background_color:
            raise ValueError("Background color can not be empty.")
        background_color = ImageColor.getrgb(background_color)
        break
    except ValueError:
        print("Invalid input, try again.")
else:
    print("\nToo many errors, using default: Black")
    background_color = ImageColor.getrgb('black')
        
for attempt in range(3):
    try:
        orientation = int(input('Enter 1 for portrait and 2 for landscape: ').strip())
        if orientation not in (1, 2):
            raise ValueError("Enter 1 or 2: ")
        break
    except ValueError:
        print("Enter 1 or 2: ")
else:
    print("\nToo many errors, using default: Portrait")
    orientation = 1
    
for attempt in range(3):
    try:
        text = input('Enter text(Use \\n for new lines, e.g., Line1\\nLine2): ').strip()
        if not text:
            raise ValueError("Text can not be empty.")
        print(f"Before replace: {repr(text)}")
        text = text.replace("\\n", "\n")
        print(f"After replace: {repr(text)}")
        break
    except ValueError:
        print("Invalid input, try again.")
else:
    print("\nToo many errors, using default: Bread\nis\ngood.")
    text = "Bread\nis\ngood"

for attempt in range(3):
    try:
        font_color = input('Enter font color: ').strip()
        if not font_color:
            raise ValueError('Font color can not be empty.')
        font_color = ImageColor.getrgb(font_color)
        break
    except ValueError:
        print("Invalid input. Enter again")
else:
    print("\nToo many errors, using default: White.")
    font_color = ImageColor.getrgb('white')
    
font_path = get_font_path()
try:
    font = ImageFont.truetype(font_path, size=40)
except IOError:
    print("Font not found, using default")
    font = ImageFont.load_default()

for attempt in range(3):
    try:
        file_name = input('Enter file name(without .jpg): ').strip()
        if not file_name:
            raise ValueError("File name can not be empty.")
        if not file_name.endswith('.jpg'):
            file_name += '.jpg'
        invalid_chars = '<>:"/\\?*'
        if any(char in file_name for char in invalid_chars):
            raise ValueError("File name contains invalid errors.")
        break
    except ValueError:
        print("Invalid input. Enter again")
else:
    print("\nToo many errors. Using default: wallpaper")
    file_name = 'wallpaper.jpg'

device_width, device_height = (1080, 1920) if orientation == 1 else (1920, 1080)

img = Image.new('RGB', (device_width, device_height), background_color)
draw = ImageDraw.Draw(img)

text_bbox = draw.multiline_textbbox((0,0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x = (device_width - text_width)//2
y = (device_height - text_height)//2

draw.multiline_text((x,y), text, fill=font_color, font=font, align="center")

img.save(file_name)
img.show()
