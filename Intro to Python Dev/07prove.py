
# This line imports or includes the library we will need
from PIL import Image
print('workie\n*\n')

# This line opens the image and loads it into a variable called "image_original"
# image_original = Image.open("beach.jpg")
image_original = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach.jpg")
print('ran the open image without explicit error')
# # This line attempts to open a new window to display the image.
image_original.show()

# print(image_original.size)
width, height = image_original.size
print(width)
print(height)

pixels_original = image_original.load()

print('the color settings in [100,200]')
r, g, b = pixels_original[100, 200]
print(r)
print(g)
print(b)
print()

# Show the color settings on five pixels.
print('Show the color settings on five pixels.')
print(pixels_original[50, 300])
print(pixels_original[200, 300])
print(pixels_original[100, 300])
print(pixels_original[300, 300])
print(pixels_original[150, 300])

# Setting new color values on several pixels.
# Similarly, you can set new red, green, and blue values for the pixel at some x, y location in the picture like this:
# Don't forget to use parentheses around your (r, g, b)
pixels_original[100, 200] = (255, 0, 255)
pixels_original[101, 201] = (255, 0, 255)
pixels_original[102, 202] = (255, 0, 255)
pixels_original[100, 203] = (255, 0, 255)
pixels_original[101, 204] = (255, 0, 255)
pixels_original[102, 205] = (255, 0, 255)
pixels_original[100, 206] = (255, 0, 255)
pixels_original[101, 207] = (255, 0, 255)
pixels_original[102, 208] = (255, 0, 255)

# When you are ready to save an image out to a new file, you can call the save function like this:
image_original.save(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\the_file_goes_here.jpg")
image_original = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\the_file_goes_here.jpg")
image_original.show()
