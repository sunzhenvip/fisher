"""
 Created by sz on 2021/2/19
"""
__author__ = 'sz'

from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1293334778@qq.com', body='Test',
    #               recipients=['sunzh@net-east.com']
    #               )
    # mail.send(msg)
    msg = Message('[好书]' + ' ' + subject,
                  sender=current_app.config['MAIL_SENDER'],
                  recipients=[to]
                  )
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
