#! /bin/python3.11
from subprocess import run, PIPE
from re import sub
import config as c


def find_way(line):
    '''Подставляет путь по ключу, если он нужен'''

    if '@user' in line:
        return sub('@user', c.user, line)
    return line


def execute(orders):
    '''Возвращает описание и результат(OK или stderr) команд'''

    logs = []
    for order in orders:
        command = find_way(order[1])
        exe_com = run(
            command,
            shell=True,
            stderr=PIPE,
            encoding='utf-8',
        )
        com_err = sub(r'\n', '. ', exe_com.stderr)
        result_com = ('OK', com_err)[bool(exe_com.returncode)]
        logs.append(f'{order[0]} {result_com}\n')
    return logs