from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:edilma@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(4294967295))

    def __init__(self,title,content):
        self.title = title
        self.content= content




@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('write.html',blogPost['',''])


    

@app.route('/', methods=['POST'])
def GetContent():
    title= request.form('title')
    content = request.form('content')
    blogPost = [title,content]
    error = validatePost(blogPost)
    if error!="":
        #TODO  validar la information from the form of the blog
        return render_template('write.html')
    else:
        #TODO post the info in the database
        return render_template('write.html')





if __name__ == "__main__":
    app.run()