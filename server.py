from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')


# def write_to_csv(data):
#     with open('database.csv', mode='a', newline='') as database2:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])


# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect('/thankyou.html')
#         except:
#             return 'Something went wrong. Please try again later'
#     else:
#         return 'Something went wrong'
