# project-1---vulnerabilities-equipa_34

## Descrição
Este projeto consiste numa webapp para uma loja, onde os seus clientes podem verificar a disponibilidade de produtos e reservá-los. Apenas utilizadores autenticados podem reservar produtos. Utilizadores não autenticados só podem verificar a disponibilidade e quantidade de cada produto. O Admin pode adicionar e remover produtos e também aumentar e diminuir a sua quantidade, mas não pode reservar produtos. Um produto para ser removido tem de se reduzir a sua quantidade a 0 e voltar a fazer o *remove request*. Foi utilizado flask para o backend e sqlite3 para a base de dados.

### Contas presentes na base de dados:
1. email: admin@admin.com  ||  password: 1234 (admin user)
2. email: diogo@diogo.com  ||  password: 1234 (normal user)

## Autores
- Pedro Miguel Tavares Rodrigues, 92338
- Diogo Pereira de Jesus, 97596
- Diogo Alexandre Almeida Santos Torrinhas, 98440
- João Pedro Almeida Santos Torrinhas, 98435
## Vulnerabilidades implementadas
- [CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')](https://cwe.mitre.org/data/definitions/79.html)
- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](https://cwe.mitre.org/data/definitions/89.html)
- [CWE-200: Exposure of Sensitive Information to an Unauthorized Actor](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-328: Use of Weak Hash](https://cwe.mitre.org/data/definitions/328.html)
- [CWE-862: Missing Authorization](https://cwe.mitre.org/data/definitions/862.html)
- [CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine](https://cwe.mitre.org/data/definitions/1336.html)
## Como correr o código
1. Criar um virtual environment:
```bash
python3 -m venv venv
```

2. Ativar o virtual environment (executar sempre após iniciar uma nova sessão):
```bash
source venv/bin/activate
```

3. Instalar os requisitos:
```bash
pip install -r requirements.txt
```

4. Executar um dos seguintes comandos para correr a versão vunerável ou segura:
```bash
python3 app/app.py
python3 app_sec/app.py
```

