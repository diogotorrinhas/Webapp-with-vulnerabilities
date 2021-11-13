# [CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](https://cwe.mitre.org/data/definitions/89.html)
Esta vulnerabilidade está presente no sistema de login. Como a verificação do input do utilizador não é feita, um atacante pode autenticar-se em qualquer conta existente sem saber as credenciais.

![Exemplo de ataque](assets/sqlinjection1.png)

O resultado é o seguinte:

![Resultado do ataque](assets/sqlinjection2.png)

## Código
Como podemos ver a seguir, o acesso à base de dados está a ser feito executando diretamente o comando sql. Como não é feita nenhuma verificação aos inputs do utilizador, a vulnerabilidade está presente.

![Código vulnerável](assets/sqlinjection3.png)

A forma usada para corrigir esta vulnerabilidade foi usar as funções disponibilizadas pelo flask-sqlalchemy, como add, remove e filter_by, para evitar más implementações do código sql.

![Código corrigido](assets/sqlinjection4.png)
