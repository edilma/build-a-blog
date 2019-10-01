from flask import Flask, request, redirect, render_template, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#TODO fix the database conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:edilma@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lily'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(4294967295))

    def __init__(self,title,content):
        self.title = title
        self.content= content




@app.route('/', methods=["GET"])
def index():
    return redirect("/blog")



@app.route('/newpost', methods=["GET"])
def create():
    #posts = Post.query.all()
    #return render_template('posts.html', title=title, content=content)
    return render_template('newpost.html')


@app.route('/blog', methods=["GET"])
def viewPosts():
    id =  request.args.get('id')
    if id:
        posts = Post.query.filter_by(id=id).all()
    else:
        posts = Post.query.all()

    return render_template('/posts.html',posts=posts)


    

@app.route('/', methods=['POST'])
def GetContent():
    title= request.form ['title']
    content = request.form ['content']
    #error = None
    if not title:
        flash ("Title can NOT be empty")
        error="error"
        return render_template('write.html')
    if not content:
        flash ("Content can NOT be empty")
     #   error='error'
        return render_template('write.html')
        
    #what to do if there is an error
    else:
        new_post = Post(title,content)
        db.session.add(new_post)
        db.session.commit()
        posts = Post.query.all()
        return render_template('posts.html', posts=posts)
        
        

    
    
    





if __name__ == "__main__":
    app.run()