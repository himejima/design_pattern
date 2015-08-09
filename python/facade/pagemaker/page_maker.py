#!/usr/bin/python
# -*- coding: utf-8 -*-

from html_writer import HtmlWriter
from database import Database

class PageMaker():
    def __init__(self):
        pass

    @staticmethod
    def make_welcome_page(mailaddr, filename):
        # try:
            # username = 'username'
            # mailaddr = 'mailaddr'
            mailprop = Database.get_properties('maildata')
            # print mailprop
            username = mailprop.get('user', mailaddr)

            myfile = open(filename, 'w')
            writer = HtmlWriter(myfile)
            writer.title('Welcom to ' + username + ' s page!')
            writer.paragraph(username + 'のページへようこそ。')
            writer.paragraph('メールまっていますね。')
            writer.mailto(mailaddr, username)
            writer.closing()

            print filename + ' is created for ' + mailaddr + ' (' + username + ')'
        #except:
        #    pass
