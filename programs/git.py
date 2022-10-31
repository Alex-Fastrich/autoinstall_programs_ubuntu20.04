#! /bin/python3.11
from subprocess import run, PIPE
from re import sub


orders = {
    'GIT\n- Установка -': 'apt install git',
    }

def ppa():
    order_ppa = run(
        'add-apt-repository ppa:git-core/ppa',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_ppa_stderr = sub(r'\n', '. ', order_ppa.stderr)
    result_order_ppa = ('OK', order_ppa_stderr)[bool(order_ppa.returncode)]
    return f'- Добавляю репозиторий GIT - {result_order_ppa}\n'


def install(way_user):
    logs = []
    for order in orders.items():
        command = order[1]
        if 'way_user' in command:
            command = sub(r'way_user', way_user, command)
        execute_command = run(
            command,
            shell=True,
            stderr=PIPE,
            encoding='utf-8',
            )
        command_stderr = sub(r'\n', '. ', execute_command.stderr)
        result_ecexute_command = ('OK', command_stderr)[bool(execute_command.returncode)]
        logs.append(f'{order[0]} {result_ecexute_command}\n')
    return logs

