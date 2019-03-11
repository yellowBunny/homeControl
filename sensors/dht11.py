import Adafruit_DHT, json
from datetime import datetime 

class PinConectionError(Exception):
    def __ini__(self,mgs):
        Exception.__init__(self,mgs)
        
class DHT11:    
    def grab_temp(self, pin=0):
        if pin:                
            # set sensor DHT11        
            sensor = Adafruit_DHT.DHT11
            # set temp and humanidity
            humanidity, temp = Adafruit_DHT.read_retry(sensor, pin)
            print('temp: {} C\nhumanidity: {} %'.format(temp, humanidity))
            return temp, humanidity        
        else:
            print('Set Pin!!')
            raise PinConectionError('Check GPIO pin connection and try again')
        
    def JSONtemp(self, pin):
        'transform tuple to dict and to json data '
        temp_from_sensor = self.grab_temp(pin) #tuple
        d = {key: val for key,val in zip(['temperature','humanidity'], temp_from_sensor)} # dict
        json_encoder = json.JSONEncoder() #sprawdzic zamiast biblioteki json mozna zastosowac po prostu '{}'.format(d) bo po konwersji przez json
        temp = json_encoder.encode(d) # zwraca string 
        return temp #json format
            
            

if __name__ =='__main__':
    instance = DHT11()
##    instance.grab_temp(1)
##    instance.grab_temp(16)
##    instance.grab_temp(12)
    print(instance.JSONtemp(16))