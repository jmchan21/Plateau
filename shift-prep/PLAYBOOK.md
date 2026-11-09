# Shift Prep Playbook: UCI Health Hospitalist / Nocturnist / ICU

Goal: understand every patient well enough to be safe in about 5 minutes each, on the day of service, while hitting quality measures and documenting to the level of care you provide.

Context this is built for:
- UC Irvine, academic center, two hospitals on **one Epic system** (set up once, works at both).
- Paid per shift. RVU content is here so you **learn it for a future practice**, and because the department still tracks attending documentation and wRVUs.
- Department dot phrases and note templates already exist. Your personal phrases are **add-ons**: A/P blocks, an MDM phrase, quality checks, and Secure Chat messages. Attestations: always UCI's approved versions (see `SMARTPHRASES.md`).
- Abridge is available. You haven't used it yet (see the Abridge section).

## The reframe

The question is not "how do I review charts faster." It is:

> How do I build a reliable picture of each patient in 5 minutes, on the day I see them, in a way that leaves a better chart for the next doctor?

1. **Review on the day of service, not the day before.** For time-based billing, non-face-to-face time counts only on the date of the encounter. Even on a per-shift salary, this is the habit you want for future practice.
2. **Let Epic do the reading.** Saved filters and list columns show what changed. You read deltas, not whole charts.
3. **Leave a running summary.** A 3 to 5 line "Hospital Course to Date" (`.JMCCOURSE`) at the top of your A/P means the next doctor (often you, two weeks later) never rebuilds the story.

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
Load `SMARTPHRASES.md`, and write A/Ps per `AP-STYLE.md`. Before building any, open SmartPhrase Manager and search the department's existing phrases (search by author of a full-time hospitalist you like, or keywords like "sepsis", "attest", "secure chat"). Copy and personalize instead of starting from scratch.

## Your shift types

### A. Day shift: 12 new-to-you patients plus about 5 overnight admissions

This is the hardest shift because nothing is familiar. The fix is **tiered review depth** plus **reviewing into the note**: you write the A/P as you read, so chart review and documentation happen once, not twice.

**Time-boxed plan for a 17-patient day**

| Time | Task |
|---|---|
| 0700 to 0715 | Sign-out from the nocturnist. Ask three questions: who's sickest, who could go home today, what's pending. |
| 0715 to 0730 | List triage (columns sorted by Deterioration Index, then EDD). Tag each patient: **Sick / Going home / New admit / Stable**. Secure Chat case management with likely discharges (`.JMCSCDISPO`). |
| 0730 to 0900 | Review into the note (tiers below). Place consult orders and call consultants for new admits **now**, so consults happen today. |
| 0900 to 1130 | Bedside: Sick, then Going home (discharge orders by 1100), then New admits (use Abridge here), then Stable. About 8 min each. |
| 1130 to 1300 | Consultant and family calls; discharge summaries. |
| 1300 to 1600 | Finish notes (already about 70% written), afternoon recheck of Sick, update EDDs and handoff. |

**Tiered review depth (about 85 min total for 17 patients)**

| Tier | Who | Depth | Time each |
|---|---|---|---|
| 1 | Going home and stable long-stayers | Last progress note A/P, Synopsis, MAR, Dispo filter | 3 min |
| 2 | Sick established patients | Full 6-step review below | 5 min |
| 3 | Overnight admissions | H&P A/P, ED note, overnight results, quality gap check | 7 min |

**Review into the note:** open your progress note (department template), copy forward the last A/P (or the H&P A/P for new admits), then edit each problem line by line as you check the chart. Rewrite each problem title to the specific diagnosis, add a trajectory word, and delete what you can't verify (see `AP-STYLE.md`). After the bedside visit, you only add the exam and any changes.

