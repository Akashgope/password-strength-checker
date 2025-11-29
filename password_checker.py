import re

def check_password_strength(password):
    """
    Check the strength of a password based on criteria:
    - Minimum 8 characters length
    - Contains both uppercase and lowercase letters
    - Contains at least one digit (0-9)
    - Contains at least one special character (!@#$% etc.)
    
    Args:
        password (str): The password to check
        
    Returns:
        bool: True if password meets all criteria, False otherwise
    """
    
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for digits
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit (0-9)"
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (!@#$% etc.)"
    
    return True, "Password is strong!"

def get_password_feedback(password):
    """
    Provide detailed feedback on password strength
    """
    feedback = []
    
    # Check each criterion
    if len(password) >= 8:
        feedback.append("✓ Minimum length (8 characters)")
    else:
        feedback.append("✗ Minimum length (8 characters)")
    
    if re.search(r'[A-Z]', password):
        feedback.append("✓ Uppercase letter")
    else:
        feedback.append("✗ Uppercase letter")
    
    if re.search(r'[a-z]', password):
        feedback.append("✓ Lowercase letter")
    else:
        feedback.append("✗ Lowercase letter")
    
    if re.search(r'\d', password):
        feedback.append("✓ Digit (0-9)")
    else:
        feedback.append("✗ Digit (0-9)")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("✓ Special character")
    else:
        feedback.append("✗ Special character")
    
    return feedback

def main():
    """
    Main function to run the password strength checker
    """
    print("🔐 Password Strength Checker")
    print("=" * 40)
    print("Password requirements:")
    print("- Minimum 8 characters")
    print("- Uppercase and lowercase letters")
    print("- At least one digit (0-9)")
    print("- At least one special character (!@#$% etc.)")
    print("=" * 40)
    
    while True:
        try:
            # Get password input from user
            password = input("\nEnter your password (or 'quit' to exit): ").strip()
            
            # Check if user wants to quit
            if password.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            # Check password strength
            is_strong, message = check_password_strength(password)
            
            # Display results
            print(f"\nPassword: {'*' * len(password)}")
            print(f"Strength: {'STRONG ✅' if is_strong else 'WEAK ❌'}")
            print(f"Message: {message}")
            
            # Show detailed feedback
            if not is_strong:
                print("\nDetailed feedback:")
                feedback = get_password_feedback(password)
                for item in feedback:
                    print(f"  {item}")
            
            # Suggest strong password if weak
            if not is_strong:
                print("\n💡 Tip: Try adding missing elements to make your password stronger!")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()