# Proxy Courses

Peer-tutoring and advising web app for IUB students (CSE451 semester project).
A responsive web app first; a native mobile app later reuses `/api`.

## Documents
- `docs/prd.md`: requirements FR-01…36, NFR-01…12 (cite FR IDs in commits and tests)
- `docs/trd.md` · `docs/architecture.md` · `docs/data-model.md` · `docs/api.md`
- `docs/roadmap.md`: milestones and tasks · `docs/test-plan.md`: test cases
- `docs/adr/`: decisions (0001 stack, 0002 payment adapter)
- `_project/STATUS.md`: where we are

## Stack
Next.js (App Router, TypeScript strict) · Tailwind · PostgreSQL + Prisma · Zod · Vitest · Playwright · GitHub Actions.

## Commands (once scaffolded)
- `npm run dev`: app on http://localhost:3000
- `npm run lint` · `npm run typecheck` · `npm test` (Vitest) · `npm run e2e` (Playwright)
- `npx prisma migrate dev` · `npx prisma db seed`

## Layout
`src/app` pages and `app/api` routes → `src/server/services` (all rules) → `src/server/adapters`
(db, payments, storage, mailer) · `src/lib` shared · `prisma/` · `tests/unit`, `tests/e2e`.

## Rules
- Business rules and role checks live in services, never only in UI or routes.
- Money is integer taka. Prices and the split come from `Setting`, never from user input.
- Payment callbacks are idempotent on `gatewayTxnId`.
- Tests and CI use `MockGateway`, the console mailer and local storage. No network calls.
- Transcripts are never public; serve them through short-lived signed routes for the admin and the owner only.
- Log every admin and money action to `AuditLog`.
- Secrets go only in `.env` (git-ignored); keep `.env.example` current.
