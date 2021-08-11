from cryptography.fernet import Fernet
import base64, os, sys, hashlib,codecs,argparse

parser = argparse.ArgumentParser(description='Encrypt and decrypt files')
parser.add_argument('--password', help="the password used to encrypt and decrypt the given file")
parser.add_argument('--encrypt', help="encrypts a file")
parser.add_argument('--decrypt', help="dencrypts a file")
args = parser.parse_args()



password = str(args.password)
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


if args.encrypt != None:
    
    try:
        contents = get_file_contents(args.encrypt)
        print("encrypting")
        f = codecs.open(args.encrypt, 'wb')
        try:
            contents = fernet.encrypt(contents)
        except:
            print("failed to encrypt")
        f.write(contents)
        f.close()

    except:
        for dirname, _, filenames in os.walk(str(args.encrypt)):
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

if args.decrypt != None:
    
    try:
        contents = get_file_contents(args.decrypt)
        print("decrypting")
        f = codecs.open(args.decrypt, 'wb')
        try:
            contents = fernet.decrypt(contents)
        except:
            print("failed to decrypt")
        f.write(contents)
        f.close()

    except:
        for dirname, _, filenames in os.walk(str(args.decrypt)):
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



