import tkinter as tk
from tkinter import ttk
import time
import threading
import random

#MCP
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#MCP

#BME
import board
import busio
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
#BME

#import Adafruit_GPIO.SPI as SPI #MCP3008
#import Adafruit_MCP3008
'''
spikids = busio.SPI(board.SCK_1, MOSI=board.MOSI_1, MISO=board.MISO_1)
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spikids, bme_cs)
'''
#MCP
spi = busio.SPI(board.SCK_1, MOSI=board.MOSI_1, MISO=board.MISO_1)
mcp = MCP.MCP3008(spi, digitalio.DigitalInOut(board.D18))
chan = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
#MCP

#BME
spikids = busio.SPI(board.SCK_1, MOSI=board.MOSI_1, MISO=board.MISO_1)
bme_cs = digitalio.DigitalInOut(board.D5)
bme_cs1 = digitalio.DigitalInOut(board.D6)
bme_cs2 = digitalio.DigitalInOut(board.D13)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spikids, bme_cs)
bme2801 = adafruit_bme280.Adafruit_BME280_SPI(spikids, bme_cs)
bme2802 = adafruit_bme280.Adafruit_BME280_SPI(spikids, bme_cs)
#BME


#SPI_PORT   = 1 #MCP3008
#SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#values = [0]*2

def read_sensor():
    #BME    
    # Read all the ADC channel values in a list.
    values = [0]*3
    values[0] = chan.value
    values[1] = chan1.value
    values[2] = chan2.value
    #MCP
    waterlevel = sum(values) / 3
    #BME
    avgTemp = (bme280.temperature+bme2801.temperature+bme2802.temperature)/3
    avgHum = (bme280.relative_humidity+bme2801.relative_humidity+bme2802.relative_humidity)/3
    avgPressure = ((bme280.pressure+bme2801.pressure+bme2802.pressure)/3) * 0.014503768078
    #ave = (bme280.altitude+bme2801.altitude+bme2802.altitude)/3
    #BME
    return avgTemp, avgHum, avgPressure, waterlevel

def check_conditions(temp,hum,press,wl):
    if (temp < 5) or (temp > 40):
        tempcolor = 'red'
    else:
        tempcolor = 'black'
    if wl > 1000:
        wlcolor = 'red'
    else:
        wlcolor = 'black'
    if hum > 80:
        humcolor = 'red'
    else:
        humcolor = 'black'
    return tempcolor, wlcolor, humcolor


def get_case():
    #this will assign a case id somehow
    return 1

def update_labels():
    while True:
        temp, hum, press, wl = read_sensor()
        case_ID = get_case()
        tc, wc, hc = check_conditions(temp,hum,press,wl)
        case_ID_label.config(text=f"Case {case_ID}")
        temp_label.config(text=f"Temperature: {temp:.1f} °C", foreground=tc)
        hum_label.config(text=f"Humidity: {hum:.1f} %", foreground=hc)
        press_label.config(text=f"Pressure: {press:.1f} psi")
        wl_label.config(text=f"Water level: {wl:.1f}", foreground=wc)
        time.sleep(2)

# GUI setup
root = tk.Tk()
root.geometry('320x240')
root.title("Microsoft Scalable Drone Deployment Container")

case_ID_label = ttk.Label(root,text="Case --",font=("Arial",10))
case_ID_label.pack(pady=10)

temp_label = ttk.Label(root, text="Temperature: -- °C", font=("Arial", 10))
temp_label.pack(pady=10)

hum_label = ttk.Label(root, text="Humidity: -- %", font=("Arial", 10))
hum_label.pack(pady=10)

press_label = ttk.Label(root, text="Pressure: -- psi", font=("Arial", 10))
press_label.pack(pady=10)

wl_label = ttk.Label(root, text="Water Reading: -- ", font=("Arial", 10))
wl_label.pack(pady=10)

# Start background thread to update sensor values
threading.Thread(target=update_labels, daemon=True).start()

root.mainloop()
