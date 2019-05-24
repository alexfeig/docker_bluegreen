import socket
import os
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    url = request.url
    header = request.environ
    if os.getenv("app_color") is None:
        color = 'Undefined'
    else:
        color = os.environ['app_color'].lower()

    if color == 'blue':
        bg_color = '#167ebf'
    elif color == 'green':
        bg_color = '#57a815'
    else:
        bg_color = '#bbbcba'

    return render_template('index.html', host_ip=host_ip, server_name=host_name,
                           url=url, color=color, bg_color=bg_color, header=header)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
