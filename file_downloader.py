import sys
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import TrawlNet



class ReceiverI(Trawlnet.Receiver):
        def start(self, current=None):
                
        def destroy(self, current):
                try:
                        current.adapter.remove(current.id)
                        print("Receiver Destroyed"), flush=True)
                except Exception as e:
                        print(e, flush=True)

class ReceiverFactoryI(Trawlnet.ReceiverFactory):
        def create(string fileName, Sender* sender Transfer* transfer):
                servant=ReceiverI()
                proxy=current.adpter.addwithUUID(servant)
                
                return Trawlnet.ReceiverPrx.checkedCast(proxy)
        
class Client(Ice.Application):
        def run(self,argv):
                prxT="Transfer72 -t -e 1.1 @ AdapterTransfer72"
        
                proxy=self.comunicator().stringToProxy(prxT)
                transfer_factory=TrawlNet.TransferFactoryPrx.checkedCast(proxy)

                if transfer_factory is None:
                        raise RunTimeError("Ivalid proxy of transfer_factory")
                if len(argv) < 2:
                        raise RunTimeError("No file given")

                ic = self.communicator()
                servant=ReceiverFactoryI()
                adapter=ic.createObjectAdapter("AdapterFactoryReceiver")
                proxyReceiver=adapter.add(servant,ic.stringToIdentify("Factory_receiver")

                transfer=transfer_factory.newTransfer(TrawlNet.ReceiverFactoryPrx.checkedCast(proxyReceiver))
                fileList=list(sys.argv[1:])
                transfer.createPeers(fileList)

                
                return 0

sys.exit(Client().main(sys.argv))

