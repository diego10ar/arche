#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
import IceStorm
Ice.loadSlice('trawlnet.ice')
import TrawlNet
import binascii
import os

class ReceiverI(TrawlNet.Receiver):
        def __init__(self, fileName, sender):
                self.fileName=fileName
                self.sender=sender
                
        def start(self, current=None):
                print("Empiezo a transferir archivo {0}".format(self.fileName))
                size=2048
                file_path=os.getcwd()+"/downloads/"+self.fileName
                
                with open(file_path,'w') as file_:
                        while True:
                                bloque=self.sender.receive(size)
                                if(len(bloque)==3):
                                        break
                                bl=binascii.a2b_base64(bloque[1:])
                                bl=bl.decode()
                                #print(bl)
                                file_.write(bl)
                
                self.sender.close()
                self.sender.destroy()
                


                
                print("Termino de recibir el archivo {0}".format(self.fileName))
                
                
                
        def destroy(self, current):
                try:
                        current.adapter.remove(current.id)
                        print("RECEIVER DESTROYED", flush=True)
                except Exception as e:
                        print(e, flush=True)

class ReceiverFactoryI(TrawlNet.ReceiverFactory):
        def create(self,fileName, sender, transfer,current=None):
                servant=ReceiverI(fileName,sender)
                proxy=current.adapter.addWithUUID(servant)
                
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
                        print("Faltan Argumenos (Nombre de Archivo)", flush=True)
                        return 2
                        
                ic = self.communicator()
                servant=ReceiverFactoryI()
                adapter=ic.createObjectAdapter("AdapterFactoryReceiver")
                proxyReceiver=adapter.add(servant,ic.stringToIdentity("Receiver72"))
                adapter.activate()
                                          
                transfer=transfer_factory.newTransfer(TrawlNet.ReceiverFactoryPrx.checkedCast(proxyReceiver))
                try:
                        receivers=transfer.createPeers(fileList)
              
                        for r in receivers:
                                r.start()
                                r.destroy()
                                
                                
                except Exception as e:
                        print(e,flush=True)
                        
                transfer.destroy()
                
                return 0

sys.exit(Client().main(sys.argv))

