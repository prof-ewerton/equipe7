# **Tutorial: CRUD em Python com SQLite, tratamento de exceções e gerenciamento de tabelas**

## **1. Introdução**

CRUD é uma sigla que representa as quatro operações fundamentais de manipulação de dados em sistemas computacionais:

- **Create:** criação e inserção de registros.
- **Read:** consulta e leitura de registros.
- **Update:** atualização de registros existentes.
- **Delete:** exclusão de registros.

Neste tutorial, vamos aprender a implementar essas operações utilizando Python e SQLite, incluindo:

- Criação de tabelas.
- Exclusão de tabelas existentes.
- Inserção de registros.
- Consulta de registros.
- Atualização de registros.
- Exclusão de registros.
- Tratamento de exceções com `try`, `except` e `finally`.
- Validação de dados.
- Organização do código em funções e camadas.

O objetivo é compreender a lógica de cada operação, sem concentrar toda a implementação em um único código.

## **2. Preparando o ambiente**

O Python possui o módulo `sqlite3` em sua biblioteca padrão. Portanto, não precisamos instalar bibliotecas externas para trabalhar com SQLite.

Primeiramente, realizamos a importação:

```
import sqlite3
```

Para acessar o banco de dados, utilizamos `connect()`:

```
conexao = sqlite3.connect("sistema.db")
```

Nesse exemplo, o banco de dados será armazenado no arquivo `sistema.db`. Caso ele ainda não exista, o SQLite criará o arquivo automaticamente.

Em seguida, criamos um cursor:

```
cursor = conexao.cursor()
```

O cursor é responsável por executar os comandos SQL e recuperar os resultados das consultas.

### **2.1. Tratamento de exceções na conexão**

É importante considerar que operações com banco de dados podem apresentar erros. Por exemplo, o arquivo pode estar inacessível ou uma instrução SQL pode conter erros de sintaxe.

Para tratar essas situações, utilizamos `try` e `except`.

```
try:    conexao = sqlite3.connect("sistema.db")    cursor = conexao.cursor()    print("Conexão realizada com sucesso.")except sqlite3.Error as erro:    print("Erro ao conectar ao banco:", erro)
```

O bloco `try` contém as instruções que podem gerar exceções. Caso ocorra um erro relacionado ao SQLite, o bloco `except` captura a exceção e permite apresentar uma mensagem adequada.

### **2.2. Finalizando a conexão**

Depois de utilizar o banco de dados, devemos encerrar a conexão.

O bloco `finally` é especialmente útil porque é executado independentemente de ocorrer ou não uma exceção.

```
conexao = Nonetry:    conexao = sqlite3.connect("sistema.db")    cursor = conexao.cursor()    print("Banco de dados acessado.")except sqlite3.Error as erro:    print("Erro:", erro)finally:    if conexao is not None:        conexao.close()        print("Conexão encerrada.")
```

**Entenda a diferença:**

| Estrutura | Responsabilidade                                    |
| --------- | --------------------------------------------------- |
| `try`     | Executar instruções que podem gerar erros.          |
| `except`  | Capturar e tratar os erros.                         |
| `finally` | Executar instruções independentemente do resultado. |

O `finally` é frequentemente utilizado para liberar recursos, como conexões com bancos de dados.

## **3. Criando tabelas**

Antes de inserir registros, precisamos criar uma tabela para armazenar os dados.

Considere uma entidade chamada `produto`, com os seguintes atributos:

| Atributo   | Tipo SQL | Descrição                 |
| ---------- | -------- | ------------------------- |
| id         | INTEGER  | Identificador do registro |
| nome       | TEXT     | Nome do produto           |
| preco      | REAL     | Preço do produto          |
| disponivel | INTEGER  | Indica se está disponível |
| categoria  | TEXT     | Categoria do produto      |

O comando SQL para criar essa tabela é:

```
CREATE TABLE produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    disponivel INTEGER,
    categoria TEXT
);
```

Observe os principais elementos:

