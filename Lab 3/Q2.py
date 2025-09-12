def check(word):
    vowels = "aeiouAEIOU"
    last=word[-1]  
    if last in vowels:
        print("The last letter of this word is a vowel")
    else:
        print("The last letter of this word is a consonant")

Checking_word= input("Enter a word that you want to check: ")
check(Checking_word)
