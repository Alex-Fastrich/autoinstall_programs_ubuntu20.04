#! /bin/python3


ppa = {
    '- Добавляю репозиторий NEOVIM -': \
    'add-apt-repository ppa:neovim-ppa/unstable -y',
}

init = 'https://www.dropbox.com/s/m9psbp3pvcm09o4/init.vim?dl=0'
plug = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
colors = 'https://www.dropbox.com/s/ttgi0g0jqt4mxzk/materialbox.vim?dl=0'

orders = {
    '= Neovim =\n- Установка -': \
    'apt install neovim -y',

    '- Создаю директории для конфига -': \
    f'mkdir @user/.config/nvim',

    '- Скачиваю конфиг neovim в директорию -': \
    f'wget -O @user/.config/nvim/init.vim {init}',

    '- Скачиваю vim-plug -': \
    f'wget -O /usr/share/nvim/runtime/autoload/plug.vim {plug}',

    '- Скачиваю тему для neovim -': \
    f'wget -O /usr/share/nvim/runtime/colors/materialbox.vim {colors}',
}
