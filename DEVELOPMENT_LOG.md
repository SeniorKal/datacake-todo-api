# Registro de Desenvolvimento — Backend

Este documento registra, em ordem cronológica, as etapas realizadas no desenvolvimento do backend da aplicação DataCake Todo, as decisões técnicas tomadas e a utilização de ferramentas de Inteligência Artificial durante o processo.

Algumas etapas iniciais foram documentadas retroativamente com base no histórico de commits, nos arquivos criados e nos comandos executados.

---

## 1. Criação do ambiente virtual Python

Foi criado um ambiente virtual dentro da pasta do backend:

```bash
python -m venv .venv
```

O ambiente virtual foi utilizado para manter as dependências deste projeto isoladas das demais instalações de Python presentes no computador.

Para ativar o ambiente no PowerShell, foi utilizado:

```powershell
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal passou a exibir `(.venv)`, indicando que os comandos do Python e do `pip` utilizariam o ambiente do projeto.

### Decisão técnica

Foi escolhido o uso de um ambiente virtual local para evitar conflitos de versões entre bibliotecas e facilitar a reprodução do projeto em outros computadores.

### Uso de IA

A IA foi utilizada para explicar a finalidade do ambiente virtual e orientar os comandos de criação e ativação. Os comandos foram executados e verificados manualmente.

---

## 2. Instalação do Django e Django REST Framework

Foram instaladas as dependências principais do backend:

```bash
pip install django djangorestframework
```

O Django é responsável pela estrutura principal da aplicação, gerenciamento do banco de dados, rotas e regras do sistema.

O Django REST Framework foi adicionado para permitir a construção de uma API REST que poderá ser consumida pelo aplicativo React Native.

As dependências utilizadas foram registradas no arquivo:

```text
requirements.txt
```

Esse arquivo permitirá que outra pessoa instale as mesmas bibliotecas com:

```bash
pip install -r requirements.txt
```

### Decisão técnica

As dependências foram registradas desde o início para facilitar a instalação, documentação e execução do projeto em outro ambiente.

### Uso de IA

A IA foi utilizada para explicar a diferença entre Django e Django REST Framework e orientar a instalação e o registro das dependências.

---

## 3. Criação do projeto Django

Foi criado o projeto principal do Django, responsável pelas configurações globais do backend.

A estrutura inclui a pasta:

```text
config/
```

Nela ficam arquivos como:

- `settings.py`
- `urls.py`
- `wsgi.py`
- `asgi.py`

O arquivo `settings.py` concentra configurações como aplicativos instalados, banco de dados, idioma, fuso horário e outras opções globais.

O arquivo `urls.py` é responsável pelo roteamento principal da aplicação.

### Decisão técnica

Foi utilizado o nome `config` para deixar claro que essa pasta contém as configurações gerais, e não uma funcionalidade específica do sistema.

### Uso de IA

A IA foi utilizada para explicar a diferença entre um projeto Django e um app Django, assim como a responsabilidade de cada arquivo criado automaticamente.

---

## 4. Configuração do Django REST Framework

O Django REST Framework foi adicionado à lista de aplicativos instalados no arquivo:

```text
config/settings.py
```

Foi incluído:

```python
"rest_framework",
```

Essa configuração permite que os recursos do Django REST Framework sejam utilizados no projeto.

### Decisão técnica

O framework foi configurado desde o início porque toda a comunicação entre o aplicativo mobile e o backend será realizada por meio de uma API REST.

### Uso de IA

A IA foi utilizada para explicar por que uma biblioteca instalada com `pip` também precisa ser adicionada ao `INSTALLED_APPS` em determinados casos.

---

## 5. Criação dos apps `accounts` e `tasks`

Foram criados dois apps Django:

```bash
python manage.py startapp accounts
python manage.py startapp tasks
```

O app `accounts` será responsável pelas funcionalidades relacionadas a:

- cadastro de usuários;
- autenticação;
- login;
- recuperação ou redefinição de senha;
- gerenciamento de informações da conta.

O app `tasks` será responsável pelas funcionalidades relacionadas a:

- criação de tarefas;
- listagem de tarefas;
- edição;
- marcação como concluída;
- exclusão;
- filtros;
- isolamento dos dados por usuário.

Os dois apps foram adicionados ao `INSTALLED_APPS` no arquivo `config/settings.py`.

### Decisão técnica

As funcionalidades foram separadas em apps diferentes para manter as responsabilidades isoladas e facilitar a manutenção do código.

### Uso de IA

A IA foi utilizada para explicar o conceito de apps no Django e sugerir uma separação de responsabilidades compatível com o escopo do teste.

---

## 6. Configuração inicial das rotas

Foram criados arquivos de rotas específicos dentro dos apps:

```text
accounts/urls.py
tasks/urls.py
```

As rotas dos apps foram conectadas ao arquivo principal:

```text
config/urls.py
```

Essa organização permite que cada app gerencie suas próprias URLs, evitando que todas as rotas da aplicação fiquem concentradas em um único arquivo.

### Decisão técnica

Foi escolhida uma organização modular de URLs para melhorar a legibilidade e facilitar a expansão futura da API.

### Uso de IA

A IA foi utilizada para explicar o funcionamento da função `include` do Django e a relação entre as URLs do projeto e as URLs dos apps.

---

## 7. Criação do endpoint de verificação da API

Foi criado um endpoint simples para verificar o funcionamento do servidor:

```text
/api/health/
```

O endpoint retorna uma resposta indicando que a API está ativa.

Ele foi utilizado para confirmar que:

- o servidor Django estava funcionando;
- o app estava corretamente conectado;
- as rotas estavam configuradas;
- o Django REST Framework conseguia devolver uma resposta;
- o navegador conseguia acessar a aplicação.

O servidor foi iniciado com:

```bash
python manage.py runserver
```

### Decisão técnica

O endpoint de saúde foi criado para facilitar testes rápidos e ajudar no diagnóstico de problemas durante o desenvolvimento.

### Uso de IA

A IA foi utilizada para orientar a criação da view, das URLs e explicar o fluxo completo de uma requisição até a resposta.

---

## 8. Entendimento do banco de dados SQLite

O projeto utiliza inicialmente o SQLite, banco de dados padrão do Django.

O arquivo local do banco é:

```text
db.sqlite3
```

Foi compreendido que o navegador não armazena diretamente o banco de dados.

O navegador apenas envia requisições para o servidor Django. O Django acessa o arquivo `db.sqlite3`, consulta ou modifica os dados e retorna uma resposta para o navegador ou para o aplicativo mobile.

O fluxo básico é:

```text
Aplicativo ou navegador
        ↓
