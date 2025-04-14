import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffehub.settings")
django.setup()

from products.models import Product

product_data = [
    {
        "name": "Heavenly Spice",
        "description": "Comforting",
        "price": 89.99,
        "image_url": "images/coffeproducts/heavenlyspice.png"
    },
    {
        "name": "Nescafé",
        "description": "Globally recognized instant coffee by Nestlé.",
        "price": 100,
        "image_url": "images/coffeproducts/nescafe.png"
    },
    {
        "name": "Costa",
        "description": "Tasty",
        "price": 100,
        "image_url": "images/coffeproducts/costa.png"
    },
    {
        "name": "Morning Glory",
        "description": "Rich and aromatic blend perfect for mornings.",
        "price": 75,
        "image_url": "images/coffeproducts/morningglory.png"
    },
    {
        "name": "Dark Knight Roast",
        "description": "Bold dark roast with chocolate notes.",
        "price": 120,
        "image_url": "images/coffeproducts/darkknight.png"
    },
    {
        "name": "Smooth Velvet",
        "description": "Silky smooth medium roast with caramel undertones.",
        "price": 95,
        "image_url": "images/coffeproducts/smoothvelvet.png"
    },
    {
        "name": "Espresso Express",
        "description": "Intense espresso roast for an energy boost.",
        "price": 110,
        "image_url": "images/coffeproducts/espressoexpress.png"
    },
    {
        "name": "Vanilla Sky",
        "description": "Light roast infused with natural vanilla flavor.",
        "price": 85,
        "image_url": "images/coffeproducts/vanillasky.png"
    },
]

for product in product_data:
    Product.objects.get_or_create(
        name=product["name"],
        defaults={
            "description": product["description"],
            "price": product["price"],
            "image_url": product["image_url"]
        }
    )

print("Products loaded successfully!")