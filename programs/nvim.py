#! /bin/python3.11
from subprocess import run, PIPE
from re import sub


orders = {
    'NEOVIM\n- Установка -': 'apt install neovim -y',
    '- Создаю директории для конфига -': 'mkdir way_user/.config/nvim',
    '- Скачиваю конфиг neovim в директорию -': 'wget -O way_user/.config/nvim/init.vim https://www.dropbox.com/s/m9psbp3pvcm09o4/init.vim?dl=0',
    '- Скачиваю vim-plug -': 'wget -O /usr/share/nvim/runtime/autoload/plug.vim https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim',
    '- Скачиваю тему для neovim -': 'wget -O /usr/share/nvim/runtime/colors/materialbox.vim https://www.dropbox.com/s/ttgi0g0jqt4mxzk/materialbox.vim?dl=0',
    }

def ppa():
    order_ppa = run(
        'add-apt-repository ppa:neovim-ppa/unstable -y',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_ppa_stderr = sub(r'\n', '. ', order_ppa.stderr)
    result_order_ppa = ('OK', order_ppa_stderr)[bool(order_ppa.returncode)]
    return f'- Добавляю репозиторий NEOVIM - {result_order_ppa}\n'


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

