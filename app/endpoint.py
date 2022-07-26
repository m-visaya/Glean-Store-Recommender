from flask import request, abort
from app import app, utils

import os

@app.route('/', methods=['GET','POST'])
def index():
    if request.headers.get("Token") == os.environ.get("Token"):
        if request.method == 'GET':
            return "Glean Store Recommender: running"
        elif request.method == 'POST':
            return utils.get_recommendations(int(request.form['product_id']))
    else:
        abort(401)