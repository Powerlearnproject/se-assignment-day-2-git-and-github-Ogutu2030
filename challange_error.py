def modify_file_content(content):
    """
    This function modifies the content of the file.
    You can implement any transformation logic here.
    For this example, it converts text to uppercase.
    """
    return content.upper()

def read_and_write_file():
    # Ask the user for the input file name
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Ask for the output file name
        output_filename = input("Enter the name of the file to write the modified content to: ")
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Success! The modified content has been written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: Could not read from or write to the file. Please check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
