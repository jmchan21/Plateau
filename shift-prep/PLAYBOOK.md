# Shift Prep Playbook: UCI Health Hospitalist / Nocturnist / ICU

Goal: understand every patient well enough to be safe in about 5 minutes each, on the day of service, while hitting quality measures and documenting to the level of care you provide.

Context this is built for:
- UC Irvine, academic center, two hospitals on **one Epic system** (set up once, works at both).
- Paid per shift. RVU content is here so you **learn it for a future practice**, and because the department still tracks attending documentation and wRVUs.
- Department dot phrases and note templates already exist. Your personal phrases are **add-ons**: A/P blocks, attestations, quality checks, and Secure Chat messages (see `SMARTPHRASES.md`).
- Abridge is available. You haven't used it yet (see the Abridge section).

## The reframe

The question is not "how do I review charts faster." It is:

> How do I build a reliable picture of each patient in 5 minutes, on the day I see them, in a way that leaves a better chart for the next doctor?

1. **Review on the day of service, not the day before.** For time-based billing, non-face-to-face time counts only on the date of the encounter. Even on a per-shift salary, this is the habit you want for future practice.
2. **Let Epic do the reading.** Saved filters and list columns show what changed. You read deltas, not whole charts.
3. **Leave a running summary.** A 3 to 5 line "Hospital Course to Date" (`.JCCOURSE`) at the top of your A/P means the next doctor (often you, two weeks later) never rebuilds the story.

## One-time setup (about 90 minutes, once)

### 1. Patient list columns
Patient list > wrench icon > Properties > Columns. Exact names vary; search for the closest match:
- Deterioration Index (or early warning score) and sepsis BPA flag
- Code status, admit date / LOS, expected discharge date
- Readmission risk
- New or unacknowledged results
- LDAs (central line, Foley, airway) for CLABSI and CAUTI
- Isolation, Sticky Note (private to-do)

Make two list views: **Days** (sorted by expected discharge date, then Deterioration Index) and **Nights / ICU** (sorted by Deterioration Index).

### 2. Chart Review saved filters
Set the filter, then save it (star / "Save Filter"):
- **MD notes 48h:** Progress, H&P, Consult, Procedure, Discharge note types; physician, resident, and APP authors; last 48 h.
- **Consults:** consult notes, this admission.
- **Dispo:** case management, social work, PT/OT, nutrition.
- **Events:** rapid response, code, transfer, nursing event notes.

### 3. Synopsis view
One screen, 72-hour trend: vitals, I/O, O2 device and FiO2, BMP, CBC, Mg/Phos, lactate, troponin, BNP, POC glucose, INR, cultures. ICU version adds vent settings, ABG, pressors, sedation.

### 4. Personal dot phrases
Load `SMARTPHRASES.md`. Before building any, open SmartPhrase Manager and search the department's existing phrases (search by author of a full-time hospitalist you like, or keywords like "sepsis", "attest", "secure chat"). Copy and personalize instead of starting from scratch.

## Your shift types

### A. Day shift: rounding, no admissions, inherit overnight resident admissions
**First 15 minutes:** read the handoff for every patient, scan list columns, sort into **Sick / Going home / Stable**. See sick first, then discharges (aim for the discharge order before noon), then stable.

**Overnight resident admissions (new to you):**
1. Read the resident H&P A/P, then the ED provider note.
2. Check the quality items residents often leave open: code status discussed, med rec done, VTE prophylaxis ordered, inpatient vs observation status, Foley or line justified, sepsis bundle timing documented.
3. Confirm or change the plan at the bedside. Then write your attestation (`.JCATTHP`). The resident's H&P plus your attestation is how an initial visit (99221 to 99223) gets billed in a teaching setting.

**Established patients, the 5-minute review (same order every time):**
| Step | Where | Looking for | Time |
|---|---|---|---|
| 1 | Last progress note, A/P only | Active problems, plan, pending items | 60 s |
| 2 | "MD notes 48h" filter | Consultant recs, overnight events | 60 s |
| 3 | Synopsis | Trends, new micro and imaging | 60 s |
| 4 | MAR | Antibiotic day and stop date, anticoagulation, insulin, PRN opioids, held meds | 45 s |
| 5 | Orders + LDAs | Foley, line, tele, diet, VTE prophylaxis, code status | 30 s |
| 6 | "Dispo" filter | PT/OT, placement barriers, expected discharge date | 15 s |

