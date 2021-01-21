alphabet = "abcdefghijklmnopqrstuvwxyzz"
vowels = "aeiou"

word = input()
new_word = ""

for letter in word:
    new_word += letter
    if not letter in vowels:
        idx = alphabet.index(letter)
        for shift in range(26):
            if idx - shift >= 0 and alphabet[idx - shift] in vowels:
                new_word += alphabet[idx - shift]
                break
            if idx + shift < 26 and alphabet[idx + shift] in vowels:
                new_word += alphabet[idx + shift]
                break
        for letter in alphabet[idx + 1:]:
            if not letter in vowels:
                new_word += letter
                break

print(new_word)
