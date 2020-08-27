from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            write_to_file(data)
            return redirect('thankyou.html')
        except:
            return 'Something went wrong! Please try again.'
        else:
            return 'Something went wrong! Please try again.'
