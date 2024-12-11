from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Equipamento
from .forms import CategoriaForm, EquipamentoForm

def index(request):
    return render(request, 'equipamentos/index.html')

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'equipamentos/categoria_list.html', {'categorias': categorias})

def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'equipamentos/categoria_detail.html', {'categoria': categoria})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'equipamentos/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'equipamentos/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'equipamentos/categoria_confirm_delete.html', {'categoria': categoria})

def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/equipamento_list.html', {'equipamentos': equipamentos})

def equipamento_detail(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'equipamentos/equipamento_detail.html', {'equipamento': equipamento})

def equipamento_create(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos/equipamento_form.html', {'form': form})

def equipamento_update(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos/equipamento_form.html', {'form': form})

def equipamento_delete(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipamento_list')
    return render(request, 'equipamentos/equipamento_confirm_delete.html', {'equipamento': equipamento})
