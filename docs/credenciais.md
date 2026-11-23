# Tutorial: Como remover as credenciais do GitHub do Windows

Se você deseja remover as credenciais do GitHub salvas no Windows, como usuário, senha, Personal Access Token (PAT) ou autenticação via Git Credential Manager, siga os passos abaixo.

Existem três maneiras de fazer isso.

## 1. Remover as credenciais pelo Gerenciador de Credenciais do Windows

Método recomendado1. Pressione `Win + R` no teclado.
2. Digite o comando:
   text
   ```text
   control /name Microsoft.CredentialManager
   ```
3. Pressione Enter.
4. Clique em Credenciais do Windows.
5. Procure por entradas relacionadas ao GitHub, como:
   - `git:https://github.com`
   - `github.com`
   - `Git Credential Manager`
6. Clique na credencial desejada.
7. Selecione Remover.
8. Confirme a exclusão.

GitHub credentials in university labs - BMEVIAUMB00 and BMEVIAUMB09 Business Intelligence Laboratory

![](images/git-credential-remove.png)

Pronto\! As credenciais selecionadas foram removidas do Windows.

## 2. Remover as credenciais pelo terminal (CMD ou PowerShell)

Você também pode remover as credenciais utilizando o terminal.

Passo 1: Abra o CMD ou PowerShell.

Passo 2: Execute o seguinte comando:

bash

```bash
cmdkey /list
```

Esse comando lista as credenciais armazenadas no Windows.

Passo 3: Procure entradas relacionadas ao GitHub.

Por exemplo:

text

```text
Target: LegacyGeneric:target=git:https://github.com
```

Passo 4: Remova a credencial utilizando:

bash

```bash
cmdkey /delete:LegacyGeneric:target=git:https://github.com
```

O nome informado depois de `/delete:` deve corresponder exatamente ao Target exibido pelo comando `cmdkey /list`.

## 3. Remover as credenciais pelo Git Credential Manager

Se você utiliza o Git Credential Manager, pode remover as credenciais diretamente pelo Git.

Abra o terminal e execute:

bash

```bash
echo "protocol=https host=github.com" | git credential reject
```

Esse comando solicita ao gerenciador de credenciais que descarte a autenticação armazenada para `github.com`.

## 4. Fazer login novamente no GitHub

Depois de remover as credenciais, tente executar:

bash

```bash
git fetch
```

ou:

bash

```bash
git push
```

O Git deverá solicitar uma nova autenticação, dependendo do método de autenticação configurado.

## Resumo dos comandos

| Objetivo | Comando |
| --- | --- |
| Listar credenciais do Windows | `cmdkey /list` |
| Remover credencial do GitHub | `cmdkey /delete:NOME_DA_CREDENCIAL` |
| Remover credencial pelo Git | `git credential reject` |
| Atualizar referências remotas | `git fetch` |


Observação: remover as credenciais do Windows não exclui sua conta GitHub, não apaga repositórios locais e não revoga automaticamente os tokens na sua conta GitHub. Se você suspeita que um token foi comprometido, revogue-o também em GitHub → Settings → Developer settings → Personal access tokens.