from flask import  Flask ,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)

def database_writer(data):
    with open('database.txt', mode = "a") as datafile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = datafile.write(f"\n{email} - {subject} - {message}")

def database_csv(data):
    with open('database.csv', mode = "a" , newline = '') as datacsv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvwriter = csv.writer(datacsv, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])


        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      data = request.form.to_dict()
      print(data)
      database_csv(data)
      return redirect('thankyou.html') 
    else:
        return 'something went wrong'






# @app.route('/hello/')
# @app.route('/hello/mere')
# def hello(name=None):
#     return render_template('skeleton.html', name=name)


if __name__ == '__main__':
     app.run(debug=True)