def add_time(start, duration, day=False):
    start_hour = int(start[0 : start.find(':')])
    start_min = int(start[start.find(':') + 1 : start.find(':') + 3])
    noon = start[-2:]
    duration_hour = int(duration[0 : duration.find(':')])
    duration_min = int(duration[-2:])    
    if noon == 'PM' :
        total_minutes = start_hour*60 + start_min + duration_hour*60 + duration_min + 12 *60        
    else :
        total_minutes = start_hour*60 + start_min + duration_hour*60 + duration_min  
    total_hours= int(total_minutes / 60)
    minutes_left = total_minutes % 60
    if minutes_left < 10 :
        minutes_left = "0"+str(minutes_left)
    hour = total_hours % 24
    if hour < 12 :
        time = " AM"
        if hour == 0 :
          hour = 12
    elif hour == 12 :
        time = " PM"
    elif hour == 24 :
        time = " AM"
        hour = hour - 12
    else : 
        time = " PM"
        hour = hour - 12
    days_passed = total_hours // 24    
    if days_passed == 0 :
      days = ""
    elif days_passed == 1 :
      days = " (next day)"
    else :
      days = " (" + str(days_passed) + " days later)"
    if day is False :
      return str(hour)+":"+str(minutes_left) + time +  days
    else :
      weekdays = ['monday', 'tuesday','wednesday', 'thursday', 'friday','saturday', 'sunday']
      index = weekdays.index(day.lower())    
      if days_passed == 0 :
        return str(hour)+":"+str(minutes_left) + time+', '+ weekdays[index].title() +  days 
      else :
        return str(hour)+":"+str(minutes_left) + time+', '+ weekdays[(index+days_passed)%7].title() +  days
      