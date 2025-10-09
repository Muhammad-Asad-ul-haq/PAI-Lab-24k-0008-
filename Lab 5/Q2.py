try:
    filename = input("Enter file name: ")
    search = input("Enter word to search: ")
    replace = input("Enter word to replace with: ")
    with open(filename, 'r') as f:
        text = f.read()
    text = text.replace(search, replace)
    with open(filename, 'w') as f:
        f.write(text)
    print("Replacements done successfully.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
