import os
import json
class KeepTempInFile():

    def save_to_json(self,file_name, data):
        with open(file_name, 'w') as file:
            json.dump(data, file)


    def read_from_json(self, file_name):
        with open(file_name, 'r') as file:
            readed_data = json.load(file)
        return readed_data == 1


if __name__ == '__main__':
    print(os.getcwd())
    # instance = KeepTempInFile()
    # json_encoder = json.JSONEncoder()
    # d = {'D':1, 'B':2}
    # data = json_encoder.encode(d)
    # # instance.save_to_json('empty.json',{})
    # v = instance.read_from_json('temp.json')
    # print(1 if v else 0)
