from cryptography.fernet import Fernet
import base64, os, sys, hashlib,codecs,argparse

parser = argparse.ArgumentParser(description='Encrypt and decrypt files')
parser.add_argument('--password', help="the password used to encrypt and decrypt the given file")
parser.add_argument('--encrypt', help="encrypts a file")
parser.add_argument('--decrypt', help="dencrypts a file")
parser.add_argument('--path')
args = parser.parse_args()



password = args.password
if password == None:
    password = input("password: ")

m = hashlib.sha256()
m.update(password.encode("utf-8"))
key = base64.urlsafe_b64encode(m.digest())
fernet = Fernet(key)



def get_file_contents(path):
    f = codecs.open(path, 'rb')
    contents = f.read()
    #print(contents)
    f.close()
    return contents


def encrypt(path):
    try:
        contents = get_file_contents(path)
        print("encrypting")
        f = codecs.open(path, 'wb')
        try:
            contents = fernet.encrypt(contents)
        except:
            print("failed to encrypt")
        f.write(contents)
        f.close()

    except:
        for dirname, _, filenames in os.walk(str(path)):
            for filename in filenames:
                #print(os.path.join(dirname, filename))
                
                contents = get_file_contents(os.path.join(dirname, filename))
                print("encrypting")
                f = codecs.open(os.path.join(dirname, filename), 'wb')
                try:
                    contents = fernet.encrypt(contents)
                except:
                    print("failed to encrypt")
                f.write(contents)
                f.close()


def decrypt(path):
    try:
        contents = get_file_contents(path)
        print("decrypting")
        f = codecs.open(path, 'wb')
        try:
            contents = fernet.decrypt(contents)
        except:
            print("failed to decrypt")
        f.write(contents)
        f.close()

    except:
        for dirname, _, filenames in os.walk(str(path)):
            for filename in filenames:
                #print(os.path.join(dirname, filename))
                
                contents = get_file_contents(os.path.join(dirname, filename))
                print("decrypting")
                f = codecs.open(os.path.join(dirname, filename), 'wb')
                try:
                    contents = fernet.decrypt(contents)
                except:
                    print("failed to decrypt")
                f.write(contents)
                f.close()

if args.encrypt != None:
    encrypt(args.encrypt)

elif args.decrypt != None:
    decrypt(args.decrypt)

else:
    type = input("e/d")
    if args.path != None:
        if type == "e":
            encrypt(args.path)
        elif type == "d":
            decrypt(args.path)
    else:
        if type == "e":
            encrypt(input("path: "))
        elif type == "d":
            decrypt(input("path: "))
