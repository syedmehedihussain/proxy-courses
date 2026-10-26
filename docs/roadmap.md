# Proxy Courses — Roadmap

v0.1 · 2026-10-26 · Requirements: [prd.md](prd.md) · Tests: [test-plan.md](test-plan.md)
Milestones map onto the remaining 2-week sprints. Dates are left to the team.

## M1 — Core flow prototype (proposal deliverable 9)

Usable on its own: a learner signs up, finds a verified tutor by course code, books a free demo
and subscribes with the mock gateway.
FRs: 01–06, 08–10, 13–14, 16–22, 24, 32 (applications only), 33 (default 70/30 only).

1. Scaffold: Next.js + TypeScript + Tailwind + Prisma, ESLint, Vitest, Playwright, GitHub Actions CI, `.env.example`, `.gitignore`.
2. Prisma schema for the M1 entities (User, Session, Course, TutorApplication, Offering, Demo, DemoBooking, Subscription, Payment, Setting, AuditLog) plus a seed (courses, an admin, a sample tutor, prices).
3. Auth: sign-up limited to `@iub.edu.bd`, email verification (console mailer), login, logout, password reset, role guard in services.
4. Tutor application: transcript upload through the local storage adapter, plus a "my applications" page.
5. Admin queue: approve or reject applications with the A / A- rule, a reason and an audit log.
6. Offerings: a tutor creates and publishes an offering (outline, intro YouTube link) for an approved course; offering page with the verified badge.
7. Search by course code, with sort by rating or subscribers.
8. Demos: a tutor schedules a demo with a seat limit; a learner books and cancels; the link shows only to bookers.
9. Payments: `PaymentGateway` interface, `MockGateway` and its pay / fail page, subscribe flow, idempotent callback, 70/30 split stored, "my subscriptions and receipts" page.
10. Playwright test of the whole core flow, running in CI.

**Done when**
- [ ] A non-IUB email is refused at sign-up.
- [ ] A tutor cannot publish until an admin approves an A or A- for that course.
- [ ] Searching `cse211` lists the published CSE211 offerings.
- [ ] A full demo refuses a new booking.
- [ ] A mock "fail" gives no access; a mock "pay" gives access, and a repeated callback makes no second payment.
- [ ] The payment row shows tutorShare 350 and platformShare 150.
- [ ] CI is green: lint, typecheck, unit tests, Playwright core flow.

## M2 — Subscriber content and trust

FRs: 11–12, 15, 25–29, 32 (refunds, reports), 36.

1. Materials (recording links, note PDFs) and live classes, visible to subscribers only.
2. Unpublish an offering, keeping access for existing subscribers.
3. Reviews and ratings (subscribers only, one each), with the average shown.
4. Refund request and admin decision (the rule from PRD Q1), ending access.
5. Reports on reviews and users, in the admin queue.
6. Email notifications through the Resend adapter.

**Done when:** the M2 cases in the test plan pass; a refunded learner loses access to materials.

## M3 — Advising

FRs: 07, 30–31.

1. Admin assigns the advisor role.
2. An advisor publishes slots; a student books and cancels one (one per slot).

**Done when:** two students cannot book the same slot; both sides get an email.

## M4 — Money operations

FRs: 23, 33 (top-rated 80/20), 34–35, real sandbox for 22.

1. Top-rated rule (PRD Q2) and an 80/20 split.
2. One-to-one add-on purchase.
3. Monthly payout report, CSV export, mark as paid.
4. `SslCommerzGateway` sandbox (bKash, Nagad, card).
5. Admin dashboard numbers.

**Done when:** a payout equals the tutor's shares minus refunds for the month; an SSLCommerz sandbox payment activates a subscription.

## Later (not planned)

Native mobile app using `/api`; other universities; tutor-set prices; IUB portal grade check; AI features.
