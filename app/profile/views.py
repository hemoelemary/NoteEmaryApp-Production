from app.profile import bp
from flask import render_template,session,redirect,request
from app.auth.models.auth import register,notes
from app.profile.forms.notes import addnotes
from app import db
import datetime
from sqlalchemy import func


def time_since(past_time):
    now = datetime.datetime.now()
    saved_time = datetime.datetime.strptime(past_time, "%Y-%m-%d %H:%M:%S.%f")

    diff = now - saved_time
    
    seconds = diff.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours ago"
    else:
        return f"{int(seconds // 86400)} days ago"



@bp.route("/profile",methods=["POST","GET"])
def profile():
    form = addnotes()
    email = session['email']
    password= session['password']
    obj=register.query.filter_by(email=email,password=password).first()
    if form.validate_on_submit():
        subject = form.subject.data
        chapter = form.chapter.data
        content = form.content.data
        times = datetime.datetime.now()
        noteobj = notes(subject,chapter,content,obj.id,times)
        db.session.add(noteobj)
        db.session.commit()
        return redirect('/user/dashboard')
    if obj:
        count = 0
        c=set()
        usernotes=notes.query.filter_by(foruser=obj.id).all()
        for i in usernotes:
            count+=1
            c.add(i.subject)
        countsub = 0
        for j in c:
            countsub+=1
        todaydate = str(datetime.datetime.today().date())
        results = db.session.query(notes).filter(notes.time.like(f"{todaydate}%"),notes.foruser==obj.id).all()
        counttodaynotes = 0
        for d in results:
            counttodaynotes+=1
        return render_template('profile.html',name=obj.firstname+" "+obj.lastname,notes=usernotes,email=email,form=form,count=count,countsub=countsub,todaynot=counttodaynotes,subjects=c)



@bp.route('/dashboard')
def dashboard():
    email = session['email']
    password= session['password']
    obj=register.query.filter_by(email=email,password=password).first()
    usernotes=notes.query.filter_by(foruser=obj.id).all()
    time = time_since
    count = 0
    c=set()
    for i in usernotes:
        count+=1
        c.add(i.subject)
    countsub = 0
    for j in c:
        countsub+=1
    todaydate = str(datetime.datetime.today().date())
    results = db.session.query(notes).filter(notes.time.like(f"{todaydate}%"),notes.foruser==obj.id).all()
    counttodaynotes = 0
    for d in results:
        counttodaynotes+=1

    if obj:
        return render_template('home.html',name=obj.firstname+" "+obj.lastname,email=email,usernotes=usernotes,time=time,count=count,countsub=countsub,todaynot=counttodaynotes)
    

@bp.route('/profile/delete/<id>')
def delete(id):
    email = session['email']
    password= session['password']
    obj=register.query.filter_by(email=email,password=password).first()
    usernote=notes.query.filter_by(foruser=obj.id,id=id).first()
    if obj and usernote:
        db.session.delete(usernote)
        db.session.commit()
        return redirect('/user/profile')
    
@bp.route('/admin',methods=["POST","GET"])
def admin():
    if request.method=="POST":
        name = request.form.get("name")
        password=request.form.get('password')
        if name=="ad" and password=="ad":
            print(register.query.all())
            return str(register.query.all())
    return render_template('admin.html')    
