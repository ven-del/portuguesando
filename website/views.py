from django.shortcuts import render

# Links do menu - mantidos constantes para todas as páginas
menu_links = [
    {'name': 'Home', 'url': '/', 'data_banner': 'Esta é a página inicial da nossa plataforma!'},
    {'name': 'Sobre', 'url': '/sobre/', 'data_banner': 'Conheça-nos!'},
    {'name': 'Página do Aluno', 'url': '/login/', 'data_banner': 'Acesse aqui a sua Página do Aluno!'},
    {'name': 'Aulas', 'url': '/aulas/', 'data_banner': 'Veja o seu cronograma de aulas'},
    {'name': 'Downloads', 'url': '/downloads/', 'data_banner': 'Aqui tem livros em PDF para os alunos!'},
]

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
    context = {
        'banner_text': 'Boas-vindas!',
        'menu_links': 'menu_links',
        'links': links
    }
    return render(request, 'home.html', context)

def sobre(request):
    context = {
        'banner_text': 'Saiba mais sobre nós!',
        'menu_links': menu_links,
    }
    return render(request, 'sobre.html', context)

def login(request):
    context = {
        'banner_text': 'Faça aqui o seu login.',
        'menu_links': menu_links,
    }
    return render(request, 'login.html', context)

def aulas(request):
    context = {
        'banner_text': 'Aqui está o seu cronograma de aulas',
        'menu_links': menu_links,
    }
    return render(request, 'aulas.html', context)

def downloads(request):
    context = {
        'banner_text': 'Aqui tem PDFs e outros Documentos',
        'menu_links': menu_links,
    }
    return render(request, 'downloads.html', context)