- `CREATE TABLE`: cria uma tabela.
- `PRIMARY KEY`: define a chave primária.
- `AUTOINCREMENT`: gera identificadores automaticamente.
- `TEXT`: representa valores textuais.
- `REAL`: representa números reais.
- `INTEGER`: representa números inteiros.
- `NOT NULL`: impede que o atributo receba um valor nulo.

### **3.1. Criando uma tabela com Python**

Para executar o comando SQL, utilizamos `cursor.execute()`.

```
try:    cursor.execute("""        CREATE TABLE produto (            id INTEGER PRIMARY KEY AUTOINCREMENT,            nome TEXT NOT NULL,            preco REAL,            disponivel INTEGER,            categoria TEXT        )    """)    conexao.commit()    print("Tabela criada com sucesso.")except sqlite3.Error as erro:    print("Erro ao criar tabela:", erro)
```

O método `execute()` executa a instrução SQL, enquanto `commit()` confirma a alteração no banco de dados.

### **3.2. Criando uma tabela somente se ela não existir**

Um problema comum acontece quando tentamos criar uma tabela que já existe.

Para evitar esse problema, podemos utilizar `IF NOT EXISTS`.

```
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    disponivel INTEGER,
    categoria TEXT
);
```

Essa instrução cria a tabela somente se ela ainda não existir.

No Python:

```
try:    cursor.execute("""        CREATE TABLE IF NOT EXISTS produto (            id INTEGER PRIMARY KEY AUTOINCREMENT,            nome TEXT NOT NULL,            preco REAL,            disponivel INTEGER,            categoria TEXT        )    """)    conexao.commit()except sqlite3.Error as erro:    print("Erro ao criar tabela:", erro)
```

Essa abordagem é útil quando o instalador pode ser executado várias vezes sem precisar apagar os dados existentes.

## **4. Excluindo tabelas existentes**

Em determinadas situações, precisamos apagar uma tabela e criá-la novamente.

Por exemplo, durante a instalação de um sistema, podemos desejar reconstruir a estrutura do banco de dados e inserir registros iniciais.

Para excluir uma tabela, utilizamos `DROP TABLE`.

```
DROP TABLE produto;
```

Entretanto, se a tabela não existir, o comando poderá gerar um erro.

Para evitar isso, utilizamos `IF EXISTS`:

```
DROP TABLE IF EXISTS produto;
```

Essa instrução verifica a existência da tabela antes de excluí-la.

### **4.1. Excluindo uma tabela com Python**

```
try:    cursor.execute("DROP TABLE IF EXISTS produto")    conexao.commit()    print("Tabela excluída com sucesso.")except sqlite3.Error as erro:    print("Erro ao excluir tabela:", erro)
```

Observe que `DROP TABLE` exclui a estrutura da tabela e todos os registros armazenados nela.

### **4.2. Excluindo e criando novamente uma tabela**

Podemos combinar as duas operações para reconstruir uma tabela.

```
try:    cursor.execute("DROP TABLE IF EXISTS produto")    cursor.execute("""        CREATE TABLE produto (            id INTEGER PRIMARY KEY AUTOINCREMENT,            nome TEXT NOT NULL,            preco REAL,            disponivel INTEGER,            categoria TEXT        )    """)    conexao.commit()    print("Tabela recriada com sucesso.")except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao recriar tabela:", erro)
```

Nesse exemplo:

1. A tabela existente é excluída, caso exista.
2. Uma nova tabela é criada.
3. As alterações são confirmadas com `commit()`.

Observe o uso de `rollback()`. Esse método desfaz as alterações ainda não confirmadas quando ocorre um erro durante a transação.



Atenção

&#x20;A exclusão de uma tabela é uma operação destrutiva. Todos os registros existentes serão perdidos. Utilize essa abordagem somente quando realmente desejar reconstruir a tabela.



## **5. CREATE — Inserindo registros**

A operação Create permite inserir novos registros em uma tabela.

Imagine que desejamos cadastrar um produto com os seguintes dados:

- Nome: Teclado.
- Preço: 120.50.
- Disponível: Sim.
- Categoria: Periférico.

Em SQL, utilizamos `INSERT INTO`:

