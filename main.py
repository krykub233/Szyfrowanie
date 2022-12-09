encrypted_word = ""
word = "abc"

for i in range(len(word)):
    key = i+1
    if ord(word[i]) > 122 - key:
        encrypted_word += chr(ord(word[i]) + key - 26)
    else:
        encrypted_word += chr(ord(word[i]) + key)
print("Zaszyfrowany tekst:",encrypted_word)
