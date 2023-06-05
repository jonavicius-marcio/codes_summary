AWS - Resumo
=============


# Menu
1. [configuração](#Configuração)
2. [SSH](#SSH)

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

2. [SSH](#SSH)


Entrar na maquina EC2. 

```
    SSH -i <arquivo.pem>  ec2-user@<public_ip_ec2>
```

**Note**:  Any timeout (not just for SSH) is related to security groups or a firewall. 


