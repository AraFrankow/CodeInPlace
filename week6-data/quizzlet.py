"""
Write a program that loops over a dictionary of words and quizzes the user for their corresponding Spanish translations, keeping count of how many the user gets correct!
"""
def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    total_words = len(translations)
    cont_correct = 0
    for key in translations:
        spanish = translations[key]
        answ = input(f"What is the Spanish translation for {key}? ")
        if answ == spanish:
            cont_correct += 1
            print("That is correct!\n")
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {spanish}.\n")

    print(f"You got {cont_correct}/{total_words} words correct, come study again soon!")
if __name__ == '__main__':
    main()