AWS - Resumo
=============


# Menu
1. [configuração](#Configuração)
2. [SSH](#SSH)
3. [EC2](#EC2)

# Configuração

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



