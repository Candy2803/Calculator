def word_counter():
    text = input("Type here: ")

    words = text.split()
    word_count = len(words)
    
    letter_count = len(text)

    print(f"Word count is {word_count}")
    print(f"Character count is {letter_count}")
    
word_counter()