# Tasker

How to set an environment:

    #Unix/mac
    python3 -m venv env
    source tutorial-env/bin/activate
    pip install -r requirements.txt

    #Windows
    python -m venv env
    env/Scripts/activate.bat
    pip install -r requirements.txt

How to run it:

    #Unix
    export FLASK_APP="run.py"
    export FLASK_ENV="development"
    export FLASK_DEBUG=1
    flask run
    
    #Windows (Powershell)
    $env:FLASK_APP="run.py"
    $env:FLASK_ENV="development"
    $env:FLASK_DEBUG=1
    flask run

[Instalar la extensión linux para windows para solo tener que utilizar comandos unix](https://evdokimovm.github.io/windows/zsh/shell/syntax/highlighting/ohmyzsh/hyper/terminal/2017/02/24/how-to-install-zsh-and-oh-my-zsh-on-windows-10.html)
