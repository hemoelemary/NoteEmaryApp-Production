from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField

class registerf(FlaskForm):
    firstname = StringField("First Name: ")
    secondname = StringField("Second Name: ")
    email = EmailField("Email: ")
    password = PasswordField("Password: ")
    sub=SubmitField("Submit")

class loginf(FlaskForm):
    email = EmailField("Email: ")
    password = PasswordField("Password: ")
    sub=SubmitField("Submit")
        

