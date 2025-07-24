from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
    #return HttpResponse("View is working!")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

#  Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automatique après inscription
            return redirect('list_books')  # Redirige vers la page des livres
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

#  Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirige vers la page des livres
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

#  Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Après logout, renvoie à login


from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

def check_role(role):
    def inner(user):
        try:
            return user.userprofile.role == role
        except UserProfile.DoesNotExist:
            return False
    return inner

@user_passes_test(check_role('Admin'))
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