```
INSERT INTO produto (nome, preco, disponivel, categoria)
VALUES ('Teclado', 120.50, 1, 'Periférico');
```

Não precisamos informar o atributo `id`, pois ele é gerado automaticamente.

### **5.1. Inserindo dados com Python**

No Python, devemos utilizar parâmetros na execução dos comandos SQL.

```
nome = "Teclado"preco = 120.50disponivel = 1categoria = "Periférico"cursor.execute("""    INSERT INTO produto (nome, preco, disponivel, categoria)    VALUES (?, ?, ?, ?)""", (nome, preco, disponivel, categoria))
```

Os pontos de interrogação representam os parâmetros que serão substituídos pelos valores da tupla.

A ordem dos valores deve corresponder à ordem dos parâmetros na instrução SQL.

### **5.2. Tratando erros durante a inserção**

Podemos envolver a operação em um bloco `try/except`:

```
try:    cursor.execute("""        INSERT INTO produto (nome, preco, disponivel, categoria)        VALUES (?, ?, ?, ?)    """, (nome, preco, disponivel, categoria))    conexao.commit()    print("Produto cadastrado com sucesso.")except sqlite3.IntegrityError as erro:    conexao.rollback()    print("Erro de integridade:", erro)except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao cadastrar produto:", erro)
```

Observe que utilizamos dois tipos de exceção:

- `sqlite3.IntegrityError`: ocorre quando uma regra de integridade do banco é violada, como uma restrição `NOT NULL`.
- `sqlite3.Error`: representa erros gerais relacionados ao SQLite.

O tratamento específico deve aparecer antes do tratamento mais genérico.

### **5.3. Capturando dados pela interface**

Para solicitar informações ao usuário, utilizamos `input()`.

```
nome = input("Digite o nome do produto: ")preco = float(input("Digite o preço: "))
```

O método `input()` sempre retorna uma string. Por isso, precisamos converter os valores numéricos.

Para um atributo booleano, podemos utilizar uma convenção simples:

```
resposta = input("Está disponível? (s/n): ").lower()disponivel = 1 if resposta == "s" else 0
```

Nesse exemplo, `1` representa verdadeiro e `0` representa falso.

### **5.4. Validando os dados**

Antes de inserir um registro, devemos verificar se os valores informados são válidos.

Por exemplo, um nome não deve estar vazio ou conter apenas espaços.

```
nome = input("Digite o nome: ").strip()if nome == "":    print("O nome não pode ser vazio.")
```

O método `strip()` remove os espaços em branco no início e no final da string.

Para validar valores numéricos, podemos utilizar `try/except`:

```
try:    preco = float(input("Digite o preço: "))except ValueError:    print("Digite um valor numérico válido.")
```

Nesse caso, `ValueError` ocorre quando a conversão não pode ser realizada.

Para validar uma categoria, podemos utilizar uma lista:

```
categorias = ["Periférico", "Computador", "Acessório"]categoria = input("Digite a categoria: ").strip()if categoria not in categorias:    print("Categoria inválida.")
```

Assim, somente os valores previamente definidos serão aceitos.

## **6. READ — Consultando registros**

A operação Read permite recuperar informações armazenadas no banco de dados.

Para consultar todos os produtos, utilizamos:

```
SELECT * FROM produto;
```

O caractere `*` indica que desejamos recuperar todas as colunas.

No Python:

```
cursor.execute("SELECT * FROM produto")
```

A execução realiza a consulta, mas ainda precisamos recuperar os resultados.

### **6.1. Recuperando todos os registros**

Para recuperar todos os registros retornados, utilizamos `fetchall()`:

```
registros = cursor.fetchall()
```

O método retorna uma lista contendo os registros encontrados.

Podemos percorrer essa lista com `for`:

```
for registro in registros:    print(registro)
```

Cada registro normalmente será representado por uma tupla.

Exemplo de resultado:

```
(1, 'Teclado', 120.5, 1, 'Periférico')
(2, 'Monitor', 850.0, 1, 'Computador')
```

