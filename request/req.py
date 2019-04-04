import requests, requests_html

class MyExceptions(Exception):
    pass

class ParsDataFromURL():
    '''this class parse data from url'''

    def load_data_from_url(self, url=None):
        '''load in string all content on site'''
        try:
            obj = requests.get(url)
            print(obj.text)
            return obj.text
        except:
            raise MyExceptions("brak adresu url (ULR adress doesn't set correctly)")

    def parse_data(self, obj_to_parse, search_tag=None):
        '''parse data and return list with dict [{'hour': x}, {'minute': y}] with text bettwen input tags'''

        time_container = []
        url_data_to_parse = requests_html.HTML(html=obj_to_parse)
        tag_list = url_data_to_parse.find(search_tag)
        for i, tag in enumerate(tag_list, 1):
            print('{0} | {1} | {2}'.format(i, search_tag, tag.text))
            time_container += [tag.text]
        d = {strings: time_unit for strings, time_unit in zip(['hour', 'minute'], time_container)}
        print(d)
        return [d]




if __name__ == '__main__':
    load = ParsDataFromURL()
    data = load.load_data_from_url('http://127.0.0.1:8000/sockets/')
    print(load.parse_data(data, 'h3'))