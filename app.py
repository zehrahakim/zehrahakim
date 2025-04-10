from flask import Flask, Response
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop_view():
    # Your full name
    name = "Your Full Name"  # Replace with your actual name

    # System username
    username = getpass.getuser()

    # Current IST time
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get top output (htop may not work in non-interactive mode)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    html_output = f"""
    <pre>
Name: {name}
User: {username}
Server Time (IST): {ist_time}
TOP output:
{top_output}
    </pre>
    """
    return Response(html_output, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)