from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                    fer.decrypt(passw.encode()).decode())


def add():
    name = input('account name: ')
    pwd = input("password: ")
#w, r and a are modes. w means write which creates new file or override existing file. r means read file. a means append allows you to add something to end of exiosting file. if file doest exist it creates a new file
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add a new password or view existing (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue