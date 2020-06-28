# arche_SSDD
Proyecto de prácticas para la asignatura ssdd realizado individualmente por Diego Arche Claudio
Enlace del proyecto:  https://github.com/diego10ar/arche_SSDD.git

## Que había que hacer:

Para esta práctica de Convocatoria Extraordinaria, se nos pedía la creación de un sistema cliente-servidor que permitiera la descarga de ficheros. Para ello debiamos usar ZeroC Ice con el lenguaje python teniendo en cuenta los siguientes aspectos:

  - **Transparencia de localización**

  - **Manejo de canales de Eventos**

  - **Despliegue de servidores**

Todo esto debia llevarse a cabo con la especificación que nos pedían en cuanto a las clases a usar y la comunicación a llevar a cabo.
## Que hace mi código:

Soy consiciente de que mi código no es completo ya que me ha faltado algo de tiempo para la creación del canal de eventos y no he sido capaz de saber introducirlo estos últimos días. 

Primero realice la práctica en local porque pensaba que no había que subirla al GitHub y la he ido pasando al gitHub poco a poco estos ultimos días y de paso intentar introducir los canales de eventos pero no he sido capaz como he dicho anteriormente.

Por tanto mi código ejecuta bien los servidores y los mantiene a la escucha y cuando ejecuto el cliente, si el archivo que solicita el cliente existe, comenzara a realizar la transferencia del archivo que sera introducido en la carpeta /downloads/. Una vez que se realiza la transferencia, se elimina el objeto transfer creado y el servidor se mantiene a la escucha para nuevas solicitudes. Por tanto, la creación de las Factorias y las diferentes clases me lo hace bien, la descarga del archivo y comprobacion de algunos errores también que seran impresos por pantalla.

## Manual de Usuario:

A pesar de no contar con Canal de Eventos, la práctica se realiza correctamente, si hacemos el comando **_Make_** nos realizara bien el despliegue de los servidores y en otro terminal al ejecutar **_Make run-client_** nos envía bien los tres archivos (file1, file2 y file3) que se especifican en el archivo **Makefile**
