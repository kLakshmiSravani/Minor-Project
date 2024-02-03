import re

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Compile the regex
    regex = re.compile(email_regex)
    
    # Check if the email matches the pattern
    if regex.match(email):
        return True
    else:
        return False

def validate_email_file(file_path):
    valid_emails = []
    invalid_emails = []

    try:
        with open(file_path, 'r') as file:
            email_list = file.read().splitlines()

        for email in email_list:
            if is_valid_email(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)

        return valid_emails, invalid_emails

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], []

if name == "main":
    # Example usage
    file_path = "emails.txt"  # Replace with your file path

    valid_emails, invalid_emails = validate_email_file(file_path)

    print("Valid Emails:")
    print(valid_emails)

    print("\nInvalid Emails:")
    print(invalid_emails)