### **6.2. Consultando um único registro**

Quando desejamos recuperar apenas um registro, utilizamos `fetchone()`.

```
cursor.execute(    "SELECT * FROM produto WHERE id = ?",    (1,))registro = cursor.fetchone()
```

O comando `WHERE` estabelece uma condição para filtrar os resultados.

Se nenhum registro corresponder à condição, `fetchone()` retornará `None`.

Por isso, precisamos verificar o resultado:

```
if registro is not None:    print(registro)else:    print("Produto não encontrado.")
```

### **6.3. Tratando erros durante consultas**

As consultas também podem gerar erros, por exemplo, quando uma tabela não existe.

```
try:    cursor.execute("SELECT * FROM produto")    registros = cursor.fetchall()    for registro in registros:        print(registro)except sqlite3.Error as erro:    print("Erro ao consultar produtos:", erro)
```

O tratamento permite identificar problemas na consulta sem interromper inesperadamente a aplicação.

### **6.4. Consultando registros por categoria**

Podemos utilizar `WHERE` para recuperar somente os registros de uma categoria específica:

```
cursor.execute(    "SELECT * FROM produto WHERE categoria = ?",    ("Periférico",))registros = cursor.fetchall()
```

Somente os produtos classificados como periféricos serão retornados.

### **6.5. Contando registros**

A função SQL `COUNT()` permite contar a quantidade de registros.

```
SELECT COUNT(*) FROM produto;
```

No Python:

```
try:    cursor.execute("SELECT COUNT(*) FROM produto")    quantidade = cursor.fetchone()[0]    print("Quantidade de produtos:", quantidade)except sqlite3.Error as erro:    print("Erro ao contar produtos:", erro)
```

O índice `[0]` acessa o primeiro valor da tupla retornada.

### **6.6. Agrupando registros por categoria**

A cláusula `GROUP BY` permite agrupar registros que possuem o mesmo valor em determinado atributo.

```
SELECT categoria, COUNT(*)
FROM produto
GROUP BY categoria;
```

O resultado apresenta cada categoria e a quantidade de produtos pertencentes a ela.

No Python:

```
try:    cursor.execute("""        SELECT categoria, COUNT(*)        FROM produto        GROUP BY categoria    """)    registros = cursor.fetchall()    for categoria, quantidade in registros:        print(categoria, quantidade)except sqlite3.Error as erro:    print("Erro ao agrupar produtos:", erro)
```

Essa consulta é útil para relatórios e estatísticas.

## **7. UPDATE — Atualizando registros**

A operação Update permite modificar os valores de registros existentes.

Imagine que o preço de um produto foi alterado.

Em SQL, utilizamos o comando `UPDATE`:

```
UPDATE produto
SET preco = 150.00
WHERE id = 1;
```

O comando `SET` define quais atributos serão modificados.

O `WHERE` determina quais registros serão atualizados.



Atenção

&#x20;Nunca execute um `UPDATE` sem avaliar a condição `WHERE`. Sem ela, todos os registros da tabela poderão ser modificados.



### **7.1. Atualizando dados com Python**

```
novo_preco = 150.00identificador = 1try:    cursor.execute("""        UPDATE produto        SET preco = ?        WHERE id = ?    """, (novo_preco, identificador))    conexao.commit()    if cursor.rowcount > 0:        print("Produto atualizado com sucesso.")    else:        print("Produto não encontrado.")except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao atualizar produto:", erro)
```

O atributo `rowcount` informa quantas linhas foram afetadas pela última operação.

### **7.2. Atualizando vários atributos**

Também podemos modificar vários atributos em uma única instrução:

```
try:    cursor.execute("""        UPDATE produto        SET nome = ?, preco = ?, categoria = ?        WHERE id = ?    """, ("Teclado Mecânico", 250.00, "Periférico", 1))    conexao.commit()    print("Atualização realizada.")except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao atualizar:", erro)
```

Nesse exemplo, nome, preço e categoria serão atualizados para o produto identificado pelo `id`.

## **8. DELETE — Excluindo registros**

A operação Delete permite remover registros de uma tabela.

