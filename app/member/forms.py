from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SavingsForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])

    submit = SubmitField('Save')


class LoanForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])

    duration = StringField('Duration', validators=[DataRequired()])

    reason = TextAreaField('Reason', validators=[DataRequired()])

    submit = SubmitField('Apply')