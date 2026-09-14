def mask_email(email):
    at_index = email.find("@")
    
    username = email[:at_index]
    domain = email[at_index:]
    
    first_char = username[0]
    last_char = username[-1]
    
    mask_length = len(username) - 2
    masked_middle = "*" * mask_length
    
    return f"{first_char}{masked_middle}{last_char}{domain}"

email = "myEmail@email.com"
print(mask_email(email))
