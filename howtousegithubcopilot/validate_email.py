import re

# Improved regex: robust local-part + stricter domain rules (not full RFC 5322).
EMAIL_RE = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+)*"
    r"@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}$",
    re.IGNORECASE,
)


def validate_email(email: str) -> bool:
    email = email.strip()
    if not email:
        return False
    return bool(EMAIL_RE.match(email))


def validate_emails(input_str: str):
    # Split on commas, semicolons, or any whitespace
    parts = re.split(r"[,\s;]+", input_str.strip())
    parts = [p.strip() for p in parts if p.strip()]
    valid = []
    invalid = []
    for p in parts:
        if validate_email(p):
            valid.append(p)
        else:
            invalid.append(p)
    return valid, invalid


if __name__ == "__main__":
    prompt = (
        "Enter one or more email addresses (comma/semicolon/whitespace-separated): "
    )
    data = input(prompt)
    valid, invalid = validate_emails(data)

    if valid:
        print("\nValid addresses:")
        for e in valid:
            print(" -", e)
    else:
        print("\nNo valid addresses found.")

    if invalid:
        print("\nInvalid addresses:")
        for e in invalid:
            print(" -", e)

    print(f"\nSummary: {len(valid)} valid, {len(invalid)} invalid.")
