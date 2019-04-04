import os
import json
class KeepTempInFile():
    def save_to_json(self, file_name, data):
        '''saved data to .json file'''
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file)
            print('succes data was saved!!', data, '\n')
            return True
        except:
            return False

    def read_from_json(self, file_name):
        '''read data from .json file.
         if dose't data in file return false orherwise return readed data'''
        try:
            with open(file_name, 'r') as file:
                readed_data = json.load(file)
                # print('retuned data form read_form_json func', readed_data , '\n')
            return readed_data
        except:
            print('JSON file is empty!!')
            return False


if __name__ == '__main__':
    print(os.getcwd())
    instance = KeepTempInFile()
    # json_encoder = json.JSONEncoder()
    # d = {'D':1, 'B':2}
    # data = json_encoder.encode(d)
    # # instance.save_to_json('empty.json',{})
    v = instance.read_from_json('temp.json')
    print(v)
    print(1 if v else 0)