**The 6-step review (same order every time):**
| Step | Where | Looking for |
|---|---|---|
| 1 | Last progress note, A/P only | Active problems, plan, pending items |
| 2 | "MD notes 48h" filter | Consultant recs, overnight events |
| 3 | Synopsis | Trends, new micro and imaging |
| 4 | MAR | Antibiotic day and stop date, anticoagulation, insulin, PRN opioids, held meds |
| 5 | Orders + LDAs | Foley, line, tele, diet, VTE prophylaxis, code status |
| 6 | "Dispo" filter | PT/OT, placement barriers, EDD |

**Overnight admissions quality gap check** (residents often leave these open): code status discussed, med rec done, VTE prophylaxis ordered, inpatient vs observation status correct, Foley or line justified, sepsis bundle timing documented.

**Attesting overnight H&Ps (your usual role):** you attest most overnight resident H&Ps, so the initial visit (99221 to 99223) is yours. These are your highest-value notes of the day. Your 7-minute review plus bedside visit is the "personal participation" the attestation must describe. Use UCI's approved attestation, and make sure your note shows your own findings, your image or ECG read, and what you changed. Most sepsis, respiratory failure, and new heart failure admissions meet high MDM (99223) when you document it. The date of service is the date you personally see the patient; confirm edge cases (resident admits at 0200, you see at 1000) with UCI coding.
**When a night attending already attested:** the initial visit is theirs. Your visit is subsequent care (99231 to 99233), and day 1 often meets high MDM (99233).

**The first-day tax:** writing a 3-line `.JMCCOURSE` for each of 12 new patients adds about 15 minutes on day 1. If you work the next day (or the next attending does), it saves 30+ minutes.

### Decoding a messy chart (copy-paste notes, no reasoning)

Disorganized notes are common, not a personal failing of one group: in one academic center's analysis of 23,630 inpatient progress notes, 46% of text was copied and 36% imported; only 18% was typed new (Wang, JAMA Intern Med 2017, PMID 28558106). So don't read the notes front to back. **Rebuild the story from primary sources, which can't be copy-pasted:**

| Source | Why it's reliable | What to pull |
|---|---|---|
| ED provider note and first H&P | Written fresh, before copy-forward | Why they came in, initial thinking |
| Consult notes | Usually reasoned and current | The specialist's diagnosis and plan |
| Orders (include discontinued) and MAR history | Show what doctors **did**, with dates | Antibiotic start/stop, diuretics, drips, procedures, imaging ordered |
| Synopsis trends | Objective | Is it getting better or worse |
| Nursing, case management, PT/OT notes | Often the most current narrative | Function, barriers, family dynamics |
| The nurse at the bedside (30 seconds) | Knows the last 12 hours | "What's changed, what's worrying you?" |

If UCI's Epic has note provenance highlighting (copied vs typed text) or an AI chart summary, use them to skip copied blocks and get a first-pass timeline, then verify against the sources above.

**Fill the 5-question sticky note (`.JMCRECON`) as you go, 7 minutes max:**
1. Why are they here? (one line)
2. What has been done, with dates?
3. What is working, what is not?
4. What are they waiting for?
5. What could hurt them in the next 24 hours?

If the story is still unclear after 7 minutes, stop reading. Ask the patient and nurse, and Secure Chat or call the prior attending (`.JMCSCPRIOR`). Then turn the sticky note into `.JMCCOURSE` and rewrite the A/P in your format. From that day forward the chart is clean, for you and everyone after you.

### B. Night shift with an APP (admissions and cross-cover)
- **At sign-in, agree on division of labor out loud:** who takes which admissions (for example alternating, or you take the sicker or ICU-bound ones), who takes cross-cover pages, and when you check in (for example 2300 and 0300).
- **Shared tracker:** use the Epic patient list with a "Night" column or Sticky Notes so neither of you double-works a page.
- **APP admissions:** review the A/P, see the patient if unstable or if you'll attest. Know the split/shared rules (RVU section).
- **Before 0600:** both of you update handoffs with contingencies.

