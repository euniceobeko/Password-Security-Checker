def check_password_strength(password):
    special_chars = "@#$!"   
    has_len = len(password) >= 8
    has_upper = False
    has_lower = False
    has_num = False
    has_special = False
 
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_num = True
        if char in special_chars:
            has_special = True
            
    score = sum([has_len, has_upper, has_lower, has_num, has_special])

    if score == 5:
        strength = "STRONG"
    elif score == 4:
        strength = "MEDIUM"
    elif score >= 2:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"         
   
    return f"""
Password Analysis:
[{'✓' if has_len else '✗'}] Minimum 8 characters
[{'✓' if has_upper else '✗'}] Uppercase letter
[{'✓' if has_lower else '✗'}] Lowercase letter
[{'✓' if has_num else '✗'}] Contains a number
[{'✓' if has_special else '✗'}] Special character

Password Strength: {strength}"""

def main():
    while True:
        print("\n===== PASSWORD SECURITY CHECKER =====")
        user_password = input("Enter your password: ")        
       
        if ' ' in user_password:
            print("Password should not contain spaces!")
            continue
            
        if user_password.isdigit():
            print("Password cannot contain only numbers!")
            continue            
      
        result_display = check_password_strength(user_password)
        print(result_display)        
        
        print("\n1. Check Another Password\n2. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "2":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
