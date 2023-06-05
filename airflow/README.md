Airflow - Resumo
=============


# Menu
1. [Instalação automatica](#Instalação)
2. [Instalação manual](#Instalação_manual)
3. [configuração ](#configuração )
4. [task](#task)
5. [Dag](#Dag)
6. [Decorators](#Decorators)
7. [Executores](#Executores)
8. [Paralelismo ](#Paralelismo)


## Instalação automatica

instal 
```
    pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"

```

 crie uma variavel de ambiente para informar onde a pasta das dags ficarão. Crie a pasta dags
```
    export AIRFLOW_HOME=~/study/airflow/alura
```

Esse comando já faz tudo de forma mais automática, ou seja, inicia o banco de dados padrão do airflow, cria um novo usuário e inicia os serviços principais (o webserver e o scheduler).
o user é admin e a senha fica na pasta standalone_admin_password.txt
```
    airflow standalone
```

## Instalação_manual

Instalação
```
    sudo bash
    apt install python3-pip
    pip install apache-airflow
```

Criar usuario
```
   airflow users create --username admin --firstname Marcio --lastname Rodrigues --role Admin --email seuemail@gmail.com
```

inicializar o banco de dados. 
```
    airflow db init
    cd ~/airflow/
    pwd
```

subir o scheduler. sem o scheduler o airflow não atualiza as New DAG

```
    airflow scheduler -D
```
subir o servidor 

```
    airflow webserver --port 8080 -D 
    user: admin, senha: padrao
```

Para as dags ficarem visiveis no Scheduler e Webserver, é precisor informar a dags_folder no arquivo airflow.cfg ou usar variavel de ambiente. Por default o caminho é $AIRFLOW_HOME/dags subfolder

setar a pasta onde ficarão as dags
```
    export AIRFLOW_HOME=$(pwd)

    echo $AIRFLOW_HOME 
```

listar as pastas no linux
```
   ls -lrth
```


# configuração  
as configurações ficam em  airflow.cfg. Abra a pasta com 
```
    nano  airflow.cfg
```

# task 
rodar uma task pelo terminal 
```
    airflow tasks nomeDag nomeTask
```

# Dag

# Decorators 

# Exwcutores 

# Paralelismo 




https://airflow.apache.org/docs/apache-airflow/stable/start.html
https://en.wikipedia.org/wiki/Cron#CRON_expression
https://airflow.apache.org/docs/apache-airflow/1.10.12/concepts.html#dags
https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html
https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html
https://airflow.apache.org/docs/apache-airflow/2.2.2/_modules/airflow/decorators/__init__.html
https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/macros.html
https://airflow.apache.org/docs/apache-airflow/2.3.2/executor/index.html

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html
https://airflow.apache.org/docs/apache-airflow/2.3.2/executor/index.html
https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html
https://docs.astronomer.io/learn/airflow-scaling-workers



