# CSE451 Project Requirements

Source: Progressive Project template (Prof. Syeed) and the 8 lecture PDFs. Saved 2026-10-26.
The project is one document that grows task by task: 120 marks in total, scaled to 20 marks of CLO2.
📊 = a diagram you have to draw. Progress is tracked in [checklist.md](checklist.md).

## Task 1 — Software Process (Lectures 1–2) · 10 marks
- Product characterisation write-up: application domain, software-vs-hardware traits, failure causes, maintenance split %, two software myths
- Process-model comparison table: 3 candidate models scored against 5 criteria, plus a justification of 150 words or less
- 📊 Tailored lifecycle diagram: phases with time-boxes, milestones, the artefact at each phase, reviews, and where Tasks 2–8 happen

## Task 2 — Requirements Engineering (Lecture 3) · 22 marks (the biggest task)
- Stakeholder table with at least 8 groups
- 📊 Power–Interest grid
- Elicitation plan (3 techniques) and 5 context-free questions
- Requirements catalogue: at least 12 FRs and 6 NFRs, MoSCoW priority, and a metric for every NFR
- 6 user stories, each checked against INVEST, with acceptance criteria
- 📊 Use-case diagram: at least 6 use cases, all actors including external systems, at least one «include» and one «extend»
- Fully dressed use-case narrative for one core use case
- Analysis class table (Boundary / Control / Entity)
- CRC cards for 2 key classes
- 📊 ER diagram: PKs, cardinality and modality, weak entity
- 📊 State diagram: at least 5 states, with event/guard/action on each transition
- 📊 Level-1 DFD for a core process
- Win-win negotiation record for 2 conflicting requirements
- Review checklist (8 questions) applied to 3 requirements
- Traceability matrix: requirement → use case → design module → test case
- 📊 Change-control workflow diagram and the baseline definition

The lecture also lists these as analysis models, but the template doesn't require them:
📊 activity/swimlane diagram, 📊 sequence diagram, 📊 class diagram. Ask Masum sir whether the
section wants them. A swimlane diagram also helps with Task 3.3's task analysis.

## Task 3 — Software Design (Lecture 4) · 16 marks
- Module table: at least 6 modules, with responsibility, interface, information hidden, and dependencies
- 📊 Module/component diagram with directed dependencies
- Cohesion/coupling diagnosis of a "god class"
- 📊 Before and after structure diagrams for the refactor
- Cross-cutting concerns (2 or more)
- Mandel's 3 golden rules applied to the design, 3 personas, and a task analysis
- 📊 Annotated wireframes for 2 key screens
- 📊 Corrected wireframe of the flawed login screen
- Fitts's Law justification for the main button

## Task 4 — Product Metrics (Lecture 4) · 14 marks
- Function-point table, the 14 VAF ratings, and the final FP (this number carries into Task 7)
- OO metrics (WMC, DIT, NOC, CBO, RFC, LCOM) for 2 classes, plus Whitmire's characteristics
- Halstead calculations, SMI calculation, and 2 testing metrics

## Task 5 — Quality Attributes (Lecture 5) · 10 marks
- 6 vague wishes rewritten in the six-part form and mapped to ISO 25010
- Availability and error-budget calculations
- 6×6 trade-off matrix and 2 conflict resolutions

## Task 6 — Testing (Lecture 5) · 18 marks
- 📊 V-model diagram for the project
- Test plan: test levels, environment, test data, integration strategy, stubs/drivers, entry/exit criteria, smoke and regression tests
- 📊 Flow graph, V(G) worked out 3 ways, basis paths, and test-case table
- Equivalence classes, boundary values, 📊 decision table, and the minimal test set
- Coverage targets and 📊 CI/CD pipeline diagram
- Release-gate defect metrics

## Task 7 — Project Management (Lecture 7) · 18 marks
- FP → KLOC → COCOMO estimate, a second estimate, cone of uncertainty, and a make/buy decision
- 📊 3-level WBS
- 📊 Activity-on-node network, ES/EF/LS/LF/slack table, and the critical path
- 📊 Gantt chart with milestones
- 40-20-40 effort split
- PERT table and probability calculations
- Earned value analysis (BCWS, BCWP, ACWP, SV, CV, SPI, CPI, EAC)

## Task 8 — Risk Management (Lecture 8) · 12 marks
- At least 10 risks from the 7-category checklist, written as condition → consequence statements
- Risk table with RE values and a cut-off line
- 📊 Probability–impact heat map
- RMMM entries for the top 3 risks
- RRL calculation and 📊 decision tree
- Avoid / transfer / mitigate / accept mapping
- Triggers and owners for the top 5 risks, 📊 risk burndown chart, and contingency %

## Also expected (not in the template)
- The PRD Masum sir asked for, and possibly a full SRS. Lecture 3 gives the ISO 29148 structure:
  Introduction, Overall Description, Specific Requirements, Appendices.
- Lecture 6 (Configuration Management) has no project task.

Diagram count: about 20 diagrams across the whole project.

## Rules
- **Use your own topic.** The template is written around UniRide. Do every task on your own project (Proxy Courses). Copying lecture examples counts as non-submission.
- **Submit on time.** Each task is due the week its lecture finishes. Late tasks lose their viva marks.
- **Show all your working.** Any number without working gets zero accuracy marks.
- **Check the fixed numbers with your section.** Some template items are specific to UniRide: the fare pseudocode, the reservation rule, the Task 7 activity list, and the Halstead/SMI figures. Ask Masum sir whether your section uses the same ones or makes its own.
