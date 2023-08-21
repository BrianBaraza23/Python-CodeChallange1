# Challenge 1: Converting 12-hour time to 24-hour time
# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

# You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

# Your task is to return a four-digit string that encodes that time in 24-hour time.


def convert_to_24hr_format(hr, mins, period):
    hr_24 = ""

    if period == "am":
        if hr == 12:
            hr_24 = "00"
        else:
            hr_24 = str(hr).zfill(2)
    elif period == "pm":
        if hr == 12:
            hr_24 = "12"
        else:
            hr += 12
            hr_24 = str(hr)
    else:
        print("Error: Invalid period")
        return None

    hr_24 += str(mins).zfill(2)

    return hr_24

#input your time here

print(convert_to_24hr_format(1, 15, 'pm'))  
