#!/usr/bin/env bash

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init -)"

pyenv activate blog > /dev/null 2>&1

lessc theme/static/css/style.less theme/static/css/style.css

pelican-themes -r theme
pelican-themes -i theme

make clean
make html
