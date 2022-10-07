from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app

app = create_app()
manager = Manager(app)

manager.add_command("db", MigrateCommand)


@manager.command
def routes():
    print(app.url_map)


@manager.command
def start():
    app.run(host='0.0.0.0', port='5000')


def dispatch():
    manager.run()


if __name__ == "__main__":
    dispatch()
