# This script calculates the number of letter, vowels, and consonants in the given word

# Print out a messsage to prompt user 
print('Please type in a word: ')

# take input from the user and initialize variables needed for the program to run 
word = input()
chars = 0
vowels = 0
consonants = 0

# main logic: calculate all chars, vowels, and consonants in the given word
# definition for chars: all characters in the word
# definition for vowels: a,e,i,o,u
# definition for consonants: all characters except vowels
for ch in word:
    chars = chars + 1

    if ch == 'a':
        vowels = vowels + 1
    elif ch == 'e':
        vowels = vowels + 1
    elif ch == 'i':
        vowels = vowels + 1
    elif ch == 'o':
        vowels = vowels + 1
    elif ch == 'u':
        vowels = vowels + 1
    else:
        consonants = consonants + 1

#print out output with number of letters, vowels, and consonants
print('Number of letters in the given word: %s' % chars)
print('Number of vowels in the given word: %s' % vowels)
print('Number of consonants in the given word: %s' % consonants)