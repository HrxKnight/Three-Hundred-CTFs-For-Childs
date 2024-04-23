from flask import Flask, render_template_string, request, flash
import os
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = '[238 `ajfla; xcmvn 2029]'
def waf(data):
    black_list = ["import", "os", "flag", "subprocess", "system", "open", "read", "eval", "write", "bases", "__builtins__"]
    for i in black_list:
        if i in data:
            return True
    return False

@app.route('/encode', methods=['GET'])
def encode():
    template = """
    <!doctype html>
<title>Encode</title>
<h1>Encode</h1>
<form method="POST">
    <input name="text" placeholder="Text to encode">
    <button>Encode</button>
</form>"""
    return render_template_string(template)

@app.route('/encode', methods=['POST'])
def encode_post():
    text = request.form.get('text') or None
    encoded_text = ""
    if text:
        encoded_text = base64.b64encode(text.encode()).decode()
    else:
        return "No data to encode!"
    template = """
    <!doctype html>
<title>Encode</title>
<h1>Encode</h1>
<form method="POST">
    <input name="text" placeholder="Text to encode">
    <button>Encode</button>
</form>
<p>Encoded data: {}</p>
""".format(encoded_text)
    return render_template_string(template)

@app.route('/decode', methods=['GET'])
def decode():
    template = """
    <!doctype html>
<title>Decode</title>
<h1>Decode</h1>
<form method="POST">
    <input name="text" placeholder="Text to decode">
    <button>Encode</button>
</form>
"""
    return render_template_string(template)

@app.route('/decode', methods=['POST'])
def decode_post():
    result = ""
    text = request.form.get('text') or None
    if text:
        decoded_text = base64.b64decode(text).decode()
        if not waf(decoded_text):
            result = "<p>Decoded data: {}</p></div>".format(decoded_text)
        else:
            result = "<h1 style='{color:red}'>WAF detected!</h1>"

    template = """
    <!doctype html>
<title>Decode</title>
<h1>Decode</h1>
<form method="POST">
    <input name="text" placeholder="Text to encode">
    <button>Encode</button>
</form>
    """ + result
    return render_template_string(template)

@app.route('/')
def index():
    return """
    <html><title>Encode/decode base64 system</title></html>
    <h1>Encode base64 system...</h1>
    <a href="/encode">Encode</a>
    <a href="/decode">Decode</a>
    """


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ['DOCKER_PORT'])