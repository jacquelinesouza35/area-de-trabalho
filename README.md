
# Aplicação Flask para iniciantes

   O projeto Flask para iniciantes é uma aplicação web simples construída usando o framework Flask em Python. Este projeto é ideal para desenvolvedores que estão começando a explorar o mundo do desenvolvimento web e desejam aprender os conceitos fundamentais do Flask.

Recursos do Projeto:

Página Inicial: A aplicação terá uma página inicial que dará as boas-vindas aos usuários e fornecerá uma breve descrição do projeto.

Páginas de Rotas: O projeto incluirá várias páginas de rotas, cada uma representando uma página diferente na aplicação. Os usuários poderão navegar entre essas páginas usando links ou botões.

Modelos de Página: Utilizaremos o sistema de modelos do Flask para criar páginas dinâmicas. Isso permitirá que os desenvolvedores aprendam a renderizar dados nas páginas da web usando variáveis do Python.

Formulários Simples: Implementaremos formulários básicos para coletar informações dos usuários. Os iniciantes poderão aprender como receber e processar dados enviados por meio de formulários.

CSS e Estilo: Adicionaremos estilos básicos às páginas usando CSS. Isso permitirá que os desenvolvedores aprendam como estilizar elementos HTML.

Interatividade: O projeto terá algumas funcionalidades interativas, como botões de clique, que mostrarão informações adicionais na página. Isso permitirá que os iniciantes compreendam como manipular elementos da página usando JavaScript.

Objetivos de Aprendizado:

Entender os conceitos básicos do framework Flask, como rotas, templates e views.
Aprender a criar e renderizar templates HTML usando o Jinja2.
Compreender como lidar com solicitações GET e POST de formulários web.
Adquirir conhecimento sobre a estrutura básica de um aplicativo web e suas interações com o servidor.
Pré-requisitos:

Conhecimento básico de Python.
Familiaridade com conceitos básicos de HTML e CSS será útil, mas não obrigatória.
Este projeto Flask para iniciantes oferece uma introdução prática e amigável ao desenvolvimento web usando o Flask. Ao completar este projeto, os iniciantes estarão bem preparados para explorar projetos web mais complexos e aprofundar seus conhecimentos em desenvolvimento web com Python

##  criando um ambiente de desenvolvimento:

 Primeiro passo:
Preparação do Ambiente no Windows:

```bash
  python -m venv venv
venv\Scripts\activate
```
 No macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
 Segundo passo:
Instalando o Flask

```bash
pip install Flask
```
 Terceiro passo:
Criando o App Flask

```bash
    from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo! Este é o meu primeiro aplicativo Flask.'

if __name__ == '__main__':
    app.run()
``` 
 Quarto passo:
Executando o Aplicativo

```bash
python app.py
```
O servidor Flask será iniciado e você verá algo como:

```bash
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Quinto passo:
Adicionando Mais Rotas e Páginas

```bash

@app.route('/sobre')
def sobre():
    return 'Esta é a página Sobre.'
```
 Sexto passo:
Criando Templates HTML

```bash
<!DOCTYPE html>
<html>
<head>
    <title>Meu Primeiro App Flask</title>
</head>
<body>
    <h1>Olá, mundo! Este é o meu primeiro aplicativo Flask.</h1>
    <p>Visite a <a href="/sobre">página Sobre</a>.</p>
</body>
</html>
```

Atualize a função index do arquivo app.py para renderizar esse template em vez de retornar o texto fixo:

```bash
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return 'Esta é a página Sobre.'

if __name__ == '__main__':
    app.run()
```
Ao acessar:

```bash
 http://127.0.0.1:5000/, você verá o conteúdo do template HTML renderizado
```

## Autores

- [@octokatherine](https://www.github.com/octokatherine)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)


 
