import os
import stripe


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def create_session(payment):

    if payment.course:
        title = payment.course.title
        description = payment.course.description
    else:
        title = payment.lesson.title
        description = payment.lesson.description

    product = stripe.Product.create(
        name=title,
        description=description,
    )

    payment = stripe.checkout.Session.create(
        success_url='https://example.com/success',
        line_items=[
            {
                "price": product["id"],
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return payment['url']
