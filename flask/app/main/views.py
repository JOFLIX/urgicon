from flask import Blueprint, render_template, request
from .forms import UrgiconForm
from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/', methods=["GET","POST"])
def index():
    form = UrgiconForm()
    if request.method == 'GET':
        return render_template('main/homepage.html',form=form, initial=True )
    else:

    # this is stupid but will do for now... refactor later
        chest_pain = form.chest_pain.data
        abdominal_pain = form.abdominal_pain.data
        nausea = form.nausea.data
        breathing = form.breathing.data
        injury = form.injury.data
        headache = form.headache.data
        fever = form.fever.data
        cough = form.cough.data
        rash = form.rash.data
        back_pain = form.back_pain.data
        age = form.age.data
        # if dx  > 4: go to ER call 911
        # if dx == 4: drive to ER
        # if dx == 3: go to Urgent Care
        # if dx == 2: Schedule w physician
        # if dx  < 2: do nothing
        if(chest_pain and age >= 30):
            chest_pain= 4
        dx = (2 * chest_pain +
              4 * abdominal_pain +
              2 * nausea +
              2 * breathing +
              2 * injury +
              2 * headache +
              1 * fever +
              1 * cough +
              1 * rash +
              1 * back_pain)

    return render_template('main/homepage.html', dx=dx, form=form, initial=False)
@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
