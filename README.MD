# **Requisitos da avaliação prática**

## **Primeiro dia**

### **Requisito 1 — Instalação e preparação do banco de dados**

Cada estudante deverá implementar, no arquivo `install.py`, um programa de instalação da tabela da sua entidade no banco de dados e popular com 5 linhas preenchidas desta entidade como exemplos de uso.

O instalador deverá:

1. Verificar se a tabela correspondente à sua entidade existe e, caso exista, apagá-la.
2. Criar novamente a tabela da sua entidade, contendo os quatro atributos definidos para ela e a chave primária `id`. Os quatro atributos deve ser do tipo string, integer, booleano e um campo de tipo de entidade baseado em string.
3. Inserir cinco registros iniciais na tabela, utilizando valores coerentes com os atributos e tipos definidos.
4. Garantir que a execução do instalador recrie a estrutura e os cinco registros iniciais, substituindo os dados anteriores.

### **Requisito 2 — Cadastro de registros**

Cada aluno deverá implementar a funcionalidade de cadastro de registros para sua entidade.

A funcionalidade deverá:

1. Solicitar ao usuário os valores dos quatro atributos da sua entidade.
2. Permitir que o usuário digite livremente o valor do seu atributo do tipo string.
3. Solicitar o valor do seu atributo contábil.
4. Solicitar o valor do seu atributo booleano.
5. Solicitar o valor do seu atributo do tipo categoria, permitindo que o usuário digite uma das três opções previamente definidas para sua entidade. Não deverá ser utilizado menu de seleção.
6. Validar se o atributo string não está vazio ou preenchido apenas com espaços.
7. Validar se o valor digitado para o atributo de categoria corresponde exatamente a uma das três opções permitidas, rejeitando valores incorretos ou com erros de digitação.
8. Persistir o registro no banco de dados e informar ao usuário se o cadastro foi realizado com sucesso.


# Entidades
Paulo. pesquisador - nome(string), idade(integer), ativo(boolean), especialidade (string)
Vpantaleao. Dinossauro - nome str, idade str, carnívoro bool, espécie str
Daniel. habitat - nome str, capacidade int, seguro bool, bioma str