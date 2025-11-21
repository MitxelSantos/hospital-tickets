# soporte/views.py
from django.shortcuts import render, redirect
from .forms import TicketForm
from django.contrib import messages

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, '¡Ticket creado con éxito! El equipo de sistemas lo revisará.')
            return redirect('crear_ticket')
    else:
        form = TicketForm()
    
    return render(request, 'soporte/crear_ticket.html', {'form': form})