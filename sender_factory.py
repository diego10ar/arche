#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import Ice
Ice.loadSlice('trawlnet.ice')
import TrawlNet
import binascii

class SenderI(TrawlNet.Sender):
    def __init__(self, fileName):
        self.fileName=fileName
        print("Sender Created, file: {0}".format(fileName))
        
        file_path=os.getcwd()+"/files/"+self.fileName
        self.file_ = open(file_path, 'rb')
       
        
    def receive(self,size,current=None):
        return str(binascii.b2a_base64(self.file_.read(size), newline=False))

        
    def close(self, current):
        self.file_.close()
        
    def destroy(self, current):
        try:
            current.adapter.remove(current.id)
            print('SENDER DESTROYED', flush=True)
        except Exception as e:
            print(e, flush=True)

class SenderFactoryI(TrawlNet.SenderFactory):
    def create(self, fileName, current=None):
        ruta=os.getcwd()+"/files/"+fileName
        if not os.path.isfile(ruta):
                raise TrawlNet.FileDoesNotExistError("Error searching file: {0}".format(fileName))

        servant=SenderI(fileName)
        proxyS=current.adapter.addWithUUID(servant)
        #print("Sender Created, file: {0}".format(fileName))
        sys.stdout.flush()
        
        return TrawlNet.SenderPrx.checkedCast(proxyS)

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
