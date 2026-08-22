from django.test import TestCase

from .models import Box, Product, Order, OrderItem
from .service import recommend_box


class BoxRecommendationTest(TestCase):

    def setUp(self):

        self.small_box = Box.objects.create(
            name="Small Box",
            length=20,
            width=15,
            height=10,
            max_weight=5,
            cost=30,
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=30,
            width=20,
            height=15,
            max_weight=10,
            cost=50,
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length=50,
            width=40,
            height=30,
            max_weight=20,
            cost=80,
        )

        self.laptop = Product.objects.create(
            name="Laptop",
            length=15,
            width=10,
            height=5,
            weight=2,
        )

    def test_small_box_is_recommended(self):

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.small_box)

    def test_no_box_when_product_is_too_large(self):

        large_product = Product.objects.create(
            name="Large TV",
            length=100,
            width=100,
            height=100,
            weight=50,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=large_product,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)

    def test_cheapest_suitable_box_is_selected(self):

        product = Product.objects.create(
            name="Medium Product",
            length=25,
            width=18,
            height=12,
            weight=5,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.medium_box)

    def test_multiple_products_fit_in_small_box(self):

        keyboard = Product.objects.create(
            name="Keyboard",
            length=12,
            width=5,
            height=2,
            weight=1,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=1,
        )

        OrderItem.objects.create(
            order=order,
            product=keyboard,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.small_box)

    def test_quantity_is_considered(self):

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=3,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.medium_box)

    def test_weight_limit_is_respected(self):

        heavy_product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=6,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=heavy_product,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.medium_box)

    def test_product_rotation_is_allowed(self):

        rotated_product = Product.objects.create(
            name="Rotated Product",
            length=10,
            width=20,
            height=15,
            weight=2,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=rotated_product,
            quantity=1,
        )

        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box, self.small_box)