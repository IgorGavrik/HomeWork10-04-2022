from django.shortcuts import render
from django.views import View

class MainView(View):

    def get(self, request):
        context = {
            'form': WriteLineForm(),
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            print(f"{firstname} | {lastname}")
            return render(request, 'form.html', data)