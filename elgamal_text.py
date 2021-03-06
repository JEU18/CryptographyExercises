import binascii
# Jenna Uba May 16, 2019
# This program uses Elgamal's Encryption method to take a message that is inputted by a user and encrypt it.
# The program also uses Elgamal's Decryption method to take a  message and decrypt it.


# Function One: This is a function that calculates that converts the power value into a binary (represented as a string
# for comparison purposes. It then uses this binary value to help efficiently compute the moded exponent expression


def fast_powering(b, p, m):
    power_bin = str(bin(p)[:1:-1])
    multipliers = []
    answer = 1
    for digit in range(0, len(power_bin)):
        if power_bin[digit] == '1':
            calculation = (b**(2**digit)) % m
            multipliers.append(calculation)
    for value in range(0, len(multipliers)):
        answer *= multipliers[value]

    return answer % m


# Function Two:  This is a function that finds the power by subtracting two from the inputted modulo value. This
# function then calls the fast powering algorithm function to compute the result.


def fast_inverse(a, m):
    p = m - 2
    return fast_powering(a, p, m)


# Function Three: Encrypts the inputted message. C1 and C2 are both computed and returned.


def encrypt(p, g, public_a, m):
    k = 197
    c_1 = fast_powering(g, k, p)
    c_2 = (m * fast_powering(public_a, k, p)) % p
    cipher_m = [c_1, c_2]
    return cipher_m


# Function Four: Decrypts the inputted message. C1 and C2 are used to compute the decrypted message

def decrypt(p, g, a, c):
    c_1 = int(c[0])
    c_2 = int(c[1])
    c_1_a = fast_powering(c_1, a, p)
    inverse = fast_inverse(c_1_a, p)
    cipher_c = (c_2 * inverse) % p
    test = format(cipher_c, '016b')
    i = 0
    output = ""
    while i < len(test):
        output += chr(int(test[i:i+8], 2))
        i += 8
    return output


# Function Five: Determines if the user would like to encrypt or decrypt a message. This is where inputs are taken
# from the user. Depending on the users inputs another function is called and its results are printed.

def run():
    action = input("Choose option 1 or 2\n1. Encrypt\n2. Decrypt\n")
    prime = int(input("Enter Prime: "))
    element = int(input("Enter Element: "))
    if action == "1":
        action_2 = input("Choose option 1 or 2\n1. Enter Public Key\n2. Use Default Public Key: 224\n")
        if action_2 == "1":
            key_public = int(input("Enter Public Key: "))
        else:
            key_public = 224
        message = input("Enter Message: ")
        msg = ' '.join(format(ord(x), '008b') for x in message)
        msg = msg.replace(" ", '')
        msg_int = int(msg, 2)
        print("The Encrypted Message is: ", encrypt(prime, element, key_public, msg_int))
    else:
        key_private = int(input("Enter Private Key: "))
        cipher_str = input("Enter Cipher Text is form C1 C2: ")
        cipher = [int(x) for x in cipher_str.split()]
        print("The Decrypted Message is: ", decrypt(prime, element, key_private, cipher))


run()

'''
p = 65511
g = 17
A = 63208
a = 153
m = "hi"
c = 27326, 50710


Choose option 1 or 2
1. Encrypt
2. Decrypt
1
Enter Prime: 65521
Enter Element: 17
Choose option 1 or 2
1. Enter Public Key
2. Use Default Public Key: 224
1
Enter Public Key: 63208
Enter Message: hi
The Encrypted Message is:  [27326, 50710]


Choose option 1 or 2
1. Encrypt
2. Decrypt
2
Enter Prime: 65521
Enter Element: 17
Enter Private Key: 153
Enter Cipher Text is form C1 C2: 27326 50710
The Decrypted Message is:  hi

'''
