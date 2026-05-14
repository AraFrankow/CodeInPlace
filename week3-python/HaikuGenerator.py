from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    response = call_gpt("i need  you make a haiku. In the first line i need 5 syllables, in the second 7 syllables and in the third 5 syllables. Use "+name+" and "+ topic)
    print(response)

if __name__ == "__main__":
    main()