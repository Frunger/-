from unwrap.comment import comment_bp
from unwrap.user.routes import user_bp
from unwrap.admin.routes import admin_bp
from unwrap import app


app.register_blueprint(user_bp)
app.register_blueprint(admin_bp,url_prefix="/admin")
app.register_blueprint(comment_bp, url_prefix='/comment')

if __name__ == '__main__':
    app.run(debug=True)