"""
 Created by sz on 2021/2/19
"""
__author__ = 'sz'

from threading import Thread

from app import mail
from flask_mail import Message
from flask import current_app, render_template


# 异步执行 email 发送邮件
def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1293334778@qq.com', body='Test',
    #               recipients=['sunzh@net-east.com']
    #               )
    # mail.send(msg)
    # 线程导致 真实的app核心对象获取
    app = current_app._get_current_object()
    msg = Message('[好书]' + ' ' + subject,
                  sender=current_app.config['MAIL_SENDER'],
                  recipients=[to]
                  )
    msg.html = render_template(template, **kwargs)

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
