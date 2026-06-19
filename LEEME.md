# Marilin Amaya Psicología - Streamlit corregido

Este proyecto está corregido para evitar `FileNotFoundError` cuando Streamlit no encuentra imágenes.

## Archivos esperados en la raíz del repositorio

- `app.py` o `aplicación.py`: archivo principal de la aplicación.
- `logo_b64.jpeg`: portada del negocio.
- `logo_marilin_amaya.png`: logo principal.
- `requirements.txt`: dependencias para Streamlit Cloud.

## Configuración recomendada en Streamlit Cloud

Main file path:

```text
app.py
```

Si prefieres usar el archivo en español, configura:

```text
aplicación.py
```

## Corrección aplicada

La app ahora busca las imágenes en la raíz y en carpetas comunes como `assets/`, `images/`, `imagenes/`, `img/` y `static/`.
Si no encuentra una imagen, la página igual carga y muestra un diseño alternativo.
