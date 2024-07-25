from django.shortcuts import render

def home(request):
    links = [
        {
            'name': 'Galinha Pintadinha',
            'url': 'https://www.galinhapintadinha.com.br',
            'image': 'images/galinha-pintadinha.png'
        },
        {
            'name': 'Mundo Bita',
            'url': 'https://www.mundobita.com.br',
            'image': 'images/mundo-bita.png'
        },
        {
            'name': 'Palavra Cantada',
            'url': 'https://www.palavracantada.com.br',
            'image': 'images/palavra-cantada.png'
        },
        {
            'name': 'Turma da Mônica',
            'url': 'https://turmadamonica.uol.com.br',
            'image': 'images/turma-da-monica.png'
        },
        {
            'name': 'Tv Rá Tim Bum!',
            'url': 'https://tvratimbum.com.br',
            'image': 'images/tv-ra-tim-bum.png'
        },
        {
            'name': 'Catalendas',
            'url': 'https://www.youtube.com/programacatalendas',
            'image': 'images/catalendas2.jpg'
        }
    ]
    return render(request, 'home.html', {'links': links})

def sobre(request):
    return render(request, 'sobre.html')