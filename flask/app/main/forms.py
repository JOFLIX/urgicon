from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import DataRequired

class UrgiconForm(FlaskForm):

    questions = {'chest_pain': 'Do you have chest pain?',
                 'abdominal_pain': 'Abdominal pain?',
                 'nausea_or_vomiting': 'Nausea or vomiting?',
                 'breathing': 'Shortness of breath or trouble breathing?',
                 'injury': 'Do you have an injury or laceration?',
                 'fever': 'A fever?',
                 'cough': 'A cough, or congestion?',
                 'rash': 'Rash?',
                 'headache': 'Headache?',
                 'back_pain': 'Back pain?' }

    # default field args: label, validators, filters, description, id,
    #                     default, widget, render_kw, _form, _name, _prefix,
    #                     _translations, _meta
    age = IntegerField(label = 'age', description='Enter your age')
    chest_pain = BooleanField(label = 'chest_pain', description = questions['chest_pain'])
    abdominal_pain = BooleanField(label = 'abdominal_pain', description = questions['abdominal_pain'])
    nausea = BooleanField(label = 'nausea_or_vomiting', description = questions['nausea_or_vomiting'])
    breathing = BooleanField('breathing', description = questions['breathing'] )
    injury = BooleanField('injury', description = questions['injury'] )
    fever = BooleanField('fever', description = questions['fever'] )
    cough = BooleanField('cough', description = questions['cough'] )
    rash = BooleanField('rash', description = questions['rash'] )
    headache = BooleanField('headache', description = questions['headache'] )
    back_pain = BooleanField('back_pain', description = questions['back_pain'] )

