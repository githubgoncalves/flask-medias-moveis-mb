# Médias Móveis Simples

O objetivo do projeto é entregar variações de médias móveis simples,
de 20, 50 e 200 dias, das moedas Bitcoin e Etherium que são listadas no
Mercado Bitcoin via api Rest.

# Sobre o Desevolvimento e Execução do Projeto

As APIs REST são construídas usando o framework Flask e Bancos de Dados SqlLite.
Arquitetura Clean Code baseada em (https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
Pré-commits como Git Hooks - são um mecanismo do sistema de controle de versão git. Eles permitem que você execute o código antes do commit.

### Requisitos iniciais 

- Instalar Docker

Clone o projeto usando o comando:
```bash
git clone https://github.com/githubgoncalves/variacoes-medias-moveis-simples
```

### Como iniciar a API usando Docker

Vá para o diretório do projeto:
```bash
cd variacoes-medias-moveis-simples\api
```
Execute o aplicativo com o seguinte comando para executar o container docker:
```bash

docker build -t api-flask-medias-moveis-mb . 

docker run -p 8003:8003 api-flask-medias-moveis-mb

```

**Contato com [DANIEL GONÇALVES](danielgoncalves.info@gmail.com)!**