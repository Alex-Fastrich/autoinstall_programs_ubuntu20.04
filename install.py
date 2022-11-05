#! /bin/python3.11
from subprocess import run, PIPE
from config import programs_install
from gears import execute


def exe_prog(programs):
    '''Передает список с программами функции execute и
    записывает ее вывод в logs файл'''

    with open('logs.txt', 'w') as logs:
        logs.write('PPA INSTALL\n\n')
        for program in programs:
            if program.ppa:
                logs.writelines(execute(program.ppa))
        logs.write('\n\n')

    run('apt update', shell=True)

    with open('logs.txt', 'a') as logs:
        logs.write('PROGRAMS INSTALL\n\n')
        for program in programs:
            logs.writelines(execute(program.orders))


exe_prog(programs_install)