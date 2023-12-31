# es-project

Embedded Systems Course Project

- Parsa Mohammadian - 98102284

- Kasra Amani - 98101171

- Reza Erfan - 98105919

- Kahbod Aeini - 98101209

## Introduction

The main idea is creating a smart water container using a proximity sensor to detect user requests and water level sensors to keep track of the water supply's level.

![Device](./Documentation/Device.jpg)

## Requirments

### Hardware

The project is initially implemented on following hardwares but it may work on similar hardwares:

- Raspberry pi 3b+
- HC-SR04
- Water Level Sensor
- LED
- Buzzer
- Servo Motor

### Software

- Python 3.0 (Tested on Python 3.9)
- Raspbian
- Django

## Wiring Harness

The general components wiring is similar to wiring in the schematic bellow.
![circuit](./Documentation/circuit.png)
The exact wiring and gpio ports are defined as constants in python files in `Modules` directory.

## Embedded System Design and Logic

The project contains multiple python modules including water, ultrasonic distance, buzzer, actuator and LED; these modules each contain methods and classes reagarding the specific section of the ES and when creating the main module integrating all of them together, we have used these modules to operate the actuator and buzzer.

## Web App

The user interface of this system is based on a web app. This web app is developed by Django framework. The server is running on the local host of Raspberry pie module. The documantation is divided to front-end and back-end modules and we explore how the web app is developed in what follows.

### Back-end

As we mentioned app's framework is Django. The Django server contains one single-responsibility app, named app. The function of this app is just to read the Water Level from a file, namely '/var/tmp/coleman/API.txt'. This app changes periodically by the water level module (water.py in the Modules folder). Reading from this file and changing the WLP variable, alters the water level in the UI, that is handled in the front-end.

### Front-end

User interface of the web app is based on plain HTML, CSS and a little bit of JavaScript. The UI is designed to be responsive and user-friendly. The UI is divided to 4 main parts:

- Clock
- Water Level Liquid Bar
- Water Level Percentage
- Water Level Status

## How to Run

The project consists of two main parts. First you should run the web app in order to show coleman info in raspberry pi or any device in local network.

```bash
python "ES WebApp/ES_WebApp/manage.py" runserver 0.0.0.0:8000
```

Then the web app will be accessible on `<raspberry pi ip address>:8000`.
Second you should run the `main.py` file which reads sensors, process data, and activate actuators.

```bash
python Modules/main.py`
```

## Test and Performance

Watch [working system video](./Documentation/Report.MOV).
![ui-0](Documentation/ui-0.png)
![ui-0](Documentation/ui-33.png)
![ui-0](Documentation/ui-66.png)
![ui-0](Documentation/ui-100.png)
