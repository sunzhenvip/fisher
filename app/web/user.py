"""
 Created by sz on 2021/2/5
"""
__author__ = 'sz'

from . import web


@web.route('/url')
def login():
    return "sd"
