from src.sensors import virtual_DHT11, virtual_ds18b20

class Container():
    def temp_containter_list(self):
        self.outside = virtual_ds18b20.DS18b20().json_temp(1)
        self.salon = virtual_DHT11.DHT11().json_temp(2)
        self.p1 = virtual_DHT11.DHT11().json_temp(3)
        self.p2 = virtual_DHT11.DHT11().json_temp(4)
        self.bathroom = virtual_DHT11.DHT11().json_temp(5)
        return [self.outside, self.salon, self.p1,
                                  self.p2, self.bathroom]



if __name__ == '__main__':
    instance = Container()
    print(instance.temp_containter_list())