# Proxy Courses — Product Requirements Document

v0.2 · 2026-10-26 · CSE451 / CSC445, Autumn 2026, IUB
Source: project proposal (Oct 12, 2026). Stack: [ADR-0001](adr/0001-stack-next-js-typescript-postgresql-prisma-responsive-web-fi.md) (proposed).

## 1. Problem

IUB students lack a trusted, affordable and syllabus-matched way to get help from proven seniors,
and seniors lack a fair way to offer it. Peer help happens today in Facebook groups, with no grade
check, no reviews and no refunds.

## 2. Users

| Role | Who | Wants |
|---|---|---|
| Learner | IUB student | Cheap, syllabus-matched help; a free look before paying; a refund if it goes wrong |
| Tutor | IUB senior or alumnus with a verified A / A- in the course | To earn from teaching on campus |
| Advisor | Faculty member or club executive | One place where students book their time, free |
| Admin | Platform staff (the team, for the prototype) | To verify tutors, handle refunds and disputes, pay tutors |

## 3. Goals

1. A learner can find a verified tutor for a course code, try a free demo, and subscribe in one sitting.
2. Only tutors with an admin-approved A or A- can sell a course.
3. Money is tracked end to end: payment → subscription → refund or tutor payout (70/30, 80/20 for top tutors).
4. Students can book free advising slots with faculty and club executives.

## 4. Non-goals (v1)

- Students outside IUB.
- Our own video hosting or video calls (we link to YouTube unlisted, Zoom, Google Meet).
- Paid advising; tutor-set prices; automatic grade check against the IUB portal; AI features.
- Native Android / iOS apps (the web app is responsive; native comes later and reuses the API).
- Real money: the prototype uses a sandbox payment gateway only.

## 5. Functional requirements

Priority is MoSCoW (M must, S should, C could). **Proto** marks the core flow the semester
prototype must show (proposal deliverable 9).

### Accounts and verification

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-01 | Sign up and log in with an IUB email | M, Proto | Only `@iub.edu.bd` addresses are accepted; the email is confirmed by a link or code before first use |
| FR-02 | Log out and reset password | M | A reset link sent to the IUB email sets a new password; old sessions end |
| FR-03 | Profile with name, student ID, department, photo | M | The profile is saved and shown on the tutor page |
| FR-04 | Apply as a tutor for a course by uploading a transcript (PDF / image) | M, Proto | The application shows "pending" until reviewed; files up to 5 MB |
| FR-05 | Admin approves or rejects a tutor application per course, with a reason | M, Proto | Approved: the tutor can publish that course. Rejected: the tutor sees the reason |
| FR-06 | Only A or A- grades are approvable | M | Admin cannot approve if the grade entered is below A- |
| FR-07 | Admin assigns the advisor role to faculty and club executives | M | Advisor accounts can publish advising slots |
| FR-08 | Verified badge on tutor and advisor profiles | S | The badge shows on search results and profile |

### Course offerings

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-09 | Tutor creates an offering for an approved course and semester | M, Proto | An offering cannot be created for an unapproved course |
| FR-10 | Tutor adds a free intro video link (YouTube unlisted) | M, Proto | The link is validated as a YouTube URL and playable for anyone logged in |
| FR-11 | Tutor adds recorded class links and notes (PDF) | M | Visible only to subscribed learners |
| FR-12 | Tutor schedules live group classes with a meeting link | M | Subscribers see the date, time and link; others do not see the link |
| FR-13 | Tutor schedules free live group demos with a seat limit | M, Proto | Anyone logged in can see the demo; the link is shown only to those who booked |
| FR-14 | Offering price is set by the platform (500 taka; 200 taka one-to-one add-on) | M | Tutors cannot edit the price; admin can change it in settings |
| FR-15 | Tutor can unpublish an offering | S | Existing subscribers keep access until the end of the semester |

### Discovery and demo

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-16 | Search offerings by course code (e.g. `CSE211`) | M, Proto | Partial, case-insensitive match; results in under 1 s for 1,000 offerings |
| FR-17 | Filter and sort results by rating, price, number of subscribers | S | Sorting changes the order shown |
| FR-18 | Offering page: tutor, grade badge, intro video, syllabus outline, rating, reviews | M, Proto | All the listed parts show on one page |
| FR-19 | Book a seat in a free live demo | M, Proto | Booking fails when the demo is full; the learner gets the meeting link and an email |
| FR-20 | Cancel a demo booking | S | The seat is freed |