Para excluir um produto específico, utilizamos:

```
DELETE FROM produto
WHERE id = 1;
```

A condição `WHERE` garante que somente o produto com identificador `1` seja excluído.

### **8.1. Excluindo dados com Python**

```
identificador = 1try:    cursor.execute(        "DELETE FROM produto WHERE id = ?",        (identificador,)    )    conexao.commit()    if cursor.rowcount > 0:        print("Produto excluído com sucesso.")    else:        print("Produto não encontrado.")except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao excluir produto:", erro)
```

### **8.2. Excluindo registros por categoria**

Também podemos excluir todos os registros que possuem determinada categoria:

```
DELETE FROM produto
WHERE categoria = 'Periférico';
```

No Python:

```
categoria = "Periférico"try:    cursor.execute(        "DELETE FROM produto WHERE categoria = ?",        (categoria,)    )    quantidade = cursor.rowcount    conexao.commit()    print("Quantidade de registros excluídos:", quantidade)except sqlite3.Error as erro:    conexao.rollback()    print("Erro ao excluir registros:", erro)
```

Nesse exemplo, todos os produtos classificados como periféricos serão excluídos.

### **8.3. Excluindo todos os registros**

Se desejarmos excluir todos os registros de uma tabela, podemos utilizar:

```
DELETE FROM produto;
```

Esse comando remove os registros, mas mantém a estrutura da tabela.

Não confunda:

| Comando                        | Resultado                               |
| ------------------------------ | --------------------------------------- |
| `DELETE FROM produto`          | Exclui os registros da tabela.          |
| `DROP TABLE produto`           | Exclui a tabela e seus registros.       |
| `DROP TABLE IF EXISTS produto` | Exclui a tabela somente se ela existir. |

## **9. Diferença entre erros do Python e erros do SQLite**

Durante o desenvolvimento, é importante compreender que nem todos os erros possuem a mesma origem.

Por exemplo, considere:

```
preco = float(input("Digite o preço: "))
```

Se o usuário digitar `abc`, ocorrerá um `ValueError`, pois o Python não conseguirá converter o texto para número.

Já na execução de uma instrução SQL, podemos encontrar erros relacionados ao SQLite:

```
try:    cursor.execute("SELECT * FROM tabela_inexistente")except sqlite3.Error as erro:    print("Erro no banco de dados:", erro)
```

Nesse caso, a tabela não existe e o SQLite gera uma exceção.

Portanto, devemos tratar as exceções de acordo com sua origem.

| Exceção                    | Situação comum                                                  |
| -------------------------- | --------------------------------------------------------------- |
| `ValueError`               | Conversão de texto para número inválida.                        |
| `TypeError`                | Operação com tipos incompatíveis.                               |
| `sqlite3.IntegrityError`   | Violação de uma restrição de integridade.                       |
| `sqlite3.OperationalError` | Problemas na execução de comandos SQL, como tabela inexistente. |
| `sqlite3.Error`            | Erros gerais relacionados ao SQLite.                            |

## **10. Organizando as operações em funções**

Uma boa prática é organizar cada operação CRUD em uma função específica.

Isso evita repetição de código e facilita a manutenção.

Podemos imaginar as seguintes funções:

```
def criar_tabela():    passdef excluir_tabela():    passdef inserir_produto():    passdef listar_produtos():    passdef atualizar_produto():    passdef excluir_produto():    pass
```

O comando `pass` é um marcador temporário utilizado enquanto a implementação da função ainda não foi realizada.

Cada função deverá concentrar a lógica de uma operação específica.

### **10.1. Por que utilizar funções?**

Imagine que precisamos cadastrar um produto em diferentes partes do sistema.

Se toda a lógica estiver escrita diretamente na interface, teremos que repetir os mesmos comandos em diferentes locais.

Quando criamos uma função específica, podemos reutilizá-la sempre que necessário.

Além disso, funções facilitam a identificação de erros e a realização de testes.

## **11. Separação de responsabilidades em camadas**

Em aplicações maiores, é interessante separar o código em módulos com responsabilidades diferentes.

