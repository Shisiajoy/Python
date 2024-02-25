import re

def extract_phone_numbers(phone_pattern, text): #function to extract phone number
    result = re.findall(phone_pattern, text)  #re.findall() to find all matches of phone pattern
    return result  
text = "please contact info@example for assistance.Phone:(123) 456-7890 or (111) 222-3333"
phone_pattern = r"(\d{3})?[-.\s]?\d{3}[-.\s]?\d{4}"
extracted_phone_numbers = extract_phone_numbers(text,phone_pattern) #calling the function and storing in a variable extracted_phone_numbers 
print(extracted_phone_numbers)

def extract_email_addresses(text,email_pattern): #function to extract email addresses 
    result = re.findall(email_pattern,text) #re.findall to find all matches of the email pattern
    return result
text = "please contact info@example for assistance.Phone:(123) 456-7890 or (111) 222-3333"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"
extracted_email_addresses = extract_email_addresses(text,email_pattern) #calling the function and storing in the vatiable extracted_email_addresses
print(extract_email_addresses)

def replace_email_adresses(text,email_pattern,replacement):  #function tto replace email addresses
    modified = re.sub(email_pattern,replacement,text)       #re.sub() to replace all matches of the email pattern  
    return modified
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"
print(replace_email_adresses(text,replacement))