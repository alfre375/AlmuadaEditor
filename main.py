#info
versionfull = "1.0.0"
apiver = 1
#imports
from PIL import Image

path = input("Enter the full path of the image. If the image is in the same directory as the python file, you will only need to enter the name. ")

image = Image.open(path)
image.show()

while True:
    cmd = input("")
    cmd = cmd.split()
    if cmd[0] == "resize":
        print("resize is not working at the moment. You may want to try updating")
        new_hight = int(input("Enter a new hight: "))
        new_width = int(input("Enter a new width: "))
        new_size = (new_hight,new_width)
        image.thumbnail(new_size)
        image.save(path)
    elif cmd[0] == "update-path":
        image.save(path)
        path = input("Enter the full path of the image. If the image is in the same directory as the python file, you will only need to enter the name. ")
        image = Image.open(path)
    elif cmd[0] == "open":
        image.show()
    elif cmd[0] == "end":
        print("Goodbye!")
        exit()
    elif cmd[0] == "copy":
        path = input("Enter the full path of the copy. If the copy is in the same directory as the python file, you will only need to enter the name of the copy. ")
        image.save(path)
        image = Image.open(path)
        print("You are now editing the copy.")
    elif cmd[0] == "path":
        print(path)
    elif cmd[0] == "info":
        print("AlmuadaEditor v" + str(versionfull) + " API " + str(apiver))
        print("For command help, use 'help'")
    elif cmd[0] == "help":
        print("resize: Resizes the picture to a new size")
        print("update-path: Allows you to change the picture you are working on")
        print("open: Shows your picture in your computer's default image viewing app")
        print("end: Stops the program")
        print("copy: Makes a copy of the file you are working on and shifts the path to the copy")
        print("path: Prints the current working file")
        print("info: Gives you more info on the program")
        print("help: Gives you a list of commands and a breif description")
    else:
        print("Invalid command!")


#print("Hello")
#print("How are you")
#you_feeling = input("")
#if (you_feeling == "Good"):
#    print("Oh, that is great!")
#else:
#    print("Oh well...")
#print("Hello")
#print("How are you")
#you_feeling = input("")
#if (you_feeling == "Good"):
#    print("Oh, that is great!")
#else:
#    print("Oh well...")
#print("Hello")
#print("How are you")
#you_feeling = input("")
#if (you_feeling == "Good"):
#    print("Oh, that is great!")
#else:
#    print("Oh well...")
