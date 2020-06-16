import sys
import Ice
Ice.loadSlice('trawlnet.ice')
import Trawlnet
import re

class Client(Ice.Application):
        def run(self,argv):
                return 0

sys.exit(Client().main(sys.argv))

