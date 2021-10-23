import time
import sys
if sys.version_info >= (3, 7):
    import zipfile
else:
    import zipfile37 as zipfile

dict_file = 'dictionary.txt'
our_zip = 'test.zip'

f = open(dict_file, 'r')
zipF = zipfile.ZipFile(our_zip)

for password in f.readlines():
    try:
        # print(password[:-1])
        zipF.extractall(pwd=password[:-1].encode())
        print(f"{password[:-1]} is the correct password. Zip is extracted")
        break
    except:
        print(f"{password[:-1]} is not the password")
    time.sleep(0.2)
