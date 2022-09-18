import os

from flask_migrate import Migrate
from apps import create_app, db
from apps.users.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
migrate = Migrate(app, db)


@app.shell_context_processor
def create_shell_context():
    return {"db": db, "User": User}


@app.cli.command("createsuperuser")
def create_user():
    user = User(username=os.environ.get("BLOG_USERNAME"),\
                email=os.environ.get("BLOG_ADMIN"), is_admin=True)
    user.hash_password = os.environ.get("BLOG_PASSWORD")
    db.session.add(user)
    db.session.commit()
    print("user created successfully")



@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
