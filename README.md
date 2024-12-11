# Modelo de propagación de enfermedad

![d744c463-77cf-412a-b276-27aef77ee82a](https://github.com/user-attachments/assets/460e3182-d745-4744-9a61-73336f5ad3ef)


## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Reglas](#reglas-del-automata)
5. [Codigo](https://github.com/Mancosalva/Proyecto-simulacion-de-epidemia-/blob/main/Simulacion%20Epidemia.py)
6. [Video](https://youtu.be/Rkhmkz2bDsU)
7. [Diapositivas](https://www.canva.com/design/DAGY7mXZcAs/5XaHi5yo-jfHTEkdyhPcJg/edit)


## Descripción

Este proyecto se basa en la simulacion de una epidemia, siendo este un automata celular basado el juego de la vida de John Horton Conway de 1970.

## Características

- Si una persona tiene un vecino infectado este tiene una posibilidad de infectarse 
- Despues de cierta cantidad de iteracciones si una persona esta infectada existe la probabilidad de que esta muera
- Si despues de cierta cantidad de iteraciones una persona infectada no a muerto esta se recuperara
- Si una persona sana ha pasado cierta cantidad de iteraciones sin ser infectado entrara en cuarentena y no podra ser infectado
- Se puede elegir si una persona Recuperada puede volver a ser infectada y cuantas veces esto puede ocurrir

## Instalación

### Requisitos previos

Antes de instalar este proyecto, asegúrate de tener instalados:

- pip install matplotlib
- pip install numpy

### Instrucciones de instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Mancosalva/Proyecto-simulacion-de-epidemia.git

## Reglas del Automata

![1](https://github.com/user-attachments/assets/dc4e8cd4-5de8-47e3-a6d7-dea0c79c7dbd)

![2](https://github.com/user-attachments/assets/898055ad-7dd8-461a-9d13-7c256b13fdbf)

![3](https://github.com/user-attachments/assets/79d45232-f318-4a89-b2dd-3a2e65b6123e)
