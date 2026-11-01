import math
import re

# List of common or leaked passwords to check against
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty", 
    "admin", "welcome", "monkey", "password123", "letmein"
}

def calculate_entropy(password):
    """
    Calculates the mathematical entropy of the password based on character pool size.
    """
    if not password:
        return 0.0
    
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32  # Special characters approximation
        
    if pool_size == 0:
        return 0.0
        
    # Entropy formula: length * log2(pool_size)
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def score_password(password):
    """
    Evaluates password strength using length, entropy, rule-based scoring, and common password checks.
    """
    score = 0
    feedback = []
    
    # 1. Check if it's a common password
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password is too common and easily guessable!")
        return 0, "Weak", feedback

    # 2. Length check
    length = len(password)
    if length >= 12:
        score += 30
        feedback.append("Good length.")
    elif length >= 8:
        score += 15
        feedback.append("Password could be longer (recommended: 12+ characters).")
    else:
        feedback.append("Password is too short.")

    # 3. Rule-based checks
    if re.search(r'[a-z]', password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")
        
    if re.search(r'[A-Z]', password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")
        
    if re.search(r'[0-9]', password):
        score += 20
    else:
        feedback.append("Add numbers.")
        
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 20
    else:
        feedback.append("Add special characters.")

    # Cap score at 100
    score = min(score, 100)

    # 4. Verdict evaluation
    if score >= 80:
        verdict = "Very Strong"
    elif score >= 60:
        verdict = "Strong"
    elif score >= 40:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return score, verdict, feedback

def main():
    print("==========================================")
    print("      PYTHON PASSWORD STRENGTH CHECKER    ")
    print("==========================================")
    
    password = input("Enter a password to analyze: ")
    
    length = len(password)
    entropy = calculate_entropy(password)
    score, verdict, feedback = score_password(password)
    
    print("\n--- Password Analysis ---")
    print(f"Length  : {length} characters")
    print(f"Entropy : {entropy} bits")
    print(f"Score   : {score}/100")
    print(f"Verdict : {verdict}")
    
    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f" - {item}")

if __name__ == "__main__":
    main()
