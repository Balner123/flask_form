# app/routes.py
from flask import render_template, redirect, url_for
from app.models import User
from app.forms import UserForm
from app.database import db

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = UserForm()
        if form.validate_on_submit():
            new_user = User(username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        users = User.query.all()
        return render_template('index.html', form=form, users=users)

    @app.route('/delete/<int:user_id>')
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('index'))