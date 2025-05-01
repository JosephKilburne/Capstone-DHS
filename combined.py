#MCP
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
#MCP

#BME
import time
import board
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
#BME


#MCP
SPI_PORT   = 1
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#MCP

#BME
spikids = board.SPI()
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spikids, bme_cs)
#BME

#MCP
print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} |'.format(*range(2)))
print('-' * 57)
# Main program loop.
while True:
    #BME    
    # Read all the ADC channel values in a list.
    values = [0]*2
    for i in range(2):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    print('| {0:>4} | {1:>4} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)
    #MCP
    
    #BME
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)
    #BME
    
    
        