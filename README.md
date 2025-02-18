# Iniciativas Emprendedoras: Ejercicios de Python para Machine Learning y Calidad

Bienvenido al repositorio de **Iniciativas Emprendedoras**. Aquí encontrarás todos los ejercicios en Python (presentados en notebooks de Google Colab) diseñados para profundizar en los fundamentos de Machine Learning, Calidad en la Industria y Preparación y Análisis de Datos. Este repositorio incluye ejercicios para cada team y un sistema de corrección automatizado con GitHub Actions.

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Cómo Empezar](#cómo-empezar)
- [Ejercicios Destacados](#ejercicios-destacados)
  - [Ejercicio 1: Extracción e Integración de Datos desde Fuentes Online](#ejercicio-1-extracción-e-integración-de-datos-desde-fuentes-online)
- [Sistema de Corrección Automatizado](#sistema-de-corrección-automatizado)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

---

## Descripción

Este repositorio está orientado a proporcionar ejercicios prácticos para la formación en **Machine Learning y Calidad en la Industria**. Cada notebook está diseñado para guiarte paso a paso en la resolución de ejercicios mediante instrucciones interactivas y "TODOs" que deberás completar.

**Objetivos principales:**
- Aprender a cargar y procesar datos desde fuentes online (por ejemplo, repositorios abiertos en GitHub o Kaggle).
- Explorar y fusionar datasets utilizando claves comunes.
- Preparar y limpiar datos para su análisis y modelado.
- Implementar un sistema de corrección automatizado para evaluar tus soluciones.

---

## Estructura del Repositorio


├── ejercicios/ │ ├── Ejercicio_1_Extraccion_Integracion.ipynb │ ├── Ejercicio_2_Limpieza_Validacion.ipynb │ └── Ejercicio_3_Preprocesamiento_Modelado.ipynb ├── teams/ │ ├── team1/ │ │ └── ejercicios_colab_team1.ipynb │ └── team2/ │ └── ejercicios_colab_team2.ipynb ├── tests/ │ └── test_grade.py ├── .github/ │ └── workflows/ │ └── grade.yml └── README.md


- **`ejercicios/`**: Contiene los notebooks principales con los ejercicios.
- **`teams/`**: Directorios con ejercicios personalizados para cada equipo.
- **`tests/`**: Scripts de validación y pruebas automatizadas.
- **`.github/workflows/`**: Configuración de GitHub Actions para la corrección automatizada.

---

## Cómo Empezar

1. **Abrir en Google Colab**: 
   - Navega al notebook que deseas trabajar y haz clic en el botón "Open in Colab" (puedes incluir badges de Colab en el README).
   - Ejemplo: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tu_usuario/tu_repo/blob/main/ejercicios/Ejercicio_1_Extraccion_Integracion.ipynb)

2. **Completa los "TODOs"**: 
   - Cada notebook contiene celdas con comentarios `# TODO` y preguntas de reflexión. Sigue las instrucciones y completa tu solución.

3. **Ejecuta y verifica**: 
   - Una vez finalizado, guarda tu trabajo y, si estás colaborando a través de GitHub, haz push de tus cambios.

---

## Ejercicios Destacados

### Ejercicio 1: Extracción e Integración de Datos desde Fuentes Online

- **Objetivo:** Cargar dos datasets desde URLs (CSV y JSON), identificar la clave común y fusionarlos en un único DataFrame.
- **Características:**
  - Uso de datos desde repositorios abiertos (por ejemplo, GitHub o Kaggle).
  - Preguntas interactivas y celdas de "TODO" para que completes el código.
  - Reflexiones sobre diferencias entre formatos y opciones de merge.

_Revisa el notebook [Ejercicio_1_Extraccion_Integracion.ipynb](./ejercicios/Ejercicio_1_Extraccion_Integracion.ipynb) para comenzar._

---

## Sistema de Corrección Automatizado

Utilizamos **GitHub Actions** para evaluar de forma automática los ejercicios. Cada vez que se realice un push o pull request, el workflow definido en `.github/workflows/grade.yml` se ejecutará, utilizando herramientas como **papermill** para ejecutar los notebooks y **pytest** para validar resultados clave.

_Puedes revisar el archivo [grade.yml](./.github/workflows/grade.yml) para ver la configuración._

---

## Contribuciones

¡Tus contribuciones son bienvenidas! Si deseas proponer mejoras, nuevos ejercicios o adaptar la plantilla para otros equipos, por favor sigue estos pasos:

1. Crea una rama nueva para tu contribución.
2. Realiza los cambios pertinentes.
3. Envía un pull request describiendo los cambios y la motivación detrás de ellos.

---

## Licencia

Este repositorio se distribuye bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles. Además, el material didáctico puede estar sujeto a una licencia Creative Commons (CC BY-SA) para fomentar su uso educativo.

---

## Contacto

Para cualquier duda, sugerencia o comentario, por favor contacta a:
- **Nombre:** [Tu Nombre]
- **Email:** [tu.email@ejemplo.com]
- **Sitio web:** [www.iniciativasempresariales.com](https://www.iniciativasempresariales.com)

¡Esperamos que disfrutes y aprendas mucho con estos ejercicios!

---

