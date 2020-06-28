# arche_SSDD

https://github.com/diego10ar/arche_SSDD.git

Diego Arche Claudio

-En el repositorio hay una memoria en Pdf mas detallada que lo presentado a continuación.

## Que había que hacer:

Para esta práctica de Convocatoria Extraordinaria, se nos pedía la creación de un sistema cliente-servidor que permitiera la descarga de ficheros. Para ello debiamos usar ZeroC Ice con el lenguaje python teniendo en cuenta los siguientes aspectos:

  - **Transparencia de localización**

  - **Manejo de canales de Eventos**

  - **Despliegue de servidores**

Todo esto debia llevarse a cabo con la especificación que nos pedían en cuanto a las clases a usar y la comunicación a llevar a cabo.

## Que hace mi código:

Soy consiciente de que mi código no es completo ya que me ha faltado algo de tiempo para la creación del canal de eventos y no he sido capaz de saber introducirlo estos últimos días. 

Primero realice la práctica mas o menos en local, las comunicaciones y creación de Factorias y la he ido pasando al gitHub poco a poco estos ultimos días y de paso intentar introducir los canales de eventos pero no he sido capaz como he dicho anteriormente. También pase a realizar el envió del archivo en lo que si he tenido exito.

Por tanto mi código ejecuta bien los servidores y los mantiene a la escucha y cuando ejecuto el cliente, si el archivo que solicita el cliente existe, comenzara a realizar la transferencia del archivo que sera introducido en la carpeta /downloads/. Una vez que se realiza la transferencia, se elimina el objeto transfer creado y el servidor se mantiene a la escucha para nuevas solicitudes. Por tanto, la creación de las Factorias y las diferentes clases me lo hace bien, la descarga del archivo y comprobacion de algunos errores también que seran impresos por pantalla.
A la hora de recibir un archivo, mi metodo Start del ReceiverI, llamara la lectura del sender tantas veces hasta que el tamaño se corresponda a un tamaño igual a 3 que supondra que ha llegado al final del archivo y la cadena esta vacía.

## Manual de Usuario:

A pesar de no contar con Canal de Eventos, la práctica se realiza correctamente, si hacemos el comando **_Make_** nos realizara bien el despliegue de los servidores y en otro terminal al ejecutar **_Make run-client_** nos envía bien los tres archivos (file1, file2 y file3) que se especifican en el archivo **Makefile**
Una vez realizado esto, el cliente se detendra y el servidor avisara de los archivos recibidos y lo utimo sera "**TRANSFER DESTROYED**", Eso si, se mantendrá esperando para nuevas solicitudes
