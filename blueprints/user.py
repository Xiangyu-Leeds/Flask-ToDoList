from flask import Blueprint, render_template, request,redirect,url_for,jsonify,session,flash
from exts import mail,db
from flask_mail import Message
from models import UserModel,EmailCaptchaModel
import string
import random
from datetime import datetime
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint("user",__name__,url_prefix="/user")


@bp.route("/login",methods=['GET','POST'])
def login():
    # login a account
    if request.method=='GET':
        return render_template("login.html")
    else:
        # check whether it is correct
        form = LoginForm(request.form)
        if form.validate():
            form = LoginForm(request.form)
            if form.validate():
                email = form.email.data
                password = form.password.data
                user = UserModel.query.filter_by(email=email).first()
                if user and check_password_hash(user.password, password):
                    session['user_id'] = user.id
                    return redirect(url_for("list.index"))
                else:
                    flash("The email address and password do not match")
                    return redirect(url_for("user.login"))
        else:
                flash("Incorrect email or password format!")
                return redirect(url_for("user.login"))




@bp.route("/register",methods=['GET','POST'])
def register():
   #  register a account
   if request.method=="GET":
    return render_template("register.html")
   else:
       # check whether it is correct
       form = RegisterForm(request.form)
       if form.validate():
           email = form.email.data
           username = form.username.data
           password = form.password.data
           # md5("sxy") = sadewjfrwlkfjvgl
           # hash_password = generate_password_hash(password)
           user = UserModel( username=username, password= generate_password_hash(password),email=email)
           try:
               db.session.add(user)
               db.session.commit()

           except Exception as error:
               db.session.rollback()
           else:
               return redirect(url_for("user.login"))
       else:
           flash("Incorrect email or username or password format!")
           return redirect(url_for("user.register"))

@bp.route("/logout")
def logout():
    # Clears all data from the session
    session.clear()
    return redirect(url_for('user.login'))

# memcached/redis/

@bp.route("/captcha",methods=['GET'])
def get_captcha():
    # GET,POST
    email = request.args.get("email")
    letters = string.ascii_letters+string.digits
    captcha = "".join(random.sample(letters,4))
    print(captcha)
    if email:
        message = Message(
            subject="Shen Sir register",
            recipients = [email],
            body=f"The CAPTCHA I gave you is：{captcha},I hope you don't tell anyone!",
            sender = "1534840095@qq.com"
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model =EmailCaptchaModel(email=email,captcha=captcha)
            try:
                db.session.add(captcha_model)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
        # code: 200, successful, normal request
        return jsonify({"code":200})
    else:
        # code: 400, client error
        return jsonify({"code":400,"message":"Please pass the email first!"})


