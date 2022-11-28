import wtforms
from wtforms.validators import length,email,EqualTo,InputRequired
from models import EmailCaptchaModel,UserModel



# check the public of a task
class IssueForm(wtforms.Form):
    module_title = wtforms.StringField(validators=[length(min=1, max=200)])
    assessment_title = wtforms.StringField(validators=[length(min=1, max=200)])
    description = wtforms.StringField(validators=[length(min=1)])
    due_time = wtforms.StringField(validators=[length(min=1)])
    # status = wtforms.StringField(validators=[length(min=0)])

# check the login
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[length(min=5,max=20,message="密码格式错误")])

# check the registration
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3,max=20,message="用户名格式错误")])
    email = wtforms.StringField(validators=[email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[length(min=4,max=4,message="验证码格式错误")])
    password = wtforms.StringField(validators=[length(min=6,max=20,message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # check whether captcha is correct
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("Email verification code error!")

    # check the email exits
    def validate_email(self, field):
        email = field.data
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model :
            raise wtforms.ValidationError("Email already exists！")




