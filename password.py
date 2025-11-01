import random
import string


def generate_passwords():
    print("Give Your Desired Input")
      
    # 1. Take initial user inputs once
    userinput1 = input(" -> Enter a favorite word: ")
    userinput2 = input(" -> Enter a place/country name: ")
    
    specific_char = input(" -> Enter one specific special character: ")
    
    try:
        specific_number = input(" -> Enter a specific number: ")
        # Ensure the number is treated as a string for inclusion in the password
        if not specific_number.isdigit():
             raise ValueError("Input was not a valid number.")
    except ValueError as e:
        print(f"\n❌ Invalid input for specific number: {e}. Please run the script again with a valid number.")
        return
        
    try:
        count = int(input(" -> How many passwords do you want to generate? "))
    except ValueError:
        print("\n❌ Invalid number entered for password count. Please run the script again with a valid number.")
        return

    # *** MODIFICATION START: Increased Special Characters ***
    # Now includes most common symbols for greater randomization
    special_chars = r"""!@#$%^&*()-_+=[]{}|;:'",.<>/?`~""" 
    # *** MODIFICATION END ***
    
    print("\n" + "=" * 55)
    print("Your generated passwords:")

    # 2. Loop to generate the requested number of passwords
    for i in range(1, count + 1):
        # A. Random components for this iteration
        rand_number = str(random.randint(1, 999)) # Convert to string for joining
        
        # B. Structured Password components (using user input, easier to remember)
        # Create a list of the primary components, applying desired casing/formats
        structured_components = [userinput1.title(),specific_char,specific_number,rand_number,userinput2.upper()]
        
        # *** NEW: Shuffle the order of the components ***
        random.shuffle(structured_components)
        
        # Join the shuffled components
        randomized_structured_password = "".join(structured_components)
        
    
    
        
        print(f"\n--- Password Set {i} ---")
        
        # Option 1: The NEW randomized structured password
        print(f"1. Randomized Structured: *{randomized_structured_password}* (Good balance of security/memorability)")
        
        # Option 2: A hybrid password, containing user parts but fully shuffled and lengthened
        # Create a list of all characters from the randomized structured password
        combined_list = list(randomized_structured_password)
        
        # Shuffle all individual characters for a secure hybrid
        random.shuffle(combined_list)
        hybrid_password = "".join(combined_list)
        
        print(f"2. Fully Shuffled Hybrid: *{hybrid_password}* (Highest security)")

    print("\n" + "=" * 55)

# Run the generator
if __name__ == "__main__":
    generate_passwords()