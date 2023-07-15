# Sistema de Gerenciamento Financeiro

O Sistema de Gerenciamento Financeiro é uma aplicação que permite o gerenciamento de finanças pessoais, auxiliando os usuários no controle de despesas, receitas e orçamentos.Projeto realizo no evento PyWeek2023

## Recursos

- Registro de despesas e receitas como data, descrição e valor.
- Categorização das despesas e receitas para uma melhor organização.
- Visualização de um gráficos para análise financeira.
- Definição de metas e orçamentos para um planejamento financeiro mais efetivo.
- Notificações e lembretes para acompanhar o cumprimento das metas e orçamentos.

## Requisitos do Sistema

- Python 3.8 ou superior


## Configuração do Ambiente

1. Clone o repositório do Sistema de Gerenciamento Financeiro em sua máquina local:

```shell
git clone git@github.com:CaioMaxximus/pyweek_2023_django.git
```

2. Acesse o diretório do projeto:

```shell
cd sistema-gerenciamento-financeiro
```

3. Ative o ambiente virtual:

```shell

source venv/bin/activate  # para sistemas Unix-like (Linux, macOS)
venv/Scripts/Activate  # para sistemas Windows
```

4. Configure as variáveis de ambiente necessárias no arquivo `.env`. Verifique o arquivo `.env.example` para saber quais variáveis são necessárias e defina os valores apropriados.

5. Execute as migrações do banco de dados:

```shell
python manage.py migrate
python manager.py makemigrations
```

6. Inicie o servidor de desenvolvimento:

```shell
python manage.py runserver
```

7. Acesse o sistema em seu navegador através do endereço [http://localhost:8000](http://localhost:8000).

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema, tiver sugestões de melhorias ou desejar adicionar novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.
