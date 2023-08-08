from ..models.password import Password, Key

class PasswordService:
    @staticmethod
    def import_passwords(passwords):
        success_count = 0
        failure_count = 0
        # Iterar sobre as senhas importadas
        for password_data in passwords:
            site_name = password_data.get("site_name")
            username = password_data.get("username")
            password = password_data.get("password")
            url = password_data.get("url")
            
            # Realizar qualquer validação necessária nos dados da senha
            if not site_name or not username or not password or not url:
                # Se algum campo obrigatório estiver faltando, consideramos uma falha
                failure_count += 1
                continue
            
            # Criar um novo objeto Key e salva no banco
            key_obj = Key()
            key_obj.save()

            ## Criar um novo objeto Password com os dados da senha importada e salva no banco de dados
            password_obj = Password(ref=key_obj.entry_ref)
            password_obj.encrypt_fields(site_name, username, password, url)
            password_obj.save()
            
            # Incrementar o contador de sucesso
            success_count += 1
        
        # Retornar um resultado indicando a quantidade de senhas importadas com sucesso e a quantidade de falhas
        return {"success_count": success_count, "failure_count": failure_count}
