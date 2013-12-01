#!/usr/bin/python

import tornado.ioloop
import tornado.web
import os
import sys
import datetime
import json
import socket

#date_object = datetime.strptime('2013-12-30 17:00', '%Y-%M-%D')


sys.path.append('.')



port = 1984

analytics = False
if not "MacBook" in socket.gethostname() :
    analytics = True
    print "using analytics"
    debug = False
else:
    print "not using analytics"
    debug = True


class UpdateCookieHandler(tornado.web.RequestHandler):
    def get(self, day, state):
        if debug: print day, ':', state
        cookieData = self.get_cookie("caravel_calendar", default=None)
        cookie = None
        if cookieData:
            cookie = json.loads(cookieData)
            for i in range(1, 26):
                if not str(i) in cookie.keys():
                    cookie = None
                    break
                    
        if not cookie:
            print 'new Cookie'
            cookie = {}
            for i in range (1, 26):
                cookie[i] = False
            self.set_cookie("caravel_calendar", json.dumps(cookie, separators=(',', ':')), path='/', expires_days=300)
        if state == 'yes':
            cookie[day] = True
        else:
            cookie[day] = False
        
        self.set_cookie("caravel_calendar", json.dumps(cookie, separators=(',', ':')), path='/', expires_days=300)
        
        self.write('Ok')
        
        
class MainHandler(tornado.web.RequestHandler):


    def get(self):
        previews = []
        days = [ # ['gifName', 'YYYY-MM-DD HH:MM' Starting point hour', 'author', active, date, state] 
                ['GIF1.gif','2013-12-10 00:00', 'joseph', False, 10, False],
                ['Geoffroi_04.gif','2013-12-15 00:00', 'joseph', False, 15, False],
                ['GIF_france.gif','2013-12-24 00:00', 'maxime', False, 24, False],
                ['3_max_trap.gif','2013-12-03 00:00', 'geoffroi', False,3, False],
                ['gif-playa150x108.gif','2013-12-22 00:00', 'maxime', False, 22, False],
                ['Xmas_tree_watercolor.gif','2013-12-14 00:00', 'peter', False, 14, False],
                
                ['night.gif','2013-12-04 00:00', 'gaelle', False, 4, False],
                ['6_max_camap.gif','2013-12-06 00:00', 'marie', False, 6, False],
                ['Geoffroi_01.gif','2013-12-01 00:00', 'joseph', False, 1, False],
                ['gif-cadeau150x108.gif','2013-12-20 00:00', 'joseph', False, 20, False],
                ['GIF4.gif','2013-12-08 00:00', 'joseph', False, 8, False],
                ['GIF_iran.gif','2013-12-23 00:00', 'joseph', False, 23, False],
                
                ['gif-festin-anim-B-150x108.gif','2013-12-21 21:00', 'joseph', False, 21, False],
                ['9_max_tapis.gif','2013-12-02 00:00', 'joseph', False, 2, False],
                ['Xmas_triangle.gif','2013-12-12 00:00', 'joseph', False, 12, False],
                ['GIF3.gif','2013-12-17 00:00', 'joseph', False, 17, False],
                ['Geoffroi_03.gif','2013-12-13 00:00', 'joseph', False, 13, False],
                ['GIF-nigeria.gif','2013-12-07 00:00', 'joseph', False, 7, False],
                
                ['Geoffroi_02.gif','2013-12-16 00:00', 'joseph', False, 16, False],
                ['GIF2.gif','2013-12-18 00:00', 'joseph', False, 18, False],
                ['23_max_sapin.gif','2013-12-09 00:00', 'joseph', False, 9, False],
                ['gif_foot-prints-snow-blue-reparation150x108.gif','2013-12-05 00:00', 'joseph', False, 5, False],
                ['present.gif','2013-12-19 10:00', 'joseph', False, 19, False],
                ['GIF_groenland.gif','2013-12-11 00:00', 'joseph', False, 11, False],
                
                ['gifgift25th_v001.gif','2013-12-25 11:00', 'joseph', False, 25, False],
                
            
            
        ]
        now = datetime.datetime.now()
        
        cookieData = self.get_cookie("caravel_calendar", default=None)
        cookie = None
        if cookieData:
            cookie = json.loads(cookieData)
            for i in range(1, 26):
                if not str(i) in cookie.keys():
                    cookie = None
                    break
                    
        if not cookie:
            print 'new Cookie'
            cookie = {}
            for i in range (1, 26):
                cookie[i] = False
            self.set_cookie("caravel_calendar", json.dumps(cookie, separators=(',', ':')), path='/', expires_days=300)
        else:
            for i in range (0, len(days)):
                days[i][5] = cookie[str(days[i][4])]
            
        
        
        for i in range (0,len(days)):
            if datetime.datetime.strptime(days[i][1], '%Y-%m-%d %H:%M') <= now:
                days[i][3] = True
            if False:
                days[i][3] = True
                
                
            
        self.render('gifgift.html', days=days, analytics=analytics)

    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/setCookie/(.*)/(.*)", UpdateCookieHandler),
            
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
