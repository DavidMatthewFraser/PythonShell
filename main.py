"""
Python Shell Based on #https://danishpraka.sh/2018/09/27/shell-in-python.html
"""


import subprocess
import os

def execute(command):
    # execute commands and handle piping
    try:
        if "|" in command:
            # hold the original values of stdout and stdin to restore them later on
            standard_in = 0
            standard_out = 0
            standard_in = os.dup(0) # os.dup(0) => terminal input 
            standard_out = os.dup(1) # os.dup(1) => terminal output

            #first command takes commandut from stdin
            input_fd = os.dip(standard_in)

            # iterate over all commands that are piped
            for arg in command.split("|"):
                """
                Create a duplicate of stdin and 
                """
                os.dup2(input_fd, 0)
                os.close(input_fd)

                #restore stdout if this is the last command
                if cmd == command.split("|")[-1]:
                    input_fd = os.dup(s_out)
                else:
                    input_fd, output_fd = os.pipe()
                
                # redirect stdout to pipe
                os.dup2(output_fd, 1)
                os.close(output_fd)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("psh: command not found: {}".format(cmd.strip()))
            
            # restore stdout and stdin
            os.dup2(standard_in, 0)
            os.dup2(standard_out, 1)
            os.close(standard_in)
            os.close(standard_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("psh: command not found: {}".format(command))

# method to change directory
# otherwise cd is run in a subshell
def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory")

# get user input in a loop
def main():
    while True:
        # exit loop if user enters exit
        inp = input("$ ")
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            psh_cd(inp[3:])
        else:
            execute(inp)

if '__main__' == __name__:
    main()


