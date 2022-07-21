import datetime
from ..models import *

def CreatePlan(UserID,CurrentWeight,TargetWeight,TargetDate):
    plan = Plan.objects.get().UserID
    if Plan.TargetDate < datetime.now().strftime("%m/%d/%Y, %H:%M:%S"):
        print(" target time is not less than current time")
    WeeklyRate=(int) (Plan.TargetDate-datetime.now()).isocalendar[1]
    CurrentWeight= plan.Weight
    height= plan.Height
    age=datetime.now().year-plan.DOB.year
    sex=plan.Sex
    if sex=="Male":
        BMR=  (10*CurrentWeight+6.25*height-5*age+5)
    elif sex=="Female":
        BMR= ( 10*CurrentWeight+6.25*height-5*age-161)
    Plan.objects.create(UserID,CurrentWeight=CurrentWeight,TargetWeight=TargetWeight,TargetDate=TargetDate,WeeklyRate=WeeklyRate,BMR=BMR)
    return{
        "CurrentWeight":CurrentWeight,
        "TargetWeight":TargetWeight,
        "TargetDate":TargetDate,
        "WeeklyRate":WeeklyRate,
        "BMR":BMR,
    }
    


  
