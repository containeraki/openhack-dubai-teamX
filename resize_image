from PIL import Image
size = (128, 128)
image = Image.open('gloves/10344697x1038817_zm.jpeg')
image.thumbnail(size, Image.ANTIALIAS)

# Create a white background
background = Image.new('RGB', size, (255, 255, 255))
# Scale the original image keeping aspect ratioa, and paste on top of the background
background.paste(image, (int((size[0] - image.size[0]) / 2), int((size[1] - image.size[1]) / 2))  )
background.save("output.jpg")

#Display it
img=mpimg.imread('output.jpg')
imgplot = plt.imshow(img)
