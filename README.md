# 🚀 Desafio Login

Este repositório contém uma aplicação de login e cadastro desenvolvida em Django.

## 📌 Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- PostgreSQL
- Virtualenv
- Decouple

---

## 🛠️ Configuração do Ambiente

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/emilyrizo/desafio-login.git
cd desafio-login
```

### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# Ativar (no Windows com bash)
source venv\Scripts\activate
```

### 3️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e configure-o com as informações do banco de dados:

```env
DATABASE_URL='postgresql://usuario:senha@host:porta/database?sslmode=require'
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=xxxxxxxxxxxxxxxx
FROM_EMAIL=email@gmail.com
```
---

## 🚀 Executando a Aplicação

### 5️⃣ Aplicar as Migrações

```bash
python manage.py migrate
```

### 6️⃣ Criar um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 7️⃣ Rodar o Servidor

```bash
python manage.py runserver
```

Acesse a aplicação no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📧 Envio de E-mail

A aplicação inclui uma funcionalidade para enviar um e-mail de confirmação após o registro de um novo usuário. Para que isso funcione, certifique-se de configurar corretamente as variáveis de ambiente relacionadas ao e-mail no arquivo .env.

---

## 📖 Documentação

- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 📌 Autor

Desenvolvido por **Emily Rizo**.