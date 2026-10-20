import data.py

path = input("Enter the path:")

data = data.load_files(path)

while True:
    print("Functionalities:")

    print("1. Inspect files.")
    print("2. Organize files.")
    print("3. Find duplicates.")

    func = int(input("Enter the functionality:"))

    if func == 1:


    elif func == 2:


    elif func == 3:


    else:
        print("GoodBye and GodSpeed.")

    