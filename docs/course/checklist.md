# CSE451 Deliverables Checklist — Proxy Courses

Updated 2026-10-26 (Tasks 1–3 drafted) · Requirements: [requirements.md](requirements.md)
Status: ✅ done · 🟡 partial (source to build from) · ⬜ not started · 📊 diagram
Each task lives in its own numbered folder with `diagrams/` (SVG + PNG + source). Rebuild diagrams: `bash docs/course/_tools/build.sh`. Progress slides: [`slides/`](slides/).

## Summary

| Task | Marks | Due (fill in) | Status |
|---|---|---|---|
| 1 Software Process | 10 | | ✅ 3 / 3 · 1 diagram |
| 2 Requirements Engineering | 22 | | ✅ 16 / 16 · 6 diagrams (optional 3 pending sir) |
| 3 Software Design | 16 | | ✅ 9 / 9 · 6 diagrams |
| 4 Product Metrics | 14 | | ⬜ 0 / 3 |
| 5 Quality Attributes | 10 | | 🟡 0 / 3 done, 1 partial |
| 6 Testing | 18 | | 🟡 0 / 6 done, 2 partial |
| 7 Project Management | 18 | | ⬜ 0 / 7 |
| 8 Risk Management | 12 | | 🟡 0 / 7 done, 1 partial |
| PRD / SRS | — | | 🟡 PRD done; SRS not started |

## Task 1 — Software Process → [`1. Software Process/`](1.%20Software%20Process/task-1-software-process.md)
- [x] ✅ Product characterisation: domain, software vs hardware traits, failure causes, maintenance split %, 2 myths
- [x] ✅ Process-model table: 3 models × 5 criteria + justification ≤150 words
- [x] ✅ 📊 Tailored lifecycle diagram: phases, time-boxes, milestones, artefacts, reviews, where Tasks 2–8 sit

## Task 2 — Requirements Engineering → [`2. Requirements/`](2.%20Requirements/task-2-requirements.md)
- [x] ✅ Stakeholder table, ≥8 groups
- [x] ✅ 📊 Power–Interest grid
- [x] ✅ Elicitation plan (3 techniques) + 5 context-free questions
- [x] ✅ Requirements catalogue ≥12 FR, ≥6 NFR, MoSCoW, metric per NFR
- [x] ✅ 6 user stories + INVEST check + acceptance criteria
- [x] ✅ 📊 Use-case diagram: ≥6 UCs, all actors incl. external systems (payment gateway, email), «include», «extend»
- [x] ✅ Fully dressed narrative for one core UC
- [x] ✅ Analysis class table (Boundary / Control / Entity)
- [x] ✅ CRC cards for 2 key classes
- [x] ✅ 📊 ER diagram: PKs, cardinality and modality, weak entity
- [x] ✅ 📊 State diagram ≥5 states, event/guard/action
- [x] ✅ 📊 Level-1 DFD for a core process
- [x] ✅ Win-win record for 2 conflicting requirements
- [x] ✅ Review checklist (8 questions) applied to 3 requirements
- [x] ✅ Traceability matrix FR → UC → module → test case
- [x] ✅ 📊 Change-control workflow + baseline definition
- [ ] ❓ Optional, ask sir: 📊 activity/swimlane, 📊 sequence, 📊 class diagram

## Task 3 — Software Design → [`3. Design/`](3.%20Design/task-3-design.md)
- [x] ✅ Module table ≥6 modules: responsibility, interface, info hidden, dependencies
- [x] ✅ 📊 Module/component diagram with directed dependencies
- [x] ✅ Cohesion/coupling diagnosis of a "god class"
- [x] ✅ 📊 Before and after refactor structure diagrams
- [x] ✅ ≥2 cross-cutting concerns
- [x] ✅ Mandel's 3 golden rules + 3 personas + task analysis
- [x] ✅ 📊 Annotated wireframes for 2 key screens
- [x] ✅ 📊 Corrected wireframe of the flawed login screen
- [x] ✅ Fitts's Law justification for the main button (Subscribe)

## Task 4 — Product Metrics
- [ ] ⬜ FP table + 14 VAF ratings + final FP (feeds Task 7)
- [ ] ⬜ OO metrics (WMC, DIT, NOC, CBO, RFC, LCOM) for 2 classes + Whitmire's characteristics
- [ ] ⬜ Halstead + SMI calculations + 2 testing metrics (❓ ask sir: UniRide figures or our own)

## Task 5 — Quality Attributes
- [ ] 🟡 6 vague wishes → six-part form → ISO 25010 (PRD NFR-01…12 are the raw material)
- [ ] ⬜ Availability + error-budget calculations (NFR-02 targets 99%)
- [ ] ⬜ 6×6 trade-off matrix + 2 conflict resolutions

## Task 6 — Testing
- [ ] ⬜ 📊 V-model diagram
- [ ] 🟡 Test plan: levels, environment, test data, integration strategy, stubs/drivers, entry/exit, smoke, regression (test-plan.md covers levels and cases; the rest is missing)
- [ ] ⬜ 📊 Flow graph + V(G) three ways + basis paths + test-case table (suggest: the payment callback or refund-eligibility function)
- [ ] ⬜ Equivalence classes + boundary values + 📊 decision table + minimal test set (suggest: refund rule, sign-up email)
- [ ] 🟡 Coverage targets + 📊 CI/CD pipeline diagram (70% target and CI steps are in trd.md; the diagram is missing)
- [ ] ⬜ Release-gate defect metrics

## Task 7 — Project Management
- [ ] ⬜ FP → KLOC → COCOMO, a second estimate, cone of uncertainty, make/buy (make/buy: payments, video, calls are "buy")
- [ ] ⬜ 📊 3-level WBS
- [ ] ⬜ 📊 Activity-on-node network + ES/EF/LS/LF/slack table + critical path (❓ ask sir: UniRide activity list or our own)
- [ ] ⬜ 📊 Gantt chart with milestones
- [ ] ⬜ 40-20-40 effort split
- [ ] ⬜ PERT table + probability calculations
- [ ] ⬜ Earned value analysis (BCWS, BCWP, ACWP, SV, CV, SPI, CPI, EAC)

## Task 8 — Risk Management
- [ ] 🟡 ≥10 risks from the 7-category checklist as condition → consequence (PRD §7 has 6, written as a table)
- [ ] ⬜ Risk table with RE values + cut-off line
- [ ] ⬜ 📊 Probability–impact heat map
- [ ] ⬜ RMMM for the top 3 risks
- [ ] ⬜ RRL calculation + 📊 decision tree
- [ ] ⬜ Avoid / transfer / mitigate / accept mapping
- [ ] ⬜ Triggers and owners for the top 5 + 📊 risk burndown + contingency %

## PRD / SRS
- [x] ✅ PRD: [docs/prd.md](../prd.md)
- [ ] ⬜ SRS in ISO 29148 structure (❓ ask sir if required; it can mostly be assembled from the PRD + Task 2)

## Questions for Masum sir
1. Are the activity/swimlane, sequence and class diagrams required for Task 2?
2. Is a full SRS (ISO 29148) required, or is the PRD enough?
3. Do we use the UniRide figures (fare pseudocode, reservation rule, Task 7 activity list, Halstead/SMI) or make our own?
4. Due week for each task.

## Blocking gaps outside the docs
- Team roles (product owner, scrum master, QA lead) are blank in the proposal; Tasks 7 and 8 need names as owners.
