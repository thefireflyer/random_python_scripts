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
    f = codecs.open(path, 'r')
    contents = f.read()
    #print(contents)
    f.close()
    return contents


if args.encrypt != None:
    contents = get_file_contents(args.encrypt)
    print("encrypting")
    f = codecs.open(args.encrypt, 'w')
    f.write(fernet.encrypt(contents.encode()).decode())
    f.close()

if args.decrypt != None:
    contents = get_file_contents(args.decrypt)
    print("decrypting")
    f = codecs.open(args.decrypt, 'w')
    try:
        contents = fernet.decrypt(contents.encode()).decode()
    except:
        print("failed to decrypt")
    f.write(contents)
    f.close()

