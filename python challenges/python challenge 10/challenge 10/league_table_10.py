import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents
#comma seperated values
def process(csv_list):
    mydict={}
    for row in csv_list:
        home_team=row[1]
        away_team=row[2]
        home_goal=row[3]
        away_goal=row[4]
        winner=row[5]
        
        if home_team not in mydict:
            mydict[home_team]=[0,0,0,0,0]#win,draw,loss,goal difference and points
        if away_team not in mydict:
            mydict[away_team]=[0,0,0,0,0]
        if winner=="D":
            mydict[home_team][1]+=1
            mydict[away_team][1]+=1

            mydict[home_team][4]+=1
            mydict[away_team][4]+=1
            
        if winner=="H":
            mydict[home_team][0]+=1
            mydict[away_team][2]+=1
            mydict[home_team][4]+=3
            mydict[away_team][4]+=0
        if winner=="A":
            mydict[away_team][0]+=1
            mydict[home_team][2]+=1
            mydict[away_team][4]+=3
            mydict[home_team][4]+=0
            
        goal_difference= int(home_goal)-int(away_goal)
        goal_difference2=int(away_goal)-int(home_goal)
        mydict[home_team][3]+=goal_difference
        mydict[away_team][3]+=goal_difference2
                                
            
    return mydict

def printdictinrow(dictionary1):
    print(f"football team name wins draws: loss: goal difference: points:")
    for key,value in dictionary1.items():
        
        print(f"{key:<30}{value[0]:<5}{value[1]:<5}{value[2]:<5}{value[3]:<5}{value[4]:<5}")
        
        
        
          
 
        
        
    

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    league_dict = process(file_contents)
    printdictinrow(league_dict)
    
     
