from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:edilma@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'lily'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(4294967295))
    
    def __init__(self,title,content):
        self.title = title
        self.content= content
    
 
def validatePost(blog_name,blog_content):
    title= blog_name
    content = blog_content
    if title=="":
        return "Title is Required"
    if content=="":
        return "Content is required"
    else:
        return "ok"

#first time they go to the website
@app.route('/blog', methods=["GET"])
def index():
    posts = Post.query.all()
    return render_template('post_template.html',  posts=posts) #add this variable and iterate 


#after they fill in the form and POST it.
@app.route('/newpost', methods=['POST'])
def GetContent():
    blog_name= request.form['title']
    blog_content = request.form['content']
    isValid = validatePost (blog_name,blog_content)
    if isValid=="ok":
        post = Post(blog_name,blog_content)
        db.session.add(post)
        db.session.commit()
        #print (blogPost)
    else: 
        flash(isValid) #todo fix flash
    #todo load current posts
    posts = Post.query.all()
    return redirect('/blog',id=id)
    #return render_template('post_template.html',  posts=posts) #add this variable and iterate 

    


if __name__ == "__main__":
    app.run()