API Django
        ↓
Model
        ↓
Banco de dados SQLite
```

### Decisão técnica

O SQLite foi mantido durante o desenvolvimento por ser simples, não exigir instalação de um servidor de banco separado e ser suficiente para esta etapa do projeto.

### Uso de IA

A IA foi utilizada para explicar a diferença entre navegador, backend e banco de dados, assim como o local onde os dados são realmente armazenados.

---

## 9. Criação do model `Task`

Foi criado o model `Task` no arquivo:

```text
tasks/models.py
```

Esse model representa uma tarefa armazenada no banco de dados.

Foram definidos campos para informações como:

- título;
- descrição;
- status de conclusão;
- data de criação;
- data de atualização.

O model será a representação Python da tabela de tarefas no banco de dados.

### Decisão técnica

Os campos foram escolhidos com base nas funcionalidades obrigatórias do desafio, que exigem criação, edição, conclusão, exclusão e filtragem de tarefas.

Os campos de data também permitirão implementar posteriormente filtros por data de criação.

### Uso de IA

A IA foi utilizada para explicar o funcionamento dos models, dos tipos de campos e da relação entre uma classe Python e uma tabela do banco de dados.

O código foi revisado antes da geração das migrações.

---

## 10. Criação e aplicação das migrações

Após a criação do model `Task`, foi executado:

```bash
python manage.py makemigrations
```

Esse comando analisou as alterações realizadas nos models e gerou o arquivo:

```text
tasks/migrations/0001_initial.py
```

Esse arquivo descreve as alterações que precisam ser aplicadas no banco de dados.

Depois, foi executado:

```bash
python manage.py migrate
```

Esse comando aplicou as migrações pendentes e criou a tabela correspondente ao model `Task`.

### Entendimento dos comandos

O comando `makemigrations` não altera diretamente o banco de dados. Ele cria instruções de migração.

O comando `migrate` executa essas instruções no banco.

### Decisão técnica

O arquivo de migração foi versionado no Git, pois ele faz parte da estrutura do projeto e permite que outras pessoas reproduzam o mesmo banco de dados.

O arquivo `db.sqlite3` permanece apenas no ambiente local e não deve ser versionado.

### Uso de IA

A IA foi utilizada para explicar a diferença entre `makemigrations` e `migrate`, evitando que os comandos fossem apenas executados sem entendimento.

---

## 11. Criação do serializer de tarefas

Foi criado o arquivo:

```text
tasks/serializers.py
```

Nesse arquivo foi implementado o `TaskSerializer` utilizando:

```python
serializers.ModelSerializer
```

O serializer é responsável por converter objetos do Django em dados que podem ser enviados em formato JSON para o aplicativo mobile.

Ele também converte os dados recebidos pela API em valores que podem ser validados e utilizados para criar ou atualizar tarefas.

Foram definidos explicitamente os campos expostos pela API:

- `id`;
- `title`;
- `description`;
- `completed`;
- `created_at`;
- `updated_at`.

Os campos abaixo foram configurados apenas para leitura:

- `id`;
- `created_at`;
- `updated_at`.

Esses valores devem ser controlados pelo sistema e não definidos manualmente pelo usuário.

### Decisão técnica

Os campos foram listados explicitamente em vez de utilizar:

```python
fields = "__all__"
```

Essa escolha torna claro quais dados são expostos pela API e reduz o risco de expor futuramente algum campo interno por engano.

### Uso de IA

A IA foi utilizada para explicar o papel do serializer dentro da arquitetura da API e a diferença entre model, serializer e view.

---

## 12. Validação do título da tarefa

Foi adicionada uma validação personalizada ao serializer:

```python
def validate_title(self, value):
```

A validação utiliza:

```python
value.strip()
```

para remover espaços no início e no final do título.

Também foi adicionada uma verificação para impedir títulos:

- vazios;
- formados apenas por espaços.

Quando o valor é inválido, a API retorna uma mensagem legível:

```text
O título da tarefa não pode ficar vazio.
```

### Decisão técnica

A validação foi colocada no serializer porque ela está relacionada aos dados recebidos pela API.

Essa abordagem também permite que o aplicativo mobile receba uma mensagem de erro clara e possa apresentá-la ao usuário.

### Uso de IA

A IA sugeriu a estrutura inicial da validação e explicou a convenção do Django REST Framework para métodos no formato:

```python
validate_nome_do_campo
```

A implementação foi analisada para compreender por que o método é chamado automaticamente.

---

## 13. Organização do histórico de commits

As alterações do backend foram separadas em commits de acordo com sua responsabilidade.

Entre os commits realizados estão etapas como:

```text
chore: initialize django rest framework project
build: add backend dependencies list
feat: add health check endpoint
feat: add Task model and initial migration
feat: add task serializer validation
```

### Decisão técnica

Foi evitado o uso de um único commit grande.

Cada commit representa uma mudança lógica e facilita a leitura da evolução do projeto, a revisão do código e a identificação de eventuais problemas.

### Uso de IA

A IA foi utilizada para sugerir mensagens de commit claras seguindo um padrão semântico.

As alterações adicionadas em cada commit foram verificadas com:

```bash
git status
```

antes da confirmação.

---

## 14. Implementação inicial do CRUD de tarefas

Foi criado o `TaskViewSet`, responsável por receber as requisições HTTP relacionadas às tarefas.

O ViewSet foi implementado utilizando:

```python
viewsets.ModelViewSet
```

Com essa implementação, a API passou a oferecer operações para:

- listar tarefas;
- criar tarefas;
- visualizar uma tarefa específica;
- atualizar tarefas;
- excluir tarefas.

Também foi criado o arquivo:

```text
tasks/urls.py
```

Nesse arquivo, foi utilizado o `DefaultRouter` do Django REST Framework para gerar automaticamente as rotas do CRUD.

As rotas foram conectadas ao arquivo principal:

```text
config/urls.py
```

Com isso, o endpoint de tarefas passou a ficar disponível em:

```text
/api/tasks/
```

### Rotas disponibilizadas

```text
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/<id>/
PUT    /api/tasks/<id>/
PATCH  /api/tasks/<id>/
DELETE /api/tasks/<id>/
```

### Autenticação e isolamento dos dados

Foi configurada a permissão:

```python
permissions.IsAuthenticated
```

A criação de tarefas passou a associar automaticamente a nova tarefa ao usuário autenticado:

```python
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
```

A listagem também passou a retornar apenas as tarefas pertencentes ao usuário autenticado:

```python
def get_queryset(self):
    return Task.objects.filter(user=self.request.user)
