from django.shortcuts import render

# Baby step - Usually a Model is used
finches = [
    {'name': 'Tweety', 'species': 'Canary', 'description': 'bright yellow with a lovely singing voice', 'age': 1},
    {'name': 'Pip', 'species': 'Zebra Finch', 'description': 'small and energetic, with black and white striped feathers', 'age': 2},
    {'name': 'Rio', 'species': 'Parrot Finch', 'description': 'colorful with a playful personality', 'age': 1},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })