# Entornos virtuales.
- python -m venv my_environment
Si estas en Windows es probable que tengas que conceder permisos sobre la carpeta.
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Finalmente puedes activar el entorno virtual
- Windows
    - my_environment/Source/activate
- Linux
    - source my_environment/bin/activate

Para más información la puedes encontrar en la documentación oficial: ![https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html]