from portfolio import *  # # __init__ file


@app.route("/")
def index():
    return render_template('index.html')

@app.get('/projetos/list')
def listar_projetos():
    return 'listando projetos'
