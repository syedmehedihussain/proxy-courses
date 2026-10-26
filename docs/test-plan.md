# Proxy Courses — Test Plan

v0.1 · 2026-10-26 · Feeds course Task 6 (white-box and black-box).

## Levels

| Level | Tool | What | Where |
|---|---|---|---|
| Unit (white-box) | Vitest + a test Postgres | Service rules: domain check, grade rule, seat limit, split, idempotency, refund window, permissions | `tests/unit/`, CI |
| API (black-box) | Vitest calling route handlers (Postman collection optional for the report) | Status codes, validation errors, role refusals | `tests/unit/api/`, CI |
| Browser (black-box) | Playwright, Chromium, at 390 px and 1280 px | Core flows below | `tests/e2e/`, CI |
| By hand | Checklist | Look and feel, emails, accessibility (keyboard, contrast) | Before each sprint review |

Coverage target: 70% or more of lines in `src/server/services` (NFR-10).

## M1 unit cases

- Sign-up: `a@iub.edu.bd` accepted; `a@gmail.com` and `a@iub.edu.bd.evil.com` refused.
- Approval: `A` and `A-` approvable; `B+` refused.
- Offering: creating one without an approved application is refused (403).
- Demo: booking at seatLimit gives 409; cancelling frees a seat; a double booking is refused.
- Payment: the split of 500 is 350/150; the same `gatewayTxnId` twice makes one payment; a failed payment leaves the subscription `PENDING`.
- Access: a non-subscriber's offering view hides subscriber fields.

## M1 browser test: core flow

1. Sign up as `learner@iub.edu.bd`; open the verification link from the console mailer; log in.
2. Sign up as `tutor@iub.edu.bd`; apply for CSE211 with grade A and a sample PDF.
3. Log in as the seeded admin; approve the application.
4. As the tutor, create and publish a CSE211 offering with a YouTube intro link; add a demo with 1 seat.
5. As the learner, search `cse211`; open the offering; see the intro video and the verified badge.
6. Book the demo; see the meeting link. A second learner trying to book sees "Demo full".
7. Subscribe → mock pay page → choose **Fail** → no access.
8. Subscribe again → choose **Pay** → subscription active; the receipt shows 500 taka.
9. Run the same flow at 390 px width.

## M2–M4

Add cases when each milestone is planned in detail: refund ends access; one review per learner;
one student per advising slot; payout = sum(tutorShare) − refunds; SSLCommerz sandbox by hand.
