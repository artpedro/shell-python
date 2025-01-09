import sys
import os

HOME = "/home/artur"
builtin_commands = ["echo","exit","type","pwd","cd"]

def type_command(type_command, all_paths=None,quiet=True):

    found = False

    if type_command in builtin_commands:
        print(f"{type_command} is a shell builtin")
        found = True
        search_path = "shell builtin"

    if (not found) and all_paths:
        for path in all_paths:
            search_path = f"{path}/{type_command}"
            if os.path.isfile(search_path):
                if not quiet:
                    print(f"{type_command} is {search_path}")
                found = True
                break

    if not found:
        search_path = None

    return found, search_path

def get_current_dir(absolute=False):
    return os.getcwd()
    

def cd(path):
    if path.startswith("~"):
        path = path.replace("~", HOME)
    try:
        os.chdir(path)
    except:
        print(f"cd: {path}: No such file or directory")

def main():

    PATH = os.environ.get("PATH")

    while True:
        check_dir = get_current_dir(absolute=True)

        if (check_dir.lstrip("/home/") == ""):
            current_dir = get_current_dir(absolute=True)
        else:
            current_dir = get_current_dir(absolute=False)

        if PATH:
            all_paths = PATH.split(":")

        #sys.stdout.write(f"{current_dir}$ ")
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        
        # Force exit
        if command == "exit 0":
            break
        
        # Parse user input
        user_stdin = command.split(" ")
        main_command = user_stdin[0]

        # Handle builtin commands
        if main_command in builtin_commands:
            
            if main_command == "echo":
                print(" ".join(user_stdin[1:]))
            
            elif main_command == "type":
                if PATH:
                    found, search_path = type_command(user_stdin[1],all_paths,quiet=False)
                if not found:
                    print(f"{user_stdin[1]}: not found")
                
            elif main_command == "pwd":
                print(os.getcwd())

            elif main_command == "cd":
                cd(user_stdin[1])
        # Handle external commands
        elif PATH:
            found, search_path = type_command(main_command,all_paths)
            if found:
                os.system(command)
            else:
                print(f"{main_command}: command not found")


if __name__ == "__main__":
    main()
