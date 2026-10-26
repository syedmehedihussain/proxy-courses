# Proxy Courses — Data Model

v0.1 · 2026-10-26 · All entities live in PostgreSQL (Prisma). Files live in storage; the DB keeps only their key.
Every table has `id` (cuid), `createdAt`, `updatedAt`. Money is integer taka.

| Entity | Key fields | Notes |
|---|---|---|
| **User** | email (unique, `@iub.edu.bd`), passwordHash, name, studentId, department, photoKey, emailVerifiedAt, roles (`LEARNER`, `TUTOR`, `ADVISOR`, `ADMIN`) | One account can hold several roles |
| **Session** | userId, tokenHash, expiresAt | Database sessions |
| **Course** | code (unique, e.g. `CSE211`), title | Seeded catalogue |
| **TutorApplication** | userId, courseId, grade (`A`, `A-`, …), transcriptKey, status (`PENDING`, `APPROVED`, `REJECTED`), reason, reviewedById, reviewedAt | One approved application per user and course allows offerings (FR-04–06) |
| **Offering** | tutorId, courseId, semester (e.g. `2026-AUT`), title, outline, introVideoUrl, status (`DRAFT`, `PUBLISHED`, `UNPUBLISHED`), ratingAvg, ratingCount | Price comes from Settings, not stored here |
| **Material** | offeringId, kind (`RECORDING`, `NOTE`), title, url or fileKey | Subscribers only (FR-11) |
| **LiveClass** | offeringId, startsAt, durationMin, meetingUrl | Subscribers only (FR-12) |
| **Demo** | offeringId, startsAt, durationMin, meetingUrl, seatLimit | Free (FR-13) |
| **DemoBooking** | demoId, learnerId, cancelledAt | Unique (demoId, learnerId) |
| **Subscription** | learnerId, offeringId, status (`PENDING`, `ACTIVE`, `REFUND_REQUESTED`, `REFUNDED`, `EXPIRED`), activatedAt | Unique (learnerId, offeringId) |
| **AddOn** | subscriptionId, kind (`ONE_TO_ONE`), status, paymentId | FR-23 |
| **Payment** | userId, purpose (`SUBSCRIPTION`, `ADD_ON`), subscriptionId?, addOnId?, amount, method (`BKASH`, `NAGAD`, `CARD`, `MOCK`), gateway, gatewayTxnId (unique), status (`PENDING`, `PAID`, `FAILED`, `REFUNDED`), tutorShare, platformShare | The split is stored at payment time (FR-33) |
| **RefundRequest** | subscriptionId, reason, status, decidedById, decidedAt | FR-25–26 |
| **Review** | offeringId, learnerId, rating 1–5, text | Unique (offeringId, learnerId) (FR-27) |
| **Report** | reporterId, targetType (`REVIEW`, `USER`), targetId, reason, status | FR-29 |
| **AdvisingSlot** | advisorId, startsAt, durationMin, location or meetingUrl, bookedById?, cancelledAt | One student per slot (FR-30–31) |
| **Payout** | tutorId, month (`2026-11`), gross, refunds, net, status (`DUE`, `PAID`), paidAt | Built from Payments (FR-34) |
| **Setting** | key, value | `price.subscription`=500, `price.oneToOne`=200, `split.default`=70, `split.top`=80, refund and top-rated rules |
| **AuditLog** | actorId, action, entityType, entityId, data (JSON) | NFR-07 |
