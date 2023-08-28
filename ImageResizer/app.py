# installing pillow library
# import pillow
# open up the image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

def resize_image(size1, size2, img_name):

    image = Image.open('test.jpg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1,size2))
    resized_image.save(img_name + ".jpg")

size1 = int(input("Enter a width: "))
size2 = int(input("Enter a length: "))
img_name = input("Enter a new image name: ")
resize_image(size1,size2,img_name)