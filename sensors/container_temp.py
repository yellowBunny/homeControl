from sensors import virtual_DHT11, virtual_ds18b20, static_container

class Container():
    FILE_PATH = 'temp.json'


    def temp_containter_list(self):
        try:
            self.outside = virtual_ds18b20.DS18b20().grab_temp(10)
            self.salon = virtual_DHT11.DHT11().transform_to_dict(12)
            self.p1 = virtual_DHT11.DHT11().transform_to_dict(13)
            self.p2 = virtual_DHT11.DHT11().transform_to_dict(14)
            self.kitchen = virtual_DHT11.DHT11().transform_to_dict(16)
            self.bathroom = virtual_DHT11.DHT11().transform_to_dict(15)
            return [self.salon, self.p1, self.p2, self.kitchen, self.bathroom]
        except:
            return False

    def json_container(self):
        '''method who saved data in list to json file'''
        contenet_obj = static_container.KeepTempInFile()
        temp_list = self.temp_containter_list()
        contenet_obj.save_to_json(self.FILE_PATH, temp_list)





if __name__ == '__main__':
    instance = Container()
    print(instance.temp_containter_list())
    # instance.json_container()