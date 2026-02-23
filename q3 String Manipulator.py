# String Manipulator Program

# Ask user for input
sentence = input("Enter a sentence: ")

# 1. Original sentence
print("Original:", sentence)

# 2. Total characters (with spaces)
print("Characters (with spaces):", len(sentence))

# 3. Total characters (without spaces)
print("Characters (without spaces):", len(sentence.replace(" ", "")))

# 4. Total words
words = sentence.split()
print("Total words:", len(words))

# 5. UPPERCASE
print("UPPERCASE:", sentence.upper())

# 6. lowercase
print("lowercase:", sentence.lower())

# 7. Title Case
print("Title Case:", sentence.title())

# 8. First word
print("First word:", words[0])

# 9. Last word
print("Last word:", words[-1])

# 10. Reversed sentence
print("Reversed:", sentence[::-1])