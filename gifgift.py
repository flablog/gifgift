#!/usr/bin/python

import tornado.ioloop
import tornado.web
import os
import sys
sys.path.append('.')


debug = False
port = 1984


        
        
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello World")

    
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
