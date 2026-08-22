from itertools import permutations

from .models import Box, Order


def product_fits_in_box(product, box):
    product_dimensions = [
        product.length,
        product.width,
        product.height,
    ]

    box_dimensions = [
        box.length,
        box.width,
        box.height,
    ]

    for dimensions in permutations(product_dimensions):
        if all(
            product_dimension <= box_dimension
            for product_dimension, box_dimension
            in zip(dimensions, box_dimensions)
        ):
            return True

    return False


def recommend_box(order):
    items = order.orderitem_set.select_related("product").all()

    total_weight = sum(
        item.product.weight * item.quantity
        for item in items
    )

    total_volume = sum(
        item.product.length
        * item.product.width
        * item.product.height
        * item.quantity
        for item in items
    )

    suitable_boxes = []

    for box in Box.objects.all():

        if total_weight > box.max_weight:
            continue

        box_volume = box.length * box.width * box.height

        if total_volume > box_volume:
            continue

        if not all(
            product_fits_in_box(item.product, box)
            for item in items
        ):
            continue

        suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    return min(
    suitable_boxes,
    key=lambda box: (
        box.cost,
        box.length * box.width * box.height,
    )
)