from password_checker import check_password_strength

def test_passwords():
    """
    Test various passwords to verify the strength checker works
    """
    test_cases = [
        "weak",           # Too short
        "weakpass",       # No uppercase, digit, or special
        "Weakpass",       # No digit or special
        "Weakpass1",      # No special character
        "WEAKPASS1!",     # No lowercase
        "weakpass1!",     # No uppercase
        "Weak1!",         # Too short
        "StrongPass123!", # Should pass all criteria
        "Another$123Pass", # Should pass all criteria
    ]
    
    print("Testing Password Strength Checker")
    print("=" * 50)
    
    for password in test_cases:
        is_strong, message = check_password_strength(password)
        status = "✅ STRONG" if is_strong else "❌ WEAK"
        print(f"Password: {password:20} -> {status:10} | {message}")

if __name__ == "__main__":
    test_passwords()