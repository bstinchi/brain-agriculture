# 🧠 Brain Agriculture — API de Gerenciamento de Fazendas

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-FF3366)
![PostgreSQL](https://img.shields.io/badge/Postgres-DB-316192)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Tests](https://img.shields.io/badge/Tests-Pytest-000000)

### Trabalho em progresso: devido ao pouco tempo não consegui finalizar todas as funcionalidades e realizar os testes que gostaria, caso haja a possibilidade de um prazo mais extenso gostaria de finalizar o projeto.  

## 🎯 Sobre o Projeto

Este projeto é uma API RESTful completa desenvolvida em Python para um teste técnico de alto nível. Seu objetivo é gerenciar produtores rurais, suas fazendas e as culturas plantadas, fornecendo também dados de agregação para um Dashboard.
O foco principal do desenvolvimento foi a **qualidade de código**, a **arquitetura moderna** e a **manutenibilidade**

### Stack Tecnológica Principal

| Categoria | Tecnologia |
| :--- | :--- |
| **Linguagem** | Python 3.11+ |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **ORM** | [SQLModel](https://sqlmodel.tiangolo.com/) (Integração Pydantic + SQLAlchemy) |
| **Banco de Dados** | PostgreSQL 15 |
| **Orquestração** | Docker e Docker Compose |
| **Testes** | Pytest, httpx e pytest-asyncio |

### Princípios Arquiteturais Aplicados

| Princípio | Implementação |
| :--- | :--- |
| **SOLID/SRP** | Separação de responsabilidades em módulos dedicados (`crud.py`, `models.py`, `schemas.py`). |
| **KISS** | Manutenção da simplicidade e clareza. Ausência de *patterns* complexos desnecessários. |
| **Clean Code** | Nomes de classes e métodos expressivos, validações de dados centralizadas. |
| **Concorrência** | Uso de conexões assíncronas com `asyncpg` e `SQLModel` para alta performance. |

---

## 🚀 Instalação e Execução

### Pré-requisitos

* Docker e Docker Compose instalados.

### Passos

1.  **Clone o Repositório:**
    ```bash
    git clone [https://www.dio.me/articles/enviando-seu-projeto-para-o-github](https://www.dio.me/articles/enviando-seu-projeto-para-o-github)
    cd brain-agriculture
    ```

2.  **Configurar Variáveis de Ambiente:**
    Copie o arquivo de exemplo para criar o arquivo local de configuração (`.env`).
    ```bash
    cp .env.example .env
    ```
    *Dica: Você pode editar o arquivo `.env` para alterar as credenciais do PostgreSQL, mas ele será ignorado pelo Git.*

3.  **Subir os Containers:**
    O `docker-compose` irá construir a imagem da API e iniciar os serviços `web` (FastAPI) e `db` (Postgres).
    ```bash
    docker-compose up --build
    ```

### Acesso à Documentação e API

* **API Principal:** `http://localhost:8000`
* **Documentação Interativa (Swagger UI):** `http://localhost:8000/docs`
* **Documentação Redoc:** `http://localhost:8000/redoc`

---

## 🧪 Testes

Os testes são executados de forma isolada dentro do container da aplicação.

1.  **Acesse o Terminal do Container Web:**
    ```bash
    docker exec -it brain-agriculture-web-1 /bin/bash
    ```
2.  **Execute a Suíte de Testes:**
    ```bash
    pytest
    ```

---

## 📈 Próximos Passos e Otimizações

As seguintes melhorias estão prontas para serem implementadas em um cenário de produção:

1.  **Migrations (Alembic):** Adicionar gerenciamento de migrations para controle de esquema de banco de dados em produção.
2.  **Validação Robusta:** Implementar validação completa de CPF/CNPJ (Módulo 11) com bibliotecas como `validate-docbr`.
3.  **Segurança:** Implementar Autenticação e Autorização (ex: JWT) para proteger endpoints.
4.  **Paginação:** Adicionar paginação eficiente (`limit`/`offset`) em todos os endpoints de listagem.
