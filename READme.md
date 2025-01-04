# Django Backend - Sistema de Avaliações e Comentários

Bem-vindo ao repositório do backend para o sistema de avaliações e comentários. Este projeto foi desenvolvido em Django e inclui funcionalidades completas para gerenciar usuários, professores, disciplinas, avaliações e comentários.

## **Recursos principais**

- **Autenticação JWT**: Permite login seguro e gerencia acessos.
- **CRUD Completo**:
  - Usuários
  - Professores
  - Disciplinas
  - Avaliações
  - Comentários
- **Permissões personalizadas**:
  - Criação, edição e exclusão de avaliações e comentários exigem autenticação.
  - Listagem pública de avaliações e comentários.
- **Relacionamentos**:
  - Usuários estão vinculados a avaliações e comentários.
  - Professores e disciplinas associados a avaliações.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes itens instalados:

- Python 3.9+
- Virtualenv
- Django 4+
- Banco de dados SQLite (ou outro de sua preferência, com configuração adequada)

---

## **Configuração do projeto**

### **1. Clone o repositório**

```bash
$ git clone https://github.com/seu-usuario/seu-repositorio.git
$ cd seu-repositorio
```

### **2. Crie e ative o ambiente virtual**

```bash
$ python -m venv venv
$ source venv/bin/activate  # Linux/Mac
$ venv\Scripts\activate  # Windows
```

### **3. Instale as dependências**

```bash
$ pip install -r requirements.txt
```

### **4. Configure o banco de dados**

Crie as migrações iniciais e aplique-as:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### **5. Crie um superusuário**

Para acessar o painel administrativo:

```bash
$ python manage.py createsuperuser
```

### **6. Execute o servidor de desenvolvimento**

```bash
$ python manage.py runserver
```

O servidor estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **Endpoints disponíveis**

### **Autenticação**
- `POST /login/`: Retorna o token JWT para autenticação.
  - Exemplo de payload:
    ```json
    {
        "email": "usuario@example.com",
        "password": "senha123"
    }
    ```

### **Usuários**
- `POST /usuarios/`: Criação de novos usuários.
- `GET /usuarios/:id/`: Detalhes de um usuário.

### **Professores e Disciplinas**
- `GET /professores/`: Lista todos os professores.
- `POST /professores/`: Criação de professor com associação a disciplinas.
- `GET /disciplinas/`: Lista todas as disciplinas.

### **Avaliações**
- `POST /avaliacoes/`: Cria uma avaliação (autenticado).
- `GET /avaliacoes/`: Lista todas as avaliações (público).
- `GET /avaliacoes/:id/`: Detalhes de uma avaliação (público).

### **Comentários**
- `POST /comentarios/`: Cria um comentário (autenticado).
- `GET /comentarios/`: Lista todos os comentários (público).
- `GET /comentarios/:id/`: Detalhes de um comentário (público).

---

## **Testando o projeto**

### **Rodando os testes**

Para garantir que tudo está funcionando corretamente:

```bash
$ python manage.py test
```

---

## **Contribuição**

Fique à vontade para contribuir com melhorias e novas funcionalidades! Abra uma issue ou envie um pull request com suas ideias.

---

## **Licença**

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

