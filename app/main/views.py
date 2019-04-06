from flask import Blueprint, render_template, request
from .forms import UrgiconForm
from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/', methods=["GET","POST"])
def index():
    form = UrgiconForm()
    if request.method == 'GET':
        return render_template('main/homepage.html',form=form )
    else:
        chest_pain = request.form.get('chest_pain')
        abdominal_pain = request.form.get('abdominal_pain')
        nausea = request.form.get('nausea')
        breathing = request.form.get('breathing')
        injury = request.form.get('injury')
        fever = request.form.get('fever')
        cough = request.form.get('cough')
        pain = request.form.get('pain')
        rash = request.form.get('rash')
        headache = request.form.get('headache')
        back_pain = request.form.get('back_pain')

        dx = 5*chest_pain + 5*abdominal_pain + 3*nausea + 2*breathing + \
            2*injury + fever + cough + rash + 2*headache + back_pain
    return render_template('main/homepage.html', dx=dx, form=form)
@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
