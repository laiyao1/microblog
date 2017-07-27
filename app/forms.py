from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired,Length

class LoginForm(Form):
    name = StringField('Name',validators=[DataRequired(),Length(min=6)])
    password = PasswordField('password',validators=[DataRequired(),Length(min=6)])
    remember_me = BooleanField('Remeber_me',default=False)

if __name__=="__main__":
    print ()