"""
 Created by sz on 2021/2/2
"""

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'
# SQLALCHEMY_ECHO = True


# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1293334778@qq.com'
MAIL_PASSWORD = 'jyqfjmheyglqbagd'
# MAIL_SUBJECT_PREFIX = '[数急]'
MAIL_SENDER = '鱼书 <1293334778@qq.com>'
