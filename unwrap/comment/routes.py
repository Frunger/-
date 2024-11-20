from flask import render_template, request, flash
from . import comment_bp

# 内存中简单的评论存储
comments = []


@comment_bp.route('/', methods=['GET', 'POST'])  # 修改为根路径
def comments_page():
    if request.method == 'POST':
        username = request.form.get('username')
        comment = request.form.get('comment')
        if username and comment:
            comments.append({'username': username, 'comment': comment})
            flash('评论提交成功！', 'success')
        else:
            flash('请填写用户名和评论内容。', 'danger')
    return render_template('comment.html', comments=comments)

