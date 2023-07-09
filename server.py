from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_database(data):
    with open('./database/database.txt', 'a') as database_file:
        database_file.write(
            f"\n{data['email']}, {data['subject']}, {data['message']}")


def write_to_csv_database(data):
    with open('./database/database.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data['email'], data['subject'], data['message']])


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/<string:page>')
def show_post(page=None):
    return render_template(page)


@app.route('/submit_form', methods=['POST', "GET"])
def login():
    if (request.method == 'POST'):
        try:
            form_data = request.form.to_dict()
           # write_to_database(form_data)
            write_to_database(form_data)
            return redirect('/')
        except:
            return 'dit not save to database'

    return 'Something went wrong'
