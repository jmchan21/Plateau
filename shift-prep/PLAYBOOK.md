# Per Diem Shift Prep Playbook (Hospitalist / Intensivist, Epic)

Goal: understand every patient well enough to be safe in about 5 minutes each, on the day of service, with no unpaid prior-day chart review, while hitting quality measures and documenting to the level of care you actually provide.

## The reframe

The question is not "how do I review charts faster." It is:

> How do I build a reliable picture of each patient in 5 minutes, on the day I bill, in a way that leaves a better chart for the next doctor?

Three consequences:
1. **Move chart review to the day of service.** Under the 2023 E/M rules, non-face-to-face time (reading notes, reviewing results) counts toward time-based billing only on the date of the encounter. Prior-day review is unpaid. Same-day review is billable time.
2. **Let Epic do the reading.** Saved filters, patient list columns, and SmartLinks surface what changed. You read deltas, not whole charts.
3. **Leave a running summary.** A "Hospital Course to Date" block in every note means the next per diem doctor (often you) never has to rebuild the story.

## One-time setup (about 2 hours per Epic system)

Do this once at each health system. Separate health systems usually run separate Epic instances, so personalization does not travel. Keep the master text in `SMARTPHRASES.md` and paste it into each system's SmartPhrase Manager.

### 1. Patient list columns (the 60-second triage)
Add these columns to your patient list (right-click the column header, or the wrench icon, then "Properties" / "Columns"). Names vary by organization; search for the closest match:
- Deterioration Index or early warning score
- Sepsis alert / BPA flag
- Code status
- Admit date and LOS (compare with the GMLOS column if your site has it)
- Expected discharge date
- Readmission risk score
- New results / unacknowledged results flag
- LDA column (central lines, Foley, airway) for CLABSI and CAUTI
- Isolation
- Sticky note (your private per-patient to-do)

Sort by Deterioration Index first. Sick patients get seen first; dischargeable patients get seen second so the discharge order goes in early.

### 2. Chart Review saved filters
In Chart Review, set a filter and save it ("Save Filter" or the star). Build four:
- **MD notes 48h:** Progress, H&P, Consult, Discharge, Procedure note types; physician and APP authors; last 48 hours.
- **Consults only:** all Consult notes, this admission.
- **Dispo:** Case management, Social work, PT/OT, Nutrition notes.
- **Events:** Rapid response, Code, Transfer, Nursing event notes.

### 3. Results Review / Synopsis
Build a Synopsis or flowsheet view with: vitals trend, I/O, O2 device and FiO2, BMP, CBC, Mg/Phos, lactate, troponin, BNP, glucose POC, INR, cultures. One screen, 72-hour trend.

### 4. SmartPhrases
Load the templates in `SMARTPHRASES.md`: progress note, H&P, cross-cover note, critical care attestation, discharge summary, and a quality checklist. SmartLink names (the `@...@` tokens) differ between organizations. In the SmartPhrase editor, type `@` and search for the equivalent (vitals, labs, I/O, active meds, LDAs, problem list).

