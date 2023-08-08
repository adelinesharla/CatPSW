from flask import Blueprint, request
from ..services.password_service import PasswordService
from csv import DictReader
import tempfile

password_bp = Blueprint("password", __name__)

@password_bp.route("/passwords/import", methods=["POST"])
def import_passwords():
    file = request.files.get("csv_file")
    if file is None:
        return {"message": "No file uploaded"}, 400

    # Criar um arquivo temporário
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_path = temp_file.name

    file.save(temp_path)

    # Processar o arquivo CSV e extrair as senhas
    passwords = process_csv_file(temp_path)

    # Call the PasswordService to handle the import logic
    count = PasswordService.import_passwords(passwords)

    return {"message": count}, 200

def process_csv_file(file):
    passwords = []
    
    # Abrir o arquivo CSV para leitura
    with open(file, newline='') as csvfile:
        reader = DictReader(csvfile)
        
        # Iterar sobre as linhas do arquivo CSV
        for row in reader:
            site_name = row['name']
            username = row['username']
            password = row['password']
            url = row['url']
            note = row.get('note', '')  # Obtém o valor da coluna 'note' ou retorna uma string vazia se não existir
            
            # Criar um dicionário com as informações da senha
            password_data = {
                'site_name': site_name,
                'username': username,
                'password': password,
                'url': url,
                'note': note
            }
            # Adicionar o dicionário à lista de senhas
            passwords.append(password_data)
    
    return passwords

