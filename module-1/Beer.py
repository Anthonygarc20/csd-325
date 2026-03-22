def bottle_countdown(num_bottles):
    """
    Manages the countdown and handles plural/singular logic.
    """
    while num_bottles > 1:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        
        # Check if the next number is singular or plural
        suffix = "bottle" if num_bottles == 1 else "bottles"
        print(f"Take one down and pass it around, {num_bottles} {suffix} of beer on the wall.\n")

    # Handle the final 1 bottle case
    if num_bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottles of beer on the wall.\n")

def main():
    try:
        # Ask user for input
        user_input = int(input("Enter number of bottles: "))
        
        # Call the countdown function
        bottle_countdown(user_input)
        
        # Final reminder in main program
        print("Time to buy more bottles of beer.")
        
    except ValueError:
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()
