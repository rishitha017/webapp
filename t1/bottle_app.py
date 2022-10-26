
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, get, template
import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/')
def hello_world():
    return 'Hello from Rishitha!'

@route('/hi')
def hi_world():
    return 'Hi from Rishitha!'

@route('/bye')
def bye_world():
    return 'bye from Rishitha!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return "the shopping list is here!: ",str(rows)
    return template("shopping_list.tpl", name="rishitha", shopping_list=rows)


application = default_app()

