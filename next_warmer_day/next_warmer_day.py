dates = [12, 16, 10, 9, 15, 19, 18]
result = []

for date_index, date in enumerate(dates):
    remaining_dates = dates[date_index:]

    for rd_index, remaining_date in enumerate(remaining_dates):
        if date < remaining_date:
            result.append(rd_index)
            break
        else:
            if rd_index == (len(remaining_dates) - 1):
                result.append(0)

print(result)