```

Essa implementação impede que um usuário visualize ou manipule tarefas de outro usuário.

### Testes realizados

Foram realizados testes utilizando a Browsable API do Django REST Framework.

Durante o primeiro teste de criação, foi identificado o erro:

```text
NOT NULL constraint failed: tasks_task.user_id
```

O erro ocorreu porque o model exige que toda tarefa tenha um usuário associado, mas o usuário ainda não estava sendo atribuído durante a criação.

Após a implementação do método `perform_create()`, a tarefa passou a ser salva corretamente com o usuário autenticado como proprietário.

Também foi criado um superusuário com:

```bash
python manage.py createsuperuser
```

A autenticação de sessão da Browsable API foi disponibilizada pela rota:

```text
/api-auth/
```

Depois do login, foi possível criar uma tarefa com sucesso. A API retornou:

```text
HTTP 201 Created
```

Em seguida, uma requisição `GET` confirmou que a tarefa criada estava sendo listada corretamente.

### Configuração de redirecionamento

Para facilitar os testes pela interface navegável, foram adicionadas as configurações:

```python
LOGIN_REDIRECT_URL = "/api/tasks/"
LOGOUT_REDIRECT_URL = "/api-auth/login/"
```

Essas configurações são usadas apenas para melhorar o fluxo de teste com autenticação por sessão no navegador.

A autenticação definitiva do aplicativo mobile ainda será implementada com tokens.

### Decisão técnica

Foi decidido que o aplicativo não enviará o identificador do usuário ao criar uma tarefa.

O backend identifica o usuário por meio da autenticação e associa a tarefa automaticamente.

Essa abordagem reduz o risco de um usuário tentar criar tarefas em nome de outra pessoa.

Também foi escolhido filtrar as tarefas pelo usuário autenticado em vez de utilizar:

```python
Task.objects.all()
```

Isso garante o isolamento dos dados exigido pelo desafio.

### Uso de IA

A IA foi utilizada para explicar o funcionamento dos ViewSets, Routers, permissões, autenticação por sessão e isolamento dos dados por usuário.

O erro de integridade encontrado durante o teste foi analisado para compreender sua causa antes da correção.

## 15. Implementação do endpoint de cadastro de usuários

Foi implementado o primeiro endpoint responsável pelo cadastro de usuários da aplicação.

O endpoint foi disponibilizado em:

```text
POST /api/register/
```

Para essa implementação foi criado o arquivo:

```text
accounts/serializers.py
```

contendo o `RegisterSerializer`, responsável por validar os dados recebidos e criar novos usuários.

Também foi criada a classe:

```python
RegisterView
```

utilizando:

```python
generics.CreateAPIView
```

Essa classe recebe requisições HTTP do tipo `POST`, envia os dados para o serializer, executa todas as validações e cria o usuário no banco de dados.

A rota foi registrada no arquivo:

```text
accounts/urls.py
```

e integrada automaticamente ao projeto através de:

```text
config/urls.py
```

### Campos utilizados

O cadastro utiliza os seguintes campos:

- email;
- password;
- password_confirm.

Embora o model padrão do Django exija o campo `username`, foi decidido manter uma interface mais simples para o usuário.

Internamente, o backend utiliza o próprio e-mail como username durante a criação da conta.

A criação é realizada utilizando:

```python
User.objects.create_user(
    username=validated_data["email"],
    email=validated_data["email"],
    password=validated_data["password"],
)
```

Essa abordagem mantém compatibilidade com o sistema de autenticação do Django sem exigir que o usuário escolha um nome de usuário.

### Validações implementadas

Foram implementadas validações para:

- tamanho mínimo da senha;
- confirmação da senha;
- existência de outro usuário utilizando o mesmo e-mail;
- normalização do e-mail para letras minúsculas.

Os campos de senha foram configurados como:

```python
write_only=True
```

garantindo que nunca sejam retornados nas respostas da API.

### Permissões

O endpoint de cadastro utiliza:

```python
permissions.AllowAny
```

permitindo que usuários ainda não autenticados possam criar uma conta.

Essa configuração é diferente dos endpoints de tarefas, que utilizam:

```python
permissions.IsAuthenticated
```

pois exigem autenticação.

### Testes realizados

Foram realizados testes utilizando a Browsable API do Django REST Framework.

Os seguintes cenários foram verificados:

- cadastro realizado com sucesso;
- tentativa de cadastro utilizando senhas diferentes;
- tentativa de cadastro utilizando um e-mail já existente.

Nos casos inválidos, a API retornou corretamente:

```text
HTTP 400 Bad Request
```

com mensagens específicas indicando o motivo da falha.

Foi confirmado que apenas usuários válidos são criados no banco de dados.

### Decisão técnica

Foi decidido manter o fluxo de cadastro baseado apenas em e-mail e senha para simplificar a experiência do usuário no aplicativo mobile.

O campo `username` permanece apenas como um requisito interno do Django, sendo preenchido automaticamente com o mesmo valor do e-mail.

Essa abordagem reduz a quantidade de informações solicitadas ao usuário e mantém compatibilidade com o sistema de autenticação padrão do framework.

### Uso de IA

A IA foi utilizada para explicar o funcionamento das Generic Views do Django REST Framework, a responsabilidade dos Serializers durante o cadastro, a utilização do método `create_user()` para armazenamento seguro da senha e as diferenças entre permissões públicas (`AllowAny`) e autenticadas (`IsAuthenticated`).

Todas as implementações foram compreendidas antes de serem adicionadas ao projeto.

## 16. Implementação da autenticação JWT

Foi implementado o sistema de autenticação utilizando JSON Web Tokens (JWT) através da biblioteca `djangorestframework-simplejwt`.

A biblioteca foi adicionada ao projeto para permitir autenticação baseada em tokens, substituindo o uso exclusivo de sessões durante a comunicação entre o aplicativo mobile e a API.

As dependências do projeto foram atualizadas no arquivo:

```text
requirements.txt
```

### Configuração do Django REST Framework

No arquivo:

```text
config/settings.py
```

foi configurado o Django REST Framework para utilizar autenticação JWT juntamente com autenticação por sessão.

Essa configuração permite que:

- o aplicativo React Native utilize Bearer Tokens;
- a Browsable API continue funcionando normalmente durante o desenvolvimento.

### Endpoints de autenticação

Foram adicionadas duas rotas:

```text
POST /api/login/
POST /api/token/refresh/
```

O endpoint de login é responsável por autenticar o usuário e retornar:

- Access Token;
- Refresh Token.

O endpoint de refresh permite gerar um novo Access Token sem que o usuário precise informar novamente suas credenciais.

### Personalização do login

A implementação padrão do SimpleJWT utiliza o campo `username` para autenticação.

Como o aplicativo mobile foi projetado para utilizar apenas e-mail e senha, foi criado um serializer personalizado chamado:

```text
LoginSerializer
```

Esse serializer recebe:

- email;
- password.

Internamente o e-mail é convertido para o campo `username`, permitindo reutilizar toda a lógica original do Django sem alterar o funcionamento da autenticação.

Também foi criada uma `LoginView`, responsável por utilizar esse serializer personalizado.

Dessa forma, a API passou a aceitar exatamente o mesmo formato utilizado pelo aplicativo mobile.

### Testes realizados

Foram realizados testes utilizando a Browsable API do Django REST Framework.

Foram verificados os seguintes cenários:

- login com credenciais válidas;
- login com senha incorreta;
- login utilizando usuário inexistente;
- geração do Access Token;
- geração do Refresh Token.

Também foi confirmado que o endpoint passou a utilizar o campo `email` em vez de `username`, mantendo consistência entre backend e frontend.

### Decisão técnica

Foi decidido personalizar a autenticação do SimpleJWT para manter o contrato da API alinhado com a interface do aplicativo mobile.

Essa abordagem elimina adaptações futuras no frontend e torna a API mais intuitiva para consumo.

### Uso de IA

A IA foi utilizada para explicar o funcionamento do JWT, a diferença entre Access Token e Refresh Token, a personalização do `TokenObtainPairSerializer`, a criação de uma `LoginView` personalizada e o fluxo completo de autenticação entre cliente e servidor.

Todas as implementações foram compreendidas antes de serem adicionadas ao projeto.