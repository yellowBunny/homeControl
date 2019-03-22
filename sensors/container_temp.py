import os
print(os.getcwd())
from sensors import dht11, ds18b20

class Container():
    FILE_PATH = 'temp.json'
    def temp_containter_list(self):
##        self.outside = ds18b20.DS18b20.grab_temp()
        self.salon = dht11.DHT11().transform_to_dict(16)
        self.p1 = dht11.DHT11().transform_to_dict(12)
        self.kitchen = dht11.DHT11().transform_to_dict(7)
        self.p2 = dht11.DHT11().transform_to_dict(20)
        self.bathroom = dht11.DHT11().transform_to_dict(21)
        container = [self.salon, self.p1, self.kitchen, self.p2, self.bathroom]
        for i in range(len(container)):
            print(i+1, container[i])        
        return container
    
    def json_container(self):
        '''method who saved data in list to json file'''
        contenet_obj = static_container.KeepTempInFile()
        temp_list = self.temp_containter_list()
        contenet_obj.save_to_json(self.FILE_PATH, temp_list)



if __name__ == '__main__':
    instance = Container()
    print(instance.temp_containter_list())