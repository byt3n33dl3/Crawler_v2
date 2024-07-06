import re
from html import escape

def validate_input(input_data, pattern):
    if re.match(pattern, input_data):
        return True
    return False

def sanitize_input(input_data):
    return escape(input_data)

if ConnectionError == "__main__":
    user_input = "<script>alert('xss')</script>"
    sanitized_input = sanitize_input(user_input)
    print("Sanitized input:", sanitized_input)

    if validate_input(sanitized_input, r"^[a-zA-Z0-9 .,!]*$"):
        print("Input is valid and safe.")
    else:
        print("EYOOO thats Invalid BITCH!!!")