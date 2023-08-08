from peewee import Model, BlobField, AutoField, ForeignKeyField
from cryptography.fernet import Fernet
from main import db
import base64

class Key(Model):
    class Meta:
        database = db
        table_name = "keys"
    id = AutoField(primary_key=True)
    key = BlobField()
    entry_ref = BlobField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key = Fernet.generate_key()
        self.entry_ref = base64.b64encode(str(self.id).encode())

    
    @classmethod
    def get_by_entry_ref(cls, entry_ref):
        return cls.get(cls.entry_ref == entry_ref)



class Password(Model):
    class Meta:
        database = db
        table_name = "passwords"

    id = AutoField(primary_key=True)
    site_name_encrypted = BlobField()
    username_encrypted = BlobField()
    password_encrypted = BlobField()
    url_encrypted = BlobField()
    ref = BlobField()


    def __init__(self, ref, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ref = ref


    def encrypt_fields(self, site_name, username, password, url):
        self.site_name_encrypted = self.encrypt_value(site_name)
        self.username_encrypted = self.encrypt_value(username)
        self.password_encrypted = self.encrypt_value(password)
        self.url_encrypted = self.encrypt_value(url)

    def encrypt_value(self, value):
        key_obj = Key.get_by_entry_ref(self.ref)
        cipher_suite = Fernet(key_obj.key)
        encrypted_value = cipher_suite.encrypt(str(value).encode())
        return encrypted_value

    def decrypt_value(self, encrypted_value):
        key_obj = Key.get_by_entry_ref(self.ref)
        cipher_suite = Fernet(key_obj.key)
        decrypted_value = cipher_suite.decrypt(encrypted_value).decode()
        return decrypted_value