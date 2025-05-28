# TASK ; Write a code to read helloworld.txt and then write it back
# message : Hello world in French language
# Program title : read_write_file.py

def read_write_file():
    input_filename = 'helloworld.txt'
    output_filename = 'helloworld_copy.txt'

    try:
        # Read from the file
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Write the content back to a new file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Content successfully copied from '{input_filename}' to '{output_filename}'.")

    except FileNotFoundError:
        print(f"The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    read_write_file()
