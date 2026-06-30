# Q15) Take a string from user, print and count the number of vowels present

text = input("Enter a string: ")

vowels = "aeiouAEIOU"   # include both cases so we catch 'A' and 'a' alike

found_vowels = []  # to store each vowel character found, in order
count = 0           # running count of vowels

# Loop through every character in the string
for char in text:
    if char in vowels:        # check membership against the vowels string
        found_vowels.append(char)
        count += 1

print("Vowels found:", found_vowels)
print("Total number of vowels:", count)