Uma possibilidade é utilizar a arquitetura em camadas:

| Camada    | Responsabilidade                                  |
| --------- | ------------------------------------------------- |
| Entity    | Representar os dados e atributos da entidade.     |
| DAO       | Executar comandos SQL e acessar o banco de dados. |
| Service   | Implementar regras de negócio e validações.       |
| Interface | Interagir com o usuário por meio do terminal.     |

Considere o fluxo de um cadastro:

1. A Interface solicita os dados ao usuário.
2. A Interface encaminha os dados para a Service.
3. A Service verifica se os dados são válidos.
4. A Service solicita à DAO a inserção do registro.
5. A DAO executa o comando SQL.
6. O resultado retorna para a Interface.
7. A Interface apresenta uma mensagem ao usuário.

A mesma organização pode ser utilizada nas operações de consulta, atualização e exclusão.

### **11.1. Responsabilidade do tratamento de exceções**

O tratamento de exceções também deve respeitar a separação de responsabilidades.

Uma sugestão de organização:

- **Interface:** trata erros de entrada do usuário, como conversões numéricas inválidas.
- **Service:** valida regras de negócio e decide como reagir a situações inválidas.
- **DAO:** trata erros relacionados à execução de comandos SQL e ao acesso ao banco de dados.

Por exemplo, a DAO pode identificar que uma operação SQL falhou e comunicar o erro à Service. A Service, por sua vez, pode encaminhar uma mensagem adequada para a Interface.

Não é necessário apresentar ao usuário mensagens técnicas detalhadas do SQLite. Essas informações são mais úteis para depuração e registro de erros.

## **12. Boas práticas no desenvolvimento**

Ao desenvolver aplicações CRUD com Python e SQLite, considere as seguintes recomendações:

1. Utilize parâmetros `?` nas instruções SQL.
2. Valide os dados antes de enviá-los ao banco de dados.
3. Utilize `commit()` para confirmar alterações.
4. Utilize `rollback()` quando precisar desfazer uma transação que falhou.
5. Utilize `try/except` para tratar exceções.
6. Utilize `finally` quando precisar garantir a liberação de recursos.
7. Utilize `WHERE` nas operações de atualização e exclusão de registros específicos.
8. Verifique se os registros existem antes de modificá-los ou excluí-los.
9. Utilize funções para organizar as operações.
10. Mantenha os comandos SQL na camada DAO.
11. Concentre as regras de negócio na camada Service.
12. Evite misturar a interação com o usuário e os comandos SQL.
13. Tenha cuidado com `DROP TABLE`, pois essa instrução elimina a tabela e todos os seus registros.


## **Erros mais comuns ao utilizar SQL com Python**

Ao desenvolver aplicações que utilizam Python e SQLite, é comum encontrar erros relacionados à escrita dos comandos SQL, à manipulação dos dados e à comunicação entre o programa e o banco de dados. Conhecer esses erros ajuda a identificá-los e corrigi-los com mais facilidade.

### **1. Esquecer de criar o cursor**

O cursor é o objeto responsável por executar comandos SQL por meio da conexão com o banco de dados. Um erro comum é tentar executar um comando diretamente na conexão, utilizando um método que pertence ao cursor.

```
conexao = sqlite3.connect("banco.db")cursor = conexao.cursor()cursor.execute("SELECT * FROM aluno")
```

**Como evitar:** depois de estabelecer a conexão, crie um cursor com `conexao.cursor()` e utilize `cursor.execute()` para executar os comandos SQL.

### **2. Esquecer de confirmar as alterações com&#x20;**`commit()`

Comandos como `INSERT`, `UPDATE` e `DELETE` modificam os dados armazenados. Um erro comum é executar esses comandos e não confirmar as alterações.

```
cursor.execute(    "INSERT INTO aluno (nome) VALUES (?)",    ("Maria",))conexao.commit()
```

**Como evitar:** utilize `conexao.commit()` depois de operações que alteram os dados, garantindo que as modificações sejam confirmadas no banco.

