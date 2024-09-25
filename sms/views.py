from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
import requests 
import openpyxl
from app1.models import ActiveBranch, Customer
from sms.models import SMSReport
from environ import Env

env = Env()
Env.read_env()
token=env('TOKEN')
greenweburl=env('SMS_URL')


@login_required
@permission_required('sms.add_smsreport', raise_exception=True)
def sms_single(request):
    if request.method == "POST":
        msg = request.POST.get('sms_body')
        to_numbers = request.POST.get('mobile').replace(' ', '')
        phone_numbers = to_numbers.split(',')

        response_texts = []
        for number in phone_numbers:
            data = {'token': token, 'to': number, 'message': msg}
            response = requests.post(url=greenweburl, data=data)
            response_texts.append(response.text)

            SMSReport.objects.create(
                sms_type="Single SMS",
                mobile_number=number,
                sms_body=msg,
                sent_by=request.user.username)

        context = {
            'response_texts': response_texts
        }
        return render(request, 'sms/sms_single.html', context)
    else:
        return render(request, 'sms/sms_single.html')


@login_required
@permission_required('sms.add_smsreport', raise_exception=True)
def sms_bulk(request):
    if request.method == "POST":
        msg = request.POST.get('sms_body')
        file = request.FILES['filename']

        wb = openpyxl.load_workbook(file)
        sheet = wb.active

        phone_numbers = []
        for row in sheet.iter_rows(min_row=2, min_col=1, max_col=1, values_only=True):
            if row[0]:
                phone_numbers.append(str(row[0]).strip())

        to = ','.join(phone_numbers)

        data = {'token': token, 'to': to, 'message': msg} 
        response = requests.post(url=greenweburl, data=data) 
        response_text = response.text 

        for number in phone_numbers:
            SMSReport.objects.create(
                sms_type="Bulk SMS",
                mobile_number=number,
                sms_body=msg,
                sent_by=request.user.username)

        context = {'response_text': response_text}
        return render(request, 'sms/sms_bulk.html', context)
    else:
        return render(request, 'sms/sms_bulk.html')


@login_required
@permission_required('sms.add_smsreport', raise_exception=True)
def sms_customer(request):
    response_texts = [] 
    if request.method == "POST":
        customer_type = request.POST.get('type')
        sms_body = request.POST.get('sms_body')


        branch = ActiveBranch.objects.get(user=request.user).branch
        customers = Customer.objects.filter(branch=branch)

        if customer_type == "only_active_member":
            customers = customers.filter(status='Active')
        elif customer_type == "all_dps":
            customers = customers.filter(dps__isnull=False).distinct()
        elif customer_type == "only_active_dps":
            customers = customers.filter(dps__status='active').distinct()
        elif customer_type == "all_loan":
            customers = customers.filter(loanac__isnull=False).distinct()
        elif customer_type == "only_active_loan":
            customers = customers.filter(loanac__status='active').distinct()
        elif customer_type == "all_fdr":
            customers = customers.filter(fdr__isnull=False).distinct()
        elif customer_type == "only_active_fdr":
            customers = customers.filter(fdr__status='active').distinct()

        
        for customer in customers:
            to = customer.mobile_number
            data = {'token': token, 'to': to, 'message': sms_body}
            responses = requests.post(url=greenweburl, data=data)
            response_texts.append(responses.text)

            SMSReport.objects.create(
                sms_type=customer_type,
                mobile_number=to,
                sms_body=sms_body,
                sent_by=request.user.username
            )

    context = {
        'response_texts': response_texts
    }
    return render(request, 'sms/sms_customer.html', context)


@login_required
@permission_required('sms.add_smsreport', raise_exception=True)
def sms_report(request):
    sms_reports = SMSReport.objects.all().order_by('-id')

    context = {
        'sms_reports': sms_reports
    }
    return render(request, 'sms/sms_report.html', context)


