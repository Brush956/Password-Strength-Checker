# Password Strength Checker

A simple Python tool that checks how strong your password is based on common security requirements.

## Requirements

- Python 3.6+

## How to Run

```bash
python "Password Strength Checker.py"
```

Then enter your password when prompted.

## Password Requirements

Your password must have:
- At least 8 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number
- At least 1 special character

## Scoring

- **0-2 points** = Weak Password ❌
- **4-6 points** = Moderate Password ⚠️
- **8-10 points** = Strong Password ✅

Each requirement met = 2 points (max 10 points).

## Example

```
Password Strength Checker

Enter your password: MyPassword123!
Your password meets the minimum length requirement ✅
Contains lowercase ✅
Contains uppercase ✅
Contains number ✅
Contains special character ✅

Your password strength score is: 10/10
Strong Password!
```

