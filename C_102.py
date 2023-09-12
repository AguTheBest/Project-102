import os 
import shutil
src = "c:/Users/System-01/Downloads/C102_assets-main"
dst = "C:/Users/System-01/Desktop"
files = os.listdir(src)
print(files)
for file in files:
    n,e = os.path.splitext(file)
    print(n,e)
    if(e == ""):
        continue
    elif(e in [".jpg",".png",".gif",".jfif"]):
        path1 = src + "/"+ file 
        path2 = dst + "/images"
        path3 = path2+"/"+file
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)    
