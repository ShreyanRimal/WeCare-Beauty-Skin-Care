def read():
    file = open("products.txt", "r")  # open the file in read mode
    mydict = {}  # create an empty dictionary to store the data
    sn = 1  
    for line in file:
        line = line.replace('\n', '')# remove newline character only
        mydict[sn] = line.split(",")  # split the line by commas and add it to the dictionary
        sn += 1  
    file.close()  
    return mydict 

def fread():
    file = open("products.txt", "r") 
    sn = 1 
    for line in file:
        # remove newline character and replace commas with pipes
        print(str(sn) + " | " + line.replace(",", " | "))
        sn += 1
    file.close()  # close the file when done
