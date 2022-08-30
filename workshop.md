<p align="center" width="100%">
  <img src="https://ploomber.io/images/logo.svg" width="20%"><br><strong>¡Apóyanos con una estrella ⭐️  en el repo de Ploomber! <a href="https://github.com/ploomber/ploomber" target="_blank">Da click aquí.</a></strong>
</p>

---

# **Ploomber:** Desarrolla código listo para producción desde Jupyter, VSCode o PyCharm


## Bloque 1: Introducción a Ploomber

> Motivaremos el proyecto y explicaremos por qué invertir en organizar nuestro proyecto como un flujo (**_pipeline_**) modular (múltiples scripts/notebooks) en lugar de un gran script/notebook nos ayuda a desarrollar más rápido y mejora la colaboración.


<!-- #region -->
### Antes de comenzar...

#### **Opción 1.** Configuración de un entorno local

> **Importante:** Si no tuviste oportunidad de configurar tu entorno local previo al taller, te recomendamos ir a la *Opción 2*, dado que es más simple y rápida de abordar.

Verifiquemos tu configuración. Ejecuta lo siguiente en tu terminal:

**Paso 1:** Clona el repositorio al que has hecho _Fork_.

```sh
git clone https://github.com/{tu-usuario}/latam-ai
cd latam-ai
```

