# Limpieza y Ordenamiento de Contactos

Este script de Python se encarga de limpiar y ordenar una lista de contactos almacenados en un archivo JSON. El resultado se guarda en un archivo Excel (XLSX) ordenado alfabéticamente.

## Requisitos

Para utilizar este script, debes tener Python 3 instalado en tu sistema y las siguientes bibliotecas de Python:

os
json
pandas
Puedes instalar las bibliotecas requeridas usando pip:

```bash pip install pandas```

## Uso

Asegúrate de que tienes un archivo JSON con tus contactos llamado TUARCHIVOJCONTACTOS.json. Puedes cambiar el nombre del archivo en el código si es necesario.

Copia el código proporcionado en un archivo Python con extensión .py, por ejemplo, clean_contacts.py.

Ejecuta el script utilizando tu terminal o línea de comandos. Ve al directorio donde se encuentra el archivo Python y ejecuta:
```python clean_contacts.py```

El script leerá el archivo JSON, limpiará los contactos y los ordenará alfabéticamente.
El resultado se guardará en un archivo Excel llamado sorted_contacts.xlsx.

Detalles del Código
El script abre el archivo JSON de contactos, elimina aquellos con números de teléfono que no siguen el formato deseado y omite los contactos que contienen la palabra "Familia" en su nombre.

Luego, ordena los contactos por nombre.

Finalmente, guarda los contactos ordenados en un archivo Excel llamado sorted_contacts.xlsx.

## Notas

Asegúrate de tener un archivo JSON de contactos válido con la estructura de datos esperada antes de ejecutar el script.

Puedes personalizar el nombre del archivo de salida cambiando 'sorted_contacts.xlsx' en la última línea del script.

¡Listo! Ahora tienes un script para limpiar y ordenar tus contactos almacenados en un archivo JSON.