### 5. Check what AI tools the site has
Many Epic sites now offer generative AI summaries in Chart Review and ambient documentation (Abridge, DAX Copilot, or Epic's own). If available, use the hospital-approved tool for a first-pass summary, then verify against primary data. **Never paste PHI into a consumer AI tool** (including personal Claude, ChatGPT, or notes apps) unless the hospital has a BAA covering it.

## Shift workflow

### Minute 0 to 15: triage the whole list
1. Read the I-PASS handoff for every patient (Handoff activity or sign-out report).
2. Scan the patient list columns. Flag: high deterioration score, sepsis alert, new results, LDA present, EDD today or tomorrow.
3. Sort into three buckets: **Sick** (see first), **Going home** (see second, discharge order before noon), **Stable** (see last).

### Per patient: the 5-minute review (same order every time)
| Step | Where | What you are looking for | Time |
|---|---|---|---|
| 1 | Last progress note, A/P only | Active problems, plan, pending items | 60 s |
| 2 | H&P A/P (first encounter only) | Why they came in, baseline | 30 s |
| 3 | "MD notes 48h" filter | Consultant recs, overnight events | 60 s |
| 4 | Synopsis / Results Review | Trends, not single values. New micro, imaging | 60 s |
| 5 | MAR | Antibiotic day and stop date, anticoagulation, insulin, PRN opioid use, held meds | 45 s |
| 6 | Active orders + LDAs | Foley, central line, telemetry, diet, VTE prophylaxis, code status | 30 s |
| 7 | "Dispo" filter | PT/OT recs, placement barriers, EDD | 15 s |

Write a private Sticky Note with your 1-line to-dos while you review. Then see the patient.

### Night shift / cross-cover version
- Admissions: use the H&P template. Admissions are the highest-RVU encounters you do; document MDM fully.
- Cross-cover calls: use the cross-cover note. A brief event note with your assessment and plan is billable (usually 99231 to 99232, or 99291 if critical care time is met) and documents your reasoning if something goes wrong later.
- Before you leave: update the I-PASS handoff with your contingencies.

## Quality measures to build into every note

These are the measures most hospitals track on hospitalist and ICU scorecards. Confirm your own scorecard with each site's medical director.

**Daily checklist (built into the progress note template):**
- [ ] VTE prophylaxis ordered, or contraindication documented
- [ ] Foley still needed? (CAUTI) Remove if no indication
- [ ] Central line still needed? (CLABSI) Remove if no indication
- [ ] Antibiotics: day number, indication, planned stop date (stewardship)
- [ ] C. diff testing only if 3+ unformed stools in 24 h and no laxatives (HO-CDI)
- [ ] Glucose: avoid severe hypo and hyperglycemia (CMS Hospital Harm eCQMs)
- [ ] Opioids: avoid opioid plus benzodiazepine at discharge (Safe Use of Opioids eCQM); naloxone if indicated
- [ ] Code status confirmed and documented
- [ ] Expected discharge date and barriers documented
- [ ] ICU: SAT/SBT done, sedation target, delirium screen, early mobility (ABCDEF bundle)

**Admission-specific:**
- SEP-1: lactate, blood cultures before antibiotics, antibiotics within 3 h, 30 mL/kg crystalloid for hypotension or lactate 4 or higher (or documented reason for less), repeat lactate if initial above 2, vasopressors for persistent hypotension. Document the time of your reassessment.
- Medication reconciliation completed.

**Discharge-specific:**
- Discharge order before noon when possible.
- Readmission risk: follow-up appointment within 7 days for HF, COPD, pneumonia, AMI (HRRP conditions). Clear medication changes list.

**Documentation that drives your observed/expected metrics (CDI):**
Hospitals judge physicians on mortality and LOS indexes (observed over expected). "Expected" comes from what you document. Be specific:
- "Acute on chronic HFrEF" (not "CHF exacerbation")
- "Acute hypoxic respiratory failure" with criteria (SpO2 below 91% on room air, or P/F below 300, plus work of breathing)
- "Sepsis with acute organ dysfunction" or "septic shock" (name the organ)
- "AKI, KDIGO stage 2" (not "elevated creatinine")
- "Severe protein-calorie malnutrition" when the dietitian documents criteria (also the CMS malnutrition measure)
- "Acute metabolic encephalopathy" (not "confusion" or "AMS")
- "Type 2 MI" vs "demand ischemia" vs "non-ischemic myocardial injury" (follow the Fourth Universal Definition)
Answer CDI queries the same day. Query response time is a tracked metric at many sites.

## Billing and RVU cheat sheet (2023+ CPT rules)

Pick the level by **MDM or total same-day time, whichever is higher.** Time includes chart review, documentation, family meetings, and talking with consultants on the date of service. It excludes separately billed procedures.

| Code | Service | Time threshold |
|---|---|---|
| 99221 / 99222 / 99223 | Initial hospital care | 40 / 55 / 75 min |
| 99231 / 99232 / 99233 | Subsequent care | 25 / 35 / 50 min |
| 99238 / 99239 | Discharge day | 30 min or less / more than 30 min |
| 99291 | Critical care, first 30 to 74 min | 30 min minimum |
| 99292 | Each additional 30 min | Medicare: at 104 min total. CPT: at 75 min |
| G0316 (Medicare) | Prolonged inpatient, each 15 min | With 99223 at 90 min; with 99233 at 65 min |
| 99418 (non-Medicare) | Prolonged inpatient, each 15 min | 15 min past the top of the 99223 / 99233 range |
| 99497 / 99498 | Advance care planning | 16 min minimum / each additional 30 min |

**How to reach high MDM (99223 / 99233) honestly:** you need 2 of 3:
- **Problems:** 1 or more chronic illness with severe exacerbation, or an acute illness posing a threat to life or bodily function.
- **Data:** 2 of 3 categories: (a) 3 items from unique tests reviewed or ordered, external notes reviewed, independent historian; (b) independent interpretation of a test (your own read of the ECG, CXR, or CT images); (c) discussion of management with an external physician (consultant).
- **Risk:** drug therapy requiring intensive monitoring for toxicity (heparin drip, vancomycin levels, insulin drip, aminoglycosides); decision about escalation of hospital-level care; decision about DNR or de-escalation; parenteral controlled substances.

Hospitalists commonly under-document what they already do: "I personally reviewed the CXR images: ...", "Discussed with cardiology (Dr. X) who recommends ...", "Heparin infusion requiring q6h anti-Xa monitoring for toxicity."

**Easy RVUs often missed:**
- Advance care planning (99497) during a goals-of-care talk of 16 min or more. Document time, participants, and content. Also supports code status quality metrics.
- Prolonged services on complex admissions and long family meetings.
- Critical care (99291) for floor patients during a rapid response if you spend 30 min or more on critical care.
- Discharge over 30 min (99239) is common for complex discharges. Document the time.

**Do not** bill time spent on the day before your shift, time spent teaching, or time already counted in a procedure.

## Track it: personal shift log (no PHI)

Keep a log per shift with only counts and codes: date, site, census, admissions, discharges, codes billed, critical care minutes, minutes spent on pre-rounding. Use it to see which sites and habits pay off. A Google Sheet works.

## This is also a research project

This workflow is a ready-made QI project that fits your interests:
- **Question:** Does a standardized EHR review bundle (saved filters, templated notes, quality checklist) reduce per-patient pre-rounding time and improve quality measure capture for per diem hospitalists?
- **Design:** pre/post, single physician or small group. Measures: minutes per patient (Epic Signal / audit log data if the site shares it, or self-timed), VTE prophylaxis compliance, Foley days, discharge before noon, documented code status, wRVU per shift.
- **Venue:** SHM Converge abstract or the hospital's QI symposium.
- Ask the site's QI office whether IRB determination is needed (usually "QI, not human subjects research").

## References
- Starmer AJ, et al. Changes in medical errors after implementation of a handoff program (I-PASS). N Engl J Med. 2014;371:1803-1812. doi:10.1056/NEJMsa1405556 (PMID to confirm on PubMed).
- Wong A, et al. External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. JAMA Intern Med. 2021;181:1065-1070. PMID 34152373. (Why sepsis alerts are a prompt, not a diagnosis.)
- Thygesen K, et al. Fourth Universal Definition of Myocardial Infarction (2018). J Am Coll Cardiol. 2018;72:2231-2264. PMID 30153967.
- AMA CPT 2023 E/M Guidelines (hospital inpatient and observation services).
- CMS Medicare Claims Processing Manual 100-04, Ch. 12, and MLN006764 (Evaluation and Management Services Guide), for G0316 thresholds.

For education. Billing rules change yearly and payers differ. Confirm with each site's coding or compliance team.
