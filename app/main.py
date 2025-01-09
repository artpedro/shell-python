import sys

builtin_commands = ["echo","exit","type"]

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        
        # Wait for user input
        command = input()
        
        if command == "exit 0":
            break
        
        user_stdin = command.split(" ")
        main_command = user_stdin[0]

        if main_command in builtin_commands:
            if main_command == "echo":
                print(" ".join(user_stdin[1:]))
            elif main_command == "type":
                if user_stdin[1] in builtin_commands:
                    print(f"{user_stdin[1]} is a shell builtin")
                else:
                    print(f"{user_stdin[1]}: command not found")
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
