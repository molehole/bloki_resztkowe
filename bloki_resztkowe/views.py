from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'bloki_resztkowe/index.html', {})

def pobierz_blok(request):
    wpisy = {
        'typ_zadania': 'pobierz',
        'rodzaje_pianki': Pianka.objects.all(),
    }
    return render(request, 'bloki_resztkowe/wybierz_blok.html', wpisy)

def wprowadz_blok(request):
    wpisy = {
        'typ_zadania': 'Wprowadz',
        'rodzaje_pianki': Pianka.objects.all(),
    }
    return render(request, 'bloki_resztkowe/wybierz_blok.html', wpisy)

def nowy_nesting(request):
    if request.POST:
        nesting_id = request.POST.get('nesting_id', None)
        wybrany = Nesting.objects.get(id=nesting_id)
        wybrany.zatwierdz()
        return HttpResponse()


def zakonczenie_nestingu(request):
    if request.POST:
        nesting_id = request.POST.get('nesting_id', None)
        wybrany = Nesting.objects.get(id=nesting_id)
        wybrany.zakoncz()
        return HttpResponse()

def zaplanuj(request):
    wpisy = {}
    do_zaplanowania = Nesting.objects.filter(zatwierdzony=False).order_by('pianka__typ')
    wpisy['do_zaplanowania'] = do_zaplanowania
    wpisy['planowanie'] = True  
    wpisy['typ_zadania'] = 'Zaplanuj'
    return render(request, 'bloki_resztkowe/potwierdz.html', wpisy)

def wybor(request, typ_zadania, pianka):
    if pianka == 'wszystkie':
        wpisy = {
            'wybrany_wymiar': 'Wszystkie',
            'typ_zadania': typ_zadania,        
        }
        zaplanowane = Nesting.objects.filter(zatwierdzony=True, zakonczony=False).order_by('pianka__typ')
        do_zaplanowania = Nesting.objects.filter(zatwierdzony=False).order_by('pianka__typ')
        wpisy['do_zaplanowania'] = do_zaplanowania        
        wpisy['zaplanowane'] = zaplanowane        
        wpisy['pobieranie'] = True
        return render(request, 'bloki_resztkowe/potwierdz.html', wpisy)

    wybrana_pianka = Pianka.objects.get(typ=pianka)
    wpisy = {
        'wybrany_wymiar': wybrana_pianka,
        'typ_zadania': typ_zadania,        
    }
    if typ_zadania == "pobierz":        
        zaplanowane = Nesting.objects.filter(pianka=wybrana_pianka, zatwierdzony=True, zakonczony=False)
        if wybrana_pianka == 'wszystkie':
            zaplanowane = Nesting.objects.filter(zatwierdzony=True, zakonczony=False).order_by('pianka__typ')
        wpisy['zaplanowane'] = zaplanowane        
        wpisy['pobieranie'] = True
        return render(request, 'bloki_resztkowe/potwierdz.html', wpisy)
    elif typ_zadania == "wprowadz":
        if request.POST:
            x = request.POST.get('x_value', False)
            y = request.POST.get('y_value', False)
            z = request.POST.get('z_value', False)
            try:
                float(x)
                float(y)
                float(z)
                Nesting.objects.create(
                pianka = wybrana_pianka,
                x = x,
                y = y,
                z = z,
                )
            except Exception as e:
                error = {
                    'message': "Błąd: " + str(e),
                    'color': "red"
                }
                print(e)
                wpisy = {
                    'wybrany_wymiar': wybrana_pianka,
                    'typ_zadania': typ_zadania,
                    'error': error
                }
                return render(request, 'bloki_resztkowe/wprowadz_wymiar.html', wpisy)            
            error = {
                'message': "Nesting dodany!",
                'color': "green"
            }
            wpisy['error'] = error
            return render(request, 'bloki_resztkowe/wprowadz_wymiar.html', wpisy)
        return render(request, 'bloki_resztkowe/wprowadz_wymiar.html', wpisy)
