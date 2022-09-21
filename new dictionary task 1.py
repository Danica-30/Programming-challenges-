def splitdate(date):
    newdate= date.split("-")
    return newdate

date1= input("please enter a date in the form (dd-mmm-yy) e.g: 8-mar-85:")

list_dates =splitdate(date1)

month ={"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":7,"sep":8,"oct":9,"nov":10,"dec":11}

for list_dates[1] in month.keys():
    if month==list_dates[1]:
    
    
    
