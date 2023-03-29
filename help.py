import os
import subprocess

def help():
    print(functions)

# Performs git add and commit, with option to also push to GitHub
def commit():
    message = 'git commit'

    # prompt for commit message, with each input creating a new line
    while True:
        msg = input("Commit message: ")
        if msg == 'x':
            break
        if msg == 'h':
            help.help()
        message += ' -m "' + msg + '"'

    os.system("git add .")
    os.system(message)
    # Option to push repo to GitHub
    push = input("Push(y/n)? ")
    if push == 'y':
        os.system('git push')
    os.system('git status')

def newBranch():
    sysMsgs = ['git checkout -b ', 'git push origin ', 'git push --set-upstream origin ']
    msg = input("What would you like to name your new branch? ")
    if msg == 'x':
        return
    for sysmsg in sysMsgs:
        cmd = sysmsg + msg
        os.system(cmd)
    os.system("git branch")

def mergeBranch():
    branches = gitBranches()
    cwb, branchlist = branches
    while True:
        prompt = f"Which branch would you like to merge '{cwb}' into?"
        print(prompt)
        ind = 0
        for branch in branchlist:
            print(str(ind) + ": " + branch)
            ind += 1
        msg = int(input("> "))
        prompt = f"Merge '{cwb}' into '{branchlist[msg]}'(y/n)? "
        confirm = input(prompt)
        if confirm == 'n':
            continue
        if confirm == 'x':
            break
        sysmsg = f"git checkout '{branchlist[msg]}'"
        os.system(sysmsg)
        sysmsg = f"git merge {cwb}"
        os.system(sysmsg)
        deleteBranch(cwb)
        sysmsg = f"git checkout {cwb}"
        break

def gitBranches():
    gitbranch = subprocess.run(['git', 'branch'], capture_output=True, text=True)
    branches = gitbranch.stdout.strip().split('\n')
    cwb = ''
    brlst = []
    for branch in branches:
        if not branch.startswith('*'):
            brlst.append(branch.strip())
            continue
        cwb = branch.split()[1]
    return cwb, brlst

def deleteBranch(cwb):
        prompt = f"Would you like to delete '{cwb}'(y/n)? "
        delbranch = input(prompt)
        cmds = ['branch -d', 'push --delete origin']
        if delbranch == 'n':
            return
        if delbranch == 'y':
            for cmd in cmds:
                prompt = f"git {cmd} {cwb}"
                os.system(prompt)
        os.system("git branch")


# Quits program at git_commands prompt
def endProgram():
    while True:
        break

functions = {
    's': 'Shortcuts',
    'h': help,
    'c': commit,
    'nb': newBranch,
    'mb': mergeBranch,
    'x': endProgram,
    'b': gitBranches,
}