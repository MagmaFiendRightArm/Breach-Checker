import requests
import hashlib

def check_password_breach(password):
    """Check if a password has been involved in known data breaches using the HaveIBeenPwned API."""
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
    return 0

def main():
    password = input("Enter a password to check: ")
    count = check_password_breach(password)
    
    if count:
        print(f"This password has been seen {count} times in known data breaches.")
        print("It's recommended to choose a different password.")
    else:
        print("Good news! This password hasn't been found in known data breaches.")
    print("Remember to use unique, strong passwords for each of your accounts.")

if __name__ == "__main__":
    main()
