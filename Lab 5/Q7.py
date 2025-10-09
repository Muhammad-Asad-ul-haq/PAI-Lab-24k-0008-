def fix_file():
    try:
        with open("replacement_needed.txt", "r") as f:
            text = f.read()
        corrected = ""
        for ch in text:
            if ch == "x":
                corrected += "e"
            else:
                corrected += ch
        with open("replacement_needed.txt", "w") as f:
            f.write(corrected)
        print("Correction done successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

fix_file()
