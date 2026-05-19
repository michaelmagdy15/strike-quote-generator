import base64
from PIL import Image

def convert_logo():
    # Load the image
    img = Image.open('strikelogo.png').convert('RGBA')
    
    # Extract channels
    r, g, b, a = img.split()
    
    # Create white channels with same size
    white_channel = Image.new('L', img.size, 255)
    
    # Merge white RGB channels with the original Alpha channel
    white_img = Image.merge('RGBA', (white_channel, white_channel, white_channel, a))
    
    # Save the white image
    white_img.save('strikelogo_white.png')
    print("Saved strikelogo_white.png successfully!")
    
    # Get base64 string
    with open('strikelogo_white.png', 'rb') as f:
        img_data = f.read()
        b64_str = base64.b64encode(img_data).decode('utf-8')
        
    # Write base64 string to file
    with open('logo_base64.txt', 'w') as f:
        f.write(b64_str)
    print("Saved base64 string to logo_base64.txt!")

if __name__ == '__main__':
    convert_logo()
