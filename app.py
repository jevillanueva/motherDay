import re
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from configuration import Configuration
from flask_basicauth import BasicAuth

from versos_form import VersosForm
from versos_service import registrar_verso
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

if __name__ == '__main__':
    app.run(debug=Configuration.APP_DEBUG)

    