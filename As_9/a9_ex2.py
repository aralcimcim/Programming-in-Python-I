import re

def extract_emails(text: str) -> list[str]:
    pattern = r"(?:\s|\n)([_a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    return re.findall(pattern, text)

t = """
Here are some email addresses:
john.doe@example.com, alice_smith123@gmail.com, ABC+@a-b-c.aBc,
contact@company.org, and info@sub.domain.co.uk.
Some invalid email addresses are:
john@, @example.com, user@domain, us/er@email.com,
invalid@domain.f and invalid.email@invalid@domain.com.
"""
print(extract_emails(t))