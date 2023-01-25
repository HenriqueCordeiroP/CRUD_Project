from django.shortcuts import render, redirect
from .models import BookList
from django.contrib import messages
def index(request):
    if request.method == 'POST':
        page = list(request.POST)[1]
        return redirect(f'{page}')
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        create_form = request.POST
        title = create_form['title']
        author = create_form['author']
        year = create_form['year']
        BookList.objects.create(title=title, author=author, year=year)
        return redirect('index')
    return render(request, 'create.html')

def read(request):
    book_list = BookList.objects.all()
    context = {'book_list': book_list}
    # print("CONTEXT: ", context)
    if request.method == "POST":
        return redirect('index')
    return render(request, 'read.html', context)

def update(request):
    if request.method == "POST":
        update_form = request.POST
        title = update_form['title'] 
        updated_book = BookList.objects.filter(title=title)
        if updated_book:
            updated_book.update(author=update_form['author'], year=update_form['year'])
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "This Book Doesn't exist.")

    return render(request, 'update.html')

def delete(request):
    if request.method == "POST":
        title = request.POST['title']
        deleted_book = BookList.objects.filter(title=title)
        if deleted_book:
            deleted_book.delete()
        return redirect('index')
            
    return render(request, 'delete.html')