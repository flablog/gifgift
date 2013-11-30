#!/usr/bin/python

import tornado.ioloop
import tornado.web
import os
import sys
import datetime

#date_object = datetime.strptime('2013-11-30 17:00', '%Y-%M-%D')


sys.path.append('.')


debug = True
port = 1984


        
class MainHandler(tornado.web.RequestHandler):


    def get(self):
        days = [ # ['gifName', 'YYYY-MM-DD HH:MM' Starting point hour', 'author', active, date] 
                ['present.gif','2013-11-30 10:00', 'joseph', False, 10],
                ['23_max_sapin.gif','2013-11-30 15:00', 'joseph', False, 15],
                ['9_max_tapis.gif','2013-11-30 23:59', 'maxime', False, 24],
                ['3_max_trap.gif','2013-11-30 03:00', 'geoffroi', False,3],
                ['GIF-nigeria.gif','2013-11-30 22:00', 'maxime', False, 22],
                ['Geoffroi_01.gif','2013-11-30 14:00', 'peter', False, 14],
                
                ['GIF1.gif','2013-11-30 04:00', 'gaelle', False, 4],
                ['6_max_camap.gif','2013-11-30 06:00', 'marie', False, 6],
                ['GIF2.gif','2013-11-30 01:00', 'joseph', False, 1],
                ['GIF3.gif','2013-11-30 20:00', 'joseph', False, 20],
                ['GIF4.gif','2013-11-30 08:00', 'joseph', False, 8],
                ['GIF_france.gif','2013-11-30 23:00', 'joseph', False, 23],
                
                ['Geoffroi_02.gif','2013-11-30 21:00', 'joseph', False, 21],
                ['Xmas_tree_watercolor.gif','2013-11-30 02:00', 'joseph', False, 2],
                ['GIF_iran.gif','2013-11-30 12:00', 'joseph', False, 12],
                ['Geoffroi_03.gif','2013-11-30 17:00', 'joseph', False, 17],
                ['Geoffroi_04.gif','2013-11-30 13:00', 'joseph', False, 13],
                ['Xmas_triangle.gif','2013-11-30 07:00', 'joseph', False, 7],
                
                ['gif-cadeau150x108.gif','2013-11-30 16:00', 'joseph', False, 16],
                ['GIF_groenland.gif','2013-11-30 18:00', 'joseph', False, 18],
                ['night.gif','2013-11-30 09:00', 'joseph', False, 9],
                ['gif-festin-anim-B-150x108.gif','2013-11-30 05:00', 'joseph', False, 5],
                ['gif-playa150x108.gif','2013-11-30 19:00', 'joseph', False, 19],
                ['gif_foot-prints-snow-blue-reparation150x108.gif','2013-11-30 11:00', 'joseph', False, 11],
                
            
            
        ]
        now = datetime.datetime.now()
        
        for i in range (0,len(days)):
            if datetime.datetime.strptime(days[i][1], '%Y-%m-%d %H:%M') <= now:
                days[i][3] = True
                
        self.render('gifgift.html', days=days)

    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            
        ]
                
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, debug=debug, **settings)


if __name__ == "__main__":
    print "\nStarting ", __file__
    print "serveur demarre sur port ", port 
    if debug:
        print "Debug Mode ON"
        import datetime
        print datetime.datetime.now()
    app = Application()
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
