from flask import Flask
import config
from peewee import PostgresqlDatabase

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá, mundo!'

# Criar a instância do PostgreSQL
db = PostgresqlDatabase(database=config.DATABASE_URL)


if __name__ == "__main__":
    # Importar os modelos para que o PostgreSQL possa criá-los no banco de dados
    from app.models.password import Password
    # Importar os blueprints das rotas
    from app.controllers.password_controller import password_bp
    # Registrar os blueprints no aplicativo Flask
    app.register_blueprint(password_bp)
    app.run()
