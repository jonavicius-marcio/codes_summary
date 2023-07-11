Airflow - Resumo
=============


# Menu
1. [Instalação automatica](#Instalação)
2. [Instalação manual](#Instalação_manual)
3. [configuração ](#configuração )
4. [task](#task)
5. [Dag](#Dag)
6. [Control](#Control)
6. [Operators](#Operators)
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


# Instalar em um ambiente virtual   

Comandos Utilizados:

criar ambiente 
```
python3 -m venv .env
source .env/bin/activate
```

criar variavel de ambiente 
```
export AIRFLOW_HOME=$(pwd)/airflow
```

instalar 
```
AIRFLOW_VERSION=2.2.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apa...{AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Criar user 

```
airflow users create     --username admin     --firstname name     --lastname lastname     --role Admin     --email email

```
iniciar o airflow
```
airflow db init

airflow scheduler -D

airflow webserver
```
https://airflow.apache.org/docs/apache-airflow/2.2.0/installation/installing-from-pypi.html


mostrar todas as instancias
```
top
```

Matar instancia 
```
sudo kill -9 <list of pids>
```


# configuração  
as configurações ficam em  airflow.cfg. Abra a pasta com 
```
    nano  airflow.cfg
```
crtl + x fechar

para de mostrar os exemplos (mudar no airflow.cfg )
load_examples = False




Control Flow
Formas de controlar a execução de tarefas.
● Branching:  Determina qual tarefa mover a partir de uma condição.
● Latest Only : Só é executada em DAGs em execução no presente.
● Depends on Past: Tarefas podem depender de si mesmas de umavexecução anterior.
● Trigger Rules:  Permite definir as condições para um DAG executar
uma tarefa.

# task 
rodar uma task pelo terminal 
```
    airflow tasks nomeDag nomeTask
```

Estados de cada tarefa.
● none: a tarefa ainda não foi enfileirada para execução (suas dependências ainda não foram atendidas).
● scheduled: O agendador determinou que as dependências da Tarefa são atendidas e deve ser executado.
● queued: A tarefa foi atribuída a um executor e está aguardando um trabalhador.
● running: a tarefa está sendo executada em um trabalhador (ou em um executor local / síncrono).
● success: a tarefa terminou em execução sem erro.
● failed: a tarefa teve um erro durante a execução e falhou ao executar.
● skipped: a tarefa foi ignorada devido a ramificação, LatestOnly ou semelhante.
● upstream_failed: uma tarefa upstream falhou e a regra de acionamento diz que precisávamos dela.
● up_for_retry: A tarefa falhou, mas ainda restam novas tentativas e será reprogramada.
● up_for_reschedule: A tarefa é um Sensor que está em modo de reprogramação.
● sensing: a tarefa é um sensor inteligente
● removed: a tarefa desapareceu do DAG desde o início da execução.


# Xcom 
com SQLite pode compartilhar 2gb, com postgres 1gb, mysql 64kb


# Dag
DAG (Directed Acyclic Graphs) -


Using CRON expressions to schedule a DAG

One way to configure your DAG for a basic schedule is by defining its schedule argument using either a cron expression or selecting one of the available cron "presets".

**None** : Don’t schedule, use for exclusively “externally triggered” DAGs
@once : Schedule once and only once
@hourly : Run once an hour at the end of the hour
@daily : Run once a day at midnight (24:00)
@weekly : Run once a week at midnight (24:00) on Sunday
@monthly :Run once a month at midnight (24:00) of the first day of the month
@quarterly : Run once a quarter at midnight (24:00) on the first day
@yearly : Run once a year at midnight (24:00) of January 1


https://crontab.guru/ 

**catchup**

By default, Airflow will run any past scheduled intervals that have not been run. In order to avoid catchup, we need to explicitly pass the parameter catchup=False in the DAG definition.

**Backfill**
If for some reason we want to re-run DAGs on certain schedules manually we can use the following CLI command to do so.

```
airflow backfill -s <START_DATE> -e <END_DATE> --rerun_failed_tasks -B <DAG_NAME>
```

**Scheduler **
O Scheduler (agendador) é responsável por assegurar que as tasks dentro de um DAG sejam executadas no momento adequado. Em outras palavras, o scheduler é um processo que cuida do agendamento dos fluxos de trabalho e faz o envio das tasks para o executor, seguindo as etapas:

Faz a leitura dos arquivos DAG criado pelo usuário, extrai as informações e as coloca no banco de dados;
Determina quais tarefas serão executadas e as coloca no estado enfileirado para executar na ordem correta; e
Busca e executa as tarefas que estão no estado enfileirado.


# Control

**Control Flow** 

As dependências entre tasks podem ser definadas por: 

● extracao >> [transformacao, carga]
● carga << notificacao

Ou

● extracao.set_downstream([transformacao, carga])
● carga.set_upstream(notificacao)

**Edges Labels** 
Podemos definir labels para documentar as relações e dependências entre tarefas.

get_acuracy_op >> check_acuracy_op >> Label("Limit 90%") >> [deploy_op, retrain_op] >> notify_op
● get_acuracy_op.set_downstream(check_acuracy, Label("Métrica ACC"))


**Trigger Rules**

Nos permite controlar o comportamento de acionamento das tarefas.
● all_success (padrão): Todas as tarefas anteriores foram bem-sucedidas.
● all_failed: Todas as tarefas anteriores estão em um estado de falha ou upstream_failed.
● all_done: todas as tarefas upstream são feitas com sua execução.
● one_failed: pelo menos uma tarefa anterior falhou (não espera que todas as tarefas anteriores já
tenham executado).
● one_success: pelo menos uma tarefa anterior foi bem-sucedida (não espera que todas as tarefas
anteriores tenham executado).
● none_failed: Todas as tarefas anteriores não falharam ou upstream_failed - ou seja, todas as tarefas
anteriores foram bem-sucedidas ou foram ignoradas.
● none_failed_or_skipped: Todas as tarefas anteriores não falharam ou upstream_failed, e pelo menos
uma tarefa anterior foi bem-sucedida.
● none_skipped: nenhuma tarefa anterior está em um estado ignorado - ou seja, todas as tarefas
anteriores estão em um estado de sucesso, falha ou upstream_failed.
● dummy: sem dependências, execute esta tarefa a qualquer momento.

# Operators
Operator é o componente que determina qual ferramenta será utilizada para executar as tasks

**Branch Operator** : is used where you need to decide between multiple tasks to execute based on the results of an upstream task.
**BashOperator** - executa um comando bash.
**PythonOperator** - chama uma função Python.
**EmailOperator** - envia um e-mail.
**SimpleHttpOperator** - envia uma requisição http.
**SqliteOperator** - operador para trabalhar com sqlite.

# Templates


![image](files/Users/jzhang/Desktop/Isolated.png)


https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html

# Executores 

# Papermill

https://papermill.readthedocs.io/en/latest/installation.html 


**Vantagens**
● Alternativa mais rápida e simples.
● Ideal para etapas de prototipação.
● Desenvolvimento simples.
● Sem aumentar a curva de aprendizado.

**Desvantagens**
● Difícil manutenção e controle de erros.
● Todo o processo é atômico. Difícil dividir as operações.
● Todo o processamento é feito no nível do Kernel.

links uteis: 

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



