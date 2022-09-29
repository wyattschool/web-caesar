from flask import Flask, request
from caesar import rotate_string

app = Flask('app')

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rot"><label>
						Rotate by:
						<input type="text" name="rot" value="0" autofocus></input>
        <textarea name="text" placeholder="Enter some text to encrypt here.">{0}</textarea>
        <button type="submit">Submit Query</button>
        </form>
    </body>
</html>"""

@app.route('/')
def index():
  return form.format("")

@app.route('/', methods=['POST'])
def encrypt():
	rotate = int(request.form['rot'])
	form_text = request.form['text']
	new_text = rotate_string(form_text,rotate)
	return form.format(new_text)

app.run(host='0.0.0.0', port=8080)