from model import Base, add_user, create_user_task
import json
from flask.cli import FlaskGroup
from app import app
from sqlalchemy.exc import IntegrityError

cli = FlaskGroup(app)

@cli.command('reset-db')
def reset_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

@cli.command('fill-users')
def fill_users():
    with open('MOCK_DATA.json') as f:
        mock = json.load(f)
    for i in mock:
        add_user(**i)

@cli.command('fill-tasks')
def fill_tasks():
    with open('tasks.json') as f:
        mock = json.load(f)
    for i in mock:
        try:
            create_user_task(**i)
        except IntegrityError:
            continue

cli()