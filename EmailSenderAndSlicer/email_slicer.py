# collecting email from user
# splitting the email using the @ symbol, the first part as the user name and the second part as domain
# splitting domain using . symbol

def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)

while True:
    main()