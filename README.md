# Password Strength Analyzer

A robust Python script designed to evaluate the strength and security of user-entered passwords using character analysis, mathematical entropy calculation, rule-based scoring, and common leak checks.

## Features
- **Length Analysis:** Measures total character count.
- **Entropy Calculation:** Computes the mathematical unpredictability and strength against brute-force attacks based on character pool variety (lowercase, uppercase, digits, symbols).
- **Rule-Based Scoring:** Awards points based on character diversity.
- **Common Password Check:** Flags weak passwords found in common lists or previous data leaks.
- **Actionable Feedback:** Provides specific recommendations to improve password strength.

## Requirements
- Python 3.x

## Usage
Run the script from your terminal:
```bash
python password_checker.py
```

## Project Structure
```text
password-strength-analyzer/
│
├── password_checker.py    # Main script with entropy and rule-based logic
└── README.md              # Project documentation
```
