Capstone-DHS
=============

Dependencies:
=============

Adafruit Blinka

.. code-block:: shell

  sudo pip3 install Adafruit-Blinka

Adafruit ADC 

.. code-block:: shell

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

SDO - PIN 35/GPIO19/SPMISO_1

SCK - PIN 40/GPIO20/SPSCLK_1

SDI - PIN 38/GPIO21/SPMOSI_1

CS - PIN 29/GPIO5

CS1 - PIN 31/GPIO6

CS2 - PIN 33/GPIO13

GND - PIN 6/GND

VCC - PIN 1/3.3v


* **MCP3008**

SDO - PIN 35/GPIO19/SPMISO_1

SCK - PIN 40/GPIO20/SPSCLK_1

SDI - PIN 38/GPIO21/SPMOSI_1

CS - PIN 12/GPIO18/SPI1CE0

GND - PIN 6/GND

VCC - PIN 1/3.3v

Water sensor 1 - MCP3008 Channel 0

Water sensor 2 - MCP3008 Channel 1

Water sensor 3 - MCP3008 Channel 2


.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

