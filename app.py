# import flask
from flask import Flask,session,g
import config
from exts import db,mail
from blueprints import list_bp
from blueprints import user_bp
from flask_migrate import Migrate
from models import UserModel
app = Flask(__name__)
# the config
app.config.from_object(config)
db.init_app(app)


mail.init_app(app)
#the migration of database
migrate = Migrate(app,db)
#import a blueprint
#import a blueprint
app.register_blueprint(list_bp)
app.register_blueprint(user_bp)

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # Bind g to a variable called user whose value is the variable user

            g.user = user
        except:
            g.user =None

#The request is coming -> before_request -> view function -> Template returned from view function -> context_processor

@app.context_processor
def context_processor():
    if hasattr(g,"user"):
        return {"user":g.user}
    else:
        return {}



if __name__ == '__main__':
    app.run()
