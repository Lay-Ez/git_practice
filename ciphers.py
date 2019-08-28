
#creates an alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

#decodes vigenere cipher

def decode_vigener(message, keyword):
    pointer = 0
    keyword_phrase = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            keyword_phrase += keyword[pointer%len(keyword)]
            pointer += 1
        else:
            keyword_phrase += message[i]
    coded_phrase = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            coded_phrase += alphabet[(alphabet.find(message[i]) - alphabet.find(keyword_phrase[i]))]
        else:
            coded_phrase += message[i]
    print(coded_phrase)

#codes vigenere cipher

def code_vigener(message, keyword):
    pointer = 0
    keyword_phrase = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            keyword_phrase += keyword[pointer%len(keyword)]
            pointer += 1
        else:
            keyword_phrase += message[i]
    coded_phrase = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            coded_phrase += alphabet[(alphabet.find(message[i]) + alphabet.find(keyword_phrase[i]))%26]
        else:
            coded_phrase += message[i]
    print(coded_phrase)

print("\n ---Welcome to vigenere ciphering machine!---\n")

while True:
    user_input = input("\n Enter 'code' to cipher the message, enter 'decode' to decipher the message\n")
    if user_input == "code":
        user_message = input("\n Enter the message you want to cipher\n")
        user_codeword = input("\n Enter the codeword\n")
        print("\n\n This is your coded message:\n  ")
        code_vigener(user_message, user_codeword)
        continue
    if user_input == "decode":
        user_message = input("\n Enter the message you want to decipher\n")
        user_codeword = input("\n Enter the codeword\n")
        print("\n\n This is your decoded message:\n  ")
        decode_vigener(user_message, user_codeword)
        continue
    if user_input == "exit":
        print("\n\n ---finishing---\n")
        break
