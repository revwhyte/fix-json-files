import os

# trace path with all files to fix
caminho = 'data/'

# get a list with all file names
files = os.listdir(caminho)
print(len(files))

# loop through all files in data/*
for file in files:
    # open file and read all lines in a list
    with open(caminho + file, 'r') as f:
        lines = f.readlines()

    # remove spaces and then put each document in a single line
    # http://dontpad.com/arrange-file-python
    lines = [line.rstrip("\n\r") for line in lines]
    lines = [line.replace("}{", "}\n{") for line in lines]

    # finally, write lines in the file
    with open(caminho + file, 'w') as f:
        f.writelines(lines)