### B. Night shift with an APP (admissions and cross-cover)
- **At sign-in, agree on division of labor out loud:** who takes which admissions (for example alternating, or you take the sicker or ICU-bound ones), who takes cross-cover pages, and when you check in (for example 2300 and 0300).
- **Shared tracker:** use the Epic patient list with a "Night" column or Sticky Notes so neither of you double-works a page.
- **APP admissions:** review the A/P, see the patient if unstable or if you'll attest. Know the split/shared rules (RVU section).
- **Before 0600:** both of you update handoffs with contingencies.

### C. Night ICU with two IM residents (teaching)
- **Huddle at sign-in:** illness severity for each patient (I-PASS), who's on the edge, which resident covers which beds, your call thresholds ("call me for any new pressor, intubation, MAP under 65 for 15 min, rapid response, family asking for goals of care").
- **Your review:** spend your 5 minutes per patient on the sickest third. For the rest, rely on the resident handoff and spot-check the Synopsis.
- **Documentation:** residents write; you attest. Critical care time counts **only your own time** (not time teaching, not resident time without you). Use `.JCATTCC`.
- **Midnight and 0400 check:** quick list review by Deterioration Index and new results.

### D. Night ICU solo
- Your highest-acuity, highest-RVU night. Triage the same way, but write brief notes in real time. A 3-line event note at 0200 takes 2 minutes. Reconstructing it at 0630 takes 15 and is less accurate.
- Use `.JCCC` for critical care and `.JCEVENT` for events.
- Procedures (central line, arterial line, intubation, thoracentesis) are billed separately and their time is **subtracted** from critical care time. Write the procedure note right after the procedure.

### E. Cross-cover pages (any night)
- Use `.JCEVENT` for anything that changed management: bedside eval, new imaging, transfer, new med beyond a one-time PRN.
- Use the Secure Chat phrases to close the loop with nursing quickly and set parameters, so the same page doesn't come back in 2 hours.

## Abridge: how to start

Ambient AI (Abridge) records the conversation and drafts the note. Best uses for your shifts:
- **Admissions (resident, APP, or your own):** drafts the HPI and history, often the slowest part.
- **Family meetings and goals-of-care talks:** captures who was there and what was discussed, which supports advance care planning documentation.
- **Day rounds on talkative patients:** subjective and interval history.

Less useful: codes, rapid responses, and the ICU at 0300, where the encounter is mostly orders and procedures.

