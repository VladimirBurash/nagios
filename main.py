from nagios import NagiosBot
from tornado.ioloop import  IOLoop
from roboman.server import RobomanServer

if __name__ == "__main__":
    bots = [
        # SekonomBot,
        # EvoBot,
        NagiosBot
    ]


    IOLoop.instance().start()
    server = RobomanServer(bots=bots)
    server.start()