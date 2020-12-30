import uuid
import string
from random import choice, shuffle


def generate_password(data):

    print(data)

    characters = string.ascii_lowercase
    password = ''

    if data.get('has_numbers'):
        characters += string.digits
    
    if data.get('has_uppercases'):
        characters += string.ascii_uppercase
    
    if data.get('has_special'):
        characters += string.punctuation

    length = int(data.get('length'))
    for _ in range(length):
        random_character = choice(characters)
        password += random_character
    
    return password
