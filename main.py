# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                               protection="scryptAndAES128-CBC")

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

print(key.publickey().export_key())

print("-----------------------------------------------------------------")

secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

print(key.publickey().export_key())

print(key.export_key())

# Hash a single string with hashlib.sha256
import hashlib
a_string = 'this string holds important and private information'
hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print("here is the last part")
print(hashed_string)
# Returns:
# 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1

