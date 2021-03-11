from PIL import Image
import time
import os



def decode(img):
    extracted_bin = []
#with Image.open("source_secret.png") as img:
    width, height = img.size
    byte = []
    for x in range(0,width):
        for y in range(0,height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0,3):
                extracted_bin.append(pixel[n]&1)
   # print(pixel)
   # print(extracted_bin)
    data = "".join([str(x) for x in extracted_bin])
    return data



def steg_find(bin_str):

    for i in range(0,1):
        
        mes=''.join(chr(int(bin_str[i*8:i*8+8],2)) for i in range(len(bin_str)//8))
    return mes
#print(decode_binary_string(S))


#def dec():

filename = input("\n\t\tENTER THE STEGO IMAGE TO EXTRACT THE SECRET MESSAGE: ")
img = Image.open(filename, "r")

#pixels = img.load()

#alphabets = "abcdefghijklmnopqrst"
print("------------searching for image...")
time.sleep(0.1)
r=decode(img)
print("------------decoding in process...")
time.sleep(3)
#px_values = flatten_image(img)
result=steg_find(r)
#result = steg_find(px_values)
#os.system("clear")
print("\n\n\t\tTHE SECRET MESSAGE IS : \n\t\t\t" )
#print("NOTE: LOOK FOR THE TEXT AT THE START OF THE MESSAGE")
#print("Decoded text is: {}".format(result))
print('\t\t',end='')
for i in result:
    if i=='%':
        break
    else:
        print(i, end='')
#c=int(input("enter your choce: "))
#if c==1:
 #   dec()
#else:
#    print("inva")
        
        
