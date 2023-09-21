import stripe
from config.settings import STRIPE_SECRET_KEY_TEST


def get_create_payment(instance):
    stripe.api_key = STRIPE_SECRET_KEY_TEST

    title_product = f'{instance.lesson}' if instance.lesson else ''
    title_product += f'{instance.course}' if instance.course else ''

    product = stripe.Product.create(name=f'{title_product}')
    price = stripe.Price.create(
        unit_amount=instance.amount*100,
        currency="rub",
        product=f"{product.id}",
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": f'{price.id}',
                "quantity": 1,
            },
        ],
        mode="payment",
        customer_email=f"{instance.user.email}"
    )

    return session


def get_payment_retrieve(session):
    stripe.api_key = STRIPE_SECRET_KEY_TEST
    return stripe.checkout.Session.retrieve(session)
