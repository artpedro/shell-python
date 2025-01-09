import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
    

        
        # Wait for user input
        command = input()
        valid_commands = ["cd", "pwd", "echo", "exit"]

        if command == "exit 0":
            break
        if command in valid_commands:
            print(command)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
