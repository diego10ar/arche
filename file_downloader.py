import sys
import Ice
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
                prx='ReceiverManager.Proxy'
                proxy=self.comunicator().propertyToProxy(prx)
                transfer_factory=TrawlNet.TransferFactoryPrx.checkedCast(proxy)

                if transfer_factory is None:
                        raise RunTimeError("Ivalid Proxy")
                if len(argv) < 2:
                        raise RunTimeError("No file given")


                broker = self.communicator()
                servant=ReceiverFactory()
                adapter=broker.createObjectAdapter("ReceiverFactoryAdapter")
                prx2=adapter.add(servant,broker.stringToIdentify("receiver_factory1")

                transfer=transfer_factory.newTransfer(TrawlNet.ReceiverFactoryPrx.checkedCast(prx2))
                fileList=list(sys.argv[1:])
                transfer.createPeers(fileList)

                
                return 0

sys.exit(Client().main(sys.argv))

