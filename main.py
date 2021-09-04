import IndianRecipie as ir
import json

file = open("hyderabadDishes.txt", "w")  # Open's and write in to file
file.write(json.dumps(ir.get_data()))  # write data in json format
file.close()  # closing file is very important
print("Data written in to File Successfully ... !")
