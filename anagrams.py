def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if are_anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")