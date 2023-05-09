def zad8(**kwargs):
    for key, value in kwargs.items():
        if key == 'hour':
            hour = value
        if key == 'minute':
            minute = value
    hour_ = hour * 30 + minute * 0.5
    minute_ = minute * 6
    return abs(hour_ - minute_)


print(zad8(hour=9, minute=15))
