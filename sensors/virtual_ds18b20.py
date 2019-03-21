import random, json

class DS18b20():
    def grab_temp(self, pin):
        print('tu mamy pin: {}'.format(pin))
        rand_temp = random.randrange(-50, 50)
        return [rand_temp]

    def transform_list_to_dict(self, pin):
        temp_in_list = self.grab_temp(pin)
        return {'temp' : temp for temp in temp_in_list}

    def json_temp(self,pin):
        temp_in_dict = self.transform_list_to_dict(pin)
        json_encoder = json.JSONEncoder()
        return json_encoder.encode(temp_in_dict)

if __name__ == '__main__':
    instance = DS18b20()
    print(instance.json_temp(99))