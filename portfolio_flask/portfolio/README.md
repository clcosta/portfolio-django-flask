# Bem vindo ao **Portfolio com o FLASK**!
<p><img height="20" src="https://img.shields.io/badge/Version-1.0-blue"/></p>

Neste arquivo você encontrará todas as especificações do site com o Flask. Como utilizar em servidor, e claro como utilizar todas as funcionalidades.
--
---
## Instalação

1. Primeiramente caso já não tenha feito você pode clonar este repositório.

```
$ git clone https://github.com/clcosta/portfolio-django-flask.git
```

2. Agora a instalação das bibliotecas   
__Com a intenção de diminuir o requirements.txt eu criei uma versão para cada framework, então certifique-se de instalar o requirements do *FLASK* que está neste mesmo diretorio.__

```
pip install -r requirements.txt
```

3. Subir o servidor     
__Como estamos lidando com um site, vamos subir o servidor local, para isso no seu terminal utilize o comando__

```
py app.py
```

 -> __Se tudo estiver certo você ja deve ter acesso ao servidor local com o site carregado__   
*OBS: Por padrão deste repositorio, o modo DEBUG é desativado*.

# Funcionalidades
**Com tudo já instalado e o servidor local rodando o site vamos ver o que podemos fazer.**

Como é esperado em um site de portfolio você tem que mostrar todos os seus projetos, o usuario já na página principal tem que conseguir ver um pouco sobre você e seus projetos. Como não irei upar o meu banco de dados neste repositorio vou refazer todo o passo a passo para upar os projetos no site.   

1. ### Criando o banco de dados
 *vamos utilizar o **SQL Alchemy** mesmo, padrão do flask*   
no terminal digite a seguinte linha de comando:
```
flask db migrate
```
_OBS: Caso faça alguma alteração no model.py será necessário refazer o migrations, você pode consultar neste [link](https://flask-migrate.readthedocs.io/en/latest/)_

__Se não tiver ocorrido nenhum problema, você tera um arquivo novo criado na <ins>pasta portfolio</ins>, chamado <ins>db.db</ins>, ele é o nosso banco de dados.__   

2. ### Obtendo Credenciais
*a unica maneira de criar projetos é por uma **REST API**, que por segurança necessita de uma credencial para funcionar. Eu recomendo criar um arquivo **credentials.json** com a variável <ins>API_KEY</ins>, ou um arquivo **.env** com a mesma variável. Pórem caso queira defini-la manualmente é so entrar no arquivo **portfolio/routes.py***

### credentials.json
```json
{
    "API_KEY": <SEUTOKEN>
}
```

### .env
```
API_KEY = SUA CHAVE AQUI
```
🔻 __Não Mostre sua API_KEY a todos, quem tiver acesso a ela poderá criar, editar, deletar todos os seus projetos__   

3. ### Criando um projeto
*No meu portfolio eu escolhi alguns campos para apresentar o meu projeto, sendo todos eles obrigatorios:*   
 *- Titulo*   
 *- Capa do Projeto (imagem) -> será a imagem que aparecerá na tela quando o mause passar em cima do titulo do projeto*   
 *- Link para um vídeo de apresentação -> será incorporado dentro do site em uma página de detalhes do projeto*   
 *- Link do código no github*   

*Com o banco de dados criado, temos acesso a todos os metodos CRUD por end point da mesma rota do site.*

## End Points

| Função    | End Point               | Token | Método       |
| --------- | ----------------------- | ----- | ------------ |
| Criar     | /projeto/new            | SIM   | POST         |
| Listar    | /projetos               | Não   | GET          |
| Atualizar | /projeto/atualizar/< id >   | SIM   | PATCH, POST  |
| Deletar   | /projeto/deletar/< id >     | SIM   | GET          |

## Token
🔻 __O Token: NÃO__ é uma informação que deve ser pública, só você terá acesso,
o token que está no seu arquivo *credentials.json* tem que ser utilizado em todo *end point* que for necessário o token, acima tem uma tabela com todos eles e quais precisam do token.

### Exemplos:
- ### Listar Projetos
```python
import requests

url = "http://localhost:5000/projetos"

response = requests.get(url)
```

- ### Criar projeto
```python
import requests

data = {
    "titulo":"teste",
    "capa":"capa.png",
    "link_codigo":"github/clcosta",
    "iframe_video":"iframe do meu video"
}

url = "http://localhost:5000/projeto/new/<SEUTOKEN>"

reponse = requests.post(url, data=data)
```
- ### Atualizar Projetos
```python
import requests

url = "http://localhost:5000/projeto/atualizar/1/<SEUTOKEN>"

data = {
    "titulo":"novo teste",
    "capa":"novacapa.png",
    "link_codigo":"github/clcosta/novo",
    "iframe_video":"iframe do meu novo video"
}

response = requests.patch(url, data=data)
```
- ### Deletar Projetos
```python
import requests

url = "http://localhost:5000/projeto/deletar/id/<SEUTOKEN>"

response = requests.get(url)
```

__Agora que já sabe, só ir adicionando os projetos.__
<img align="center" style="margin-left: 10px" height="20" width="20" src="https://www.ifpb.edu.br/relacoes-internacionais/imagens/check-mark-304890_640.png/@@images/41276dba-701d-4071-b23c-c0325bba5228.png" alt="Bluebelt"><br>


--- 

## Detalhes do projeto

Todos os projetos tem uma página de renderização dos seus detalhes, na página principal, depois de ter os projetos adicionado é só clicar no nome do projeto que ela será renderizada.

# Referências

- [Documentação oficial](https://flask.palletsprojects.com/en/2.0.x/)

- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

- [Flask SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

- [Flask build CRUD API](https://www.digitalocean.com/community/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)
