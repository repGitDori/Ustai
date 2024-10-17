import datetime

# Function to prompt the user, assign priority, and save the result to a file
def get_priority_and_save():
    # Prompt for the user's name and the tool they're using
    user_name = input("Please enter your name: ").strip().replace(" ", "_")
    tool_name = input("Please enter the name of the tool you are using: ").strip().replace(" ", "_")
    
    print("\nWelcome! Let's figure out the priority of your issue.")
    print("Please select the category that best describes your issue:")
    print("1. Fixing bugs or improving core functionality")
    print("2. Improving user experience (making things easier to use)")
    print("3. Data security and privacy concerns")
    print("4. Integrating with other tools or devices")
    print("5. Adding new features or innovation")

    # Get user input for category
    choice = int(input("Enter the number that corresponds to the issue (1-5): "))

    # Ask for the description of the issue
    description = input("\nPlease describe the issue in a few sentences: ")

    # Determine the priority title based on user input
    if choice == 1:
        priority = "Highest Priority: Fixing Core Functionality"
        priority_number = "1"
    elif choice == 2:
        priority = "High Priority: Improving User Experience"
        priority_number = "2"
    elif choice == 3:
        priority = "Medium Priority: Data Security"
        priority_number = "3"
    elif choice == 4:
        priority = "Low-Medium Priority: Integration with Other Tools"
        priority_number = "4"
    elif choice == 5:
        priority = "Low Priority: Adding New Features"
        priority_number = "5"
    else:
        print("\nInvalid choice. Please select a number between 1 and 5.")
        return

    # Get the current date and time in YYYYMMDD_HHMM format
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M")

    # Create the dynamic filename using the date first, tool, user's name, and priority as a number
    filename = f"{current_time}_{tool_name}_{user_name}_priority_{priority_number}.txt"

    # Prepare the content for the file, including the title information
    title_info = f"Tool: {tool_name}\nUser: {user_name}\nDate: {current_time}\n"
    priority_info = f"{priority}\n"
    description_info = f"\n{description}\n"

    # Combine everything into the final content
    content = f"{title_info}\n{priority_info}{description_info}"

    # Save the content to the text file
    with open(filename, "w") as file:
        file.write(content)

    print(f"\nThe priority and description have been saved to {filename}")

# Run the function to prompt the user and save the result
get_priority_and_save()
