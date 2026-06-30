# Q16) Convert a lowercase letter to uppercase using ONLY ord() and chr()
# (no built-in .upper() or .capitalize() allowed)
#
# Brief on ASCII: ASCII (American Standard Code for Information Interchange)
# assigns every character a unique numeric code. Lowercase letters 'a' to 'z'
# occupy codes 97-122, while uppercase letters 'A' to 'Z' occupy codes 65-90.
# Notice that each lowercase letter is EXACTLY 32 more than its uppercase
# counterpart (e.g., 'a'=97, 'A'=65, difference = 32). So subtracting 32 from
# a lowercase letter's ASCII code gives the uppercase version's ASCII code.

letter = input("Enter the letter: ")

# Get the ASCII value of the input character
ascii_value = ord(letter)

# Subtract 32 to shift from lowercase range (97-122) to uppercase range (65-90)
uppercase_ascii_value = ascii_value - 32

# Convert the new ASCII value back into a character
uppercase_letter = chr(uppercase_ascii_value)

print("Output:", uppercase_letter)
