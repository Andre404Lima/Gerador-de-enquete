# Sistema de Enquetes Django

## Descrição

Projeto web em Django para criação e gerenciamento de enquetes com múltiplas opções.  
Possui painel administrativo para criar perguntas, adicionar opções e controlar data de encerramento.  
Ideal para quem quer aprender Django básico, modelos, migrações e admin.

## Requisitos

- Python 3.8+  
- Django 4.x  
- (Opcional) PostgreSQL para banco de dados

## Instalação

1. Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd sistema_enquetes

cpp
Copiar
Editar

2. Crie e ative o ambiente virtual:

python -m venv venv

Windows
.\venv\Scripts\Activate.ps1

Linux/macOS
source venv/bin/activate

csharp
Copiar
Editar

3. Instale as dependências:

pip install django

markdown
Copiar
Editar

4. (Opcional) Configure banco PostgreSQL em `settings.py`.

5. Execute as migrações:

python manage.py migrate

markdown
Copiar
Editar

6. Crie um superusuário para acessar o admin:

python manage.py createsuperuser

markdown
Copiar
Editar

7. Inicie o servidor:

python manage.py runserver

markdown
Copiar
Editar

8. Acesse o admin em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Como usar

- No painel admin, crie enquetes e opções.  
- Enquetes podem ter data de encerramento para bloquear votos depois.  
- (Próximos passos: criar interface pública para votar.)

## Estrutura do projeto

- `enquete/models.py` — modelos das tabelas Enquete e Opcao  
- `enquete/admin.py` — configuração do painel administrativo  
- `enquete_site/settings.py` — configurações do Django  


## Implementações Futuras

🚧 Criar views e templates para exibir enquetes para usuários votarem  

🚧 Implementar sistema de votação com atualização dos votos  

🚧 Criar página de resultados das enquetes  

🚧 Adicionar autenticação de usuários comuns para controlar quem pode votar  

🚧 Melhorar design com CSS e frameworks front-end  

🚧 Implementar testes automatizados para garantir qualidade  

🚧 Configurar deploy em servidor de produção com PostgreSQL  
