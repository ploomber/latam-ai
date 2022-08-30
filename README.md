<p align="center" width="100%">
  <img src="https://ploomber.io/images/logo.svg" width="20%"><br><strong>¡Apóyanos con una estrella ⭐️  en el repo de Ploomber! <a href="https://github.com/ploomber/ploomber" target="_blank">Da click aquí.</a></strong>
</p>

---

# **Ploomber:** Desarrolla código listo para producción desde Jupyter, VSCode o PyCharm

**Facilitadores:** [Eduardo Blancas](https://github.com/edublancas) y [Rodolfo Ferro](https://github.com/RodolfoFerro)

> *Por favor sigue las instrucciones de configuración previas al taller.* Si presentas algún problema, envíanos un [mensaje a través de Slack](https://ploomber.io/community). Si abres este archivo desde JupyterLab, no olvides ejeccutar la siguiente celda para suscribirte a nuestro newsletter.


```sh
from IPython.display import HTML
HTML("""
<div id="revue-embed">
  <form action="https://www.getrevue.co/profile/ploomber/add_subscriber" method="post" id="revue-form" name="revue-form"  target="_blank">
  <div class="revue-form-group" id="email-text-field">
    <input class="revue-form-field" placeholder="Your email address" type="email" name="member[email]" id="member_email">
  </div>
  <div class="revue-form-actions" id="submit-btn">
    <input type="submit" value="Subscribe" name="member[subscribe]" id="member_submit">
  </div>
  </form>
</div>

<div class="newsletter-copy">¡Gracias por suscribirte!</div>
""")
```

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

- Si usas [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

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

### **Opción 2.** JupyterLab desde MyBinder

Para simplificar la configuración, puedes utilizar MyBinder con el entorno que hemos  preparado para ti.

Para habilitar el repositorio desde MyBinder, basta con abrir el [este link](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Flatam-ai%26urlpath%3Dlab%252Ftree%252Flatam-ai%252FREADME.md%26branch%3Dmain) o dar click en el siguiente botón:

[![Binder](https://mybinder.org/badge_logo.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Flatam-ai%26urlpath%3Dlab%252Ftree%252Flatam-ai%252FREADME.md%26branch%3Dmain)

## Probando la configuración 

Para aprobar tu configuración, ejecuta lo siguiente desde una terminal (puede tomar algunos segundos):

```
python check.py
```

Si todo está  en orden, verás el sigueitne mensaje:

> Everything is working correctly!


Si presentas algún problema con la configuración, envíanos un mensaje en el canal `#ask-anything` de [nuestra comunidad](https://ploomber.io/community) y resolveremos cualquier  duda que tengas.

## Contenidos del taller 

Visita la  sección de [`workshop.md`](workshop.md).
