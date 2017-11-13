from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.

# def get_index(request):
#     results
#     return render(request, "index.html");
    


def get_index(request):
    items = TodoItem.objects.all()
    return render(request, "index.html", {'items': items})    


    
def add_item(request):
    if request.method == "POST":
        # Get the details from the request
        form = TodoItemForm(request.POST, request.FILES)
        # handle saving to database
        if form.is_valid:
            form.save()
            return redirect(get_index)
    else:
        # GET Request so just give them a bkank form
        form = TodoItemForm()
    return render(request, "item_form.html", {"form": form})    



def edit_item(request, id):
    item = get_object_or_404(TodoItem, pk=id);  # standard django shortcut function - automatically returns 404 i fnot found
    if request.method == "POST":
        form = TodoItemForm(request.POST, request.FILES, instance=item);
        if form.is_valid:
            form.save();
            return redirect(get_index);
    else:
        form = TodoItemForm(instance=item);
    return render(request, "item_form.html", {"form": form})    



def toggle_item(request, id):
    item = get_object_or_404(TodoItem, pk=id);
    
    item.done = not item.done;

    item.save();
    return redirect(get_index);
