from django.shortcuts import render

from .models import Order
from .service import recommend_box


def home(request):
    orders = Order.objects.all()

    recommended_box = None
    no_box = False
    selected_order = None

    if request.method == "POST":

        order_id = request.POST.get("order_id")

        selected_order = Order.objects.get(id=order_id)

        recommended_box = recommend_box(selected_order)

        if recommended_box is None:
            no_box = True

    return render(
        request,
        "box_selector/home.html",
        {
            "orders": orders,
            "recommended_box": recommended_box,
            "no_box": no_box,
            "selected_order": selected_order,
        },
    )