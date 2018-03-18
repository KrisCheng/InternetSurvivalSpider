# -*- coding: utf-8 -*-

class HtmlOutput(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return 
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<h2>Final Result:</h2>")
        fout.write("<table border=1>")
        fout.write("<tr>")
        fout.write("<td>URL</td>")
        fout.write("<td>TITLE</td>")
        fout.write("<td>SUMMARY</td>")
        fout.write("</tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
        