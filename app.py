from flask import Flask, render_template, request, redirect, url_for, session, flash
from win10toast import ToastNotifier
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Predefined credentials
USER_EMAIL = "root@gmail.com"
USER_PASSWORD = "admin123"

# Initialize Windows toaster for notifications
toaster = ToastNotifier()

def notify_windows(message):
    """Send a Windows notification"""
    toaster.show_toast("Project C VPN", message, duration=10)

@app.route('/', methods=['GET'])
def index():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if email == USER_EMAIL and password == USER_PASSWORD:
        session['logged_in'] = True
        # Send "Connected" notification
        threading.Thread(target=notify_windows, args=("VPN Connected!",)).start()
        flash('Login successful!')
        return redirect(url_for('welcome'))
    else:
        flash('Invalid email or password')
        return redirect(url_for('index'))

@app.route('/welcome', methods=['GET'])
def welcome():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('index'))
    return render_template('welcome.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    # Send "Disconnected" notification
    threading.Thread(target=notify_windows, args=("VPN Disconnected!",)).start()
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Expose to the network by binding to 0.0.0.0
