import sys
import os
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import Trawlnet

class TransferI(TrawlNet.Transfer):
    prxR="ReceiverFactory.Proxy"
    prxS="SenderFactory.Proxy"
    def crearePeers(self, files, current=None):
        for f in files:
            if not os.path.isfile(os.path.join(os.getcwd(),f)):
                #cerrar todo y parar ya que uno no existe
                
        #si sigue la ejecucion
        for fi in files:
            proxyS = self.communicator().propertyToProxy(prxS)
            sender_factory=Trawnet.SenderFactoryPrx.checkedCast(proxyS)
            sender= sender_factory.create(fi)

            proxyR = self.communicator().propertyToProxy(prxR)
            receiver_factory=Trawnet.ReceiverFactoryPrx.checkedCast(proxyR)
            receiver= receiver_factory.create(fi,sender, transfer)

class TransferFactoryI(TrawlNet.TransferFactory):
    def newTransfer(self,receiverFactory, current=None):
        servant=TransferI()
        proxy=current.adapter.addwithUUid(servant)

        return TrawlNet.TransferPrx.checkedCast(proxy)

class TranferManager(Ice.Application):
    def run(self, argv):
        
s
