email = input("Enter your Email: ")
index = email.index("@")
userName = email[:index]
domain = email[index+1:] # +1 refers markelimentfrom index to next element.

print (f"Your user name is {userName} and domain is {domain}")