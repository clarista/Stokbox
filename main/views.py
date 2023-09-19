from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product;
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'name'  : 'Clarista',
        'class' : 'PBP C',
        # 'name1'    : 'Pisang Cavendish',
        # 'price1'   : 20000,
        # 'amount1'  : 12,
        # 'description1' : 'Pisang Cavendish berasal dari Lampung dan memiliki ukuran yang relatif normal serta rasa yang sangat manis.',
        # 'name2'    : 'Stroberi All Seasons',
        # 'price2'   : 55000,
        # 'amount2'  : 3,
        # 'description2' : 'Stroberi All Seasons merupakan produk lokal dan memiliki ukuran relatif normal dibanding jenis stroberi lainnya.',
        # 'name3'    : 'Anggur Shine Muscat',
        # 'price3'   : 70000,
        # 'amount3'  : 8,
        # 'description3' : 'Produk Impor dari China dan memiliki rasa yang sangat manis dan sedikit asam, serta tidak memiliki biji.',
        # 'name4'    : 'Melon Madu',
        # 'price4'   : 55000,
        # 'amount4'  : 18,
        # 'description4' : 'Melon Madu dipanen dari Jawa Timur dan memiliki ukuran relatif lebih besar serta memiliki tekstur daging yang renyah dan dijamin manis.',
        # 'name5'    : 'Apel Fuji WangShan',
        # 'price5'   : 41500,
        # 'amount5'  : 26,
        # 'description5' : 'Produk impor dari China dan memiliki tekstur yang renyah serta memiliki rasa yang lebih manis dan sedikit asam.',
        'products' : products,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")