import os
import encrypt
import functionnalities
import decrypt

print ("Welcome!")
print ("# Press 1 to upload file")
print ("# Press 2 to download file")
print ("# Press 3 to list all files")
print ("# other key to exit")

op = int(input())

if (op == 1):
    drive = functionnalities.googleDrive()
    file_location = input('Enter file name with path: (without "") ')
    encrypted = encrypt.main()
    decrypted = decrypt.main()
    if (encrypted == decrypted):
        functionnalities.uploadFile(drive, file_location)
        print("DONE!")
    else:
        print("ACCESS DENIED!")    
elif (op == 2):
    drive = functionnalities.googleDrive()
    file_id = input("Enter File id: ")
    encrypted = encrypt.main()
    decrypted = decrypt.main()
    if (encrypted == decrypted):
        functionnalities.downloadFile(drive, file_id)
        print("DONE!")
    else:
        print("ACCESS DENIED!")    
elif (op == 3):
    drive = functionnalities.googleDrive()
    functionnalities.listFiles(drive)
else:
    os._exit(0)