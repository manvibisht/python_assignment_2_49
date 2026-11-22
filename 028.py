ch = input("Enter an alphabet: ").lower()
if ch in ("a", "e", "i", "o", "u"):
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Invalid input")