def vowel_counter():
    text = input("Type Here: ")
    vowels = "aeiou"
    
    vowel_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        
    print(f"\n Vowel count = {vowel_count}")
    
vowel_counter()