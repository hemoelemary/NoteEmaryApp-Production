from flask import Flask,render_template,redirect,render_template_string
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.auth import bp as authbp
    from app.profile import bp as profilebp

    app.register_blueprint(authbp,url_prefix='/auth')
    app.register_blueprint(profilebp,url_prefix='/user')

    @app.route('/')
    def index():
        return redirect('/auth/login')
    
    @app.errorhandler(500)
    def internal_server_error(error):
        msg = """
        <h1 style='text-align: center;'>
            تقريبًا السيرفر بيواجه مشكلة او جرب تحط بياناتك صح او جرب بعد شوية
        </h1>
        <small style='text-align: center;'>
            <strong>جاري الاصلاح</strong>
        </small>
        """
        return render_template_string(msg)
    
    @app.errorhandler(404)
    def notfound(error):
        msg = """
        <h1 style='text-align: center;'>
           صفحة غير موجودة
        </h1>
        <small style='text-align: center;'>
            <strong>التزم بالفيديو</strong>
        </small>
        """
        return render_template_string(msg)
    
    @app.errorhandler(502)
    def internal_error(error):
        msg = """
        <h1 style='text-align: center;'>
            تقريبًا السيرفر بيواجه مشكلة او جرب تحط بياناتك صح او جرب بعد شوية
        </h1>
        <small style='text-align: center;'>
            <strong>جاري الاصلاح</strong>
        </small>
        """
        return render_template_string(msg)
    
    return app