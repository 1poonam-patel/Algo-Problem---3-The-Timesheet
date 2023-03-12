# Defining Time Class

class Time:
        
    def __init__(self,hour,min,sec) :
        self.hour = hour
        self.min = min
        self.sec = sec
        self.totalseconds = self.hour*3600 + self.min*60 + self.sec
        
    def setTotalSeconds(self) :
        self.totalseconds = self.hour*3600 + self.min*60 + self.sec
        
    def getListHMS(seconds) :
        hour = (seconds//3600)
        min = (seconds-hour*3600)//60
        sec= (seconds-hour*3600)%60
        
        return [hour,min,sec]
    
    def _str_(self) :
        return " ".join([self.hour,self.min,self.sec])
        

d = {}

f = open("TT_small.txt","r")
lines = f.readlines()

#setting dictionary

for i in range(1,len(lines)) :
    
    #setting list properly
    
    line = lines[i].split(" ")
    
    line.remove("")
    line.remove("")
    line[-1] = line[-1][:-1:]

    #editing dictionary,
    
    timeList = line[2].split(":")
    timeList = [int(temp) for temp in timeList]

    timeObj = Time(timeList[0],timeList[1],timeList[2])
    dateDictionary = {line[3] : timeObj}
    
    if(line[0] not in d) :
        d[line[0]] = {}
        d[line[0]][line[1]] = dateDictionary
        
    else :
        if line[1] in d[line[0]].keys():
            d[line[0]][line[1]][line[3]] = timeObj
        else :
            d[line[0]][line[1]] = {}
            d[line[0]][line[1]][line[3]] = timeObj
        
# setting work-time per day in dictionary
# listing employee total-work

empWork = []

for emp in d.keys() :
    totalwork = 0
    for date in d[emp].keys() :
        day = d[emp][date]
        if "clock-out" not in d[emp][date].keys() :
            day["clock-out"] = Time(19,30,0)
        
        worktime = day['clock-out'].totalseconds-day["clock-in"].totalseconds
        breaktime = day["break-stop"].totalseconds - day["break-start"].totalseconds 
        d[emp][date]["daywork"] = worktime-breaktime
        
        totalwork += d[emp][date]["daywork"]
    d[emp]["totalwork"] = totalwork
    empWork.append(totalwork)
    
empWork
bestWork = max(empWork)
worstWork = min(empWork)
totalWork = 0
for work in empWork:
    totalWork += work
avgWork = totalWork/len(empWork)

bestTime = Time.getListHMS(bestWork)
worstTime = Time.getListHMS(worstWork)
avgTime = Time.getListHMS(avgWork)


with open("small_output.txt","w") as output:
    output.write(f'{int(bestTime[0])}:{int(bestTime[1])}:{int(bestTime[2])} {int(worstTime[0])}:{int(worstTime[1])}:{int(worstTime[2])} {int(avgTime[0])}:{int(avgTime[1])}:{int(avgTime[2])}')