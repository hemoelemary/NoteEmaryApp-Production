from app import db



class register(db.Model):
    __tablename__='register'
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    email = db.Column(db.Text,unique=True)
    password = db.Column(db.Text)
    #one to many
    notes=db.relationship('notes',backref='register')
    __table_args__ = (
        db.UniqueConstraint('email', name='uq_register_email'),
    )
    def __init__(self,firstname,lastname,email,password):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=password
    def __repr__(self):
        return f"{self.firstname+self.lastname} email:{self.email} password:{self.password}"

class notes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.Text)
    chapter = db.Column(db.Text)
    content = db.Column(db.Text)
    foruser = db.Column(db.Integer,db.ForeignKey('register.id'))
    time = db.Column(db.Text)
    def __init__(self,subject,chapter,content,foruser,time):
        self.subject=subject
        self.chapter=chapter
        self.content=content
        self.foruser=foruser
        self.time=time        
    
    
    