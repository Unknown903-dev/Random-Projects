def replace_string_in_file(file_path, old_string, new_string):
    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the old string exists
        if old_string in content:
            print(f"'{old_string}' found in the file. Replacing with '{new_string}'...")
            # Replace the old string with the new string
            updated_content = content.replace(old_string, new_string)

            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(updated_content)
            
            print("Replacement complete.")
        else:
            print(f"'{old_string}' not found in the file. No changes made.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'move_cursor.py'  # Replace with your file path
old_string = 'click_mouse'    # Replace with the string to search for
new_string = 'Click'    # Replace with the string to replace it with

replace_string_in_file(file_path, old_string, new_string)