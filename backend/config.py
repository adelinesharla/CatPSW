from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

# Chave de criptografia
SECRET_KEY = os.environ.get('SECRET_KEY')