### **3. Não utilizar parâmetros nos comandos SQL**

Um erro comum é montar comandos SQL concatenando textos e variáveis. Essa prática pode causar problemas quando os dados possuem aspas e também abre espaço para ataques de injeção de SQL.

**Forma inadequada:**

```
nome = input("Nome: ")sql = "INSERT INTO aluno (nome) VALUES ('" + nome + "')"cursor.execute(sql)
```

**Forma recomendada:**

```
nome = input("Nome: ")cursor.execute(    "INSERT INTO aluno (nome) VALUES (?)",    (nome,))
```

**Como evitar:** utilize `?` como marcador de parâmetro e passe os valores em uma tupla. Mesmo quando houver apenas um parâmetro, é necessário colocar a vírgula depois do valor: `(nome,)`.

### **4. Informar uma quantidade incorreta de parâmetros**

A quantidade de valores fornecidos ao comando SQL deve corresponder à quantidade de marcadores `?`.

**Exemplo de erro:**

```
cursor.execute(    "INSERT INTO aluno (nome, idade) VALUES (?, ?)",    ("Maria",))
```

Nesse exemplo, o comando espera dois valores, mas recebeu apenas um.

**Forma correta:**

```
cursor.execute(    "INSERT INTO aluno (nome, idade) VALUES (?, ?)",    ("Maria", 20))
```

**Como evitar:** confira se a quantidade de marcadores `?` corresponde à quantidade de valores passados ao método `execute()`.

### **5. Escrever incorretamente o comando SQL**

Erros de digitação na instrução SQL são bastante comuns. Por exemplo, utilizar `INSER` em vez de `INSERT`, esquecer uma vírgula ou escrever incorretamente o nome de uma tabela ou coluna.

**Exemplo de erro:**

```
cursor.execute("SELEC * FROM aluno")
```

**Forma correta:**

```
cursor.execute("SELECT * FROM aluno")
```

**Como evitar:** revise a sintaxe SQL e confira se os nomes das tabelas e colunas correspondem exatamente aos definidos na criação do banco de dados.

### **6. Tentar inserir dados em uma tabela que não existe**

Se a tabela ainda não foi criada, comandos como `INSERT`, `SELECT`, `UPDATE` e `DELETE` podem gerar erros.

```
cursor.execute(    "INSERT INTO aluno (nome) VALUES (?)",    ("Maria",))
```

Se a tabela `aluno` não existir, o SQLite apresentará um erro indicando que ela não foi encontrada.

**Como evitar:** garanta que o processo de instalação do banco de dados seja executado antes de utilizar as operações de manipulação dos registros.

### **7. Confundir&#x20;**`CREATE TABLE`**&#x20;com&#x20;**`CREATE TABLE IF NOT EXISTS`

Esses comandos possuem comportamentos diferentes.

```
CREATE TABLE aluno (
    id INTEGER PRIMARY KEY,
    nome TEXT
);
```

Se a tabela já existir, o comando gera um erro.

Já o comando:

```
CREATE TABLE IF NOT EXISTS aluno (
    id INTEGER PRIMARY KEY,
    nome TEXT
);
```

Cria a tabela somente se ela ainda não existir. Se já existir, mantém a tabela e seus dados, sem recriá-la.

**Como evitar:** escolha o comando de acordo com o objetivo. Para preservar uma tabela existente, utilize `CREATE TABLE IF NOT EXISTS`. Para recriá-la do zero, utilize primeiro `DROP TABLE IF EXISTS` e depois `CREATE TABLE`.

### **8. Esquecer de utilizar&#x20;**`fetchone()`**&#x20;ou&#x20;**`fetchall()`**&#x20;no SELECT**

O comando `SELECT` consulta os dados, mas o resultado precisa ser recuperado para que o programa possa utilizá-lo.

```
cursor.execute("SELECT * FROM aluno")alunos = cursor.fetchall()for aluno in alunos:    print(aluno)
```

Os métodos mais comuns são:

- `fetchone()`: recupera apenas um registro do resultado.
- `fetchall()`: recupera todos os registros do resultado.

