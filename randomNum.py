import random
import os
import stat

# Generate a random number
number = random.randint(1, 10)

try:
    guess = int(input("Pick a number between 1 and 10: "))

    if guess == number:
        print("You are Lucky!")
    else:
        file_path = r"D:\Saikripa Sharma N2430013 CA"  # Use raw string for Windows paths
        
        if os.path.exists(file_path):
            # Remove read-only restriction
            os.chmod(file_path, stat.S_IWRITE)  
            os.read(file_path)
            print(f"File {file_path} has been deleted.")
        else:
            print(f"File {file_path} not found, cannot delete.")
except ValueError:
    print("Invalid input! Please enter a number.")
except PermissionError:
    print("Permission denied! Try running the script as Administrator.")
except Exception as e:
    print(f"An error occurred: {e}")
