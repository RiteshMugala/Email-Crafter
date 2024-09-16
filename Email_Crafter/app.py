from flask import Flask, request, render_template, redirect, url_for
import subprocess
from email_bot import generate_email, send_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def describe_email():
    if request.method == 'POST':
        user_prompt = request.form['user_prompt']
        email_content = generate_email(user_prompt)
        return render_template('display_email.html', email_content=email_content)
    return render_template('describe_email.html')

@app.route('/confirm_email', methods=['POST'])
def confirm_email():
    email_content = request.form['email_content']
    action = request.form['action']
    if action == 'continue':
        new_prompt = request.form['new_prompt']
        email_content = generate_email(new_prompt)
        return render_template('display_email.html', email_content=email_content)
    elif action == 'done':
        return render_template('enter_subject.html', email_content=email_content)

@app.route('/enter_recipient', methods=['POST'])
def enter_recipient():
    email_content = request.form['email_content']
    subject = request.form['subject']
    return render_template('enter_recipient.html', email_content=email_content, subject=subject)

@app.route('/send_email', methods=['POST'])
def send_email_route():
    email_content = request.form['email_content']
    subject = request.form['subject']
    recipient = request.form['recipient']
    send_email(recipient, subject, email_content)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
