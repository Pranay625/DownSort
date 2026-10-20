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

        print("---Inspection Report---")

        report = logic.inspect_file(data)

        for ext, count in report.items():
            print(f"Extension: {ext.upper()} | Total Files: {count}")

    elif func == 2:

        print("\n---Organizing Files---")

        instructions = logic.organize_files(data)

        if not instructions:
            print("No files to organize.")
        else:

            data.save_files(instructions)
            print(f"Successfully organized {len(instructions)} files!")

    elif func == 3:

        print("\n---Duplicate files---")

        duplicates = logic.find_duplicate(data)

        if not duplicates:
            print("No duplicates found!")
        else:
            print(duplicates)


    else:
        print("GoodBye and GodSpeed.")
        break

    