Si ya lo has clonado, [sincronízalo con el repo original.](https://stackoverflow.com/a/65401892/709975)

**Paso 2:** Activa tu entorno virtual.

```sh
# conda
conda activate ploomber-workshop

# pip
source ploomber-workshop/bin/activate
```

**Paso 3:** Verifica tu configuración local.

```sh
python check.py
```

**Paso 4:** Inicia JupyterLab


```sh
jupyter lab
```

#### **Opción 2.** JupyterLab hosteado en un servidor

Para simplificar la configuración, te ofrecemos un JupyterLab hosteado en un servidor.

[Regístrate aquí](https://docs.ploomber.io/en/latest/cloud/api-key.html). Luego, accesa al [JupyterLab aquí](https://docs.ploomber.io/en/latest/cloud/guide.html#hosted-jupyterlab).


Una vez que JupyterLab haya iniciado:

**Paso 1:** Clona el repositorio al que has hecho _Fork_.

```sh
git clone https://github.com/{tu-usuario}/latam-ai
cd latam-ai
```

Si ya lo has clonado, [sincronízalo con el repo original.](https://stackoverflow.com/a/65401892/709975)

**Paso 2:** Instala las dependencias.

```sh
# Crea un entorno virtual
conda create --name ploomber-workshop python=3.9 --yes

# Activa el entorno
conda activate ploomber-workshop

# Instala los requerimientos
pip install -r requirements.txt
```

**Paso 3:** Verifica tu configuración local.

```sh
python check.py
```
<!-- #endregion -->


### 1.1 - Refactorizando un cuaderno **_legacy_**

> Vamos a mostrar cómo usar nuestra herramienta de código abierto para convertir cuadernos monolíticos en _pipelines_ de Ploomber con un solo comando.

```sh
cd material
soorgeon refactor notebook.ipynb --df-format parquet --file-format py
```

Abre el archivo [material/pipeline.yaml](material/pipeline.yaml)

```sh
cd material
ploomber plot --backend d3
```

Abre el archivo [material/pipeline.html](material/pipeline.html)


### 1.2 - El archivo `pipeline.yaml`

> El archivo `pipeline.yaml` es donde declararemos las tareaes en nuestro flujo. `soorgeon refactor` ha generado uno para nosotros dado que hemos refactorizado un cuaderno existente, pero si vamos a iniciar un proyecto desde cero podríamos crearlo  manualmente:

```py
from pathlib import Path
from IPython.display import Markdown

def display(path):
    """Utility function to display files
    """
    path = Path(path)
    content = path.read_text()
    ext = path.suffix[1:]
    return Markdown(f'```{ext}\n# content of {str(path)}\n\n{content}\n```')

display('material/pipeline.yaml')
```


### 1.3 - La interfaz de línea de comandos (CLI)

> Vamos a intrducir la interfaz de línea de comandos (CLI), que nos permite gestionar nuestro pipeline: ya sea ejecutar nuestro _workflow_ completamente o parcialmente, generar un diagrama de nuestro pipeline y/o verificar el estado del flujo.

```sh
ploomber --help
```

```sh
cd material
ploomber build
```

```sh
cd material/output
ls
```

También podemos utilizar la API de Python (¡ésta se actualiza en tiempo real!):

```py
from ploomber.spec import DAGSpec

dag = DAGSpec('material/pipeline.yaml').to_dag()
dag.build(force=True)
```

La mayoría de comandos en el CLI tienen un método equivalente en la API de Python:

```sh
cd material
ploomber status
```

```py
dag.status()
```

<!-- #region -->
### 1.4 - Usando Ploomber desde JupyterLab, VSCode o PyCharm

> Mostraremos cómo los profesionales pueden usar Ploomber desde su editor de texto favorito.

#### **JupyterLab:**

No es necesario hacer algo extra, el complemento se instala y configura automáticamente al instalar **Ploomber**. Los archivos `.py` deberían abrirse como cuadernos automáticamente, si no lo hacen, haz click derecho sobre ellos y selecciona *Abrir con > Cuaderno*:

![open-with-notebook](static/lab-open-with-notebook.png)

[Documentation](https://docs.ploomber.io/en/latest/user-guide/jupyter.html)

#### **Otros editores (VSCode, PyCharm, Spyder)**

Ejecuta lo siguiente para inyectar manualmente la celda (y ejecuta nuevamente si has modificado el archivo `pipeline.yaml`):

```sh
ploomber nb --inject
```

[Documentation](https://docs.ploomber.io/en/latest/user-guide/editors.html)

![injected-cell](static/injected.png)

### 1.5 - Parametrización de un pipeline

> Introduciremos el concepto de parametrización, que nos permite ejecutar nuestro pipeline con diferentes parámetros. La parametrización nos ayuda a aplicar el mismo análisis a datos adicionales para organizar nuestros experimentos.

`param` estático:

```yaml
# content of pipeline.yaml

- source: tasks/load.py
  product:
    df: output/load-df.parquet
    nb: output/load.ipynb
  params:
    sample: true
```

**Ejercicio 1:** Modifica `material/pipeline.yaml` y añade un parámtero al  cuaderno `material/tasks/load.py` (bajo la sección de `params`), posterior a ello añade una nueva celda al cuaderno para imprimir el valor del parámetro. Luego, ejecuta lo siguiente y verifica si la salida del cuaderno (`material/output/load.ipynb`) imprime el valor corrrecto:
<!-- #endregion -->

```sh
cd material
ploomber build
```

<!-- #region -->
Convierte `param` en un _placeholder_:

```yaml
# content of pipeline.yaml

- source: tasks/load.py
  product:
    df: output/load-df.parquet
    nb: output/load.ipynb
  params:
    sample: '{{sample}}'
```

Añade `env.yaml`:


```yaml
# content of env.yaml

sample: true
```

**Ejercicio 2:** Convierte `sample` en un _placeholder_, luego crea un archivo `env.yaml`, declara el parámetro `sample` ahí y verifica que el cuaderno se ejecuta sin problema alguno:
<!-- #endregion -->

```sh
cd material
ploomber task load --force
```

```sh
cd material
ploomber task --env--sample false load
```

<!-- #region -->
## Bloque 2: Características avanzadas

### 2.1 - Añadiendo nuevas tareas

> Vamos a mostrar cómo agregar nuevas tareas a nuestro piepeline existente y cómo establecer las relaciones de dependencia entre las tareas.

```yaml
- source: {path/to/source}
  product:
    nb: {path/to/notebook}
    {key}: {path/to/output}
    ...
```

```sh
ploomber scaffold
```

**Ejercicio 3**: Añade un nuevo cuaderno `tasks/fit.py`, luego ejecuta `ploomber scaffold` (dentro de la carpeta `material`) para crear el cuaderno. Posteriormente, agrega el código de `tasks/linear-regression.py`.

### 2.2 - _Builds_ incrementales

> El análisis de datos es un proceso iterativo, y muy a menudo hacemos pequeños cambios y volvemos a ejecutar el código para ver cómo eso afecta nuestros resultados. Vamos a mostrar cómo los _builds_ incrementales permiten a los usuarios ejecutar más experimentos más rápido al almacenar en caché los resultados anteriores.

![incremental](static/incremental.png)

**Ejercicio 4**: Añade una sentencia print a la tarea `tasks/fit.py` (o a cualquier otra tarea) y ejecuta `ploomber build`. Verifica que sólo esa tarea, y cualesquiera dependientes de ella, se ejecutan.
<!-- #endregion -->

<!-- #region -->
## Bloque 3: Escalando tus experimeintos

### 3.1 - Ejecutando experimentos en parelelo

> A menudo queremos ejecutar algún análisis con los mismos datos de entrada, pero con diferentes parámetros. Los usuarios generalmente terminan confiando en el uso de módulos como `multiprocessing` para lograr esto, pero requieren mucho código y conocimientos técnicos. Vamos a mostrar cómo paralelizar experimentos en Ploomber, que gestiona las partes de multiprocesamiento.

![parallel](static/parallel.png)

```yaml
executor: parallel

tasks:
  # ... more tasks here

- source: tasks/fit.py
  name: fit-
  product:
    nb: output/fit.ipynb
  grid:
    model:
      - sklearn.linear_model.LinearRegression
      - sklearn.svm.SVR
      - sklearn.ensemble.GradientBoostingRegressor
      - sklearn.ensemble.RandomForestRegressor
```

Snippet para inicializar modelos desde una cadena de texto:

```py
import importlib

module_name, _, attribute = model.rpartition('.')
module = importlib.import_module(module_name)
lr = getattr(module, attribute)
```

**Ejercicio 5:** Cambia al ejecutor `parallel` y crea una tarea `tasks/fit.py` para entrenar varios modelos al mismo tiempo.

### 3.2 - Ejecución en entornos distribuidos

> Vamos a mostrar cómo los usuarios pueden exportar sus flujos de trabajo locales para ejecutarlos en entornos distribuidos. Por ejemplo, muchas universidades e institutos de investigación tienen clústeres SLURM disponibles. Ploomber puede exportar pipelines a SLURM (y otras plataformas como Kubernetes) para escalar experimentos.

[Documentation](https://soopervisor.readthedocs.io/en/latest/)

Plataformas soportadas (open-source):

* Kubernetes (via Argo Workflows)
* Kubeflow
* SLURM
* Airflow
* AWS Batch

### 3.3 - Ploomber Cloud (free tier):

[Instrucciones para obtener una API Key.](https://docs.ploomber.io/en/latest/cloud/api-key.html)

Almacena la llave:

```sh
ploomber cloud set-key {KEY}
```

Ejecuta en la nube:

```sh
ploomber cloud build
```

Verifica que tu pipeline se ha programado:

```sh
ploomber cloud list
```

Verifica los _logs_:

```sh
ploomber cloud logs {run-id} --image --watch
```

```sh
ploomber cloud logs {run-id} --watch
```

Verifica el estado de las tareas:

```sh
ploomber cloud status {run-id} --watch
```

Descarga las salidas:

```sh
ploomber cloud download '*'
```

**Ejercicio 6:** Ejecuta tu pipeline en la nube.
<!-- #endregion -->

## Conoce más sobre Ploomber

* [Documentación de Ploomber](https://docs.ploomber.io/)
* [Repository de GitHub](https://github.com/ploomber/ploomber) - ¡Muestra tu apoyo con una ⭐️!
* [Comunidad en Slack](https://ploomber.io/community)
