from flask import Flask, render_template
from board import create_checkerboard
app = Flask(__name__)

@app.route('/')
def checkerboard():
    output = create_checkerboard(8,8)
    return render_template("index.html", output=output)




if __name__=='__main__':
    app.run(debug=True)
    