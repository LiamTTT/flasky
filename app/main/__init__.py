from flask import Blueprint

main = Blueprint('main', __name__)  # 必须指定蓝本所在模块和蓝本的名称

from . import views, errors
