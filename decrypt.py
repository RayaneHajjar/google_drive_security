from Crypto.Cipher import AES

def decryptAES(cipherAESd,cipherText):
    dec= cipherAESd.decrypt(cipherText)
    return dec

def decrypt(pk, ciphertext):
    d, n = pk
    m = [chr((char ** d) % n) for char in ciphertext]
    return m

def main():
    # Getting the private key and the AES symmetric key from the user input
    pri = tuple(int(item) for item in input("Enter the Private Key without (): ").split(','))
    cipherKey = [int(item) for item in input("Enter the AES Symmetric Key without []: ").split(',')]
    # Reading the cipherText from the cipher.txt file
    f = open("cipher.txt", "r")
    cipherText = f.read()
    cipherText = cipherText[1:]
    cipherText = cipherText[1:]
    cipherText = cipherText.rstrip("\'")
    cipherText = bytes(cipherText,'utf-8')
    cipherText = cipherText.decode('unicode-escape').encode('ISO-8859-1')
    # Getting the nonce from the user input
    nonce = input("Enter the nonce: ")
    nonce = nonce[1:]
    nonce = nonce[1:]
    nonce = nonce.rstrip("\'")
    nonce = bytes(nonce,'utf-8')
    nonce = nonce.decode('unicode-escape').encode('ISO-8859-1')
    # Decrypting the AES Symmetric Key
    decriptedKey=''.join(decrypt(pri,cipherKey))
    decriptedKey = decriptedKey.encode('utf-8')
    cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
    # Decrypting the message using the AES symmetric key
    decrypted = decryptAES(cipherAESd,cipherText)
    decrypted = decrypted.decode()

    return decrypted    