### C. Night ICU with two IM residents (teaching)
- **Huddle at sign-in:** illness severity for each patient (I-PASS), who's on the edge, which resident covers which beds, your call thresholds ("call me for any new pressor, intubation, MAP under 65 for 15 min, rapid response, family asking for goals of care").
- **Your review:** spend your 5 minutes per patient on the sickest third. For the rest, rely on the resident handoff and spot-check the Synopsis.
- **Documentation:** residents write; you attest. Critical care time counts **only your own time** (not time teaching, not resident time without you). Use UCI's approved critical care attestation.
- **Midnight and 0400 check:** quick list review by Deterioration Index and new results.

### D. Night ICU solo
- Your highest-acuity, highest-RVU night. Triage the same way, but write brief notes in real time. A 3-line event note at 0200 takes 2 minutes. Reconstructing it at 0630 takes 15 and is less accurate.
- Use `.JMCCC` for critical care and `.JMCEVENT` for events.
- Procedures (central line, arterial line, intubation, thoracentesis) are billed separately and their time is **subtracted** from critical care time. Write the procedure note right after the procedure.

### E. Cross-cover pages (any night)
- Use `.JMCEVENT` for anything that changed management: bedside eval, new imaging, transfer, new med beyond a one-time PRN.
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

**Research angle 2 (note quality):** your frustration with disorganized notes is a measurable QI problem. Design: rate a random sample of hospitalist progress notes with the PDQI-9 (a validated 9-item note quality tool; Stetson, Appl Clin Inform 2012, PMC3347480), introduce a standardized A/P format (`AP-STYLE.md`) as a department template, and re-rate after 3 months. Add note length and copied-text percentage if Epic provenance data is available. Fits SHM Converge or a hospital QI symposium.

**Research angle:** "Effect of ambient AI documentation on note time and after-hours charting for nocturnists and per diem hospitalists" is a timely QI or research question. UCI likely has Epic Signal data (time in notes, pajama time). Ask the department's QI lead whether pre/post data on Abridge adoption is available.

## Quality measures built into every note

Confirm UCI's hospitalist and ICU scorecard with the division's quality lead. Common ones:

**Daily (in `.JMCQC`):** VTE prophylaxis or contraindication; Foley still needed (CAUTI); central line still needed (CLABSI); antibiotic day and stop date; C. diff testing only with 3+ unformed stools in 24 h and no laxatives (HO-CDI); avoid severe hypoglycemia and hyperglycemia (CMS Hospital Harm eCQMs); no opioid plus benzodiazepine at discharge without reason; code status confirmed; expected discharge date and barriers; ICU: SAT/SBT, sedation target, delirium screen, mobility (ABCDEF bundle).

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

### MDM: the honest route when your time is short
See `MDM-GUIDE.md`: a plain-language guide with the 2-of-3 scoring rule, examples, nuances, and the `.JMCMDM` phrase. Discharge, critical care, advance care planning, and prolonged services are billed by time only.

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
- Wang MD, Khanna R, Najafi N. Characterizing the source of text in electronic health record progress notes. JAMA Intern Med. 2017;177:1212-1213. PMID 28558106.
- Stetson PD, et al. Assessing electronic note quality using the Physician Documentation Quality Instrument (PDQI-9). Appl Clin Inform. 2012;3:164-174. PMC3347480.
- Starmer AJ, et al. Changes in medical errors after implementation of a handoff program (I-PASS). N Engl J Med. 2014;371:1803-1812. doi:10.1056/NEJMsa1405556 (PMID to confirm on PubMed).
- Wong A, et al. External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. JAMA Intern Med. 2021;181:1065-1070. PMID 34152373. (Why sepsis alerts are a prompt, not a diagnosis.)
- Thygesen K, et al. Fourth Universal Definition of Myocardial Infarction (2018). J Am Coll Cardiol. 2018;72:2231-2264. PMID 30153967.
- AMA CPT 2023 E/M Guidelines (hospital inpatient and observation services).
- CMS Medicare Claims Processing Manual 100-04, Ch. 12 (teaching physician, split/shared, critical care); MLN006764 Evaluation and Management Services Guide (G0316 thresholds).

For education. Billing rules change yearly and payers differ. Confirm with UCI's coding and compliance team before relying on any of this for billing.