How to start, low-risk:
1. Complete UCI's Abridge onboarding or training and follow its consent script.
2. Pilot it on 2 or 3 stable patients on one day shift. Compare the draft with what you'd have written.
3. Keep your own A/P dot phrases. Let Abridge draft the HPI and subjective, and you write the assessment. The A/P is where your clinical reasoning, MDM, and quality items live.
4. Always read the draft before signing (check meds, doses, laterality, and anything the patient said that wasn't true).

**Research angle:** "Effect of ambient AI documentation on note time and after-hours charting for nocturnists and per diem hospitalists" is a timely QI or research question. UCI likely has Epic Signal data (time in notes, pajama time). Ask the department's QI lead whether pre/post data on Abridge adoption is available.

## Quality measures built into every note

Confirm UCI's hospitalist and ICU scorecard with the division's quality lead. Common ones:

**Daily (in `.JCQC`):** VTE prophylaxis or contraindication; Foley still needed (CAUTI); central line still needed (CLABSI); antibiotic day and stop date; C. diff testing only with 3+ unformed stools in 24 h and no laxatives (HO-CDI); avoid severe hypoglycemia and hyperglycemia (CMS Hospital Harm eCQMs); no opioid plus benzodiazepine at discharge without reason; code status confirmed; expected discharge date and barriers; ICU: SAT/SBT, sedation target, delirium screen, mobility (ABCDEF bundle).

**Admissions:** SEP-1 (lactate, cultures before antibiotics, antibiotics within 3 h, 30 mL/kg for hypotension or lactate 4 or higher or documented reason for less, repeat lactate if above 2, timed reassessment); med rec; correct inpatient vs observation status.

**Discharges:** order before noon when possible; 7-day follow-up for HF, COPD, pneumonia, AMI (HRRP conditions); clear med change list.

**Documentation that drives observed-to-expected mortality and LOS:** be specific. "Acute on chronic HFrEF", "acute hypoxic respiratory failure" with criteria, "sepsis with acute organ dysfunction" or "septic shock", "AKI, KDIGO stage 2", "severe protein-calorie malnutrition" per dietitian criteria, "acute metabolic encephalopathy", "type 2 MI" vs "non-ischemic myocardial injury" (Fourth Universal Definition). Answer CDI queries the same day.

## Learning RVUs (for your future practice)

### Why it matters even on a per-shift salary
- Many private and community hospitalist groups pay base plus productivity (wRVUs) plus quality bonus. Knowing the rules now lets you judge contracts.
- Academic departments track attending wRVUs and documentation quality.

### Code levels and time thresholds (2023+ CPT)
Pick the level by **MDM or total same-day time, whichever is higher.**

| Code | Service | Time threshold | Approx. wRVU* |
|---|---|---|---|
| 99221 / 99222 / 99223 | Initial hospital care | 40 / 55 / 75 min | 1.63 / 2.61 / 3.50 |
| 99231 / 99232 / 99233 | Subsequent care | 25 / 35 / 50 min | 1.00 / 1.59 / 2.40 |
| 99238 / 99239 | Discharge day | 30 min or less / more than 30 | 1.50 / 2.15 |
| 99291 | Critical care, first 30 to 74 min | 30 min minimum | 4.50 |
| 99292 | Each additional 30 min | Medicare: at 104 min total. CPT: at 75 min | 2.25 |
| G0316 (Medicare) | Prolonged inpatient, per 15 min | With 99223 at 90 min; with 99233 at 65 min | |
| 99497 / 99498 | Advance care planning | 16 min minimum / each additional 30 | 1.50 / 1.40 |

*Approximate 2023 Medicare values for learning purposes. Values shift slightly each year; check the CMS Physician Fee Schedule Look-Up tool for current numbers.

Notice the spread: a day of 99232s vs 99233s on 16 patients is about 13 wRVUs. Documenting what you already do to the right level is the largest lever.

### High MDM (99223 / 99233): need 2 of 3
- **Problems:** chronic illness with severe exacerbation, or acute illness posing a threat to life or bodily function.
- **Data:** 2 of 3 categories: (a) 3 items from unique tests reviewed or ordered, external notes reviewed, independent historian; (b) independent interpretation of a test ("I personally reviewed the CXR images: ..."); (c) discussion of management with an external physician ("Discussed with cardiology, who recommends ...").
- **Risk:** drug therapy requiring intensive monitoring for toxicity (heparin or insulin drip, vancomycin levels); decision about escalation of hospital-level care; decision about DNR or de-escalation; parenteral controlled substances.

### Teaching physician rules (your resident shifts)
- For MDM-based billing, the resident documents and you attest that you saw the patient and participated in the key or critical portions, and agree or amend.
- For **time-based** billing (including critical care), only **your** time counts: time you personally spend, or time you are present with the resident. Time spent teaching does not count.
- A vague attestation ("seen and agree") does not support billing. State what you personally did and decided.

### Split/shared visits (your APP shifts)
- When you and an APP in the same group both see a hospital patient, the one who performs the **substantive portion** bills: more than half the total time, or the substantive part of the MDM (CMS rule since 2024). Use modifier FS.
- If the APP bills alone, Medicare pays 85% of the physician rate. If you did the substantive part, document it.
- Critical care can be split/shared (substantive portion = more than half of total critical care time).

### ICU procedures (billed separately; time excluded from critical care)
Central line (36556) plus ultrasound guidance (76937, needs documentation of vessel patency, real-time visualization, and a saved image); arterial line (36620); intubation (31500); thoracentesis with imaging (32555); paracentesis with imaging (49083). Add modifier 25 to the E/M or critical care code when billed with a procedure on the same day.

### Often missed
- Advance care planning (99497) during a goals-of-care talk of 16 min or more.
- Critical care (99291) on a floor patient during a rapid response if 30 min or more of critical care.
- Discharge over 30 min (99239).
- Prolonged services on complex admissions and long family meetings.

### Practice exercise (no PHI)
For one shift a week, privately code each of your notes (level and why) in a simple log: date, shift type, code you'd bill, MDM elements present, time. Compare with what the department's coder assigns, if they'll share it. After 4 to 6 weeks you'll code reliably.

## References
- Starmer AJ, et al. Changes in medical errors after implementation of a handoff program (I-PASS). N Engl J Med. 2014;371:1803-1812. doi:10.1056/NEJMsa1405556 (PMID to confirm on PubMed).
- Wong A, et al. External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. JAMA Intern Med. 2021;181:1065-1070. PMID 34152373. (Why sepsis alerts are a prompt, not a diagnosis.)
- Thygesen K, et al. Fourth Universal Definition of Myocardial Infarction (2018). J Am Coll Cardiol. 2018;72:2231-2264. PMID 30153967.
- AMA CPT 2023 E/M Guidelines (hospital inpatient and observation services).
- CMS Medicare Claims Processing Manual 100-04, Ch. 12 (teaching physician, split/shared, critical care); MLN006764 Evaluation and Management Services Guide (G0316 thresholds).

For education. Billing rules change yearly and payers differ. Confirm with UCI's coding and compliance team before relying on any of this for billing.
