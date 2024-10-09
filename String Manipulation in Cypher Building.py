#Cypher text and Cypher key
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

#Function with arguments: message, key and direction
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        #If iteration of message.lower is a letter, add to final_message variable
        if not char.isalpha():
            final_message += char
        #For non-letter characters
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

#Function is when you have an encrypted message
def encrypt(message, key):
    return vigenere(message, key)
    
#Function is when you want to encrypt your message
def decrypt(message, key):
    return vigenere(message, key, -1)

#A print of the cypher
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')