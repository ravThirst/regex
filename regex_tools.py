import re


def format_phone_number(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)[1:]
    if len(cleaned_number) == 10:
        formatted_number = re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'+7(\1)\2-\3-\4', cleaned_number)
    elif len(cleaned_number) > 10:
        formatted_number = re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})(\d+)', r'+7(\1)\2-\3-\4 доб.\5', cleaned_number)
    else:
        formatted_number = phone_number
    return formatted_number
