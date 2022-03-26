# Médias Móveis Simples

O objetivo do projeto é entregar variações de médias móveis simples,
de 20, 50 e 200 dias, das moedas Bitcoin e Etherium que são listadas no
Mercado Bitcoin via api Rest.

# Sobre o Desevolvimento e Execução do Projeto

As APIs REST são construídas usando o framework Flask e Bancos de Dados SqlLite.
Arquitetura Clean Code baseada em (https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
Pré-commits como Git Hooks - são um mecanismo do sistema de controle de versão git. Eles permitem que você execute o código antes do commit.

### Principais dependências:
- [FLASK](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLALCHEMY](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)


### Compatibilidade:
- Python 3.8

### Requisitos iniciais 

- Instalar Docker

Clone o projeto usando o comando:
```bash
git clone https://github.com/githubgoncalves/variacoes-medias-moveis-simples
```

### Como iniciar a API usando Docker

Vá para o diretório do projeto:
```bash
cd flask-medias-moveis-mb\api
```
Execute o aplicativo com o seguinte comando para executar o container docker:
```bash

docker build -t api-flask-medias-moveis-mb . 

docker run -p 8003:8003 api-flask-medias-moveis-mb

```

### Sobre o projeto

O projeto está dividido em endpoints: **convert-date-to-timestamp**, **load-data-base** e **indicators**.

 - **convert-date-to-timestamp**: Endpoint de suporte para converter uma data em timestamp.
 - **load-data-base**: Endpoint para buscar os dados da api externa do mercado bitcoin 
   (https://mobile.mercadobitcoin.com.br/v4/BRLBTC/candle?from=1643751346&to=1647984946&precision=1d), e 
   calcular a media movel de 20, 50 e 200 periodos. 
 - **indicators**: buscar os dados das medias mveis calculadas.
 
### Documentação Swagger 

O Projeto utiliza a lib [flask_restx](https://flask-restx.readthedocs.io/en/latest/) 
para documentação das APIs com o Swagger.

O Swagger é um framework composto por diversas ferramentas que, independente da linguagem, 
auxilia a descrição, consumo e visualização de serviços de uma API REST. 

Swagger - http://localhost:8003/


### Testes

Para a criação de testes unitários o projeto utiliza o pytest.


**Contato com [DANIEL GONÇALVES](danielgoncalves.info@gmail.com)!**