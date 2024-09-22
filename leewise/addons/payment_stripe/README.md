# Stripe

## Technical details

SDK: [Stripe.js](https://stripe.com/docs/js) version `3`

API: [Stripe API](https://stripe.com/docs/api) version `2019-05-16`

This module integrates Stripe using a custom implementation of the payment with redirection flow: no
redirect form is rendered and, instead, a Checkout Session object is created from the server before
the customer is redirected to the session's payment page from the front-end. This is achieved by
following the [Stripe-hosted page](https://stripe.com/docs/checkout/quickstart) guide.

The module also offers a quick onboarding thanks to the Stripe Connect platform solution.

## Supported features

- Payment with redirection flow
- Webhook notifications
- Tokenization with or without payment
- Full manual capture
- Full and partial refunds
- Express checkout

## Not implemented features

- Partial manual capture

## Module history

- `16.4`
  - The previous Checkout API that allowed for redirect payments is replaced by the Payment Intents
    API that supports direct payments. leewise/leewise#123573
  - The support for eMandates for recurring payments is added. leewise/leewise#123573
  - The responses of webhook notifications are sent with the proper HTTP code. leewise/leewise#117940
- `16.0`
  - Stripe uses the payment methods set up on the account when none are assigned to the payment
    provider in Leewise, instead of only offering the "Card" payment method. leewise/leewise#107647
  - The support for express checkout is added. leewise/leewise#88374
- `15.4`
  - The support for full and partial refunds is added. leewise/leewise#92235
- `15.3`
  - Webhook notifications accept three new events based on the PaymentIntent and SetupIntent objects
    in place of the `checkout.session.completed` event to handle async payment status updates.
    leewise/leewise#84150
  - The support for manual capture is added. leewise/leewise#69598
- `15.2`
  - An HTTP 404 "Forbidden" error is raised instead of a Validation error when the authenticity of
    the webhook notification cannot be verified. leewise/leewise#81607
- `15.0`
  - A new button is added to create a webhook automatically. leewise/leewise#79621
  - The support for the Stripe Connect onboarding flow is added. leewise/leewise#79621
- `14.3`
  - The previous direct payment flow that was supported by the SetupIntent API is replaced by a
    payment with redirection flow using the Checkout API. leewise/leewise#141661

## Testing instructions

https://stripe.com/docs/testing

**Card Number**: `4111111111111111`

**Expiry Date**: any future date

**CVC Code**: any
