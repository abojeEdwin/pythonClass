def seconds_since_midnight(x,y,z):
	hour_in_seconds = x * 3600
	minute_in_seconds = y * 60
	seconds = z
	number_of_seconds = hour_in_seconds + minute_in_seconds + seconds
	return number_of_seconds


print(seconds_since_midnight(13,30,45))