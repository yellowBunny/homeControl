import os
print(os.getcwd())
from sensors import dht11, ds18b20

class Container():
    def temp_containter_list(self):
##        self.outside = ds18b20.DS18b20.grab_temp()
        self.salon = dht11.DHT11().transform_to_dict(16)
        self.p1 = dht11.DHT11().transform_to_dict(12)
        self.p2 = dht11.DHT11().transform_to_dict(7)
##        self.kitchen = virtual_DHT11.DHT11().transform_to_dict(16)
##        self.bathroom = virtual_DHT11.DHT11().transform_to_dict(15)
        return [self.salon, self.p1, self.p2]



if __name__ == '__main__':
    instance = Container()
    print(instance.temp_containter_list())