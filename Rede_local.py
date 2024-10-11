"""
Para aqueles que quiserem usar para testar a portabilidade do site, precisam seguir os passos citados abaixo;
Baixar o ngrock que está no repositório raiz.
Criar uma conta no site "https://dashboard.ngrok.com/get-started/setup/windows" é só entrar com o github que entra em dois cliques
Copiar o link de identificação que fica na pagina inicial e colar no cmd
iniciar esse arquivo python
Colar "ngrok http 8000" no cmd e clicar no link com .app no final
"""



import http.server
import socketserver
import socket
import os

# Capturar o IP local
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)

print(f"IP Local: {ip_local}")

# Definir a porta onde o servidor vai rodar
PORT = 8000

# Caminho para os diretórios
TEMPLATES_DIRECTORY = "templates"
STATIC_DIRECTORY = "static"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # Se o caminho solicitar arquivos do diretório static, altere o diretório de serviço
        if self.path.startswith("/static"):
            self.directory = STATIC_DIRECTORY
            self.path = self.path[len("/static"):]  # Remover "/static" do caminho para localizar o arquivo corretamente
        else:
            self.directory = TEMPLATES_DIRECTORY  # Caso contrário, sirva arquivos do diretório de templates
        return super().do_GET()

# Configurar o servidor para escutar em todos os IPs (0.0.0.0)
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    print(f"Acesse a página em http://{ip_local}:{PORT}/registrar.html")
    httpd.serve_forever()
