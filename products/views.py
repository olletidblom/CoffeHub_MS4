from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            return redirect('product_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'products/details.html', {
        'product': product,
        'comments': comments,
        'form': form
    })