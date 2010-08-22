
def ltmo_context(request):

    f = open('README.markdown', 'r')
    return {'about':f}
