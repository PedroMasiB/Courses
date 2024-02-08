def add_time(start, duration, day = ''):

    try:
        new_time_list = []
        start_list = start.split(':')
        duration_list = duration.split(':')

        for i in range(len(start_list)-1):
            start_list[i] = int(start_list[i])
            duration_list[i] = int(duration_list[i])
        if start_list[2] == 'PM' and start_list[0] != 12:
            start_list[0] = start_list[0] + 12 
             
        h_result = start_list[0] + duration_list[0]
        m_result = start_list[1] + duration_list[1]
        extra_h = m_result // 60
        left_m = m_result % 60
        h_result = h_result + extra_h
        left_h = h_result % 24
        n = h_result // 24

        if left_h == 0:
            new_time_list.append('00')
        elif left_h > 12:
            new_time_list.append(str(abs(left_h-12)))
        elif left_h < 10:
            new_time_list.append('0' + str(abs(left_h)))
        else:
            new_time_list.append(str(abs(left_h)))

        if left_m == 0:
            new_time_list.append('00')
        elif left_m < 10:
            new_time_list.append('0' + str(left_m))
        else:
            new_time_list.append(str(left_m))
        
        if left_h >= 12:
            new_time_list.append('PM')
        else:
            new_time_list.append('AM')
        

        new_time = new_time_list[0] + ':' + new_time_list[1] + ' ' + new_time_list[2]

        day = day.upper()
        numbers_to_days = {
        1: "MONDAY",
        2: "TUESDAY",
        3: "WEDNESDAY",
        4: "THURSDAY",
        5: "FRIDAY",
        6: "SATURDAY",
        7: "SUNDAY"
        }

        day_key = 0
        for key, value in numbers_to_days.items():
            if value == day:
                day_key = key

        if not day:
            if n == 1:
                new_time += ' (next day)'
            elif n > 1:
                new_time += ' (' + str(n) + ' days later)'
        else:
            if n == 1:
                day_key += n
                new_time += ' ' + numbers_to_days[day_key].capitalize() + ' (next day)'
            elif n > 1 and n < 7:
                day_key += n
                new_time += ' ' + numbers_to_days[day_key].capitalize() + ' (' + str(n) + ' days later)'
            else:
                day_key += n % 7
                new_time += ' ' + numbers_to_days[day_key].capitalize() + ' (' + str(n) + ' days later)'
                 
        return new_time
    except:
        print("Error")
