import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        content = file.read()
        print(f"Contents of {filepath}:")
        print(content)
        print("-" * 40)
print(myfiles)