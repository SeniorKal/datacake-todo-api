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

