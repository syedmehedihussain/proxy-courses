# 0001 — Stack: Next.js (TypeScript) + PostgreSQL + Prisma, responsive web first

- **Status:** Accepted
- **Date:** 2026-10-26
- **Proposed by:** Claude (chat)
- **Done:** not yet

## Context

Proxy Courses is a CSE451 semester project for 4 part-time students over 14 weeks. The graded output is the course documents (Tasks 1–8) plus a working prototype covering sign-up, tutor search, demo booking and sandbox subscription payment. The data is relational: users, verifications, offerings, subscriptions, payments, refunds and payouts. Hosting has to be free or on a student tier. Native mobile apps are out of scope for the prototype, but the backend should stay reusable for them later.

## Options

1. **Next.js + PostgreSQL + Prisma** — Trade-off: One language and one repo with free hosting; the API routes need care to stay clean for mobile.
2. **Django + PostgreSQL** — Trade-off: Free admin panel and a strong ORM; less app-like pages, and mobile needs DRF later.
3. **React SPA + Express API + PostgreSQL** — Trade-off: Clearest separation of parts, but two projects to build and host.
4. **React + Firebase** — Trade-off: Fastest start, but a poor fit for payments, refunds and relational reports.

## Decision

Build one responsive web app in Next.js (App Router, TypeScript) with PostgreSQL through Prisma. Server route handlers under /api are the API, so a mobile app could use them later. Tests run on Vitest (unit) and Playwright (browser), with GitHub Actions running both on every push. Host on Vercel with a free Postgres (Neon or Supabase).

## Consequences

- Good: a single TypeScript codebase, so all 4 members can review every change.
- Good: Playwright browser tests cover Task 6 black-box testing directly.
- Bad: no free admin panel, so admin screens (verification, refunds) have to be built.
- Follow-up: the payment gateway choice is separate (sandbox adapter).
- Follow-up: native mobile is a later milestone that reuses /api.
