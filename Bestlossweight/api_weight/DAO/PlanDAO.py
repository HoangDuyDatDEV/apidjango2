import datetime
from ..models import *

def CreatePlan(UserID,CurrentWeight,TargetWeight,TargetDate):
    plan = Plan.objects.get().UserID.DOB 
    if Plan.TargetDate < datetime.now().strftime("%m/%d/%Y, %H:%M:%S"):
        print(" target time is not less than current time")
    Plan.WeeklyRate=(int) (Plan.TargetDate-datetime.now()).isocalendar[1]
    CurrentWeight= plan.Weight
    height= plan.Height
   
    age=datetime.now().year-Plan.objects.get().UserID.DOB.year
    sex=plan.Sex
    if sex=="Male":
        Plan.BMR=  (10*CurrentWeight+6.25*height-5*age+5)
    elif sex=="Female":
        Plan.BMR= ( 10*CurrentWeight+6.25*height-5*age-161)
    Plan.save()
    return{
        "CurrentWeight":CurrentWeight,
        "TargetWeight":TargetWeight,
        "TargetDate":TargetDate,
        "WeeklyRate":Plan.WeeklyRate,
        "BMR":Plan.BMR,
        "UserID":UserID,
    }
    


  
