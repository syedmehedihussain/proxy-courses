# Proxy Courses — Technical Requirements

v0.1 · 2026-10-26 · Requirements: [prd.md](prd.md) · Stack: ADR-0001 (proposed)

## Platform

- One responsive web app (360 px phone → desktop). No native apps in v1 (NFR-03, NFR-12).
- All business logic behind JSON routes under `/api/*` so a later mobile app can reuse them.

## Stack

| Part | Choice |
|---|---|
| Language | TypeScript (strict) |
| Web app + API | Next.js (App Router); route handlers under `app/api` |
| UI | React server components + Tailwind CSS |
| Database | PostgreSQL 16 through Prisma ORM and migrations |
| Auth | Email + password, IUB domain only, email verification, database sessions (Better Auth or similar; Builder confirms) |
| File storage | Transcripts and notes: local `uploads/` folder in dev, S3-compatible bucket (Supabase Storage) in prod, behind one `storage` module |
| Email | `mailer` module: logged to the console in dev, Resend free tier in prod |
| Payments | `payments` adapter: `MockGateway` (M1), `SslCommerzGateway` sandbox (later). bKash, Nagad and cards all go through SSLCommerz |
| Validation | Zod on every API input |
| Tests | Vitest (unit, service layer), Playwright (browser, core flow) |
| CI | GitHub Actions: lint, typecheck, unit, Playwright on every push and PR |
| Hosting | Vercel (app) + Neon or Supabase Postgres, free tiers |

## Limits and rules

- Prices are platform settings, not tutor input: subscription 500 taka, one-to-one 200 taka (FR-14).
- Money is stored as integer taka (`Int`), never floats.
- Payment callbacks are idempotent: one gateway transaction ID gives one payment record (FR-22).
- The revenue split is computed and stored on each payment at the time of payment (FR-33).
- Transcript files: PDF / JPG / PNG, 5 MB max, never served publicly (NFR-05).
- Every admin and money action writes an `AuditLog` row (NFR-07).
- Role checks run in the service layer, not only in the UI (NFR-04).
- Secrets live only in `.env` (git-ignored); `.env.example` lists the keys.

## Quality targets

See PRD NFR-01 … NFR-12. The ones checked in CI: lint + typecheck clean, unit coverage ≥ 70% on
`src/server/services`, and the Playwright core flow passing.
