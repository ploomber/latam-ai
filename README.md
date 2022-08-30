<p align="center" width="100%">
  <img src="https://ploomber.io/images/logo.svg" width="20%"><br><strong>¡Apóyanos con una estrella ⭐️  en el repo de Ploomber! <a href="https://github.com/ploomber/ploomber" target="_blank">Da click aquí.</a></strong>
</p>

---

# **Ploomber:** Desarrolla código listo para producción desde Jupyter, VSCode o PyCharm

**Facilitadores:** [Eduardo Blancas](https://github.com/edublancas) y [Rodolfo Ferro](https://github.com/RodolfoFerro)

> *Por favor sigue las instrucciones de configuración previas al taller.* Si presentas algún problema, envíanos un [mensaje a través de Slack](https://ploomber.io/community).


## Instrucciones de configuración ⚙️

* Asegúrate de tener una cuenta de GitHub
* Dale **_Fork_** a este repositorio (click el botón de **_Fork_** en la parte superior derecha o en este [link](https://github.com/ploomber/latam-ai/fork))

### **Opción 1.** Configuración de un entorno local

Clona tu fork:

```sh
# Clona el repo (sustituye por tu usuario)
git clone https://github.com/{tu-usuario}/latam-ai
cd latam-ai
```

- Si usas [conda](https://www.google.com/search?q=miniconda):

    ```sh
    # Crea un entorno virtual
    conda create --name ploomber-workshop python=3.9 --yes

    # Activa el entorno
    conda activate ploomber-workshop

    # Instala los requerimientos
    pip install -r requirements.txt
    ```

- Si usas `pip`:

    ```sh
    # Crea un entorno virtual
    python -m venv ploomber-workshop

    # Activa el entorno (si usas Windows, revisa la nota debajo)
    source ploomber-workshop/bin/activate

    # Instala los requerimientos
    pip install -r requirements.txt
    ```

    *Nota:* Si utilizas Windows, el comando para activar el entorno es diferente, [da click aquí](https://docs.python.org/3/library/venv.html) y encontrarás una tabla con el comando de ejecución dependiendo tu sistema operativo.

Para iniciar JupyterLab localmente:

```sh
jupyter lab
```

### **Option 2.** JupyterLab hosteado en un servidor

Para simplificar la configuración, te ofrecemos un JupyterLab hosteado en un servidor.

[Regístrate aquí](https://docs.ploomber.io/en/latest/cloud/api-key.html). Luego, accesa al [JupyterLab aquí](https://docs.ploomber.io/en/latest/cloud/guide.html#hosted-jupyterlab).


Una vez que JupyterLab haya iniciado, clona tu repositorio al que haz hecho Fork:

```sh
# Clona el repo (sustituye por tu usuario)
git clone https://github.com/{tu-usuario}/latam-ai
cd latam-ai
```

## Probando la configuración 

Par aprobar tu configuración, ejecuta o siguiente (puede  tomar algunos segundos):

```
python check.py
```

Si todo está  en orden, verás el sigueitne mensaje:

> Everything is working correctly!


If you have any issues setting up, send us a message on our [community's](https://ploomber.io/community) `#ask-anything` channel.

## Contenidos del taller 

Visita la  sección de [`workshop.md`](workshop.md).
