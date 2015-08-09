#!/usr/bin/python
# -*- coding: utf-8 -*-

class HtmlWriter():
    def __init__(self, writer):
        self.__writer = writer

    def title(self, title):
        self.__writer.write('<html>')
        self.__writer.write('<head>')
        self.__writer.write('<title>' + title + '</title>')
        self.__writer.write('</head>')
        self.__writer.write('<body>')
        self.__writer.write('<h1>' + title + '</h1>')

    def paragraph(self, msg):
        self.__writer.write('<p>' + msg + '</p>\n')

    def link(self, href, caption):
        self.paragraph('<a href="' + href + '">' + caption + '</a>')

    def mailto(self, mailaddr, username):
        self.link('mailto:' + mailaddr, username)

    def closing(self):
        self.__writer.write('</body>')
        self.__writer.write('</html>\n')
        self.__writer.close()
