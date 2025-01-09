import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    
    valid_commands = ["cd", "pwd", "echo", "exit"]
    # Wait for user input
    command = input()
    if command in valid_commands:
        print(command)
    else:
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
