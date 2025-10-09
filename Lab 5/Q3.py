try:
    list1 = input("Enter first list elements separated by space: ").split()
    list2 = input("Enter second list elements separated by space: ").split()
    if len(list1) != len(list2):
        print("Both lists must have the same number of elements.")
    else:
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = list2[i]
        with open("dictionary.txt", "w") as f:
            for k, v in d.items():
                f.write(f"{k}: {v}\n")
        print("Dictionary saved to dictionary.txt")
except Exception as e:
    print("Error:", e)
