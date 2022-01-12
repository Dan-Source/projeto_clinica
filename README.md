## Projeto de Clinica para Programação p/ Internet 2

No que consite este projeto:
- Administrar medicos e especialidade e agendas
- Criar uma agenda para disponibilizar as consultas
- Permitir o usuario escolher um consulta em dia e horario de acordo com agenda do medico.

## Configurando o ambiente para executar a aplicação web.
Faça o download deste repositorio:

```
$ git clone git@github.com:Dan-Source/projeto_clinica.git
```

Crie um maquina virtual e instale a bibliotecas disponiveis no 
arquivo requirementes.txt:

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd projeto_clinica
$ python3 -m venv venv
```
Depois voce deve ativa-lo com o seguinte comando:

```
$ source ./venv/bin/activate
```
Apos ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requirements.txt
```
Para poder ter o primeiro acesso e pode configurar o aplicação vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuario:
```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Para iniciar o servidor depois deste passo você deve:
```
(venv)$ ./manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)

