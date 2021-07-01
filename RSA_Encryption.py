import json
  
#load alfabet.json JSON file
f = open ('alfabet.json', "r")  
# Reading from file
data = json.loads(f.read())



print('''
  _____       _     _                ___    __   ___  
 |  __ \     (_)   | |              / _ \  / /  / _ \ 
 | |__) |__ _ _  __| | ___  ___ _ _| (_) |/ /_ | | | |
 |  _  // _` | |/ _` |/ _ \/ _ \ '_ \__, | '_ \| | | |
 | | \ \ (_| | | (_| |  __/  __/ |_) |/ /| (_) | |_| |
 |_|  \_\__,_| |\__,_|\___|\___| .__//_/  \___/ \___/ 
            _/ |               | |                    
           |__/                |_|    RSA ENCRYPTION 
''')


print()
print("Public key and Private key for this program is: ")
# key generation :
# in this case we use two prime number : 
prime_1 = 5
prime_2 = 17

n = prime_1*prime_2

# Calculate the totient function φ(n):
totientFunction = (prime_1 - 1)*(prime_2 - 1)

# choose e :
# 1 < e < φ(n)
# and e and φ(n) are prime to each other
# Let e = 13 as gcd(e, φ(n)) = 1
e = 13

# now public key is (e, n)
print('Public key = ( ',e , ',', n, ')')

# let d = 5
d = 5

# now private key is (d, n)
print('Private key = (',d , ',', n, ')')




# in this case we use,
# e = 13
# d = 5
# n = 85
# Public key = (  13 , 85 ) and
# Private key = ( 5 , 85 )



# functions:
# encryption with alfabet position value
def encryption(message):
        encry_mess = pow(message, e) % n
        return encry_mess

# decryption with alfabet position value
def decryption(encryption_message):
    decry_mess = pow(encryption_message, d) % n
    return decry_mess

# function to return key for any value
def get_key(val):
    for key, value in data.items():
         if val == value:
             return key


# encrypted original text:
def encryption_text(message):
    encry_lst = list(message)
    # print(lst)
    encry_message_lst = []
    for alfabet in encry_lst:    
        mess_num = data.get(str(alfabet))
        encry_message_lst.append(int(mess_num))
    # print(message_lst)

    encry_mess_lst = []
    for mess in encry_message_lst:
        encry_mess_lst.append(encryption(mess))
    # print(encry_mess_lst)

    encry_ascii_lst = []
    for encry_num in encry_mess_lst:
        encry_ascii_lst.append(get_key(encry_num))
    # print(encry_ascii_lst)

    separator = ''
    encryption_message = separator.join(encry_ascii_lst)
    return encryption_message
    
# decrypted encrypted text : 
def decryption_text(decryption_message):
    decry_mess = decryption_message
    decry_lst = list(decry_mess)

    decry_message_lst = []
    for alfabet in decry_lst:    
        mess_num = data.get(str(alfabet))
        decry_message_lst.append(int(mess_num))

    decry_mess_lst = []
    for mess in decry_message_lst:
        decry_mess_lst.append(decryption(mess))

    decry_ascii_lst = []
    for decry_num in decry_mess_lst:
        decry_ascii_lst.append(get_key(decry_num))
    # print(decry_ascii_lst)

    separator = ''
    decryption_message = separator.join(decry_ascii_lst)
    return decryption_message






# for user command:
print('''
           :Executive Command: 
1.For encrypt your message Press: E /e /1
2.For decrypt your encrypt message Press: D /d /2
3.For all encryption and decryption Press: A /a /3
4.For exit Press: X /x /4
''')
# for input your message : 
command = input("Enter Your Executive Command: ")
print()
if command == "e" or command == "E" or command == "1":
    message = input("Enter Your Message (only english) For Encryption: ")
    # output message: 
    encrypted_message =  encryption_text(message)   
    print("Encrypt message is: ",encrypted_message)
elif command == "d" or command == "D" or command == "2":
    message = input("Enter Your Encrypt Message (only english) For Decrypt: ")
    decrypted_message = decryption_text(message)
    print("Now the original Decrypt message is: ",decrypted_message)
elif command == "a" or command == "A" or command == "3":
    message = input("Enter Your Message: ")
    encrypted_message =  encryption_text(message)   
    print("Encryption message (only english) is: ",encrypted_message)
    decrypted_message = decryption_text(encrypted_message)
    print("Now the original Decryption message is: ",decrypted_message)
elif command == "x" or command == "X" or command == "4":
    print("Exit")

else:
    print("Please type above any command for execute this program.")
