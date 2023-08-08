-- Tabela "keys"
CREATE TABLE keys (
    id SERIAL PRIMARY KEY,
    key BYTEA NOT NULL,
    entry_ref BYTEA NOT NULL
);

-- Tabela "passwords"
CREATE TABLE passwords (
    id SERIAL PRIMARY KEY,
    site_name_encrypted BYTEA NOT NULL,
    username_encrypted BYTEA NOT NULL,
    password_encrypted BYTEA NOT NULL,
    url_encrypted BYTEA NOT NULL,
    ref BYTEA NOT NULL
);


-- Conceder permissão de leitura, atualização, gravação e exclusão para a tabela "keys" para o usuário específico
GRANT SELECT, INSERT, UPDATE, DELETE ON keys TO pucatpsw;

-- Conceder permissão de leitura, atualização, gravação e exclusão para a tabela "passwords" para o usuário específico
GRANT SELECT, INSERT, UPDATE, DELETE ON passwords TO pucatpsw;

-- Permissão da primary key
GRANT USAGE, SELECT ON SEQUENCE passwords_id_seq TO pucatpsw;
GRANT USAGE, SELECT ON SEQUENCE keys_id_seq TO pucatpsw;