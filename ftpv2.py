from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
import socket
import os

# Configurações do servidor
HOST = "0.0.0.0"  # Endereço do servidor
PORT = 2121  # Porta para a conexão FTP

def get_server_directory():
    drive_letter = input("Digite a letra da unidade que deseja compartilhar (por exemplo, C, D, E), ou pressione Enter para selecionar o diretório raiz padrão do sistema: ")
    if not drive_letter:
        if os.name == 'nt':  # Verifica se está rodando no Windows
            return os.path.abspath(os.sep)  # Retorna o diretório raiz padrão do sistema no Windows
        else:
            return os.sep  # Retorna o diretório raiz padrão do sistema no Linux
    return f"{drive_letter.upper()}:\\"

def main():
    # Solicitar a letra da unidade desejada
    SERVER_DIR = get_server_directory()

    authorizer = DummyAuthorizer()

    # Adicionar acesso anônimo com permissões máximas
    authorizer.add_anonymous(SERVER_DIR, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    # Obter o endereço IP do computador
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"Endereço IP do computador: {ip_address}")

    # Configurações do servidor FTP
    server = servers.FTPServer((HOST, PORT), handler)
    print(f"Servidor FTP iniciado em {HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()
