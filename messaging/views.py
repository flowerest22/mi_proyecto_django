from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'messaging/bandeja_entrada.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'messaging/enviar_mensaje.html', {'form': form})
