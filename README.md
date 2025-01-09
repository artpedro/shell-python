# Shell - Python Implementation

A custom shell environment written in Python. The `Shell` supports basic built-in commands and can execute external commands from the system `PATH`. This project serves as a lightweight shell environment, showcasing the fundamentals of shell programming and Python scripting.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Built-in Commands](#built-in-commands)
- [Directory Structure](#directory-structure)

## Introduction

The `Shell` is a custom Python-based shell environment designed to handle common built-in commands such as `echo`, `pwd`, `cd`, and more. Additionally, it allows execution of external commands available in the system's `PATH`.

The shell is lightweight, making it a great starting point for learning shell programming or extending functionality for specific use cases.

## Features

- **Built-in commands**: `echo`, `pwd`, `cd`, `type`, and `exit`.
- **Command Execution**: Supports running external commands from the system's `PATH`.
- **Error Handling**: Provides feedback for invalid commands or directories.
- **Cross-platform Compatibility**: Runs on any system with Python 3.x.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/artpedro/shell-python.git
   cd shell-python
   ```

## Usage

Run the shell locally using the provided script:

```bash
./your_program.sh
```

### Example Session

```bash
$ echo Hello, world!
Hello, world!
$ pwd
/home/user
$ cd /tmp
$ pwd
/tmp
$ exit 0
```

## Built-in Commands

| Command   | Description                                             |
|-----------|---------------------------------------------------------|
| `echo`    | Prints the input string to the terminal.                |
| `pwd`     | Displays the current working directory.                 |
| `cd`      | Changes the current directory.                          |
| `type`    | Checks if a command is a shell built-in or external.    |
| `exit 0`  | Exits the shell environment.                            |

## Directory Structure

```
artpedro-shell-python/
├── your_program.sh   # Shell script to run the program
└── app/
    └── main.py       # Python implementation of the shell
```
