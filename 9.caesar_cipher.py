import string

alphabet= string.ascii_letters

while True:
    what_to_do= input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ").strip().lower()
    if what_to_do not in ["decrypt","encrypt"]:
        print("Please! Type valid input")
        continue
    
    # encryption
    if what_to_do == "encrypt":
        message= input("Type your message: ").strip().lower()
        
        # checking value of number given by user is digit or not
        while True:
            number= input("Type the shift number: ")            
            if number.isdigit():
                break
            else:
                print("Please! Enter number only.")
                continue
        key= int(number)

        i= 0
        position= 0
        encrypt_text= ""
        for char in message:
            if char in alphabet:
                position= alphabet.index(char)  #alphabet ma char ko index position ma assign garxa
                new_position= (position+key)%26
                encrypt_text+= alphabet[new_position]
                # print(f"alphabet: {char} org_position: {position} new_position: {new_position} encrypted_text: {encrypt_text}")
            else:
                encrypt_text += char

            i+=1
        print(f"org_text:{message} ")
        print(f"encrypted_text:{encrypt_text}")

        # encryption bata auto decryption ko lagi
        decrypt_text= ""
        for char in encrypt_text:
            if char in alphabet:
                position= alphabet.index(char)
                new_position= (position-key)%26
                decrypt_text+= alphabet[new_position]
                # print(f"alphabet: {char} org_position: {position} new_position: {new_position} encrypted_text: {encrypt_text}")
            else:
                decrypt_text += char

            i+=1
        print(f"encrypted_text:{encrypt_text} ")
        print(f"decrypted_text:{decrypt_text}")

    # if user type decrypt ko lagi 
    # decryption
    if what_to_do == "decrypt":
        decrypt_text= input("Type your message: ").strip().lower()

        while True:
            number= input("Type the shift number: ")
            
            if number.isdigit():
                break
            else:
                print("Please! Enter number only.")
                continue
        key= int(number)

        i= 0
        position= 0
        plain_text= ""
        for char in decrypt_text:
            if char in alphabet:
                position= alphabet.index(char)
                new_position= (position-key)%26
                plain_text+= alphabet[new_position]
                # print(f"alphabet: {char} org_position: {position} new_position: {new_position} encrypted_text: {encrypt_text}")
            else:
                plain_text += char

            i+=1
        print(f"decrypted_text:{decrypt_text} ")
        print(f"decrypted_text:{plain_text}")


        while True:
            question= input("Type 'yes' if you want to go again. otherwise type 'no: '(yes/no)").strip().lower()
            if question not in ["yes", "no"]:
                print("please type valid answer")
                continue
            if question in ["yes"]:
                break
            else:
                print("Thanks for visiting")
                exit()

        
        




        



