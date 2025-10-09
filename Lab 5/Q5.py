try:
    n = int(input("Enter number of people: "))
    d = {}
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        d[name] = age
    with open("data.json", "w") as f:
        f.write(str(d))
    with open("data.json", "r") as f:
        content = f.read()
        data = eval(content)
    max_age = max(data.values())
    names = [k for k, v in data.items() if v == max_age]
    print("Person(s) with maximum age:", ", ".join(names))
except Exception as e:
    print("Error:", e)
