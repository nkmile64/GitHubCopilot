import re

def is_valid_email(email):
    """
    Validate the given email address using a robust regular expression.
    
    Checks for:
    - Valid local part (before @)
    - Valid domain name
    - Valid TLD (at least 2 characters)
    - No consecutive dots or leading/trailing dots
    """
    email = email.strip()
    
    # Improved regex pattern for better robustness
    # Local part: alphanumeric, dots, underscores, hyphens, plus signs
    # Domain: alphanumeric, dots, hyphens
    # Prevents consecutive dots and leading/trailing special characters
    email_regex = r'^[a-zA-Z0-9]([a-zA-Z0-9._%-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        return False
    
    # Additional validation: no consecutive dots
    if '..' in email:
        return False
    
    return True

def validate_multiple_emails(emails):
    """
    Validate multiple email addresses and return results.
    
    Args:
        emails: List of email addresses to validate
        
    Returns:
        Dictionary with valid and invalid emails
    """
    results = {'valid': [], 'invalid': []}
    
    for email in emails:
        if is_valid_email(email):
            results['valid'].append(email)
        else:
            results['invalid'].append(email)
    
    return results

def display_results(results):
    """Display validation results in a formatted manner."""
    print("\n" + "="*50)
    print("EMAIL VALIDATION RESULTS")
    print("="*50)
    
    if results['valid']:
        print(f"\n✓ Valid Emails ({len(results['valid'])}):")
        for email in results['valid']:
            print(f"  • {email}")
    
    if results['invalid']:
        print(f"\n✗ Invalid Emails ({len(results['invalid'])}):")
        for email in results['invalid']:
            print(f"  • {email}")
    
    print("\n" + "="*50 + "\n")

# Example usage
if __name__ == "__main__":
    print("Email Validation Tool")
    print("-" * 50)
    
    # Interactive input for multiple emails
    print("\nEnter emails for validation (one per line, empty line to finish):")
    print("-" * 50)
    
    user_emails = []
    while True:
        email_input = input("Enter email (or press Enter to finish): ").strip()
        if not email_input:
            break
        user_emails.append(email_input)
    
    if user_emails:
        results = validate_multiple_emails(user_emails)
        display_results(results)
    else:
        print("No emails entered.")

