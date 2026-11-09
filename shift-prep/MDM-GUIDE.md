# Medical Decision Making (MDM): A Plain-Language Guide

## The big picture

Every hospital visit note gets a level. Higher level = more RVUs. You can earn the level in one of two ways, whichever is higher:
1. **Time:** the actual minutes you spent that day. Only honest if you really spent them.
2. **MDM:** how hard the thinking was. Minutes don't matter.

**For you, MDM is the honest route.** A sick patient you sort out efficiently in 20 minutes can still be a high-level visit, because the level reflects the difficulty and risk of the decisions, not the time spent. Efficient doctors are meant to bill by MDM.

**Never write a time statement unless the minutes are true.** Pick MDM, and leave time out of the note.

## Which visits MDM applies to

| Visit | MDM works? |
|---|---|
| Admission / initial visit (99221, 99222, 99223) | Yes |
| Daily follow-up visit (99231, 99232, 99233) | Yes |
| Same-day admit and discharge (99234, 99235, 99236) | Yes |
| Discharge day (99238, 99239) | **No, time only** (30 min or less, or more than 30) |
| Critical care (99291, 99292) | **No, time only** (30 min minimum) |
| Advance care planning (99497) | **No, time only** (16 min minimum) |
| Prolonged services | **No, time only** |

## The scoring rule: 3 boxes, you need 2

MDM has three boxes. Score each one, then take the **second highest**. In other words, any 2 boxes at the same level earn that level.

| Box | Plain question |
|---|---|
| **1. Problem** | How serious is the most serious problem I dealt with today? |
| **2. Data** | What did I look at, read, or talk about to make my decisions? |
| **3. Risk** | How risky is what I decided to do (or not do)? |

| Level | Admission code | Follow-up code |
|---|---|---|
| Low | 99221 | 99231 |
| Moderate | 99222 | 99232 |
| High | 99223 | 99233 |

### Box 1: Problem

| Level | Plain meaning | Examples |
|---|---|---|
| **High** | Could kill the patient or cost them an organ without treatment, **or** a chronic disease in a severe flare | Sepsis, respiratory failure, decompensated HF on IV diuretics, GI bleed, DKA, NSTEMI, severe hyponatremia |
| **Moderate** | A chronic disease that's getting worse or causing side effects; **or** 2 or more stable chronic diseases you actually managed; **or** a new problem without a diagnosis yet; **or** an acute illness with whole-body symptoms (fever, tachycardia) | Uncontrolled diabetes, CKD progressing, syncope workup, pneumonia with fever |
| **Low** | One stable or simple problem that still needs hospital care | Cellulitis improving on antibiotics, awaiting placement |

Nuances:
- **The problem has to be addressed, not just listed.** Writing "#HTN" doesn't count. "#HTN, BP 170s, increased amlodipine to 10 mg" does.
- **Say why it's serious.** "Acute hypoxic respiratory failure, SpO2 86% on room air" proves High. "SOB" proves nothing.
- **The level follows the patient's condition.** On the day sepsis is improving, it may still be High. Once they're stable and waiting on placement, it drops.

### Box 2: Data

Data has three categories:

