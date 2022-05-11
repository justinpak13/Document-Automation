from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length


class InputForm(FlaskForm):
    deal_name = StringField('Deal Name', validators=[DataRequired(), Length(min=2,max=50)]) 
    manager_name = StringField('Manager Name', validators=[DataRequired(), Length(min=2,max=50)])
    some_specific_word = StringField('Some Specific Word', validators=[DataRequired(), Length(min=2,max=50)])
    date = DateField('Date',validators= [DataRequired()])

    submit = SubmitField("Submit")