# web/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class BookForm(FlaskForm):
    img = FileField('表紙',validators=[FileAllowed('png','jpg')])
    title = StringField('書籍', validators=[DataRequired()])
    author = StringField('著者', validators=[DataRequired()])
    genre = SelectField('ジャンル',choices=[('小説','小説'),('経営','経営'),('歴史','歴史'),('ビジネス','ビジネス'),('宗教哲学','宗教哲学'),('自然科学','自然科学'),('社会科学','社会科学'),('工学','工学'),('芸術','芸術'),('言語','言語'),('趣味','趣味'),('その他','その他')])
    date = DateField('読了日', format="%Y-%m-%d")
    submit = SubmitField('登録')