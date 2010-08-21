from django.views.generic import list_detail, simple

def index(request):
    return simple.direct_to_template(request,'index.html')

def new_post(request):
    import ipdb; ipdb.set_trace()    
    return simple.direct_to_template(request,'success.json' , mimetype='application/json')
