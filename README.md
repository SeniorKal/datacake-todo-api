# DataCake Todo — Backend

API REST do aplicativo DataCake Todo, construída com Django e Django REST Framework. A API oferece cadastro e autenticação JWT, além do CRUD de tarefas com isolamento dos dados por usuário.

## Tecnologias

- Python 3.12 ou superior
- Django 6
- Django REST Framework
- Simple JWT
- SQLite

## Pré-requisitos

Instale o Python e confirme que os comandos estão disponíveis:

```powershell
python --version
python -m pip --version
```

## Instalação no Windows

Clone o repositório, entre na pasta do backend e crie um ambiente virtual:

```powershell
git clone <URL_DO_REPOSITORIO_BACKEND>
cd <PASTA_DO_REPOSITORIO>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuração

O arquivo `.env.example` documenta as variáveis esperadas para um ambiente configurável. Nunca versione chaves reais ou o arquivo `.env`.

Para o desenvolvimento local atual, confira também `SECRET_KEY`, `DEBUG` e `ALLOWED_HOSTS` em `config/settings.py`. Se o aplicativo rodar em um dispositivo físico, inclua nessa lista o IP local do computador que executa o backend.

## Banco de dados e migrações

Crie as tabelas do banco:

```powershell
python manage.py migrate
```

Quando houver alterações futuras nos models, gere e aplique as migrações com:

```powershell
python manage.py makemigrations
python manage.py migrate
```

O projeto usa SQLite. O arquivo `db.sqlite3` é criado localmente e não deve ser versionado.

## Usuário administrador

Crie uma conta administrativa:

```powershell
python manage.py createsuperuser
```

Com o servidor em execução, o painel fica disponível em `http://127.0.0.1:8000/admin/`.

## Dados de exemplo

Este projeto não inclui fixtures. Para criar dados de teste, registre um usuário pelo endpoint `POST /api/register/`, faça login e crie tarefas pela API ou pelo aplicativo mobile. Também é possível cadastrar dados manualmente pelo painel administrativo quando os models estiverem registrados nele.

## Executando o servidor

Para uso no próprio computador:

```powershell
python manage.py runserver
```

Para permitir acesso por um celular na mesma rede:

```powershell
python manage.py runserver 0.0.0.0:8000
```

Use apenas em uma rede de desenvolvimento confiável. O dispositivo e o computador precisam estar na mesma rede.

## Endpoints principais

| Método | Endpoint | Descrição | Autenticação |
| --- | --- | --- | --- |
| GET | `/api/health/` | Verifica a disponibilidade da API | Não |
| POST | `/api/register/` | Cadastra um usuário | Não |
| POST | `/api/login/` | Retorna os tokens JWT | Não |
| POST | `/api/token/refresh/` | Renova o access token | Não |
| GET, POST | `/api/tasks/` | Lista ou cria tarefas | JWT |
| GET, PUT, PATCH, DELETE | `/api/tasks/{id}/` | Consulta ou altera uma tarefa | JWT |

Nas rotas protegidas, envie o token no header:

```text
Authorization: Bearer <access_token>
```

Cada usuário acessa somente as próprias tarefas.

## Verificações e testes

Execute as verificações do Django:

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
```

Execute a suíte de testes:

```powershell
python manage.py test
```

Os módulos de testes existem, mas a versão atual ainda não possui casos automatizados cadastrados.

## Estrutura principal

```text
accounts/          Cadastro, login e autenticação
tasks/             Model, serializer e endpoints de tarefas
config/            Configurações e rotas principais
manage.py          Utilitário de administração do Django
requirements.txt   Dependências Python
DEVELOPMENT_LOG.md Registro cronológico do desenvolvimento
```

## Solução de problemas

- `No module named django`: ative o `.venv` e instale `requirements.txt`.
- Celular não conecta: confirme o IP em `ALLOWED_HOSTS`, libere a porta 8000 no firewall e use `runserver 0.0.0.0:8000`.
- `401 Unauthorized`: faça login novamente e envie um access token válido.
- Erro de banco: execute `python manage.py migrate`.

