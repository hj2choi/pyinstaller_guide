# Pyinstaller tutorial

## Usage
#### 1) create .spec file (python script that sets paths, runtime modules, etc)
```bash
pyi-makespec [--onefile] ${filename}.py
```

#### 2) use .spec file to generate binary executable file (supports python version 3.5+)
```bash
pyinstaller [--clean] ${filename}.spec
```
OR use Pyinstaller installed in pip3 freeze
```bash
/path/to/python3.x -m pyinstaller [--clean] ${filename}.spec
```

#### 3) run executable binary
```bash
./${filename} [*args]
```


## .Spec file
#### Analysis.pathex
paths to add
```python
paths = ["./", "./path/to/binary_exe"]
```

#### Analysis.datas
list of tuples of files to be copied [(src, dst)]
```python
datas = [("./source/directory/file.png", "./destination/directory"), ("./dir/*", "./dir/"), ...]
```

#### Analysis.hiddenimports
solves errors like "Error: cannot find module a.b.c"
```python
hiddenimports=["smartX.not.smart"]
```


## pyinstaller arguments
best practices: test with --onedirectory, and deploy using --onefile

#### --onedirectory
executable binary initializes all dependencies with bootloader and runs python script.
Easy to debug, build and deploy

#### --onefile
compress the executable into a single file.
when you run the onefile binary executable, it uncompresses the file, and then run just like --onedirectory mode.

After the execution is complete, all temporary directory and files are discarded.

(possible issue: temporary directory might not be properly removed if the executable is not terminated properly. Use --runtime-tempdir to check and manually remove stacked up temporary files)


## Technical Notes
- generated executable file is dependent on OS and system architecture. (OS, python version (2&3), 32bit&64bit, etc)

- pyinstaller reads all "import" clauses to pre-load all requirements recursively (from pip)

- packages and files read in runtime may not be loaded to the executable file. You need to specify which files to copy at .spec.Analysis.datas in .spec file. You might have to place some required packages into /lib or /usr/lib directory

- pyinstaller converts the script into .pyc format which CAN BE DECOMPILED. To prevent this, 1) convert critical module into C code and compile using Cython. or 2) encrypt python bytecode using AES256.


## Troubleshooting
if you can't find resources with hiddenimports...

inject python script into .spec file to manually copy resources

.spec:
```python
# copy configuration, model files, etc
#{0}: root directory for binary executable file.
import shutil
import os
 
# copy ini file
shutil.copyfile("./EdgeAI/AVREngine/PlateDetect/PlateDetect.ini", "{0}/PlateDetect/PlateDetect.ini".format(DISTPATH))
 
# create directories and copy model file
os.makedirs(os.path.dirname("{0}/PlateDetect/EdgeAI/AVREngine/PlateDetect/Model/CenterNet/".format(DISTPATH)), exist_ok=True)
os.makedirs(os.path.dirname("{0}/PlateDetect/EdgeAI/AVREngine/PlateDetect/CenterNet/".format(DISTPATH)), exist_ok=True)
shutil.copyfile("./EdgeAI/AVREngine/PlateDetect/Model/CenterNet/288_512_plate_model_normal_1212.pth",
              "{0}/PlateDetect/EdgeAI/AVREngine/PlateDetect/Model/CenterNet/288_512_plate_model_normal_1212.pth".format(DISTPATH))
shutil.copyfile("./EdgeAI/AVREngine/PlateDetect/Model/CenterNet/288_512_plate_model_namsan_1212.pth",
              "{0}/PlateDetect/EdgeAI/AVREngine/PlateDetect/Model/CenterNet/288_512_plate_model_namsan_1212.pth".format(DISTPATH))
```

.main:
```python
try:
  os.chdir(sys._MEIPASS)
  print(sys._MEIPASS)
except:
  os.chdir(os.getcwd())

```
