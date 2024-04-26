import os


def write_to_file(filename, content):
    """
    Writes given content to a file. If the file does not exist, it creates a new one.
    """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Written to {filename}: {content}")


def read_from_file(filename):
    """
    Reads content from a file and returns it.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Read from {filename}: \n{content}")
            return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None


def append_to_file(filename, additional_content):
    """
    Appends additional content to the existing file content.
    """
    with open(filename, 'a') as file:
        file.write(additional_content)
    print(f"Appended to {filename}: {additional_content}")


def delete_file(filename):
    """
    Deletes a file if it exists.
    """
    try:
        os.remove(filename)
        print(f"{filename} has been deleted.")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")


def file_exists(filename):
    """
    Checks if a file exists and returns True or False.
    """
    exists = os.path.exists(filename)
    print(f"Does {filename} exist? {exists}")
    return exists


def main():
    filename = "example.txt"
    initial_content = "Hello, world!\n"
    additional_content = "Here's some more text.\n"

    # Writing and reading from the file
    write_to_file(filename, initial_content)
    read_from_file(filename)

    # Appending to the file and reading it again
    append_to_file(filename, additional_content)
    read_from_file(filename)

    # Deleting the file and checking existence
    delete_file(filename)
    file_exists(filename)


if __name__ == "__main__":
    main()
