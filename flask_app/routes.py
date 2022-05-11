from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import send_file
from flask_app.forms import InputForm
from flask_app import app
from CreateDocuments import create_document

@app.route('/', methods = ['GET','POST'])
@app.route('/home')
def home():
    form = InputForm()
    if form.validate_on_submit():
        flash("Please Wait. Files Generating",'success')
        document_location = create_document()
        return send_file(f'../{document_location}')
        return redirect(url_for('home'))
    return render_template('form.html', title="home", form=form)