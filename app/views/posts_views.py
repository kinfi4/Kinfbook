from flask import render_template, request, url_for

from app import app, db
from app.models import Post


@app.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    posts_for_page = Post.query.order_by(Post.timespan.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_page = url_for('posts', page=posts_for_page.next_num) if posts_for_page.has_next else None
    prev_page = url_for('posts', page=posts_for_page.prev_num) if posts_for_page.has_prev else None

    return render_template('posts.html', title='Home', posts=posts_for_page.items, next_page=next_page,
                           prev_page=prev_page)