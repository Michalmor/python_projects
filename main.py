
#program purpose is to chech a customer's eligibility for a loan of up to 100,000n NIS.
#The program receives data from the user and calculates his grade.
# Writes the customer data to the grade file and loan terms that can be given.
from csvOAPI import Mycsv
from game import game

#from statistics import evaluate
data_path = "data.csv"
result_path = "answers2.csv"
reset = False #change if you want to overwrite your file

def evaluate(answers):
    params = {"workYears": 0,
            "Age": 0,
            "Status": 0,
            "Income": 0}
    
    inspect =  int(answers["Seniority"])
    if inspect < 3:
        params["workYears"] = 0
    elif 3 <= inspect < 5: 
        params["workYears"] = 66
    elif 5 <= inspect < 10:
        params["workYears"] = 113
    elif 10 <= inspect:
        params["workYears"] = 225
         
    inspect =  int(answers["Age"])
    if inspect < 28:
        params["Age"] = 0
    elif 28 <= inspect < 44: 
        params["Age"] = 70
    elif 44 <= inspect < 60:
        params["Age"] = 102
    elif 60 <= inspect:
        params["Age"] = 149
   
    inspect =  answers["Employment status"]
    if inspect == "Employee":
        params["Status"] = 89
    else:
        params["Status"] = 0

    inspect =  int(answers["Total net income (including partner)"]) - int(answers["Other expenses"])
    if inspect < 6000:
        params["Income"] = 0
    elif 6000 <= inspect < 12000: 
        params["Income"] = 58
    elif 12000 <= inspect:
        params["Income"] = 128

    points = sum(params.values())

    if 0 <= points < 170:
        return points, "E", "Rejected"
    elif 170 <= points < 300:
        return points, "D", "P + 14.5%"
    elif 300 <= points < 400:
        return points, "C", "P + 8.5%"
    elif 400 <= points < 591:
        return points, "B", "P + 6.6%"
    elif 591 <= points:
        return points, "A", "P + 5.5%"
        
if __name__ == "__main__":
    # read
    data = Mycsv.read(data_path)

    # Gui and game
    myGame = game(data)     #Build game object
    myGame.start()
    #Initiate game
    answers = myGame.getData()
    # evaluate input
    points, card, value = evaluate(answers) 
    
    if reset:
        Mycsv.reset(result_path , answers.keys()) 

    #Write data
    Mycsv.writeList(result_path, answers.keys())
    Mycsv.writeList(result_path , answers.values())
    Mycsv.writeList(result_path , ["points", "card", "value"])
    Mycsv.writeList(result_path , [points, card, value])