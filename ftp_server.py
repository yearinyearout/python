#!/usr/bin/env python3
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#创建用户
authorizer=DummyAuthorizer()
authorizer.add_user("banboo","root","./",perm="elradfmw")
authorizer.add_anonymous("./")
handler=FTPHandler
handler.authorizer=authorizer
server=FTPServer(("127.0.0.1",2121),handler)
server.serve_forever()