**Como evitar:** depois de executar um `SELECT`, utilize um desses métodos para obter os registros consultados.

### **9. Tentar acessar um registro inexistente**

Ao utilizar `fetchone()`, o resultado será `None` quando a consulta não encontrar nenhum registro. Tentar acessar uma posição desse resultado causará um erro.

**Exemplo de erro:**

```
cursor.execute(    "SELECT * FROM aluno WHERE id = ?",    (10,))aluno = cursor.fetchone()print(aluno[1])
```

**Forma correta:**

```
cursor.execute(    "SELECT * FROM aluno WHERE id = ?",    (10,))aluno = cursor.fetchone()if aluno is not None:    print(aluno[1])else:    print("Aluno não encontrado.")
```

**Como evitar:** sempre verifique se o resultado da consulta é diferente de `None` antes de acessar seus campos.

### **10. Utilizar&#x20;**`UPDATE`**&#x20;ou&#x20;**`DELETE`**&#x20;sem a cláusula WHERE**

A cláusula `WHERE` define quais registros serão modificados ou excluídos. Esquecê-la pode causar alterações em todos os registros da tabela.

**Exemplo perigoso:**

```
DELETE FROM aluno;
```

Esse comando exclui todos os registros da tabela `aluno`.

**Exemplo correto:**

```
cursor.execute(    "DELETE FROM aluno WHERE id = ?",    (10,))conexao.commit()
```

Nesse caso, somente o registro com `id = 10` será excluído.

**Como evitar:** antes de executar comandos `UPDATE` ou `DELETE`, confira se a cláusula `WHERE` está presente quando a intenção for modificar ou excluir registros específicos.

### **11. Esquecer de fechar a conexão com o banco de dados**

Manter conexões abertas sem necessidade pode consumir recursos e dificultar o gerenciamento do banco de dados.

Uma forma de evitar esse problema é utilizar `try`, `except` e `finally`:

```
conexao = Nonetry:    conexao = sqlite3.connect("banco.db")    cursor = conexao.cursor()    cursor.execute("SELECT * FROM aluno")    alunos = cursor.fetchall()    for aluno in alunos:        print(aluno)except sqlite3.Error as erro:    print("Erro no banco de dados:", erro)finally:    if conexao is not None:        conexao.close()
```

**Como evitar:** feche a conexão ao terminar de utilizá-la, preferencialmente em um bloco `finally`, para garantir que o fechamento aconteça mesmo quando ocorrer um erro.

### **12. Não tratar exceções durante a execução dos comandos SQL**

Um comando SQL pode falhar por diversos motivos: tabela inexistente, coluna incorreta, tipo de dado incompatível, violação de chave primária ou erro de sintaxe.

O Python permite tratar esses problemas utilizando `try` e `except`.

```
try:    cursor.execute(        "INSERT INTO aluno (nome) VALUES (?)",        ("Maria",)    )    conexao.commit()except sqlite3.Error as erro:    print("Não foi possível executar a operação:", erro)
```

**Como evitar:** utilize `try/except` nas operações que podem gerar erros, apresentando mensagens compreensíveis ao usuário. Durante o desenvolvimento, também é importante observar a mensagem original da exceção para identificar a causa do problema.

### **Recomendações gerais**

Antes de concluir uma operação com o banco de dados, confira:

- A conexão com o banco de dados foi estabelecida?
- O cursor foi criado corretamente?
- A tabela e as colunas utilizadas realmente existem?
- A sintaxe do comando SQL está correta?
- A quantidade de parâmetros corresponde aos marcadores `?`?
- Os valores foram passados como parâmetros, sem concatenação de strings?
- As operações de alteração foram confirmadas com `commit()`?
- Os resultados de consultas foram recuperados com `fetchone()` ou `fetchall()`?
- Os resultados foram verificados antes de acessar seus campos?
- A conexão foi fechada ao final da operação?

**Dica:** durante o desenvolvimento, não ignore as mensagens de erro do Python e do SQLite. Elas geralmente indicam o tipo de problema e ajudam a localizar a linha em que ele ocorreu.