### Subscriptions and payments

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-21 | Subscribe to an offering for the semester (500 taka) | M, Proto | After a successful payment, the learner sees all subscriber content right away |
| FR-22 | Pay by bKash, Nagad or card through a sandbox gateway | M, Proto | A payment that fails or is cancelled gives no access; a successful one is recorded once only, even if the gateway calls back twice |
| FR-23 | Buy a one-to-one session add-on (200 taka) for a subscribed offering | S | Allowed only with an active subscription; the tutor sees the request |
| FR-24 | Learner sees their subscriptions and payment receipts | M | Shows each payment's amount, date, method and status |
| FR-25 | Request a refund with a reason | M | Allowed only inside the refund window (see open question Q1); the status shows on the subscription |
| FR-26 | Admin approves or rejects refunds | M | An approved refund ends access and is marked refunded in the sandbox |

### Ratings and reviews

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-27 | Only subscribed learners rate (1–5) and review an offering, once each | M | A non-subscriber gets no review form; a second review edits the first |
| FR-28 | Average rating and count show on the offering and the tutor | M | Updated within one page load after a new review |
| FR-29 | Report a review or a tutor | S | The report appears in the admin queue |

### Advising

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-30 | Advisor publishes free time slots with a meeting link or room | M | Slots appear on the advisor's page |
| FR-31 | Student books and cancels an advising slot | M | One student per slot; both sides get an email |

### Admin and payouts

| ID | Requirement | Pri | Acceptance criteria |
|---|---|---|---|
| FR-32 | Admin queue for tutor applications, refunds and reports | M | Each item can be acted on and shows who acted and when |
| FR-33 | Revenue split per payment: 70% tutor / 30% platform; 80/20 for top-rated tutors | M | The split is stored on each payment; the rule for "top-rated" is configurable (Q2) |
| FR-34 | Monthly payout report per tutor (earned minus refunds) | M | The admin can export it as CSV and mark a payout as paid |
| FR-35 | Admin dashboard: users, active subscriptions, revenue, open disputes | C | The numbers match the database |
| FR-36 | Email notifications for key events (approval, payment, booking, refund) | S | An email is sent within 1 minute of the event |

## 6. Non-functional requirements

| ID | Need | Target (guesses until Task 5) |
|---|---|---|
| NFR-01 | Performance | Pages load in under 2 s on 4G; API p95 under 500 ms |
| NFR-02 | Availability | 99% monthly during the semester (free-tier hosting) |
| NFR-03 | Responsive | Usable from 360 px phone width to desktop |
| NFR-04 | Security | Passwords hashed (argon2 or bcrypt); HTTPS only; role checks on every API route |
| NFR-05 | Privacy | Transcripts visible only to the uploader and admins; no grades shown publicly beyond the A / A- badge |
| NFR-06 | Payments | No card or wallet data stored by us; the gateway handles it |
| NFR-07 | Auditability | Every money and verification action is logged with actor and time |
| NFR-08 | Accessibility | WCAG 2.1 AA for colour contrast and keyboard use on the core flow |
| NFR-09 | Cost | Runs at 0 taka per month on free tiers during the semester |
| NFR-10 | Maintainability | Lint and type check pass; every change is reviewed; unit test coverage of 70% or more on the service layer |
| NFR-11 | Testability | Core flow covered by automated browser tests in CI |
| NFR-12 | Portability | All business logic sits behind `/api` so a mobile app can reuse it |

## 7. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| IUB does not allow paid peer tutoring | Project cannot launch for real | Talk to the department early; the prototype stays sandbox-only |
| Fake or edited transcripts | Trust lost | Manual admin check; ask for the official portal PDF; allow reports |
| Payment gateway sandbox access is slow to get | Payments can't be demoed | Payment adapter with a mock gateway first (see TRD) |
| Tutors stop teaching mid-semester | Refund requests pile up | A refund window and a dispute queue; the rating shows it |
| The team overruns 14 weeks | Missing deliverables | MoSCoW: the Proto items first; Could items cut first |
| Free-tier limits (DB size, emails) | Outage during the demo | Seed small data; monitor the quotas |

## 8. Open questions

- **Q1 Refund rule.** Guess: full refund if requested within 14 days of subscribing and before the 3rd live class. Needs the team's decision.
- **Q2 Top-rated rule for 80/20.** Guess: an average of 4.5 or more with at least 10 reviews in the last semester.
- **Q3 IUB permission.** Who in the department to ask, and by when.
- **Q4 Payment gateway.** Which sandbox to use (SSLCommerz covers bKash, Nagad and cards in one; direct bKash needs merchant credentials).
- **Q5 Tutor grade source.** Is a transcript screenshot enough, or must it be the official PDF?
