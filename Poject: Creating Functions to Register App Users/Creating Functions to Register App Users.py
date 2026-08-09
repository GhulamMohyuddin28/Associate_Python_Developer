# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)


def validate_user(name, email, password):
    if validate_name(name) == False:
       raise ValueError("In valid name")
        
    if validate_email(email) == False:
        raise ValueError("In Valid Email")
    
    if validate_password(password) == False:
        raise ValueError("In Valid password")
        
    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except:
        return False
    user = {
        "name": name,
        "email": email,
        "password": password
    }

    return user
    
