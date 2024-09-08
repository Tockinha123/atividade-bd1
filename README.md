# 💻 Trabalho Prático de Banco de Dados - 2024.1

Este projeto faz parte do Trabalho Prático de Banco de Dados, onde desenvolvemos uma API Web utilizando **FastAPI** e **Poetry** para gerenciamento de usuários com operações básicas de **CRUD** (Create, Read, Update e Delete).

## 📝 Descrição do Projeto

A API desenvolvida realiza as seguintes operações:
- **POST**: Cria um novo usuário com as informações fornecidas.
- **GET**: Retorna os dados de um usuário, caso ele exista.
- **GET**: Retorna os dados de todos os usuários.

### 🧑‍💻 Estrutura do Usuário

A API lida com um objeto `Usuário` com a seguinte estrutura:
- `cpf`: inteiro 
- `nome`: string
- `data_nascimento`: data

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework web para construção de APIs rápidas e performáticas.
- **Poetry**: Ferramenta para gerenciamento de dependências e ambientes virtuais no Python.

## ⚙️ Instalação e Configuração do Ambiente

### 📋 Requisitos

- **Python 3.9+**
- **Poetry**

### 🛠️ Passos para Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
2. **Instale o poetry:**
    ```bash
    pip install poetry
    ```
    ou alternativamente, utilizando o pipx:
  
    ```bash
    pipx install poetry
    ```

3. **Instale as dependências com o Poetry:**
   ```bash
     poetry install
   ```
5. **Inicie o ambiente virtual:**
   ```bash
     poetry shell
   ```
7. **Inicie o servidor FastAPI:**
   Utilizando o taskpy, podemos iniciar o servidor digitando:
   ```bash
     task run
   ```
