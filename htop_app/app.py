from flask import Flask
import subprocess
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the htop display app. Go to /htop to see system information."

@app.route('/htop')
def htop():
    name = "Pradeep R Kummitha"
    username = os.getenv('USER', os.getenv('USERNAME', 'codespace'))
    
    server_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    server_time_str = server_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except:
        top_output = "Error retrieving top command output"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>System Information</title></head>
    <body>
        <h2>System Information</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>User:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time_str}</p>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))