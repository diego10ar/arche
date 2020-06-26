import sys
import os
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import Trawlnet

class TransferI(TrawlNet.Transfer):
    prxR="ReceiverFactory.Proxy"
    def __init__(self, sender_factory, receiver_factory):
        self.sender_factory=sender_factory
        self.receiver_factory=receiver_factory
        
        
    def createPeers(self, files, current=None):
       
        for f in files:
            if not os.path.isfile(os.path.join(os.getcwd(),f)):
                raise RuntimeError("Algun archivo no existe")
                
        #si sigue la ejecucion
        for fi in files:
           file_sender=self.sender_factory.create(fi)
           file_receiver=self.receiver_factory.create(file, sender)

    def destroy(self,current=None):
        try:
            current.adapter.remove(current.id)
        except Exception as e:
            print(e,flush=true)

    def destroyPeer(self, idP, current=None):
        proxy=idP+" -t -e 1.1 @ AdapterReceiver72"
        file_receiver = Trawlnet.ReceiverPrx.checkedCast(proxy)
        file_receiver.destroy()

class TransferFactoryI(TrawlNet.TransferFactory):
    def __init__(self, sender_factory):
        self.sender_factory=sender_factory
        
    def newTransfer(self,receiver_factory, current=None):
        servant=TransferI(self.sender_factory, receiver_factory)
        proxy=current.adapter.addwithUUid(servant)

        return TrawlNet.TransferPrx.checkedCast(proxy)

class TranferManager(Ice.Application):
    def run(self, argv):
        
        prxS="Sender72 -t -e 1.1 @ AdapterSender72"
        proxy=self.comunicator().stringToProxy(prxS)
        sender_factory=TrawlNet.TransferFactoryPrx.checkedCast(proxy)
        
        if sender_factory is None:
            raise RunTimeError("Ivalid proxy of sender_factory")

        ic = self.communicator()
        servant=TransferFactoryI(sender_factory)
        adapter=ic.createObjectAdapter("AdapterFactoryTransfer")
        proxyTransfer=adapter.add(servant,ic.stringToIdentify("Transfer72")
   
        print(proxy, flush=True)
        
        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0
    
sys.exit(TranferManager().main(sys.argv))
