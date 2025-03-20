Generador de Imágenes con Stable Diffusion

Este proyecto utiliza la librería diffusers de Hugging Face para generar imágenes a partir de descripciones textuales (prompts) utilizando un modelo de Stable Diffusion.

📖 Descripción

Este generador de imágenes permite crear imágenes artísticas y detalladas basadas en descripciones proporcionadas por el usuario (prompts). Utiliza el modelo Stable Diffusion v1-4 para la generación de imágenes.

💡 Requisitos

Asegúrate de tener instalado Python 3.8 o superior. Si no lo tienes instalado, descárgalo desde Python.org.

🔍 Verificar instalación de Python

Ejecuta este comando en la terminal para comprobar que Python está instalado: 

python --version

📥 Instalación del Proyecto

1°- Clona este repositorio en tu máquina local.

2°- Entra en la carpeta del proyecto desde la terminal:

CMD
C:/.../ChimageAI>

3°- Instala las dependencias con pip desde la raiz del proyecto:

pip install -r requirements.txt

4°- Modifica el promt si deseas generar una imagen distinta (linea 6 del codigo)

prompt = ("AQUI INGRESAS EL PROMT DE LA IMAGEN QUE DESEAS GENERAR, DE PREFERENCIA EN INGLES YA QUE HACE MEJOR INTERPRETACIÓN PARA GENERAR LAS IMAGENES")

5°- Ejecutas en main.py desde raiz del proyecto, desde la terminal con el siguiente comando:

python main.py
