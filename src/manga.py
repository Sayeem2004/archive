import json

def add(data):
    # Getting name
    print("\nWhat is the name of the manga?")
    name = input("    ")

    # Getting chapter
    print("\nWhat is the current chapter of the manga?")
    chapter = int(input("    "))

    # Getting completed status
    print("\nIs the manga completed?")
    completed = True if input("    ").lower() == "yes" else False

    # Getting summary
    print("\nWhat is the summary of the manga?")
    summary = input("    ")

    # Getting images
    print("\nWhat is the number of images you want to have?")
    num = int(input("    "))
    images = []
    for _ in range(num):
        print("\nWhat is the name of the image?")
        images.append(input("    "))

    # Making dictionary
    dict = {
        "chapter": chapter,
        "completed": completed,
        "summary": summary,
        "images": images
    }

    # Adding dictionary to data
    data[name] = dict

    # Saving json data
    file = open("data/manga.json", "w")
    json.dump(data, file, indent=4, sort_keys=True)


def update(data):
    # Printing entries and getting update number
    print("Which entry do you want to update?")
    keys = data.keys()
    for i, name in enumerate(keys):
        print("    " + str(i) + ": " + name)
    ind = int(input("    "))
    for i, name in enumerate(keys):
        if (i == ind):
            update = name

    # Getting chapter
    print("\nWhat is the new current chapter of the manga?")
    chapter = int(input("    "))

    # Getting completed status
    print("\nIs the manga now completed?")
    completed = True if input("    ").lower() == "yes" else False

    # Getting summary
    print("\nWhat is the new summary of the manga?")
    summary = input("    ")

    # Getting images
    print("\nWhat is the new number of images you want to have?")
    num = int(input("    "))
    images = []
    for _ in range(num):
        print("\nWhat is the name of the new image?")
        images.append(input("    "))

    # Making dictionary
    dict = {
        "chapter": chapter,
        "completed": completed,
        "summary": summary,
        "images": images
    }

    # Updating dictionary in data
    data[update] = dict

    # Saving json data
    file = open("data/manga.json", "w")
    json.dump(data, file, indent=4, sort_keys=True)

def remove(data):
    # Printing entries and getting remove number
    print("Which entry do you want to remove?")
    keys = data.keys()
    for i, name in enumerate(keys):
        print("    " + str(i) + ": " + name)
    ind = int(input("    "))
    for i, name in enumerate(keys):
        if (i == ind):
            remove = name

    # Removing dictionary from data
    data.pop(remove)

    # Saving json data
    file = open("data/manga.json", "w")
    json.dump(data, file, indent=4, sort_keys=True)

def main():
    while (True):
        # Reading data from json file
        fin = open("data/manga.json", "r")
        data = json.load(fin)

        # Asking for command
        print("\nHow do you want to update manga.json?\n    0: Add\n    1: Update\n    2: Remove\n    3: Exit")
        num = input("    ")
        if (num == "0"):
            add(data)
        elif (num == "1"):
            update(data)
        elif (num == "2"):
            remove(data)
        elif (num == "3"):
            print("\nShutting down manga.py")
            break
        else:
            print("\nInvalid command, no changes made")

main()
