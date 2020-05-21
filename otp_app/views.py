from django.shortcuts import render
from django.http import HttpResponse
import random
import qrcode
# Create your views here.
otp = 0


def openLoginPage(request):
    # return HttpResponse('Hello')
    return render(request, 'index.html')


def validateUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        if username == 'aakriti' and password == '1435':
            # create qr code
            random_otp = random.randint(100000, 999999)
            global otp
            otp = random_otp
            image = qrcode.make("OTP is " + str(random_otp))
            image.save(r"otp_app/static/qrimages/aakriti.jpg")
            # return HttpResponse('logged in')
            return render(request, "qr_code_page.html")
        else:
            # return HttpResponse('hello')
            return render(request, 'index.html', {"message": "Invalid User"})


def validateOTP(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        print(user_otp)
        print(otp)
        if user_otp == str(otp):
            return render(request, 'welcome.html')
        else:
            return render(request, 'index.html', {"message": "Invalid OTP. You can Try again"})

    return HttpResponse('hello otp')
