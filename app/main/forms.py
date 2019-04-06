from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UrgiconForm(FlaskForm):

    questions = {'chest_pain': 'Do you have chest pain?',
                 'abdominal_pain': 'Abdominal pain?',
                 'nausea': 'Nausea or vomiting?',
                 'breathing': 'Shortness of breath or trouble breathing?',
                 'injury': 'A bruise or cut?',
                 'fever': 'A fever?',
                 'cough': 'A cough, or congestion?',
                 'pain': 'Pain?',
                 'rash': 'Rash?',
                 'headache': 'Headache?',
                 'back_pain': 'Back pain?' }

    # default field args: label, validators, filters, description, id,
    #                     default, widget, render_kw, _form, _name, _prefix,
    #                     _translations, _meta

    chest_pain = BooleanField(label = 'chest_pain', validators=[DataRequired()], \
                              description = questions['chest_pain'])
    abdominal_pain = BooleanField(label = 'abdominal_pain', validators=[DataRequired()], \
                                  description = questions['abdominal_pain'])
    nausea = BooleanField(label = 'nausea', validators=[DataRequired()], \
                          description = questions['nausea'])
    breathing = BooleanField('breathing', validators=[DataRequired()], \
                            description = questions['breathing'] )
    injury = BooleanField('injury', validators=[DataRequired()], \
                            description = questions['injury'] )
    fever = BooleanField('fever', validators=[DataRequired()], \
                            description = questions['fever'] )
    cough = BooleanField('cough', validators=[DataRequired()], \
                            description = questions['cough'] )
    pain = BooleanField('pain', validators=[DataRequired()], \
                            description = questions['pain'] )
    rash = BooleanField('rash', validators=[DataRequired()], \
                            description = questions['rash'] )
    headache = BooleanField('headache', validators=[DataRequired()], \
                            description = questions['headache'] )
    back_pain = BooleanField('back_pain', validators=[DataRequired()], \
                            description = questions['back_pain'] )

