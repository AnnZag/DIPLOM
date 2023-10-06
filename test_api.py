# Анна Загряжская, 8а когорта - инженер по тестированию плюс. Финальный проект
import data
import sender_stand_request

def test_get_order_by_track():
    # Cоздается новый заказ
    response_order = sender_stand_request.post_new_order(data.order_body)
    track = response_order.json()["track"]

    # Получается заказ по треку
    response_order_by_track = sender_stand_request.get_order_by_track(track)

    assert response_order_by_track.status_code == 200
    print(response_order_by_track.json())
