from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

''' 将应用的创建挪到工厂函数之中
'''
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 由flask提供的配置函数，只需将想要配置的项写成类的属性
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 路由和错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)  # 当蓝本注册到app上时，定义于蓝本中的路由和错误处理程序才生效

    return app