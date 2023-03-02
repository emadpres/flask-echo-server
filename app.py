from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def debug(path):  # put application's code here
    html = f"<h1>URL = <code style='color:blue'>'{request.base_url}'</code></h1>"
    html += f"<h2>Path: '<code style='color:blue'>{path}</code>' = '<code style='color:blue'>{request.full_path}</code>'</h2>"
    html += f"<hr>"
    html += f"<h1>Headers</h1>"
    html += "<table style='border: 4px solid black;'> <tr> <th>Key</th> <th>Value</th></tr>"
    for key, value in request.headers.items():
        html += f"<tr><td>{key}</td> <td><code>{value}</code></td></tr>"
    html += "</table>"
    return html
