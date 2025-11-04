from django.shortcuts import render

def book_cover(request):
    # Render the HTML content as a template
    return render(request, 'book_cover.html')
