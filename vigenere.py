def vigenere(text, key, mode='encrypt'):
    """The Vigener Cipher"""
    result = []
    key = key.upper() 
    
    for i, char in enumerate(text):
        if not char.isalpha():
            result.append(char) 
            continue
                  
        char_upper = char.upper()
        is_ru = 'А' <= char_upper <= 'Я'
        base = ord('А') if is_ru else ord('A') 
        size = 32 if is_ru else 26 
        
        key_char = key[i % len(key)] 
        key_is_ru = 'А' <= key_char <= 'Я'
        key_base = ord('А') if key_is_ru else ord('A')
        
        shift = ord(key_char) - key_base  
    
        if mode == 'encrypt':
            new_char = chr((ord(char_upper) - base + shift) % size + base) 
        else:
            new_char = chr((ord(char_upper) - base - shift) % size + base)
        
        result.append(new_char if char.isupper() else new_char.lower()) 
    return ''.join(result)

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

key = input("Key: ")

encrypted = vigenere(text, key, 'encrypt')
with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted)

decrypted = vigenere(encrypted, key, 'decrypt')
with open('decrypted.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted)

print("Ready! Check the files encrypted.txt and decrypted.txt")