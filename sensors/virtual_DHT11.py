import json, random

class DHT11():

    def grab_temp_and_humanidity(self, pin):
        rand_temps = random.randrange(100)
        rand_humanidity = random.randrange(100)
        print('tu mamy pin: {}'.format(pin))
        return rand_temps, rand_humanidity

    def transform_to_dict(self, pin):
        temps = self.grab_temp_and_humanidity(pin)
        return {title: temp for title, temp in zip(['temp', 'humanidity'],temps)}

    def json_temp(self, pin):
        dict_data = self.transform_to_dict(pin)
        json_encoder = json.JSONEncoder()
        data = json_encoder.encode(dict_data)
        # print(data)
        return data


if __name__ == '__main__':
    instance = DHT11()
    print(instance.json_temp(20))