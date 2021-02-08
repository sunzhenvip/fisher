"""
 Created by sz on 2021/2/2
"""

from app import create_app

__author__ = 'sz'

# @app.route('/index')
# def index():
#     return '1212'
app = create_app()
# 基于类的视图(即插视图)
# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    # 生产环境 Nginx+uwsgi
    app.run(host='0.0.0.0', debug=True, port=5000)
