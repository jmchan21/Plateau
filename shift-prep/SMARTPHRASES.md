# Epic SmartPhrase Library (copy and paste into each site's SmartPhrase Manager)

How to load: Epic menu > SmartPhrase Manager > New. Name it (for example `.JCPROG`), paste the text, then replace each `@TOKEN@` with that site's SmartLink. Type `@` in the editor to search; common names are listed beside each token. `***` is a wildcard (F2 jumps to the next one). `{choice/choice}` should become a SmartList (or just delete the options you don't use).

SmartLink names differ between organizations. The ones below are common but not universal.

---

## 1. Progress note: `.JCPROG`

```
HOSPITAL MEDICINE PROGRESS NOTE
@NAME@ | @AGE@ @SEX@ | Hospital day @LOS@ | Code status: @CODESTATUS@

ONE-LINER: ***

HOSPITAL COURSE TO DATE (update daily, 3 to 5 lines; the next doctor reads this first):
***

INTERVAL / OVERNIGHT EVENTS:
***

SUBJECTIVE:
***

OBJECTIVE:
Vitals (24h): @VS24@          [or @VITALS@ / @FLOWSHEET@]
I/O: @IO24@                    [or @IOBRIEF@]
Exam: ***
Labs: @LABRCNT@                [or @CBC@ @BMP@ @LASTLABS@]
Micro: @MICRO@
Imaging: ***  (I personally reviewed the images: ***)
ECG: ***  (my independent interpretation: ***)
Lines/drains/airways: @LDA@
Active meds: @ACTMED@          [or @MEDS@ / @CMED@]

ASSESSMENT AND PLAN:
#1 ***  (be specific: acuity, type, severity, cause)
  - ***
#2 ***
  - ***

DISCUSSED WITH: *** (consultant name and recommendation)
DATA REVIEWED: *** (external notes, outside records, independent historian)

DAILY QUALITY CHECK:
VTE prophylaxis: {enoxaparin/heparin SQ/on therapeutic anticoagulation/SCDs, contraindication: ***}
Foley: {none/present, indication: ***/removed today}
Central line: {none/present, indication: ***/removed today}
Antibiotics: {none/*** day # of ***, planned stop date ***}
Glucose: {not diabetic/at goal/adjusted insulin ***}
Diet: ***   Mobility / PT-OT: ***
Code status: @CODESTATUS@ (confirmed with {patient/surrogate} on ***)
Expected discharge date: ***   Barriers: ***   Dispo: {home/home health/SNF/IRF/LTACH/hospice}

Time: I spent *** minutes on the date of service in the care of this patient, including chart review, examination, documentation, and coordination with the care team.
```

## 2. Admission H&P: `.JCHP`

```
HOSPITAL MEDICINE ADMISSION H&P
@NAME@ | @AGE@ @SEX@ | PCP: @PCP@ | Source: {ED/transfer from ***/direct}
Code status: *** (discussed with ***)

CHIEF COMPLAINT: ***
HPI: ***
Independent historian: {none/*** because ***}
External records reviewed: ***

PMH: @PMH@   PSH: @PSH@
Meds (home): @HOMEMED@   Allergies: @ALLERGY@
Social: @SOCHX@   (SDOH: housing ***, food ***, transport ***, insurance ***)
Family: @FAMHX@
ROS: ***

Vitals: @VS@   Exam: ***
Labs: @LABRCNT@   Imaging: ***  (images personally reviewed: ***)   ECG: ***  (my read: ***)

ASSESSMENT: ***-year-old with *** presenting with ***, admitted for ***.

PLAN:
#1 *** 
#2 ***

SEPSIS (if applicable): lactate ***, cultures drawn *** before antibiotics given ***, fluids *** mL/kg (or reason for less: ***), repeat lactate ***, reassessment at *** (time).
VTE prophylaxis: ***   Med rec: completed   Diet: ***   Lines/Foley: ***
Expected LOS / discharge date: ***   Anticipated dispo: ***
Status: {inpatient, expected to require 2 or more midnights because ***/observation}

Time: *** minutes on the date of service.
```

## 3. Cross-cover / event note (nights): `.JCXC`

```
CROSS-COVER EVENT NOTE
Called by *** at *** for ***.
Background (from chart and handoff): ***
Assessment at bedside: vitals @VS@, exam ***
Data reviewed: ***
Impression: ***
Actions: ***
Contingency: if ***, then ***.
Discussed with: ***   Primary team to follow up: ***
Time: *** minutes.  {Not critical care/Critical care time below}
```

## 4. Critical care attestation: `.JCCC`

```
CRITICAL CARE
The patient is critically ill with *** (organ failure), with a high probability of imminent or life-threatening deterioration.
Critical care interventions: *** (for example titration of vasopressors, ventilator management, interpretation of ABG and hemodynamics, discussion with family regarding goals).
Total critical care time: *** minutes, exclusive of separately billable procedures and teaching time.
```

## 5. Advance care planning: `.JCACP`

```
ADVANCE CARE PLANNING
Participants: ***  (patient {has/lacks} capacity)
Discussed: diagnosis and prognosis, values and goals, code status, ***
Outcome: code status ***; POLST {completed/not completed}; surrogate ***
Time spent in advance care planning, face to face, voluntary: *** minutes (separate from other E/M time).
```

## 6. Discharge summary: `.JCDC`

```
DISCHARGE SUMMARY
Admit: @ADMITDATE@   Discharge: @TODAY@   LOS: @LOS@
Principal diagnosis: ***   Secondary diagnoses (specific): ***
Hospital course by problem: ***
Procedures: ***
Medication changes: STARTED *** | STOPPED *** | CHANGED ***
(No opioid plus benzodiazepine co-prescription; or reason: ***)
Pending results at discharge and who will follow up: ***
Follow-up: PCP *** within 7 days; specialist ***
Condition: ***   Dispo: ***   Code status: ***
Time: {30 minutes or less/*** minutes, more than 30}
```

## 7. Private triage sticky note (not part of the chart): `.JCSTICKY`

```
Bucket: {SICK/GOING HOME/STABLE}
To do: ***
Pending: ***
Call back: ***
```
