from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101build@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    #body = db.Column(db.String(1000))
    
    
    def __init__(self, title):
        self.title = title
        #self.body = body

    def __repr__(self):
        return '<Title %r>' % self.title
        #return '<Body %r>' % self.body


        def get_curent_titles():
            return Title.query.all()

        def get_current_blogs():
            return Body.query.all()

   
@app.route('/', methods=['POST', 'GET'])
def index():
    
    titles = Blog.query.all()
    body = Blog.query.all()
    return render_template('blog.html', titles=titles)

@app.route("/addpost", methods=['POST', 'GET'])
def add_post():
    #title=request.form['title']
    #if title == " ":
        #error = 'Please enter a title'
        #return redirect("/?error=" + error)
    #else:

    return render_template('addpost.html')


  

@app.route("/newpost", methods=['POST', 'GET'])
def display_post():
    if request.method == 'POST':
        blog_title=request.form['title']
        body=request.form['body']
        title = Blog(blog_title)
        #new_body= Blog(blog_body)
        db.session.add(title)
        db.session.commit()
    return render_template('newpost.html', title=title, body=body)





    

if __name__ == '__main__':
    app.run()