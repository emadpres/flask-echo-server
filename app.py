from flask import Flask, request

app = Flask(__name__)

HTML_MODE:bool = False

def html(path):
    html = f"<h1>URL = <code style='color:blue'>'{request.base_url}'</code></h1>"
    html += f"<h2>Path: '<code style='color:blue'>{path}</code>' = '<code style='color:blue'>{request.full_path}</code>'</h2>"
    html += f"<hr>"
    html += f"<h1>Headers</h1>"
    html += "<table style='border: 4px solid black;'> <tr> <th>Key</th> <th>Value</th></tr>"
    for key, value in request.headers.items():
        html += f"<tr><td>{key}</td> <td><code>{value}</code></td></tr>"
    html += "</table>"
    return html

def text(path):
    text: str = ""
    text += f"+----------------------------------------------------+\n"
    text += f"URL  = '{request.base_url}'\n"
    text += f"Path = '{path}'\n"
    for key, value in request.headers.items():
        text += f"    {key: <20} = {value}\n"
    text += f"+----------------------------------------------------+\n"
    return text

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def debug(path):  # put application's code here
    if HTML_MODE:
        return html(path=path)
    else:
        return text(path=path)
