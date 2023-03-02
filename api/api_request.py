import requests

class RestfulBooker:
    url = "https://restful-booker.herokuapp.com"

    def create_token(self, body):
        #создание токена
        headers = {'Content-Type': 'application/json'}
        return requests.post(self.url + '/auth', headers=headers, data=body)


    def get_booking_ids(self, body):
        #возвращение идентификаторов бронирования
        return requests.post(self.url + '/booking', data=body)

    def create_booking(self, body):
        #создание бронирования
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        return requests.post(self.url + '/booking', headers=headers, data=body)

    def get_booking(self, id):
        #получение информации о бронировании по id
        headers = {'Accept': 'application/json'}

        return requests.get(self.url + f'/booking/{id}', headers=headers)

restful_booker = RestfulBooker()
