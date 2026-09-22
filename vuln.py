from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {id}")
    return str(cur.fetchone())

@app.route('/invoice')
def get_invoice():
    invoice_id = request.args.get('id')
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM invoices WHERE id = {invoice_id}")
    return str(cur.fetchone())
