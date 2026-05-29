from ai import call_gpt
"""
A haiku is a type of very short poem that originated in Japan. 
It has three lines. The first line has 5 syllables, the second has 7 syllables, and the third has 5 syllables again. 
Haiku usually describe a moment in nature or a feeling, using clear, simple images. 
Even though it is brief, a good haiku often gives the reader a quiet, thoughtful feeling.
"""

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    response = call_gpt("i need  you make a haiku. In the first line i need 5 syllables, in the second 7 syllables and in the third 5 syllables. Use "+name+" and "+ topic)
    print(response)

if __name__ == "__main__":
    main()