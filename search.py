import glob, os

os.chdir("/Users/ramshanm/Documents/")

for file in glob.glob("*.txt"):
    print(file)
