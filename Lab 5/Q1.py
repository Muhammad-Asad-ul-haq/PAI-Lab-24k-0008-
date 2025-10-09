try:
    filename = input("Enter file name: ")
    with open(filename, 'r') as f:
        text = f.read()
    chars = len(text)
    words = len(text.split())
    print("Characters:", chars)
    print("Words:", words)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)

