AWS - Resumo
=============


# Menu
1. [configuração](#Configuração)
2. [SSH](#SSH)
3. [EC2](#EC2)

# Configuração CLI

Windowns baixe o excutável no link: 

```
   https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

   aws --version

```

Confinguração

Passe a senha acesso para conexão
```
    aws configure
```

tipos de format:  table, text, json 

Caso tenho esquecido as credenciais pegue na pasta: 

```
    cat ~/-aws/config
    cat ~/-aws/credentials
```

# CLI 



## Help 

```
aws ec2 create-volume help
```

# SSH  

Entrar na maquina EC2. 

```
    SSH -i <arquivo.pem>  ec2-user@<public_ip_ec2>
```

**Note**:  Any timeout (not just for SSH) is related to security groups or a firewall. 


# EC2

## List : listar todas as instancias ec2

```
    aws ec2 describe-instances

```



## Create: 
cria uma instancia apartir da imagem ami-0323c3dd2da7fb37d (pegar no marketplace), count (quantidade de instancias)

```
aws ec2 run-instances --image-id "ami-0323c3dd2da7fb37d" --count 1 --instance-type "t2.micro" --key-name "MinhaChaveSSH" --security-group-ids "sg-0529062a5d07f7eab" --subnet-id "subnet-1deb2d3c"
```

##  Terminate
```
aws ec2 terminate-instances --instance-ids "id-xyz"
```

## Create AMI
Criar imagem 
```
aws ec2 create-image --instance-id i-0c6b1ca827198a44a --name "MinhaPrimeiraAMICLI" --description "AMI criada via AWS CLI" --no-reboot
```

## Create volume
```
aws ec2 create-volume --volume-type gp2 --size 80 --availability-zone us-east-1a
```
## Attach Volume
```
aws ec2 attach-volume --volume-id vol-0ad91b69b44c62007 --instance-id i-001c3531c5a4dc46b --device /dev/sdp
```






## Conexão S3 Django


https://django-storages.readthedocs.io/en/latest/index.html 

1 Criar bucket
2 criar user com credenciais CLI 
3 instalar pip install boto3 e pip install django-storages
4 pip freeze -> requirement.txt
5 python manage.py collectstatic copia todos os arquivos estaticos para o bucket


## GCP - VM


https://django-storages.readthedocs.io/en/latest/index.html 

1 Criar vm com permissão Http e https
2. Fixar IP (detalhes de rede)
3. gerar ssh-keygen
4. atualizar
sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y
sudo apt install python3.9 python3.9-venv python3.9-dev -y
sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git



## Instalando o PostgreSQL

```
# Nós fizemos isso acima
sudo apt install postgresql postgresql-contrib -y
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

### Configurações

```
sudo -u postgres psql
# Criando um super usuário
CREATE ROLE usuario WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'senha';

# Criando a base de dados
CREATE DATABASE basededados WITH OWNER usuario;

# Dando permissões
GRANT ALL PRIVILEGES ON DATABASE basededados TO usuario;

# Saindo
\q
sudo systemctl restart postgresql
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

## Configurando o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
```

