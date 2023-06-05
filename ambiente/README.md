GIT - Resumo
=============


# Menu
1. [Ambiente](#Ambiente)
2. [freeze](#freeze)



## Ambiente

create
```
    python -m venv nome_ambiente
```

 activate windowns
```
    para powershel: .\env\Scripts\Activate.ps1
    para cmd .\env\Scripts\activate.bat 
```
no powershell precisa liberar primeiro acesso. Rode o codigo abaixo como adim
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

deactivate
```
    deactivate
```

deactivate
```
    deactivate
```

create and a activate Linux
```
    python3.9 -m venv venv
    source venv/bin/activate
```

## freeze

freeze
```
    pip freeze > requirements.txt
```

install 
```
   pip install -r requirements.txt 
```
