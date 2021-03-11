from PIL import Image
import time

bitsPerPixel=3
bitsPerChar=8
maxBitStuffing = 2


def canEncode(message, new_img):
       width, height = new_img.size
       imageCapacity = width * height * bitsPerPixel
       messageCapacity = (len(message) * bitsPerChar) - (bitsPerChar + maxBitStuffing)
       if imageCapacity <messageCapacity:
           print("not sufficient")
       else:
           return imageCapacity >= messageCapacity


def str2bina(a):
    c =''.join(['0'*(8-len(bin(ord(i))[2:]))+(bin(ord(i))[2:]) for i in a])
    #print(c) -> h-01101000, i-01101001, a-01100001
    return c

# ALGO FOR ENCODE

def encode(img,data):
    i=0
    #data = "011011000110010101100100011001110110010101110010" 
    #with Image.open("source.png") as img:
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y))) #taking all pixel values ie [143,112,92],[....]
            #print(pixel[0])
            for n in range(0,3):
                if(i < len(data)):
                    #print(data[0],data[1],data[2],data[3])   
                    pixel[n] = pixel[n] & ~1 | int(data[i])                  
                    #print('    ',pixel[0])
                    """pixel[n] & ~1 will clear the
                    LSB from the channel and then we only need
                    to change to a 1 when our data says so, running | 1 will turn
                    that LSB into a 1 and | 0 will keep it as is."""
                    i+=1
                    
            img.putpixel((x,y), tuple(pixel))
    #img.save("source_secret.png", "PNG")
            #print(pixel[0],pixel[1],pixel[2])
            
    filename=input("\n\t\t ENTER THE STEGO IMAGE NAME :\n\t\t\t\t ")
    #print("\t\n---------------PROCESSING.....")
    time.sleep(3)
    new_img.save("{}".format(filename), "bmp")
    #new_img.show()
    print('----------------------------------------------------')
    print("\t\t MESSAGE ENCODED IN THE FILE {}".format(filename))
    print("_____________________________________________________")


filename = input("\n\n\t\tENTER THE COVER IMAGE WITH FORMAT : ")
new_img = Image.open(filename, "r")

pixels = new_img.load() # this is to store the pixel data into the variable called pixel

# TODO: check if message can fit inside the image
message = input("\n\t\tENTER THE MESSAGE TO BE ENCODED AND END WITH DELIMITER '%' :")
l=len(message)
#print(l) ->counts from 1 to....

#q=l*3





if canEncode(message, new_img):
       bin_message = str2bina(message)
       
       #pixel_values = flatten_image(new_img)

       #pixel_values = alter_pixels(pixel_values, bin_message)

       #stitch_image(pixels, pixel_values)
       encode(new_img,bin_message)
       new_img.show("enc")
       #filename=input("enter the steg image name: ")
       #print("the code to for this image is ",q )
       #new_img.save("{}".format(filename), "bmp")
       #new_img.save("stg")
else:
       print("\t\t!!!__Not Sufficient space__!!!")
#print("Message encoded in the file {}".format(filename))
#print("Message encoded in the file: ".stg)
