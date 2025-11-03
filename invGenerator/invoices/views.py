from django.shortcuts import render

# Create your views here.

def renderPage(request):
    return render(request, 'invoices/test-styles.html')
