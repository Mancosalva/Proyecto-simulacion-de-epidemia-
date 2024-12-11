# Modelo de propagación de enfermedad

![d744c463-77cf-412a-b276-27aef77ee82a](https://github.com/user-attachments/assets/460e3182-d745-4744-9a61-73336f5ad3ef)


## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Codigo](https://github.com/Mancosalva/Proyecto-simulacion-de-epidemia-/blob/main/Simulacion%20Epidemia.py)


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
   git clone https://github.com/Mancosalva/Proyecto-Virus-Zombie-Simulacion.git
