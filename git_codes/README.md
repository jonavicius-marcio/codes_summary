GIT - Resumo
=============


# Menu
1. [Configuração](#Configuração)
2. [Servidor](#Servidor)
3. [Commit](#Commit)
4. [Status](#Status)
5. [Resturar](#Resturar)
6. [Branch](#Branch)
7. [Merge](#Merge)
8. [Stash](#Stash)
9. [Log](#Log)


## Configuração

Para a maquina toda 
```
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
```

Para um projeto especifico
```
    git config --local user.email "you@example.com"
    git config --local user.name "Your Name"
```
Verificar usuario e email
```
    git config user.name
    git config user.email
```

## Servidor

add server
```
    git remote add <name>  <new-URL>
```

Mostra endereço do servidor

```
    git remote -v
```
Remove server
```
    git remote remove origin
```
Servidor local:  vá até a pasta do servidor e digite 

```
    git init --bare, cria servidor repositório puro

    git remote add repository_name  diretorio (ex: git remote add local C:/Users/git-e-github/servidor)
```


# Commit
adcionar para commit 

```
    git add . 
```
comitar 
```
    git commit -m “mensagem” 
```

pegar alterações feitas por outras pessoas
```
    git pull
```

enviar para o servidor
```
    git push origin 
```
-u define que sempre que usarmos git push e estivermos na master, o envio será feito para origin

usado para enviar quaisquer commits feitos localmente na branch `master` para um repositório remoto em `origin`
```
    git push -u origin master
```

# Status
```
    git status
```

# Resturar

Resturar arquivos do repositorio. Vc quer pagar as modificações feita no arquivo fazendo um copia do arquivo 
do repositorio
```
    git restore file_name
```

Caso não tenha feito o commit ainda, utilize:
```
    git reset <arquivo-ou-diretório>
```

Caso já tenha realizado um commit, utilize:
```
    git rm --cached <arquivo>
    git rm -r --cached <diretório>
```

# Branchs 
https://git-school.github.io/visualizing-git/

mostra as branchs 
```
    git branch
```
criar uma branch 
```
    git branch titulo
```
trocar de branch 
```
    git chechout -b titulo
```
muda e cria branch
```
    git checkout -b titulo (-b cria a branch)
```

deletar branch (-d ou –delete)
```
    git branch –d
```
 O checkout, Este comando também é utilizado para dispensar mudanças de um arquivo;
 Alterando o branch podemos levar alterações que não foram commitadas junto, **tome cuidado!**


# Merge

fazer um merge da branch titulo com a main. 
```
    git checkout main
    git merge titulo
```
Juntar os arquivos sem perder a log dos commits 
```
    git rebase titulo
```

# Stash  
Após o comando o branch será resetado para a sua versão de acordo com o repositório. 
```
    git stash
```
lista
```
    git stash list
```

resgata o rascunho 
```
    git stash apply  <number>
```
mostrar a alteração de cada uma
``` 
    git stash show –p <number>
```

deletar rascunho
```
    git stash drop <nome>
```

deletar todos os rascunhos
```
    git stash clear
```


```
```



```
```