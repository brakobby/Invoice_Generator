from django.shortcuts import render

# Create your views here.


def renderPage(request):
    return render(request, 'index.html')

def dashBoardView(request):
    return render(request, 'invoices/dashboard.html')

def invoice_portal(request):
    return render(request, 'invoices/invoice_portal.html')

def customer(request):
    return render(request, 'invoices/customer.html')

def reports(request):
    return render(request, 'invoices/reports.html')

def settings(request):
    return render(request, 'invoices/settings.html')

def newInvoice(request):
    return render(request, 'invoices/generate-invoice.html')

