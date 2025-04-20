from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

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

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=comment.product.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'products/editcomment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    product_pk = comment.product.pk
    if request.method == 'POST':
        comment.delete()
        return redirect('product_detail', pk=product_pk)
    return render(request, 'products/deletecomment.html', {'comment': comment})