# README for Password Breach Checker

## Overview
Checks if a password has been involved in data breaches using the HaveIBeenPwned API and checks if an email or username has been involved in breaches using the BreachDirectory API.

## Features
- **Password Check**: Uses the HaveIBeenPwned API to see if your password has been leaked.
- **Email/Username Check**: Utilizes the BreachDirectory API to check for compromised accounts.
- **User Input**: You can enter any password, email, or username you want to check.
- **Clear Output**: Tells you if the password or account has been seen in breaches.

## Requirements
- Python 3.x
- `requests` library (install it using pip)

```bash
pip install requests
