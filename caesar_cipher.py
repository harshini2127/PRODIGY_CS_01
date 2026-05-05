# Caesar Cipher Program for Encryption and Decryption
#function for encryption
def encrypt(text,shift):
    res=""
    for i in text :
        if i.isalpha():# To Check if character is a letter or not 
            ascii_val=(ord(i)) #To convert the letter into ascii value
            if i.islower():
                base=97 #base ascii value for lower-case letters
                position=ascii_val-base # Converts ASCII value to alphabet index(0–25)
            else:
                base=65 #base ascii value for upper-case letters
                position=ascii_val-base
            shifted_pos=(position+shift)% 26 # Apply shift and wrap around using modulo 26
            new_ascii=shifted_pos+base
            encrypted=chr(new_ascii) #To convert the ascii value into letter
            res=res+encrypted
        else: #if the charcter is num or symbol
            res=res+i
    return res
#function for decryption
def decrypt(text,shift):
    res=""
    for i in text :
        if i.isalpha():
            ascii_val=(ord(i))
            if i.islower():
                base=97
                position=ascii_val-base
            else:
                base=65
                position=ascii_val-base
            shifted_pos=(position-shift)% 26 # Apply negative shift for decryption and wrap using modulo 26
            new_ascii=shifted_pos+base
            decrypted=chr(new_ascii)
            res=res+decrypted
        else:
            res=res+i
    return res 

while True:
    print("USER MENU \n1.encrypt \n2.decrypt \n3.exit")
    option=int(input("choose any one:"))
    if option==1:
        text=input("enter the text you want to encrypted:")
        shift_value=int(input("enter the shift value:"))
        output=encrypt(text,shift_value)
        print("encrypted text:",output)
    elif option==2:
        text=input("enter the text you want to decrypt:")
        shift_value=int(input("enter the shift value:"))
        output=decrypt(text,shift_value)
        print("decrypted text:",output)
    elif option == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
