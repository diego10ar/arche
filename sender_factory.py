#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import Ice
Ice.loadSlice('trawlnet.ice')
import TrawlNet

class SenderI(TrawlNet.Sender):
    def __init__(self, fileName):
        self.fileName=fileName
        print("Sender Created, file: {0}".format(fileName))
        
    def close(self, current=None):
        self.file.close()

class SenderFactoryI(TrawlNet.SenderFactory):
    def create(self, fileName, current=None):
        if not os.path.isfile(os.path.join(os.getcwd(),f)):
                raise TrawlNet.FileDoesNotExistError("Error searching file: {0}".format(fileName))

        servant=SenderI(fileName)
        proxyS=current.adapter.addWithUUID(servant)
        print("Sender Created, file: {0}".format(fileName))
        sys.stdout.flush()
        
        return Trawlnet.SenderPrx.checkedCast(proxyS)

class Server(Ice.Application):
    def run(self, args):
        ic = self.communicator()
        servant=SenderFactoryI()
        adapter=ic.createObjectAdapter("AdapterFactorySender")
        proxySender=adapter.add(servant, ic.stringToIdentity("Sender72"))
   
        print(proxySender, flush=True)
        
        adapter.activate()
        self.shutdownOnInterrupt()
        ic.waitForShutdown()

        return 0

sys.exit(Server().main(sys.argv))                        
