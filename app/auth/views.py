from app.auth import bp
from flask import render_template,redirect,session
from app.auth.models.auth import register as registermodel
from app.auth.forms.authf import registerf,loginf
from app import db
@bp.route("/login",methods=["POST","GET"])
def login():
    form = loginf()
    if form.validate_on_submit():
        email = form.email.data
        password= form.password.data
        fetch=registermodel.query.filter_by(email=email,password=password).first()
        if fetch:
            session['email']=email
            session['password']=password
            return redirect('/user/dashboard')
    return render_template('login.html',form=form)

@bp.route("/register",methods=["POST","GET"])
def register():
    form = registerf()
    if form.validate_on_submit():
        fname = form.firstname.data
        lname = form.secondname.data
        email = form.email.data
        password = form.password.data
        obj = None
        if fname and lname and email and password:
            obj = registermodel(fname,lname,email,password)
            db.session.add(obj)
            db.session.commit()
        else:
            return "enter correct data"
        return redirect('/auth/login')
    
    return render_template('register.html',form=form)


