# Get input from user
letter = input("Enter a letter of the alphabet: ").lower()

# Check if the letter is a vowel
if letter in 'aeiou':
    print(letter, "is a vowel.")
elif letter == 'y':
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print(letter, "is a consonant.")