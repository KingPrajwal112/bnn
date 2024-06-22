from django.shortcuts import render
from joblib import load


model=load("./SaveModels/model12")
def predictor(request):
    return render(request,"index.html")

def formInfo(request):
    Age=int(request.GET["age"])
    Sex=int(request.GET["sex"])
    Chest_pain=int(request.GET["chest_pain"])
    Bp=int(request.GET["bp"])
    Choresterol=int(request.GET["choresterol"])
    Fbp=int(request.GET["fbp"])
    Electrograph=int(request.GET["electrograph"])
    Max=int(request.GET["max"])
    Angina=int(request.GET["angina"])
    Oldpeak=int(request.GET["oldpeak"])
    Slope=int(request.GET["slope"])
    Vessels=int(request.GET["vessels"])
    Thal=int(request.GET["thal"])
    

    kk=model.predict([[Age,Sex,Chest_pain,Bp,Choresterol,Fbp,Electrograph,Max,Angina,Oldpeak,Slope,Vessels,Thal]])
    return render(request,"result.html",{"result":kk})
