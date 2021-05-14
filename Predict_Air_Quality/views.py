from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(SO, NO, RSPM, SPM):
    import pickle
    model = pickle.load(open("model.pkl", "rb"))
 
    prediction = model.predict([[SO,NO,RSPM,SPM]])

    return prediction
        

# our result page view
def result(request):
    so = int(request.GET['so'])
    no = int(request.GET['no'])
    rspm = int(request.GET['rspm'])
    spm = int(request.GET['spm'])

    result = getPredictions(so,no,rspm,spm)

    return render(request, 'result.html', {'result':result})

    