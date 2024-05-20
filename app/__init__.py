from flask import Flask
# Usando SQLAlchemy, o ORM que usei para interagir com o banco de dados
from flask_sqlalchemy import SQLAlchemy
# Usando o Migrate para gerenciar migrações de banco de dados
from flask_migrate import Migrate

# Instância da aplicação Flask
app = Flask(__name__)

# Configurando o banco de dados para PostgreSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/sf_cafe'

# Definindo uma chave secreta para a aplicação. 
app.config['SECRET_KEY'] = 'mysecretkey'

# Instância do SQLAlchemy que vincula à aplicação Flask
db = SQLAlchemy(app)

# Instância do Migrate que vincula à aplicação Flask e ao SQLAlchemy
migrate = Migrate(app, db)

# Importando as rotas e os modelos da aplicação
from app import routes, models
