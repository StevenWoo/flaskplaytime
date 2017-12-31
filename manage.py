import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flaskproject import app, db
from models import TestResult

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

app.debug = True
manager.run()
print('got to here')
if __name__ == '__main__':
    manager.run()
    print('running as manage.py')
