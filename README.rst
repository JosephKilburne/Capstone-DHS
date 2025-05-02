Capstone-DHS
=============

Dependencies:
=============

Adafruit Blinka

.. code-block:: shell

  sudo pip3 install Adafruit-Blinka

Adafruit ADC 

.. code-block:: shell

  sudo apt-get update

  sudo apt-get install build-essential python-dev python-smbus git

  cd ~

  git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git

  cd Adafruit_Python_MCP3008

  sudo python setup.py install

  sudo pip3 install adafruit-circuitpython-mcp3xxx

Adafruit BME280

.. code-block:: shell

  sudo pip3 install adafruit-circuitpython-bme280

LCD-show

.. code-block:: shell

  git clone https://github.com/waveshare/LCD-show.git

  cd LCD-show/

  sudo ./LCD28-show

Wiring Diagram:
===============

* **LCD** 

SDO - PIN 21/SPMISO

LED - PIN 17/3.3v

SCK - PIN 23/SPSCLK

SDI - PIN 19/SPMOSI

DC - PIN 15/GPIO22

RESET - PIN 13/GPIO27

CS - PIN 24/SPCE0

GND - PIN 6/GND

VCC - PIN 1/3.3v

* **BME280**

* **MCP3008**







