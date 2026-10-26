# Proxy Courses — Architecture

v0.1 · 2026-10-26 · See [trd.md](trd.md) for the stack.

## Parts

```
 Browser (phone / desktop)
        │  HTML pages + fetch /api/*
        ▼
 ┌───────────── Next.js app ─────────────┐
 │  app/(pages)   UI, server components  │
 │  app/api/*     route handlers (JSON)  │
 │        │  Zod-validated input         │
 │        ▼                              │
 │  server/services  business rules,     │
 │                   role checks, audit  │
 │        │                              │
 │  server/adapters                      │
 │   ├─ db (Prisma) ──────────────► PostgreSQL
 │   ├─ payments ─ Mock │ SSLCommerz ──► gateway sandbox
 │   ├─ storage ─ local │ S3 bucket ───► transcripts, notes
 │   └─ mailer ─ console │ Resend ─────► email
 └───────────────────────────────────────┘
 External links only: YouTube (videos), Zoom / Meet (live classes)
```

## How they talk

- **Pages** read through the services directly (server components). **Client actions** call `/api/*`.
  Both paths go through the same service functions, so the rules live in one place.
- **Services** hold every rule: who may do what, prices, the split, the refund window, demo seats.
  They never import Next.js, so they unit test with a test database.
- **Adapters** wrap the outside world behind small interfaces and are chosen by env vars.
  Tests and CI always use the mock or local versions.
- **Payment flow:** `POST /api/subscriptions` → service creates a `pending` payment →
  gateway returns a redirect URL → learner pays → gateway calls `POST /api/payments/callback` →
  service verifies it, marks the payment `paid` once only, and activates the subscription.

## Folder layout

```
src/app/            pages and app/api route handlers
src/server/services one file per module (auth, verification, offerings, demos,
                    subscriptions, payments, reviews, advising, admin, payouts)
src/server/adapters db, payments, storage, mailer
src/lib/            shared types, zod schemas, money helpers
prisma/             schema.prisma, migrations, seed.ts
tests/unit/         Vitest
tests/e2e/          Playwright
```
