from django.contrib import staticfiles

import os, sys

def preface():
    pre = {}
    pre['title'] = u'序章 - 也许我在寻找你'
    q = open(os.path.join(os.path.dirname(__file__), 'static/text/preface'), 'r')
    pre['content'] = q.read().split('\n')
    return pre
