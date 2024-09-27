class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self):
        # Get user input
        user_input = input("Enter text to write to the file: ")

        # Write the input to the file
        with open(self.filename, 'w') as file:
            file.write(user_input)
            print(f"Data written to {self.filename}")

    def read_from_file(self):
        try:
            # Read from the file
            with open(self.filename, 'r') as file:
                content = file.read()
                print("Content of the file:")
                print(content)

        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new file...")
            # If the file does not exist, create it and write input
            self.write_to_file()
            self.read_from_file()  # Call read again after writing

# Main function to execute the program
def main():
    filename = 'user_input.txt'  # Specify the file name
    file_handler = FileHandler(filename)  # Create a FileHandler object

    # First, try to read from the file
    file_handler.read_from_file()

# Call the main function
if __name__ == "__main__":
    main()
