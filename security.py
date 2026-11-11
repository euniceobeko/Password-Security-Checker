def check_password_strength(password):
    special_chars = "@#$!"
    
    # 1. Track rules (Flags)
    has_len = len(password) >= 8
    has_upper = False
    has_lower = False
    has_num = False
    has_special = False
    
    # 2. Inspect characters one-by-one
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_num = True
        if char in special_chars:
            has_special = True
            
    # 3. Calculate points
    score = sum([has_len, has_upper, has_lower, has_num, has_special])
    
    # 4. Set the strength text
    if score == 5:
        strength = "STRONG"
    elif score == 4:
        strength = "MEDIUM"
    elif score >= 2:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"
        
    # 5. Build visual report
    analysis = "\nPassword Analysis:\n"
    
    # Convert true/false to visible symbols safely
    if has_len: analysis += "[✓] Minimum 8 characters\n"
    else: analysis += "[✗] Minimum 8 characters\n"
    
    if has_upper: analysis += "[✓] Uppercase letter\n"
    else: analysis += "[✗] Uppercase letter\n"
    
    if has_lower: analysis += "[✓] Lowercase letter\n"
    else: analysis += "[✗] Lowercase letter\n"
    
    if has_num: analysis += "[✓] Contains a number\n"
    else: analysis += "[✗] Contains a number\n"
    
    if has_special: analysis += "[✓] Special character\n"
    else: analysis += "[✗] Special character\n"
    
    analysis += f"\nPassword Strength: {strength}"
    return analysis

def main():
    while True:
        print("\n===== PASSWORD SECURITY CHECKER =====")
        user_password = input("Enter your password: ")
        
        # Rejection Guards
        if ' ' in user_password:
            print("Password should not contain spaces!")
            continue
            
        if user_password.isdigit():
            print("Password cannot contain only numbers!")
            continue
            
        # Get report and print it
        result_display = check_password_strength(user_password)
        print(result_display)
        
        # Menu Options
        print("\n1. Check Another Password\n2. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "2":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
