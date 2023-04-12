def avg_rainfall(day_list):
    non_negative_days = 0
    total_rain = 0
    for rain in day_list:
        if rain >= 0:
            total_rain += rain
            non_negative_days += 1
    if non_negative_days >0:
        average = total_rain / non_negative_days
        return "average rainfall is", average
    else:
        return "no rain"
print(avg_rainfall([-4,- 4,- 8]))

