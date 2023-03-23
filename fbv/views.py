from django.shortcuts import render

# Create your views here.
def book_list(request):
    book_name = '射雕英雄传'
    
    return render(request, 'book_list.html', {'book_name':book_name})