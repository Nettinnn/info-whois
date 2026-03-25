Ferramenta em Python para consulta de informações WHOIS utilizando comunicação direta via sockets.

---

## 📌 Descrição

O **AXN WHOIS Tool** é um script desenvolvido para realizar consultas WHOIS diretamente com servidores, sem o uso de ferramentas prontas.

A aplicação estabelece conexão com o servidor WHOIS (`whois.iana.org`) na porta 43 e envia requisições manualmente, demonstrando na prática como o protocolo funciona.

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- Sockets
- Protocolo TCP

---

## 🧠 Conceitos Aplicados

- Comunicação cliente-servidor
- Uso de sockets em Python
- Protocolo WHOIS (porta 43)
- Manipulação de dados em rede
- Encoding/Decoding de dados

---

## 🚀 Como Funciona

1. O usuário fornece um domínio como argumento
2. O script conecta ao servidor WHOIS
3. Envia a consulta via socket
4. Recebe e exibe a resposta do servidor

---

## 🛠️ Requisitos

- Python 3 instalado

---

## ▶️ Uso

```bash id="9q9x2m"
python3 axn_whois.py dominio.com
