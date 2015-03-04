from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    #Mostra el nom del usuari
    return 'Perfil de %s' % username

@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    #Mostra el nombre del post de la url
    return 'ID del post : %d' % post_id

@app.route('/flotants/<float:nombre>')
def show_float_number(nombre):
    #Mostra el nombre decimal de la url
    return 'El nombre es: %f' % nombre
    
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()
