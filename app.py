import re
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from configuration import Configuration
from flask_basicauth import BasicAuth
from objectIdHelper import JSONEncoder

from versos_form import VersosForm
from versos_service import generator_poema, generator_random_poema, registrar_verso
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = Configuration.APP_BASIC_AUTH_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = Configuration.APP_BASIC_AUTH_PASSWORD

basic_auth = BasicAuth(app)

@app.template_filter('closetaginput')
def close_tag_input(value):
    strings = re.findall( r'<\s*input[^>]*>',value)
    for string in strings:
        fixed = string[0:-1] + '/>'
        value = str(value).replace(string,  fixed)
    return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/versos', methods=['GET', 'POST'])
@basic_auth.required
def versos_view():
    form = VersosForm(request.form)
    if request.method == 'POST' and form.validate():
        registrar_verso(form.verso.data, form.poema.data, form.verso_posicion.data)
        return render_template('versos.html', form=form)
    return render_template('versos.html', form=form)


@app.route('/poema', methods=['GET', 'POST'])
def poema():
    if request.method == 'POST':
        req = request.form
    else:
        req = request.args
    poema = req.get('poema', None)
    user_versos, user_poema , user_complete = generator_poema(poema)
    return jsonify({"poema": user_poema, "versos":user_versos, "full": user_complete })

@app.route('/poema/generator', methods=['GET', 'POST'])
def poema_random():
    if request.method == 'POST':
        req = request.form
    else:
        req = request.args
    versos = req.get('versos', None)
    if versos is None:
        versos = 2
    elif versos.isnumeric():
        versos = int(req.get('versos', 2))
    else:
        versos = 2
    if versos < 0:
        return jsonify({"poema": "", "versos": []})
    
    user_versos, user_poema, user_complete  = generator_random_poema(versos)
    return jsonify({"poema": user_poema, "versos":user_versos, "full": user_complete })

if __name__ == '__main__':
    app.run(debug=Configuration.APP_DEBUG)

    