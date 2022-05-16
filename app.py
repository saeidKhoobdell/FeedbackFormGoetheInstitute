
import email
from email import message
from flask import Flask,render_template,request
from mail import send_email
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
        email = request.form['email']
        teacher = request.form['teacher']
        rate = request.form['rate']
        comment = request.form['comments']
        print(email)
        
        if email == '':
            return render_template('index.html', message='please enter your email') 
        if email == '':
            return render_template('index.html', message='please enter choice your teacher')
        send_email(email,teacher,rate,comment)    
        return render_template('succes.html')







if __name__=='__main__':
    app.debug=True
    app.run()
    
    