# 1. Where are Unix Passwords Stored
# /etc/shadow

# 2. How unix passwords are created and secured
# using salt ref. https://searchsecurity.techtarget.com/definition/shadow-password-file

# 3. Understanding the dictionary
# testuser:$y$j9T$5v6fgZbWl050qJL0oUVlt.$P3G7lBX4BxkEAvmmogOCDI6V/URm3phk2OottFV98u6:18916:0:99999:7:::

# 4. Cracking Unix Password with Dictionary based attack

import crypt


def createHash(password, salt):
    return crypt.crypt(password, salt)


if __name__ == "__main__":
    # opening the password file and extracting password hash
    password_file = 'myPassword.txt'
    f = open(password_file, 'r')
    file_string = f.read()

    print(file_string)
    splitted_file_string = file_string.split(":")
    print(splitted_file_string)
    password_salt_hash = splitted_file_string[1]
    print(password_salt_hash)
    hash_id, salt, password_hash = password_salt_hash.split('$')[1:4]
    salt = f'${hash_id}${salt}'
    print("Hash: ", password_hash)
    print("Salt: ", salt)

    dict_file = 'dictionary.txt'
    fp = open(dict_file, 'r')

    for passwords in fp.readlines():
        # password = passwords[:-1]
        created_hash = createHash(passwords[:-1], salt)
        if(created_hash == password_salt_hash):
            print(f"Password is {passwords[:-1]}")
            break
        else:
            print(f"{passwords[:-1]} is incorrect")
