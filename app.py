from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017/')
db = client['form_db']
collection = db['form_data']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']


        data = {'name': name, 'email': email}
        collection.insert_one(data)

        return render_template('data.html', form_data=[data])

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
