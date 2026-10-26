# Proxy Courses — API

v0.1 · 2026-10-26 · JSON over HTTPS under `/api`. Auth by session cookie. Inputs validated with Zod.
Errors: `{ "error": { "code": "...", "message": "..." } }` with status 400 / 401 / 403 / 404 / 409.
Role in brackets: [any] = logged in, [L] learner, [T] tutor, [Adv] advisor, [A] admin.

## Auth
| Method | Route | Who | FR |
|---|---|---|---|
| POST | /api/auth/signup | public | 01 |
| POST | /api/auth/verify-email | public | 01 |
| POST | /api/auth/login · /api/auth/logout | public · [any] | 01–02 |
| POST | /api/auth/reset-request · /api/auth/reset | public | 02 |
| GET, PATCH | /api/me | [any] | 03 |

## Verification
| Method | Route | Who | FR |
|---|---|---|---|
| POST | /api/tutor-applications (multipart: courseId, grade, transcript) | [any] | 04 |
| GET | /api/tutor-applications/mine | [any] | 04 |
| GET | /api/admin/tutor-applications?status= | [A] | 05, 32 |
| POST | /api/admin/tutor-applications/:id/decision `{approve, reason}` | [A] | 05–06 |
| GET | /api/admin/transcripts/:key (signed, short-lived) | [A], owner | 05 |
| POST | /api/admin/users/:id/roles | [A] | 07 |

## Offerings and discovery
| Method | Route | Who | FR |
|---|---|---|---|
| GET | /api/offerings?course=CSE211&sort=rating | [any] | 16–17 |
| GET | /api/offerings/:id | [any] (subscriber parts only if subscribed) | 18 |
| POST, PATCH | /api/offerings · /api/offerings/:id | [T] owner | 09–10, 15 |
| POST | /api/offerings/:id/materials · /live-classes · /demos | [T] owner | 11–13 |
| POST, DELETE | /api/demos/:id/booking | [any] | 19–20 |

## Subscriptions and payments
| Method | Route | Who | FR |
|---|---|---|---|
| POST | /api/subscriptions `{offeringId, method}` → `{redirectUrl}` | [any] | 21–22 |
| POST | /api/payments/callback (gateway; signature checked; idempotent) | gateway | 22 |
| GET | /api/payments/mock/:paymentId (mock pay page: succeed / fail) | dev only | 22 |
| POST | /api/subscriptions/:id/add-ons | [L] subscriber | 23 |
| GET | /api/subscriptions/mine · /api/payments/mine | [any] | 24 |
| POST | /api/subscriptions/:id/refund-request | [L] subscriber | 25 |
| POST | /api/admin/refunds/:id/decision | [A] | 26 |

## Reviews and reports
| Method | Route | Who | FR |
|---|---|---|---|
| PUT | /api/offerings/:id/review `{rating, text}` | [L] subscriber | 27–28 |
| POST | /api/reports | [any] | 29 |

## Advising
| Method | Route | Who | FR |
|---|---|---|---|
| GET | /api/advisors · /api/advisors/:id/slots | [any] | 30 |
| POST | /api/advising-slots | [Adv] | 30 |
| POST, DELETE | /api/advising-slots/:id/booking | [any] | 31 |

## Admin and payouts
| Method | Route | Who | FR |
|---|---|---|---|
| GET | /api/admin/queue | [A] | 32 |
| GET | /api/admin/payouts?month=2026-11 (`?format=csv`) | [A] | 34 |
| POST | /api/admin/payouts/:id/paid | [A] | 34 |
| GET | /api/admin/stats | [A] | 35 |
| GET, PATCH | /api/admin/settings | [A] | 14, 33 |
