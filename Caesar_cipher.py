letters = "abcdefghijklmnopqrstuvwxyz"
numletters = len(letters)

def encrypt_decrypt(user_input,key,mode):
    result = ""
    if mode == 'd':
        key = -key
    
    for letter in user_input:
        letter = letter.lower()
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= numletters:
                    new_index -= numletters
                result += letters[new_index]
        else:
            pass
    return result

# Driver Code
mode = input("[*] Do you want to Encrypt or Decrypt (e\d) : ")
key = int(input("[*] Enter the key : "))
if mode == 'e':
    user_input = input("[*] Enter text to Encrypt : ")
    result = encrypt_decrypt(user_input,key,mode)
    print(f'[+] Encrypted Text : {result}')
elif mode == 'd':
    user_input = input("Enter text to Decrypt : ")
    result = encrypt_decrypt(user_input,key,mode)
    print(f'[+] Decrypted Text : {result}')