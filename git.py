# Script to simplify git with terminal prompts
import os
import help

def git_commands():
    while True:
        msg = input("What would you like to do? ")
        help.functions[msg]()
        break


git_commands()