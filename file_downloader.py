#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import TrawlNet



class ReceiverI(TrawlNet.Receiver):
        def start(self, current=None):
                print("empiezo")
                
        def destroy(self, current):
                try:
                        current.adapter.remove(current.id)
                        print("Receiver Destroyed", flush=True)
                except Exception as e:
                        print(e, flush=True)

class ReceiverFactoryI(TrawlNet.ReceiverFactory):
        def create(self,fileName, sender, transfer):
                servant=ReceiverI()
                proxy=current.adpter.addwithUUID(servant)
                
                return TrawlNet.ReceiverPrx.checkedCast(proxy)
        
class Client(Ice.Application):
        def run(self,argv):
                prxT="Transfer72 -t -e 1.1 @ AdapterTransfer72"
                proxy=self.communicator().stringToProxy(prxT)
                transfer_factory=TrawlNet.TransferFactoryPrx.checkedCast(proxy)

                if transfer_factory is None:
                        raise RunTimeError("Ivalid proxy of transfer_factory")

                fileList=list(sys.argv[1:])
               
                if len(fileList) < 1:
                        print("Invalid number of arguments", flush=True)
                        return 2
                        
                ic = self.communicator()
                servant=ReceiverFactoryI()
                adapter=ic.createObjectAdapter("AdapterFactoryReceiver")
                proxyReceiver=adapter.add(servant,ic.stringToIdentity("Receiver72"))
                adapter.activate()
                                          
                transfer=transfer_factory.newTransfer(TrawlNet.ReceiverFactoryPrx.checkedCast(proxyReceiver))
                transfer.createPeers(fileList)

                
                return 0

sys.exit(Client().main(sys.argv))

