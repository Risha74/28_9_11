from api.api_request import restful_booker
from resources.prepare_data import prepare_data
from serializers.booking import *


def test_base_create_token():

    #подготавливаем данные
    data = prepare_data('create_token')
    #отправляем запрос на создание токена
    create_token = restful_booker.create_token(data)

    assert create_token.status_code == 200, f'{create_token.json()}'


def test_base_get_booking_ids():

    #подготавливаем данные
    data = prepare_data('get_ids')
    #отправляем запрос на получение ids бронирований
    get_ids = restful_booker.get_booking_ids(data)

    assert get_ids.status_code == 200, f'{get_ids.json()}'
    assert get_ids.content == b''


def test_base_create_booking():

    #подготавливаем данные
    data = prepare_data('create_booking')
    #отправляем запрос на создание нового бронирования
    create_booking = restful_booker.create_booking(data)
    #получаем его id
    booking_id = create_booking.json()['bookingid']

    get_booking = restful_booker.get_booking(booking_id)

    assert BodyCreateBooking(**data).dict() == BodyCreateBooking(**get_booking.json()).dict()
    assert get_booking.status_code == 200, f'{get_booking.json()}'
    assert get_booking.content == b''


def test_base_get_booking():
    #подготовливаем данные
    data = prepare_data('get_booking')
    #отправляем запрос на получение бронирования по id
    get_booking = restful_booker.get_booking(data)

    assert get_booking.status_code == 200, f'{get_booking.json()}'
    assert get_booking.content == b''