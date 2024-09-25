# shoppingfeedconverter
## este script se utiliza para convertir las categorias sacadas desde el ShoppingFeed
Para utilizarlo se necesita instalar las dependencias antes. Requerda que debes tener Python instalado. Para instalar las dependencias se utiliza el comando:
```
pip install -r requirements.txt
```
### Para convertir un fichero hay que ponerlo en el mismo directorio con converter.py en formato .html, después abrimos converter.py y escribimos nombre de archivo en fila input file and output file, luego en la consola ejecutamos comando:
```
python converter.py
```
En resultado recibibos mensaje: Categories were exported succefully in "nombre de archivo.txt" o error. Si todo vaya bien, en file "nombre de archivo.txt" recibirémos las categorias en formato necesario