import os
import glob

path = r"/home/arun/PycharmProjects"

# Method 1(i): To list the files in the path
fileList = os.listdir(path)
print(fileList)
# Method 1(ii): To list the files in the path recursively
for file in fileList:
    print(os.path.join(path, file))


# Method 2(i): To list the files in the path
g = glob.glob(path+"/pythonProject/*", recursive=False)
print(g)
# Method 2(ii): To list the files in the path recursively
h = glob.glob(path+"/pythonProject/**/*", recursive=True)
print(h)

# Method 3: To list the files in the path recursively
for root, direc, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
