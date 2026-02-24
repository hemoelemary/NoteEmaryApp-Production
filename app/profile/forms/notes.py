from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField

class addnotes(FlaskForm):
    subject = StringField("Subject")
    chapter = StringField("Chapter")    
    content = TextAreaField("Note Content")
    submit = SubmitField('Submit')