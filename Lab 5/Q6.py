def save_question():
    try:
        sentence = input("Enter a sentence: ")
        if sentence.endswith("?"):
            with open("questions.txt", "w") as f:
                f.write(sentence)
            print("Question saved to questions.txt")
        else:
            print("This is not a question.")
    except Exception as e:
        print("Error:", e)

save_question()
