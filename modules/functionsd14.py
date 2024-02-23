FILEPATH = "todos.txt"
def get_todos(filepath = FILEPATH):
    """Read a text file and return a list of to do items.""" # doc strings, show up if help(get_todos) executed
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):   # order: non-default and default argument
    """Write a list of to do items into a text file."""
    with open(filepath, "w") as file_loc:
        file_loc.writelines(todos_arg)

if __name__ == "__main__":
    # Execute this code only if the script is run directly, not when imported
    # This block is often used for testing or script-specific initialization
    print("This script is being run directly")
