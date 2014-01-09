import os
import sys
dirname = os.path.dirname(__file__)
root = os.path.abspath(dirname)
sys.path.insert(0, root)
os.chdir(os.path.join(root, 'bnw.search'))
from twisted.application import internet, service
from twisted.web import server
import bnw.core.base
import bnw.core.bnw_mongo

from bnw.search.search_server import RPCSearch
import config


bnw.core.base.config.register(config)
bnw.core.bnw_mongo.open_db()

application = service.Application('BnW search service')
r = RPCSearch(config.search_db, config.search_language)
search_service = internet.TCPServer(
    config.search_port, server.Site(r), interface='127.0.0.1')
search_service.setServiceParent(application)
