#Name- Tanubrata Dey
#Date- Feb 11, 2018
#This program prints: Caesar Cipher

plaintext = input('Enter message: ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 2
cipher = ''

for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]

print('Your encrypted message is: ' + cipher)
