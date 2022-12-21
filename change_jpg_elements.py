# this code can change your jpg figure into fixed elements format.
from PIL import Image

# Open the image
im = Image.open('image.jpg')

# Set the new width and height
new_width, new_height = (480,302)

# Resize the image
im_resized = im.resize((new_width, new_height), resample=Image.BICUBIC)

# Save the resized image
im_resized.save('image_resized.jpg')

