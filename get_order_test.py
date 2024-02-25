# Дмитрий Алман, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request



def test_get_order():
    track = sender_stand_request.get_order_track()
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200

