import os
def main():
    i=0
    path = os.getcwd() + "/"
    for filename in os.listdir(path):
        if filename.endswith((".jpg", ".png", ".bmp", ".gif", ".tif", ".eps", ".raw")) == True:
            new_name = "Image" + str(i) + filename[-4:]
            old_name = path + filename
            new_name = path + new_name
            os.rename(old_name, new_name)
            i+=1

if __name__ == '__main__':
    main()