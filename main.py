from flask import Flask, request, redirect, render_template
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
    body = db.Column(db.String(1000))
    
    
    def __init__(self, name):
        self.name = name
        self.read = False

    #def __repr__(self):
        #return '<Title %r>' % self.name
        #return '<Body %r>' % self.name


        #def get_curent_titles():
            #return Title.query.all()

        #def get_current_blogs():
            #return Body.query.all()

    #get_current_title = Blog.query.get_all()

@app.route('/')
def index():
    encoded_error = request.args.get("error")
    return render_template('blog.html')  



    if request.method == 'POST':
        new_title = request.form['title']
        #new_body = request.form['body']
        #new_blog = Blog('new_title')
        new_blog_body = Blog(new_title)
        db.session.add(new_blog_body)
        db.session.commit()
        #new_blog_title = request.form['new_title']
        #new_blog_body = request.form['new_body']

@app.route("/addpost", methods=['POST', 'GET'])
def add_post():
        
    return render_template('addpost.html')


    #title = Blog(title)
    #body = Blog(body)
    #db.session.add(title, body)
    #db.session.commit()
    #return render_template('newpost', title=title, body=body)




    

    

if __name__ == '__main__':
    app.run()