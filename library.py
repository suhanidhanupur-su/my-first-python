# Palindrome Checker

text = input("Enter a word or number: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is NOT a Palindrome")