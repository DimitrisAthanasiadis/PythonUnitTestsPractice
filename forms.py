from wtforms import Form, SubmitField
from wtforms.fields import StringField


class SimpleForm(Form):
    text1 = StringField("Field 1")
    text2 = StringField("Field2")
    submit = SubmitField("Submit")
