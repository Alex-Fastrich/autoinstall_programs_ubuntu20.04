#! /bin/python3
from subprocess import run
from typing import List, Tuple, Dict

from config import programs_install, user


def find_way(line: str) -> str:
    '''Подставляет путь по ключу, если он нужен'''
    if '@user' in line:
        return line.replace('@user', user)
    return line


def execute(orders: Dict[str, str]) -> List[str]:
    '''Возвращает описание и результат(True|False) команд'''
    logs = []
    for order in orders:
        command = find_way(orders[order])
        exe_com = run(
            command,
            shell=True,
            encoding='utf-8',
        )
        result_com = bool(exe_com.returncode)
        comment = f'Попробуйте ввести команду в ручную: {command}\n'
        if result_com:
            logs.append(f'{order} {not(result_com)}\n{comment}')
        else:
            logs.append(f'{order} {result_com}\n')
    return logs


def exe_prog(programs: tuple) -> None:

    '''Записывает результат исполнения команды в logs файл'''
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

