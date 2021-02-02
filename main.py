def check_digit(password):
    """ returns True if password contains a digit otherwise False """
    digit = False
    for item in password:
      if item.isdigit():
        digit = True
    return digit


def get_username():
    """ get a username 8 char lower case """
    name = input("Enter a username with 8 characters\n--> ")
    
    while len(name) !=8 :
      name = input("Enter a username with 8 characters\n--> ")
    username = name.lower() #puts into lowercase
    
    print("Welcome - your username is %s" % (username))
    return username


def get_password():
    """ get password 8 char & contains 1 digit """
    password = input("\nEnter password with at least 8 characters and 1 digit\n--> ")
    
    while not ((len(password) >= 8) and (check_digit(password) == True)) :
      password = input("Password must be at least 8 characters, containing 1 digit")
      
    re_enter = input("Re-enter your password for verification\n--> ")
    
    while not (re_enter == password):
      re_enter = input("Try again.\nRe-enter your password for verification\n--> ")
    
    return password
  
  
def register():
    """ get username & password --> write to file """
    user_name = get_username()
    user_password = get_password()
    
    # create record
    record = user_name + ", " + user_password + "\n"
    
    # write record to file
    myfile = open("passwd.txt", "a")
    myfile.write(record)
    myfile.close()
    
    print("\nWelcome - successful registration")
  
  
# MAIN PROGRAM calling register function
register()