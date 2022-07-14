from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def profile(request):
    return render(request, 'main/profile.html')
