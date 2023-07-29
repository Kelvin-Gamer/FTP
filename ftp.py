from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

# Configurações do servidor
HOST = "0.0.0.0"  # Endereço do servidor
PORT = 2121  # Porta para a conexão FTP
SERVER_DIR = "C:\\"

def main():
    authorizer = DummyAuthorizer()

    # Adicionar acesso anônimo com permissões máximas
    authorizer.add_anonymous(SERVER_DIR, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    # Configurações do servidor FTP
    server = servers.FTPServer((HOST, PORT), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
