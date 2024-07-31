import sqlite3
import click
from flask_sqlalchemy import SQLAlchemy

from flask import current_app, g


def get_db():
    pass
#     if 'db' not in g:
#         # g.db = sqlite3.connect(
#         #     current_app.config['DATABASE'],
#         #     detect_types=sqlite3.PARSE_DECLTYPES
#         # )
#         # g.db.row_factory = sqlite3.Row
#         g.db = SQLAlchemy(current_app)
#     return g.db

    # with current_app.open_resource('schema.sql') as f:
    #     db.executescript(f.read().decode('utf8'))


def init_db():
    g.db = SQLAlchemy(current_app)
    return g.db


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
