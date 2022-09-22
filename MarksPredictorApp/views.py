from django.shortcuts import render, HttpResponse
import joblib
import pandas as pd
import numpy as np


# Create your views here.

def indexPage(request):
    return render(request, 'index.html')


def predict(request):

    model = joblib.load(r'static\student_mark_predictor.pkl')

    input_features = [int(request.POST.get('hours'))]
    print(input_features)
    features_value = np.array(input_features)
    if input_features[0] < 0 or input_features[0] > 24:
        return HttpResponse("<script>alert('A day only has 24 hours, Enter a value between 0 and 24')</script>")
    else:
        score = model.predict([features_value])[0][0].round(2)
        response = {'score':score, 'name': request.POST.get('name')}
        return render(request, 'result.html', response)




