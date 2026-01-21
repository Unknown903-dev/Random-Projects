def replace_string_in_file(file_path, old_string, new_string):
    try:
        # Open and read file
        with open(file_path, 'r') as file:
            content = file.read()

        # does old exist
        if old_string in content:
            print(f"'{old_string}' found in the file Replacing with '{new_string}'")
            # Replace old with new string
            updated_content = content.replace(old_string, new_string)

            # update file
            with open(file_path, 'w') as file:
                file.write(updated_content)
            
            print("Replacement complete")
        else:
            print(f"'{old_string}' not found in the file No changes made")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'file'  
old_string = 'o ld'   
new_string = 'new'    

replace_string_in_file(file_path, old_string, new_string)