| Category | What counts | How to write it |
|---|---|---|
| **A. Tests, records, historian** | Each **unique test** ordered or reviewed (CBC = 1, BMP = 1, Mg = 1, chest X-ray = 1). Each **outside record source** reviewed (Care Everywhere, outside hospital). An **independent historian** (family, caregiver, EMS) because the patient can't give a reliable history. | "Reviewed CBC, BMP, Mg." "Reviewed outside records from ***." "History from daughter; patient confused." |
| **B. Your own read** | You personally look at the image, ECG, or rhythm strip and interpret it (and don't bill separately for reading it) | "My read of the CXR: new RLL consolidation." "My ECG read: sinus tach, no ST changes." |
| **C. Talking with another doctor** | A two-way discussion about management with a doctor of a different specialty or outside your group (phone, in person, or back-and-forth Secure Chat) | "Discussed with Dr. *** (cardiology): no inpatient ischemic workup." |

| Level | What you need |
|---|---|
| **High** | 2 of the 3 categories (for example 3 tests **and** your own CXR read) |
| **Moderate** | 1 of the 3 categories (for example 3 unique tests reviewed, **or** one own read, **or** one discussion) |
| **Low** | 2 tests, or an independent historian |

Nuances:
- **Count each test once.** Three lactates = 1 test. Ordering a test and reviewing its result = 1, not 2.
- **Only today counts.** A test you counted yesterday doesn't count again today.
- **"CXR reviewed" is not your own read.** You need to write what *you* see.
- **Reading a consultant's note is not a discussion.** It has to be a real exchange.
- **Counting UCI notes from other specialties as "outside records" is a gray area.** Outside hospital records and Care Everywhere clearly count. Ask UCI coding about the rest.

### Box 3: Risk

| Level | Plain meaning | Examples |
|---|---|---|
| **High** | **Deciding whether to hospitalize or escalate care** (admit, ICU transfer, or deciding against it) | "Decision regarding hospitalization: requires IV antibiotics and monitoring"; "Decision to transfer to ICU for pressors" |
| **High** | **Deciding on DNR or comfort care** because of poor prognosis | Goals of care with change to DNR or hospice |
| **High** | **IV or IM controlled substance** | IV hydromorphone, IV lorazepam, phenobarbital |
| **High** | **A drug that needs lab checks for toxicity** (checking for harm, not for whether it's working) | Vancomycin levels and daily Cr; aminoglycoside levels |
| **Moderate** | **Prescription drug management**: you start, stop, or change a prescription drug, or decide to continue one with a reason | "Increased furosemide to 80 mg IV BID for persistent edema" |
| **Moderate** | **Care limited by social factors** (housing, insurance, transport, food) | "Unable to discharge on apixaban due to cost; switched to warfarin" |
| **Low** | Over-the-counter meds, minor decisions | |

Nuances:
- **Insulin does not count as toxicity monitoring.** Glucose checks are mainly to see if it's working. Most hospitalist risk comes from escalation decisions, IV opioids or benzodiazepines, and vancomycin.
- **Gray zones to ask UCI coding about:** heparin drips with anti-Xa checks, and IV diuretics with daily BMPs for kidney and electrolyte toxicity. Auditors disagree.
- **"Continue home meds" alone is weak.** One clause of reasoning turns it into drug management: "Continue metoprolol; HR 70s, no hypotension."
- **The social factors item counts at Moderate**, and it is also data for your social determinants of health research interest.

## How it plays out: 3 examples

**1. Decompensated HF, hospital day 2 → 99233 (High)**
- Problem: severe flare of chronic HF → **High**
- Data: BMP, Mg, CBC reviewed (category A) + discussed with cardiology (category C) → 2 categories → **High**
- Risk: changed diuretic dose → Moderate
- Two boxes at High → **High**

**2. Cellulitis, hospital day 4, improving → 99232 (Moderate)**
- Problem: cellulitis improving, plus diabetes and HTN both adjusted → 2 chronic problems managed → **Moderate**
- Data: CBC and BMP → Low
- Risk: switched IV cefazolin to PO cephalexin → **Moderate**
- Two boxes at Moderate → **Moderate**

**3. Alcohol withdrawal admission → 99223 (High), even with little data**
- Problem: severe withdrawal (risk of seizures and DTs) → **High**
- Data: BMP only → Low
- Risk: IV phenobarbital → **High**
- Two boxes at High → **High**

## Nuances that protect you

1. **Document what you did, not what the template says.** Imported labs and copy-forward don't earn data points. Your written decisions do.
2. **Don't bill High every day on every patient.** Real hospital stays start High and step down as patients improve. Billing 99233 for everyone every day is an audit flag.
3. **The level must fit the patient.** A long note on a stable patient is still a low-level visit.
4. **Teaching notes:** with residents, MDM can rest on the resident's documentation plus UCI's approved attestation showing your participation. Use the department attestation.
5. **APP split/shared visits:** whoever does the substantive part of the MDM can bill it. Use UCI's approved split/shared attestation.
6. **When in doubt, code down.** Undercoding loses a little money; overcoding creates risk.

## The phrase: `.JMCMDM`

Paste at the bottom of the A/P. Keep only the lines that are true today and delete the rest. The bracketed tags are there for you; you can delete them before signing.

```
MEDICAL DECISION MAKING
Problem: {[HIGH] *** is a threat to life or organ function without treatment/[HIGH] *** is a severe flare of chronic ***/[MOD] *** chronic illness worsening or with treatment side effect/[MOD] 2+ chronic illnesses managed today: ***/[MOD] new undiagnosed problem with uncertain prognosis: ***/[MOD] acute illness with systemic symptoms: ***/[LOW] stable or uncomplicated illness requiring hospital care: ***}
Data:
- Tests reviewed or ordered today: ***
- Outside records reviewed: ***
- History from *** because patient ***
- My own interpretation of ***: ***
- Discussed management with Dr. *** (***): ***
Risk: {[HIGH] Decision regarding hospitalization: ***/[HIGH] Decision regarding escalation of care: ***/[HIGH] Decision regarding DNR or de-escalation due to poor prognosis: ***/[HIGH] Parenteral controlled substance: ***/[HIGH] Drug therapy requiring intensive monitoring for toxicity: *** (monitoring ***)/[MOD] Prescription drug management: ***/[MOD] Diagnosis or treatment significantly limited by social determinants of health: ***}
```

**How to use it in 20 seconds:**
1. Problem: pick the most serious one and fill in the blank.
2. Data: fill only the lines that are true; delete the rest.
3. Risk: pick the highest that's true today.
4. Check: 2 boxes at the same level? That's your code.

## Practice

For 2 weeks, add `.JMCMDM` to every note and write down the level you think it earns (just a code and date, no patient information). If UCI coding gives feedback reports, compare. Most people get reliable within 30 to 40 notes.

## Source
AMA CPT Evaluation and Management (E/M) Services Guidelines, 2023 and later (hospital inpatient and observation care), including the MDM table and definitions. Billing rules change yearly; confirm with UCI coding and compliance.
