from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from wtforms.widgets import TextArea
class VersosForm(Form):
    verso = StringField('Verso', [validators.Length(min=1)], widget=TextArea())
    poema = StringField('Poema', [validators.Length(min=1)])
    verso_posicion = IntegerField('Verso Posicion')
