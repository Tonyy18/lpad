import pygame.midi as midi
import threading

class Init:

    def __init__(self, mode="live"):
        self.functions = {}
        self.keys = False #Amount of buttons / leds
        self.mode = mode.lower()

        if(not midi.get_init()):
            midi.init()

        self.input = self.input_port()
        self.output = self.output_port()
        self.clear()

    def poll(self):
        try:
            while True:
                if(self.input.poll()):
                    data = self.input.read(1)
                    status = data[0][0][0]
                    data1 = data[0][0][1] #key
                    data2 = data[0][0][2] #event
                    data3 = data[0][0][3]
                    time = data[0][1]
                    ob = {
                        "status": status,
                        "data": [data1, data2, data3],
                        "timestamp": time
                    }
                    self.processData(ob)

        except KeyboardInterrupt:
            pass
    
    def processData(self, data):
        funcs = self.functions
        if("ondata" in funcs):
            funcs["ondata"](data)

        if(data["data"][1] == 127):
            if("keypress" in funcs):
                funcs["keypress"](data["data"][0])

        if(data["data"][1] == 0):
            if("keyup" in funcs):
                funcs["keyup"](data["data"][0])

        if(data["status"] == 2):
            if("modechanged" in funcs):
                funcs["modechanged"]()
        
        if(data["status"] == 247):
            if("modeready" in funcs):
                funcs["modeready"]()

    def on(self, key, color):
        self.output.note_on(key, velocity=color, channel=0)

    def off(self, key):
        self.output.note_off(key, velocity=0, channel=0)

    def clear(self):
        count = 100
        if(self.keys):
            count = self.keys
        
        for a in range(1, count + 1):
            self.off(a)

    def feature(self, func):
        self.functions[func.__name__.lower()] = func

    def input_port(self):

        for a in range(midi.get_count()):
            device = midi.get_device_info(a)
            name = str(device[1]).lower()
            if("launchpad" in name and device[2]):
                id = a
                if(self.mode != "live"):
                    id = a + 1
                return midi.Input(id)
        return False

    def output_port(self):

        for a in range(midi.get_count()):
            device = midi.get_device_info(a)
            name = str(device[1]).lower()
            if("launchpad" in name and device[3]):
                id = a
                if(self.mode != "live"):
                    id = a + 1
                return midi.Output(id)
        return False

    def close(self):
        self.clear()
        if(self.input):
            self.input.close()
        if(self.output):
            self.output.close()
