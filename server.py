# Use on the powershell terminal to properly run flask or check their documentation for others:

# To run the flask application you first need to tell your terminal what application to work with by exporting the
# FLASK_APP environment variable:
# > $env:FLASK_APP = "your python file name"
# > flask run
# The output should be something like this: * Running on http://127.0.0.1:5000/ (example)

# in order to activate Debug Mode, run this on your powershell terminal:
# > $env:FLASK_ENV = "development"
# > flask run

# If you have any problems in activating your virtualenv try this: 1) Right click on the PowerShell application (or
# other you're using) and select Run as Administrator 2) Run the following command: Set-ExecutionPolicy Unrestricted
# 3) Rerun the activation command: your_virtualenv_name\Scripts\activate.ps1 or just go to the folder where your
# virtual env and try Scripts\activate.ps1 , Scripts\Activate.ps1 or simply Scripts\activate, Scripts\Activate

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong try again'


if __name__ == '__main__':
    app.run()
