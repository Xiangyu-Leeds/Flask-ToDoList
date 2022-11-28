from flask import Blueprint, render_template, request, flash, redirect, url_for,g,session
from models import EventModel
from exts import db
from .forms import IssueForm
from datetime import datetime


# the blueprint
bp = Blueprint("list", __name__, url_prefix="/")


# public a task
@bp.route("/issue", methods=['GET', 'POST'])
def issue():
    # check method
    if request.method == 'GET':
        return render_template("upload.html")
    else:
        form = IssueForm(request.form)
        # get the information
        if form.validate():
            title1 = form.module_title.data
            title2 = form.assessment_title.data
            content = form.description.data
            time = form.due_time.data
            year = time[0:4]
            month = time[5:7]
            day = time[8:10]
            trash = 0
            important=0
            if int(year) > datetime.now().year:
                status = 0
            elif int(year) < datetime.now().year:
                status = 2
            else:
                if int(month) < datetime.now().month:
                    status = 2
                elif int(month) > datetime.now().month:
                    status = 0
                else:
                    if int(day) < datetime.now().day:
                        status = 2
                    else:
                        status = 0
        event = EventModel(module_title=title1, assessment_title=title2, description=content,
                               due_year=year,
                               due_month=month, due_day=day,status=status,trash=trash,important=important,author_id=g.user.id)
        try:
            # add the new task to database
            db.session.add(event)
            # commit the new database
            db.session.commit()
        except Exception as error:
            # the rollback of the database
            db.session.rollback()
        else:
            return redirect("/index")




# modify a task
@bp.route("/modified", methods=['GET', 'POST'])
def modified():
    m = EventModel.query.filter_by(id=request.args.get("id"))[0]
    # check the method
    if request.method == 'GET':
        return render_template("index.html", events=EventModel.query.filter_by(status=0))
    else:
        form = IssueForm(request.form)
        # check the modification is correct
        if form.validate():
            m.module_title = form.module_title.data
            m.assessment_title = form.assessment_title.data
            m.description = form.description.data
            time = form.due_time.data

            m.due_year = time[0:4]
            m.due_month =time[5:7]
            m.due_day =time[8:10]
            if int(m.due_year) > datetime.now().year:
                m.status = 0
            elif int(m.due_year) < datetime.now().year:
                m.status = 2
            else:
                if int(m.due_month) < datetime.now().month:
                    m.status = 2
                elif int(m.due_month) > datetime.now().month:
                    m.status = 0
                else:
                    if int(m.due_day) < datetime.now().day:
                        m.status = 2
                    else:
                        m.status = 0
            # commit the database
            db.session.commit()
            return  render_template("index.html",events = EventModel.query.filter_by(status=0,trash=0,important=0,author_id=g.user.id))



@bp.route("/delete")
def delete():
    # delete a task
    EventModel.query.filter_by(id=request.args.get("id")).delete()
    db.session.commit()

@bp.route("/important")
def important():
    # put a task into important
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    event.important = 1
    db.session.commit()

@bp.route("/delete1")
def delete1():
    # put a task into trash
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    event.trash = 1
    db.session.commit()

@bp.route("/trash")
def trash():
    # return the trash
    events = EventModel.query.filter_by(trash=1,author_id=g.user.id).order_by(db.text("create_time")).all()
    return render_template("trash.html", events=events)

@bp.route("/show_important")
def show_important():
    # show important tasks
    events = EventModel.query.filter_by(important=1,trash=0,author_id=g.user.id).order_by(db.text("create_time")).all()
    return render_template("important.html", events=events)

@bp.route("/modify")
def modify():
    # return to midify
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    return render_template("modify.html", event=event)

@bp.route("/recover")
def recover():
    # recover a task from trash to original
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    event.trash=0
    db.session.commit()

@bp.route("/cancel")
def cancel():
    # recover a task from important
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    event.important=0
    db.session.commit()


@bp.route("/completed_issue")
def completed_issue():
    # complete a task
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    event.status = 1
    db.session.commit()
    return ""

@bp.route("/uncompleted_issue")
def uncompleted_issue():
    # uncompleted a task
    event = EventModel.query.filter_by(id=request.args.get("id"))[0]
    if int(event.due_year) < datetime.now().year:
        event.status = 2
    else:
        if int(event.due_month) < datetime.now().month:
            event.status = 2
        else:
            if int(event.due_day) < datetime.now().day:
                event.status = 2
            else:
                event.status = 0
    db.session.commit()
    return ""


@bp.route("/show_completed")
def show_completed():
    #  show completed tasks
    events = EventModel.query.filter_by(status=1,trash=0,important=0,author_id=g.user.id).order_by(db.text("create_time")).all()
    return render_template("completed.html", events=events)

@bp.route("/show_overdue", methods=['GET', 'POST'])
def show_overdue():
    # show overdue tasks
    events1 = EventModel.query.filter_by(status=2,trash=0,important=0,author_id=g.user.id).order_by(db.text("create_time")).all()
    return render_template("overdue.html", events=events1)



@bp.route("/index")
def index():
    # return to index
    events = EventModel.query.filter_by(status=0,trash=0,important=0,author_id=g.user.id).order_by(db.text("create_time")).all()
    return render_template("index.html", events=events)

@bp.route("/")
def logins():
    # return to login
    return render_template("login.html")

@bp.route("/register1")
def register1():
    # return to register
    return render_template("register.html")

@bp.route("/login1")
def login1():
    # return to login from register
    return render_template("login.html")


@bp.route("/echarts")
def echarts():
    # show these two charts
    uncompleted = []
    completed = []
    overdue = []
    important = []
    events1 = EventModel.query.filter_by(status=0,trash=0,important=0, author_id=g.user.id).all()
    for event1 in events1:
        uncompleted.append(event1)
    #     the length of uncompleted tasks
    a = len(uncompleted)
    events2 = EventModel.query.filter_by(status=1,trash=0,important=0, author_id=g.user.id).all()
    for event2 in events2:
        completed.append(event2)
        #     the length of completed tasks
    b = len(completed)
    events3 = EventModel.query.filter_by(status=2,trash=0, important=0,author_id=g.user.id).all()
    for event3 in events3:
        overdue.append(event3)
        #     the length of overduetasks
    c = len(overdue)
    events4 = EventModel.query.filter_by(important=1,trash=0, author_id=g.user.id).all()
    for event4 in events4:
        important.append(event4)
        #     the length of important tasks
    d = len(important)
    return render_template("echarts.html",a=a,b=b,c=c,d=d)

@bp.route("/research")
def research():
    # research a task according to their title and description
    info=request.args.get('info')
    events = EventModel.query.filter(EventModel.module_title.contains(info)).filter_by(author_id=g.user.id,trash=0).all()
    events2 = EventModel.query.filter(EventModel.description.contains(info)).filter_by(author_id=g.user.id,trash=0).all()
    events3 = EventModel.query.filter(EventModel.assessment_title.contains(info)).filter_by(author_id=g.user.id,trash=0).all()

    for event in events2:
        if event not in events:
            events.append(event)
    for event in events3:
        if event not in events:
            events.append(event)
    #         return to search
    return render_template("search.html",events=events)



