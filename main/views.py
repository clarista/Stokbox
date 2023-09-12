from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name-1'    : 'Pisang Cavendish',
        'price-1'   : 20000,
        'amount-1'  : 12,
        'description-1' : 'Pisang Cavendish berasal dari Lampung dan memiliki ukuran yang relatif normal serta rasa yang sangat manis.',
        'name-2'    : 'Stroberi All Seasons',
        'price-2'   : 55000,
        'amount-2'  : 3,
        'description-2' : 'Stroberi All Seasons merupakan produk lokal dan memiliki ukuran relatif normal dibanding jenis stroberi lainnya.',
        'name-3'    : 'Anggur Shine Muscat',
        'price-3'   : 70000,
        'amount-3'  : 8,
        'description-3' : 'Produk Impor dari China dan memiliki rasa yang sangat manis dan sedikit asam, serta tidak memiliki biji.',
        'name-4'    : 'Melon Madu',
        'price-4'   : 55000,
        'amount-4'  : 18,
        'description-4' : 'Melon Madu dipanen dari Jawa Timur dan memiliki ukuran relatif lebih besar serta memiliki tekstur daging yang renyah dan dijamin manis.',
        'name-5'    : 'Apel Fuji WangShan',
        'price-5'   : 41500,
        'amount-5'  : 26,
        'description-5' : 'Produk impor dari China dan memiliki tekstur yang renyah serta memiliki rasa yang lebih manis dan sedikit asam.',
    }

    return render(request, "main.html", context)