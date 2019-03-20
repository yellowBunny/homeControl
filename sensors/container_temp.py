from src.sensors import virtual_DHT11, virtual_ds18b20, static_container

class Container():
    def temp_containter_list(self):
        self.outside = virtual_ds18b20.DS18b20().grab_temp(10)
        self.salon = virtual_DHT11.DHT11().transform_to_dict(12)
        self.p1 = virtual_DHT11.DHT11().transform_to_dict(13)
        self.p2 = virtual_DHT11.DHT11().transform_to_dict(14)
        self.kitchen = virtual_DHT11.DHT11().transform_to_dict(16)
        self.bathroom = virtual_DHT11.DHT11().transform_to_dict(15)
        temp_in_json =static_container.KeepTempInFile().read_from_json()
        return [self.salon, self.p1, self.p2, self.kitchen, self.bathroom]



if __name__ == '__main__':
    instance = Container()
    print(instance.temp_containter_list())