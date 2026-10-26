# 0002 — Payments through an adapter: mock gateway first, SSLCommerz sandbox second

- **Status:** Accepted
- **Date:** 2026-10-26
- **Proposed by:** Claude (chat)
- **Done:** not yet

## Context

The prototype has to show subscription payment by bKash, Nagad and card, in sandbox only. Getting gateway sandbox credentials can take a while, and browser tests in CI can't depend on an outside site. Payment, idempotency and refund rules need to be unit-testable.

## Options

1. **Adapter with mock first, then SSLCommerz** — Trade-off: Never blocked and fully testable; a small amount of extra code.
2. **SSLCommerz sandbox only** — Trade-off: Real flow from day one, but blocked on credentials and has flaky end-to-end tests.
3. **bKash + Nagad direct** — Trade-off: Closest to real use, but two integrations and two sets of credentials.

## Decision

Define a small PaymentGateway interface (createCheckout, verifyCallback, refund). Ship a MockGateway in M1 with a local "pay / fail" page. Add an SslCommerzGateway (sandbox) in a later milestone, which covers bKash, Nagad and cards. An env var picks the gateway, and tests always use the mock.

## Consequences

- Good: the M1 core flow can be demoed offline.
- Good: CI is deterministic.
- Bad: the real gateway's quirks only show up when SSLCommerz is added.
- Follow-up: apply for an SSLCommerz sandbox store early (PRD Q4).
