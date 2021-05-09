def calc_angle_between_arrows(h, m):
    if h > 11:
        h -= 12
    assert 0 <= h <= 11, "Incorrect hour"
    assert 0 <= m <= 59, "Incorrect minute"
    minute_angle = m * 6
    hour_angle = h * 30 + m / 2
    clockwise_angle = abs(minute_angle - hour_angle)
    counterclockwise_angle = 360 - clockwise_angle
    print(f"Time --> {h}:{m}")
    print(f"Hour arr --> {hour_angle}°, minut arr --> {minute_angle}°")
    print(f"clockwise angle --> {clockwise_angle}°, counterclockwise angle --> {counterclockwise_angle}°")
