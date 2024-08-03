import random

# Function to generate a list of passwords with given lengths
def generate_passwords(pw_lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet for password generation
    passwords = []  # Initialize an empty list to store generated passwords

    for length in pw_lengths:
        password = "" 
        # Generate a password of the specified length
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        
        # Replace some characters with numbers and uppercase letters
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        
        passwords.append(password)  # Add the generated password to the list
    
    return passwords

# Function to replace some characters in the password with numbers
def replace_with_number(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    return password

# Function to replace some characters in the password with uppercase letters
def replace_with_uppercase_letter(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

# Main function to handle user interaction and generate passwords
def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    
    pw_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        if length < 3:
            length = 3
        pw_lengths.append(length)
    
    passwords = generate_passwords(pw_lengths)

    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i} = {password}")

# Entry point of the program
if __name__ == "__main__":
    main()
