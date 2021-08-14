#bin/bash

pyenv install 3.9.6
pyenv local 3.9.6
pyenv rehash
pyenv init
python -m pip install -r requirements.txt
export BOT="TOKEN"