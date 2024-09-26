# shoppingfeedconverter
## este script se utiliza para convertir las categorias sacadas desde el ShoppingFeed. Se hace a través de línea de comandos. Para utilizar script se necesita instalar las dependencias antes. Requerda que debes tener Python instalado. Para asegurarte que lo tienes instalado, en PowerShell escribe ese comando:
```
python --version
```
Si ya lo tienes instalado, va a aparecer la version. En caso contrario aparecerá error.
Si no queres instalar muchos paquetes en forma global, se puede hacerlo en forma local. Para conseguirlo hay que instalar un entorno virtual con comando:
```
python -m venv .venv
```
Luego se necesita ejecutar este entorno virtual. Lo hacemos con comandos:
```
.venv/scripts/./activate
```
En caso satisfactorio antes de la ruta va a aparecer (.venv)
Para instalar las dependencias se utiliza el comando:
```
pip install -r requirements.txt
```
Para convertir un fichero hay que ponerlo en el mismo directorio con converter.py en formato .html, después abrimos converter.py y escribimos nombre de archivo en fila input file and output file, luego en la consola ejecutamos comando:
```
python converter.py
```
En resultado recibimos mensaje: Categories were exported succefully in "nombre de archivo.txt" o error. Si todo vaya bien, en file "nombre de archivo.txt" recibirémos las categorias en formato necesario
