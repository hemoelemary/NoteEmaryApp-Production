from flask import Blueprint

bp = Blueprint("profile",__name__,template_folder='templates/profile')

from app.profile import views