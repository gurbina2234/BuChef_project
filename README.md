# 2024-1-CC4401-1-grupo-10
# Proyecto BuChef

Este proyecto es una aplicación web desarrollada en Django para los estudiantes de la Facultad de Ciencias Físicas y Matemáticas (FCFM), cuyo objetivo es facilitar la elección del mejor lugar para comer cerca de la universidad. 

### Features
- Los usuarios pueden crear su propia cuenta, avisandoles cuando esto se logra exitosamente para que realicen el inicio de sesión.
- Los usuarios pueden iniciar sesión en la página con su cuenta de tenerla, de lo contrario se les notifica que deben crearla.
- Los usuarios podrán añadir reseñas a un restaurante determinado  incluyendo rating, comentario,foto , fecha (de manera opcional) y categorías que describen el local solo cuando han inciado sesión, de no estarlo se muestra una alerta avisando de esto.
- Los usuarios pueden filtrar los locales por las categorías proveídas.
- Los usuarios pueden visualizar la información actual (calificación, categorías y cantidad de reviews) de un local en específico.
- Los usuarios pueden visualizar las reseñas creadas por si mismo y otros usuarios de un local en especifico.
- Los usuarios pueden agregar un local entregando el nombre, dirección y fotografía de este al encontrarse con una sesión iniciada.
  

### Pre-requisitos 

Para visualizar e interactuar con este proyecto, se debe clonar en el computador (hacer uso de git clone).

>Se debe correr el proyecto en un nuevo ambiente virtual utilizando el requirements.txt que tiene este proyecto (se debe crear este virtual env dentro de la carpeta grupo10).

1. `python3 -m venv myvenv` en Linux o `python -m venv myvenv` en Windows para crear el nuevo ambiente virtual.
2. `source myvenv/bin/activate` en Linux o `myvenv\Scripts\activate` en Windows para iniciar el ambiente virtual.
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`

Una vez instalado todo lo anterior, es posible correr el servidor de django, con el siguiente comando:

```
python manage.py runserver
```
Finalmente, abrir en el navegador y entrar con la siguiente url `http://127.0.0.1:8000/home`

## Herramienta utilizada

* [Django 3.2.25]

## Autores 

* **Nicolás Del Valle R.** 
* **Antonia G. Calvo**
* **Alejandro Mori A.**
* **Benjamín Reyes B.**
* **Gabriela Urbina G.**
* **Vicente Zamora S.** 
 
