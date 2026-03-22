from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Order
from book.models import Book
from authentication.models import CustomUser

def order_list(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order/order_detail.html", {"order": order})


def order_create(request):
    users = CustomUser.objects.all()
    books = Book.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user")
        book_id = request.POST.get("book")
        plated_end_at = request.POST.get("plated_end_at")

        user = CustomUser.objects.get(pk=user_id)
        book = Book.objects.get(pk=book_id)

        order = Order.create(
            user=user,
            book=book,
            plated_end_at=plated_end_at
        )

        if order:
            return redirect("order:index")

    return render(request, "order/order_create.html", {
        "users": users,
        "books": books,
    })


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        plated_end_at = request.POST.get("plated_end_at")
        end_at = request.POST.get("end_at") or None

        order.update(plated_end_at=plated_end_at, end_at=end_at)
        return redirect("order:detail", pk=order.pk)

    return render(request, "order/order_edit.html", {"order": order})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect("order:index")

    return redirect("order:detail", pk=order.pk)
