import sys
import os

builtin_commands = ["echo","exit","type"]

def main():

    PATH = os.environ.get("PATH")

    while True:
        sys.stdout.write("$ ")
        
        # Wait for user input
        command = input()
        
        if command == "exit 0":
            break
        
        user_stdin = command.split(" ")
        main_command = user_stdin[0]

        if PATH:
            all_paths = PATH.split(":")

        if main_command in builtin_commands:
            
            if main_command == "echo":
                print(" ".join(user_stdin[1:]))
            
            elif main_command == "type":
                type_command = user_stdin[1]
                found = False

                if type_command in builtin_commands:
                    print(f"{type_command} is a shell builtin")
                    found = True

                elif PATH:
                    for path in all_paths:
                        search_path = f"{path}/{type_command}"
                        if os.path.isfile(search_path):
                            print(f"{type_command}: is {search_path}")
                            found = True
                            break
                        else:
                            continue
                if not found:
                    print(f"{user_stdin[1]} not found")
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
