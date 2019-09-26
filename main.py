from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template ('write.html')





if __name__ == "__main__":
    app.run()