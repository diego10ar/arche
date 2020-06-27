#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import TrawlNet

class TransferI(TrawlNet.Transfer):
    def __init__(self, sender_factory, receiver_factory):
        self.sender_factory=sender_factory
        self.receiver_factory=receiver_factory
        
        
    def createPeers(self, files, current=None):
        transfer=None
        
        for f in files:
            ruta=os.getcwd()+"/files/"+f
            #print("ruta= {0}".format(ruta))
            if not os.path.isfile(ruta):
                raise RuntimeError("Algun archivo no existe")
                
        #si sigue la ejecucion
        receivers=[]    
        for fi in files:
           file_sender=self.sender_factory.create(fi)
           file_receiver=self.receiver_factory.create(fi, file_sender, transfer)
           receivers.append(file_receiver)

        print("Todas las parejas creadas")
        return receivers
    
    def destroy(self,current=None):
        try:
            current.adapter.remove(current.id)
            print("TRANSFER DESTROYED")
        except Exception as e:
            print(e,flush=True)

    def destroyPeer(self, peerId, current=None):
        proxyReceiverId=peerId+" -t -e 1.1 @ AdapterReceiver72"
        file_receiver = Trawlnet.ReceiverPrx.checkedCast(proxyReceiverId)
        file_receiver.destroy()

class TransferFactoryI(TrawlNet.TransferFactory):
    def __init__(self, sender_factory):
        self.sender_factory=sender_factory
        
    def newTransfer(self,receiver_factory, current=None):
        servant=TransferI(self.sender_factory, receiver_factory)
        proxy=current.adapter.addWithUUID(servant)
        servant.transfer=TrawlNet.TransferPrx.checkedCast(proxy)
        
        return servant.transfer

class TranferManager(Ice.Application):
    def run(self, argv):
        
        prxS="Sender72 -t -e 1.1@ AdapterSender72"

        proxySender=self.communicator().stringToProxy(prxS)
        sender_factory=TrawlNet.SenderFactoryPrx.checkedCast(proxySender)
        
        #print("proxy={0}".format(proxySender))
        if sender_factory is None:
            raise RuntimeError("Ivalid proxy of sender_factory")

        ic = self.communicator()
        servant=TransferFactoryI(sender_factory)
        adapter=ic.createObjectAdapter("AdapterFactoryTransfer")
        proxyTransfer=adapter.add(servant,ic.stringToIdentity("Transfer72"))
   
        print(proxyTransfer, flush=True)
        
        adapter.activate()
        self.shutdownOnInterrupt()
        ic.waitForShutdown()

        return 0
    
sys.exit(TranferManager().main(sys.argv))
