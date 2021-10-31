
# This line imports or includes the library we will need
from PIL import Image


# This line opens the image and loads it into a variable called "image_original"
# image_original = Image.open("beach.jpg")
image_beach = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach.jpg")

# print(image_beach.size)
width, height = image_beach.size
print(f'{width} x {height} beach')

pixels_beach = image_beach.load()

# Penguin picture
green_penguin = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\penguin.jpg")
width2, height2 = green_penguin.size
print(f'{width2} x {height2} green penguin')
pixels_green_penguin = green_penguin.load()

# print(pixels_green_penguin[372, 389])  # (44, 207, 64)
# print(pixels_green_penguin[388, 388])
# print(pixels_green_penguin[480, 305])
# print(pixels_green_penguin[490, 435])
# print(pixels_green_penguin[396, 417])

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_green_penguin[x, y]
        (r2, g2, b2) = pixels_beach[x, y]
        # if r < 65 and g > 200 and b < 65:
        if g > 190 and r < 100:
            pixels_green_penguin[x, y] = (r2, g2, b2)
        elif (65 < r < 105) and (150 < g) and (80 < b < 100):
            pixels_green_penguin[x, y] = (r2, g2, b2)
        else:
            pass

# green_penguin.save(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach_penguin.jpg")
# beach_penguin = Image.open(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach_penguin.jpg")
# beach_penguin.show()


# Hiker picture
green_hiker = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\hiker.jpg")
width2, height2 = green_hiker.size
print(f'{width2} x {height2} green hiker')
pixels_green_hiker = green_hiker.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_green_hiker[x, y]
        (r2, g2, b2) = pixels_beach[x, y]
        # if r < 65 and g > 200 and b < 65:
        if g > 190 and r < 100:
            pixels_green_hiker[x, y] = (r2, g2, b2)
        elif (65 < r < 105) and (150 < g) and (80 < b < 100):
            pixels_green_hiker[x, y] = (r2, g2, b2)
        else:
            pass

# green_hiker.save(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach_hiker.jpg")
# beach_hiker = Image.open(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\beach_hiker.jpg")
# beach_hiker.show()


# Combine beach hiker and beach penguin by averaging values
hiker_peng_beach = Image.new("RGB", image_beach.size)
pixels_hik_peng_bea = hiker_peng_beach.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_green_hiker[x, y]
        (r2, g2, b2) = pixels_green_penguin[x, y]
        r3 = int((r+r2)/2)
        g3 = int((g+g2)/2)
        b3 = int((b+b2)/2)
        pixels_hik_peng_bea[x, y] = (r3, g3, b3)

hiker_peng_beach.save(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\hiker_peng_beach.jpg")
hiker_peng_beach = Image.open(
    "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\hiker_peng_beach.jpg")
hiker_peng_beach.show()

# print('the color settings in [100,200]')
# r, g, b = pixels_original[100, 200]
# print(r)
# print(g)
# print(b)
# print()

# # Show the color settings on five pixels.
# print('Show the color settings on five pixels.')
# print(pixels_original[50, 300])
# print(pixels_original[200, 300])
# print(pixels_original[100, 300])
# print(pixels_original[300, 300])
# print(pixels_original[150, 300])

# # Setting new color values on several pixels.
# # Similarly, you can set new red, green, and blue values for the pixel at some x, y location in the picture like this:
# # Don't forget to use parentheses around your (r, g, b)
# pixels_original[100, 200] = (255, 0, 255)
# pixels_original[101, 201] = (255, 0, 255)
# pixels_original[102, 202] = (255, 0, 255)
# pixels_original[100, 203] = (255, 0, 255)
# pixels_original[101, 204] = (255, 0, 255)
# pixels_original[102, 205] = (255, 0, 255)
# pixels_original[100, 206] = (255, 0, 255)
# pixels_original[101, 207] = (255, 0, 255)
# pixels_original[102, 208] = (255, 0, 255)

# # When you are ready to save an image out to a new file, you can call the save function like this:
# image_original.save(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\the_file_goes_here_2nd.jpg")
# image_original = Image.open(
#     "C:\\Users\\Matt O\\Desktop\\SCHOOL\\CSE110 Building Blocks of Programming\\cse110_images\\the_file_goes_here_2nd.jpg")
# image_original.show()
