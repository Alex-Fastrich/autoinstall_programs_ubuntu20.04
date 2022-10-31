#! /bin/python3
from subprocess import run, PIPE
from programs import nvim, git

user = '/home/fastrich'
programs_install = (
    nvim,
    git,
    )

with open('logs.txt', 'w') as logs:
    logs.write('PPA\n')
for program in programs_install:
    with open('logs.txt', 'a') as logs:
        logs.write(program.ppa())

run('apt update', shell=True)

for program in programs_install:
    with open('logs.txt', 'a') as logs:
        logs.write('\n')
        logs.writelines(program.install(user))
