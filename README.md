# Consumindo API do GitHub

## Configuração do projeto

### 1. Instalando `virtualenv`

Virtualenvs são uma forma de isolar diversos ambientes de desenvolvimento, assim permitindo ao programador utilizar versões específicas de diversos pacotes sem impactar instalações de outras aplicações ou sistemas.

1. Abra seu Prompt de comando e digite:

> ```py
> pip install virtualenv
> ```

2. Dentro do seu projeto, crie uma virtualenv:

   > ```py
   > python -m venv <nome da venv>
   > ```

3. Ativar a venv criada:

> ```py
> .\<nome da venv>\Scripts\activate
> ```

Após pressionar o **Enter**, irá aparecer nesse formato:

> ```assembly
> (nome da venv) C:\User\...\Desktop\(nome do seu projeto)
> ```

### 2. Instalação das bibliotecas

* Instalação requests:

> ```py
> pip install requests
> ```

* Instalação da biblioteca Pandas 

  Execute esse comando pelo `cmd` como administrador

  > ```py
  > pip install Pandas
  > ```


## Sites utilizados

1. [DOCUMENTAÇÃO DAS EXCEÇÕES](https://requests.readthedocs.io/en/latest/user/quickstart/#response-status-codes)
1. [API REST - GITHUB](https://developer.github.com/v3/)
1. []()