from cryptography.fernet import Fernet

# asking the user for a master password to grant access to the file

'''
# we have removed the write ke function because we have now generated our key.
# And there is no need for it anymore.
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb = write in bytes
        key_file.write(key) '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

#declaration of our functions
def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip()) #removes the extra spaces at the end of the file.
            user, passw = data.split("|") #splits the data at the |
            print("User:",user, "| Password:", fer.encrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

#with open the file is both automatically opens and closes when we are done using the file.
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


#enclosed within a while loop to make sure that we continue to prompt the user to input a given option.
while True:
    mode = input("Would you like to add a new password or view an existing password (view/add), press q to quit?: ").lower()
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode! Make a selection from the given choices.")
        continue

