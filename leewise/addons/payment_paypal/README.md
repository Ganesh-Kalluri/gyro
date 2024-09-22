# PayPal

## Technical details

API: [PayPal Payments Standard](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/formbasics/)

This module integrates PayPal using the generic payment with redirection flow based on form
submission provided by the `payment` module.

## Supported features

- Payment with redirection flow
- Webhook notifications

## Module history

- `17.0`
  - The support for customer fees is removed as it is no longer supported by the `payment` module.
    leewise/leewise#132104
- `16.2`
  - The "Merchant Account ID" and "Use IPN" fields are removed. leewise/leewise#104974
- `16.1`
  - Customer fees are converted into the currency of the payment transaction. leewise/leewise#100156
- `15.2`
  - An HTTP 404 "Forbidden" error is raised instead of a Validation error when the authenticity of
    the webhook notification cannot be verified. leewise/leewise#81607

## Testing instructions

Payments must be made using a separate [sandbox account](https://www.sandbox.paypal.com/myaccount/).

Read more at https://developer.paypal.com/tools/sandbox/.
