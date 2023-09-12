from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name1'    : 'Pisang Cavendish',
        'price1'   : 20000,
        'amount1'  : 12,
        'description1' : 'Pisang Cavendish berasal dari Lampung dan memiliki ukuran yang relatif normal serta rasa yang sangat manis.',
        'name2'    : 'Stroberi All Seasons',
        'price2'   : 55000,
        'amount2'  : 3,
        'description2' : 'Stroberi All Seasons merupakan produk lokal dan memiliki ukuran relatif normal dibanding jenis stroberi lainnya.',
        'name3'    : 'Anggur Shine Muscat',
        'price3'   : 70000,
        'amount3'  : 8,
        'description3' : 'Produk Impor dari China dan memiliki rasa yang sangat manis dan sedikit asam, serta tidak memiliki biji.',
        'name4'    : 'Melon Madu',
        'price4'   : 55000,
        'amount4'  : 18,
        'description4' : 'Melon Madu dipanen dari Jawa Timur dan memiliki ukuran relatif lebih besar serta memiliki tekstur daging yang renyah dan dijamin manis.',
        'name5'    : 'Apel Fuji WangShan',
        'price5'   : 41500,
        'amount5'  : 26,
        'description5' : 'Produk impor dari China dan memiliki tekstur yang renyah serta memiliki rasa yang lebih manis dan sedikit asam.',
    }

    return render(request, "main.html", context)