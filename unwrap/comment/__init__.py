from flask import Blueprint

comment_bp = Blueprint('comment', __name__, template_folder='templates', static_folder='static')

from . import routes  # 确保引入 routes 文件
