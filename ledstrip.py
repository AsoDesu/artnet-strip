from rpi_ws281x import *

LED_MASTER_CHANNEL_WIDTH = 1
LED_CELL_CHANNEL_WIDTH = 4

class LedStripCell:
    def __init__(self, master, pixel: int, address: int):
        self.master = master
        self.strip = master.strip
        self.address = address
        self.pixel = pixel
    
    def on_dmx_data(self, data: list[int]):
        # cell intensity - also affected by master
        intens = (data[self.address] / 255) * self.master.master_intensity
        # RGB for this cell
        red = data[self.address+1] * intens
        green = data[self.address+2] * intens
        blue = data[self.address+3] * intens

        self.strip.setPixelColor(self.pixel, Color(int(red), int(green), int(blue)))

class LedStrip:
    master_intensity = 0.0
    cells: list[LedStripCell] = []

    def __init__(self, cell_count: int, address: int, strip):
        self.strip = strip
        self.address = address
        strip.begin()

        for i in range(cell_count):
            cell_address = self.address + LED_MASTER_CHANNEL_WIDTH + (i * LED_CELL_CHANNEL_WIDTH)
            self.cells.append(LedStripCell(self, i, cell_address))

    def on_dmx_data(self, data: list[int]):
        self.master_intensity = data[self.address] / 255
        for cell in self.cells:
            cell.on_dmx_data(data)
        self.strip.show()

    def close(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()