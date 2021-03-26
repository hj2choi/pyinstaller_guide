from Inner import Inner_module
print("Inner_module: ", Inner_module.VARIABLE)

#.env_setup에서 하는것처럼 path에 추가함.
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir) # find parent directory
sys.path.append(parentdir)
from Common import Common_module
print("Common_module: ", Common_module.VARIABLE)



f = open("../parent_dir_text.txt", "r")
print(f.read())



f = open("Inner/child_dir_text.txt", "r")
print(f.read())
