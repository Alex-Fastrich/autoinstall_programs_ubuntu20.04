#! /bin/python3
from subprocess import run, PIPE
from re import sub


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


def install(path_user):
    logs = []

    order_1 = run(
        'apt install neovim -y',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_1_stderr = sub(r'\n', '. ', order_1.stderr)
    result_order_1 = ('OK', order_1_stderr)[bool(order_1.returncode)]
    logs.append(f'NEOVIM\n- Установка - {result_order_1}\n')

    order_2 = run(
        f'mkdir {path_user}/.config/nvim',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_2_stderr = sub(r'\n', '. ', order_2.stderr)
    result_order_2 = ('OK', order_2_stderr)[bool(order_2.returncode)]
    logs.append(f'- Создаю директории для конфига - {result_order_2}\n')

    link_init_vim = 'https://www.dropbox.com/s/m9psbp3pvcm09o4/init.vim?dl=0'
    order_3 = run(
        f'wget -O {path_user}/.config/nvim/init.vim {link_init_vim}',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_3_stderr = sub(r'\n', '. ', order_3.stderr)
    result_order_3 = ('OK', order_3_stderr)[bool(order_3.returncode)]
    logs.append(f'- Скачиваю конфиг neovim в директорию - {result_order_3}\n')

    link_plug_vim = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    order_4 = run(
        f'wget -O /usr/share/nvim/runtime/autoload/plug.vim {link_plug_vim}',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_4_stderr = sub(r'\n', '. ', order_4.stderr)
    result_order_4 = ('OK', order_4_stderr)[bool(order_4.returncode)]
    logs.append(f'- Скачиваю vim-plug - {result_order_4}\n')

    link_colorscheme = 'https://www.dropbox.com/s/ttgi0g0jqt4mxzk/materialbox.vim?dl=0'
    order_5 = run(
        f'wget -O /usr/share/nvim/runtime/colors/materialbox.vim {link_colorscheme}',
        shell=True,
        stderr=PIPE,
        encoding='utf-8',
        )
    order_5_stderr = sub(r'\n', '. ', order_5.stderr)
    result_order_5 = ('OK', order_5_stderr)[bool(order_5.returncode)]
    logs.append(f'- Скачиваю тему для neovim - {result_order_5}\n')
    return logs
