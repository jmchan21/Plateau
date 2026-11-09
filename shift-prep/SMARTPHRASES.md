# Personal Dot Phrase Library (add-ons to UCI department templates)

These do not replace the department's note templates. Drop them into the A/P or the end of a note. Loading: Epic > SmartPhrase Manager > New > name it (`.JC...`) > paste. `***` is a wildcard (F2 jumps to the next one). `{a/b/c}` should become a SmartList, or delete the options you don't use. If an `@TOKEN@` doesn't resolve, type `@` in the editor and search for the UCI equivalent.

Before building, search SmartPhrase Manager for existing department versions (keywords: sepsis, attest, critical care, secure chat). Copy and personalize instead of starting from scratch.

---

## Note add-ons

### `.JCCOURSE`: Hospital course to date (top of A/P, update daily)
```
HOSPITAL COURSE TO DATE (HD @LOS@): *** y/o with *** admitted @ADMITDATE@ for ***. Key events: ***. Current status: ***. Remaining before discharge: ***.
```

### `.JCQC`: Daily quality check (bottom of A/P)
```
QUALITY / SAFETY:
VTE ppx: {enoxaparin/heparin SQ/therapeutic anticoagulation/SCDs, pharmacologic contraindicated due to ***}
Foley: {none/present, indication: ***/removed today}  Central line: {none/present, indication: ***/removed today}
Antibiotics: {none/*** day # *** of ***, stop date ***}
Glucose: {at goal/insulin adjusted ***/not diabetic}
Code status: @CODESTATUS@ (confirmed with {patient/surrogate ***})
EDD: ***  Barriers: ***  Dispo: {home/home health/SNF/IRF/LTACH/hospice}
```

### `.JCQCICU`: ICU additions
```
ICU BUNDLE: SAT {done/held because ***}, SBT {passed/failed/not eligible because ***}. RASS goal ***, actual ***. CAM-ICU {neg/pos}. Mobility: ***. Family updated: {yes, *** /not yet}. Lines/tubes reviewed for removal: ***.
```

### `.JCDATA`: MDM data and risk (supports the level you earned)
```
Independent interpretation: I personally reviewed {CXR/CT/ECG/telemetry} images: ***.
Discussed management with ***, who recommends ***.
External records reviewed: ***.  Independent historian: ***.
Risk: {drug therapy requiring intensive monitoring for toxicity: ***/decision regarding escalation of care/decision regarding de-escalation or DNR/parenteral controlled substances}.
```

### `.JCTIME`: Time statement
```
I spent *** minutes on the date of service in the care of this patient, including chart review, examination, documentation, and coordination with the care team, excluding separately billed procedures and teaching time.
```

---

## Assessment and plan blocks (common problems, quality items built in)

### `.JCSEPSIS`
```
#Sepsis {without/with acute organ dysfunction: ***/septic shock} due to *** (source: ***)
- Lactate *** -> *** (repeat at ***). Blood cultures x2 drawn *** prior to antibiotics.
- Antibiotics: *** started at *** (day ***), narrow per cultures; planned duration ***
- Fluids: *** mL/kg crystalloid {30 mL/kg given/less given due to *** (volume overload concern, documented)}
- Reassessment of volume status and perfusion completed at ***: ***
- Pressors: {none/norepinephrine *** for MAP goal 65}
```

### `.JCAHRF`
```
#Acute {hypoxic/hypercapnic/hypoxic and hypercapnic} respiratory failure due to ***
- Criteria: SpO2 *** on *** / RR *** / work of breathing *** / ABG ***
- Support: *** (goal SpO2 ***), wean as tolerated
- Treat cause: ***
```

### `.JCHF`
```
#Acute on chronic {systolic (HFrEF, EF ***%)/diastolic (HFpEF)/combined} heart failure, NYHA ***
- Trigger: ***
- Diuresis: *** with goal net negative *** L/day; daily weights, strict I/O, BMP/Mg daily
- GDMT: {beta blocker/ARNI or ACEi/ARB/MRA/SGLT2i} - continue/hold/start ***
- Discharge: weight ***, follow-up within 7 days, HF education
```

### `.JCAKI`
```
#AKI, KDIGO stage *** (Cr *** from baseline ***), likely {prerenal/ATN/obstructive/***}
- UOP ***, UA/urine lytes ***, bladder scan ***
- Avoid nephrotoxins; renally dose meds (reviewed); hold ***
```

### `.JCTROP`
```
#{Type 1 NSTEMI/Type 2 MI due to ***/Non-ischemic myocardial injury (acute/chronic)} (Fourth Universal Definition)
- hs-troponin *** -> *** ; ECG: my interpretation ***
- Plan: ***
```

### `.JCENCEPH`
```
#Acute {metabolic/toxic} encephalopathy due to ***
- Delirium precautions, sleep hygiene, avoid deliriogenic meds (reviewed: ***), CAM ***
```

### `.JCNA`
```
#Hyponatremia, {hypotonic hypovolemic/euvolemic (SIADH)/hypervolemic}, Na ***
- Serum osm ***, urine osm ***, urine Na ***
- Correction limit: no more than 8 mEq/L in 24 h; Na q*** h
```

### `.JCAWS`
```
#Alcohol withdrawal (last drink ***, history of {seizures/DTs/none}), CIWA ***
- Symptom-triggered ***, thiamine before glucose, folate, MVI, Mg/Phos repletion
- Counseling offered; addiction medicine consult {placed/declined}
```

### `.JCGIB`
```
#{Upper/Lower} GI bleed, Hgb *** -> *** , Glasgow-Blatchford ***
- 2 large-bore IVs, type and screen, transfuse for Hgb below 7 (8 if ACS)
- IV PPI ***, GI consulted ***, hold anticoagulation/antiplatelets ***
```

---

## Attestations (resident and APP shifts)

### `.JCATTHP`: Resident admission H&P
```
TEACHING PHYSICIAN ATTESTATION
I saw and evaluated the patient on @TODAY@, and discussed the case with Dr. *** (resident). I reviewed the resident's note and agree with the findings and plan as documented, with the following additions or changes: ***.
Key findings on my exam: ***.
My assessment: ***.
I personally reviewed: ***.
```

### `.JCATTPN`: Resident progress note
```
TEACHING PHYSICIAN ATTESTATION
I saw and examined the patient today and discussed with the resident. I agree with the resident's assessment and plan with the following changes: ***. Key decisions made today: ***.
```

### `.JCATTCC`: Critical care with residents
```
TEACHING PHYSICIAN CRITICAL CARE ATTESTATION
The patient is critically ill with *** with high probability of imminent or life-threatening deterioration. I personally evaluated the patient and directed care, including ***.
My personal critical care time: *** minutes, excluding teaching time, resident time without my presence, and separately billable procedures.
```

### `.JCSPLIT`: Split/shared visit with APP
```
SPLIT/SHARED VISIT
This was a split/shared visit with *** (APP). I performed the substantive portion of the visit by {spending more than half of the total time (*** of *** minutes)/making the medical decision-making: ***}.
```

---

## Night and ICU notes

### `.JCEVENT`: Cross-cover / event note
```
CROSS-COVER EVENT NOTE
Called by *** at *** for ***.
Background (chart and handoff): ***
Bedside assessment: vitals @VS@; exam ***
Data reviewed: ***
Impression: ***
Actions: ***
Contingency: if ***, then ***.
Primary team to follow up: ***
Time: *** minutes.
```

### `.JCCC`: Critical care (solo)
```
CRITICAL CARE
The patient is critically ill with *** (organ failure), with high probability of imminent or life-threatening deterioration.
Interventions: *** (for example vasopressor titration, ventilator management, ABG and hemodynamic interpretation, family discussion of goals).
Total critical care time: *** minutes, exclusive of separately billable procedures and teaching time.
```

### `.JCACP`: Advance care planning
```
ADVANCE CARE PLANNING
Participants: ***  (patient {has/lacks} capacity)
Discussed: diagnosis and prognosis, values and goals, code status, ***
Outcome: code status ***; POLST {completed/not completed}; surrogate ***
Time spent in advance care planning (voluntary, face to face, separate from other E/M time): *** minutes.
```

---

## Secure Chat phrases (nursing communication)

Short, closed-loop, and they set parameters so the same page doesn't come back. Secure Chat in Hyperspace accepts SmartPhrases; on Haiku/Rover, use your phone's text replacement for the short ones.

### `.SCACK`: Acknowledge
```
Got it, thanks. Coming to bedside in *** min. Please {get a full set of vitals/check a POC glucose/get an ECG} before I arrive.
```

### `.SCORDER`: Order placed
```
Thanks. Ordered ***. Please let me know if ***.
```

### `.SCPARAM`: Call parameters
```
Plan for tonight: ***. Please call me if SBP below *** or above ***, HR above ***, SpO2 below *** on ***, RR above ***, UOP below *** mL over *** h, new confusion, or you're worried.
```

### `.SCPRN`: PRN clarification
```
*** PRN ordered for ***. If not effective after ***, please page me before giving a second dose.
```

### `.SCFOLEY`: Foley removal
```
Foley no longer indicated. Please remove and bladder scan q6h; straight cath if PVR above *** mL. Let me know if the patient can't void by ***.
```

### `.SCGOALS`: Family update request
```
Family would like an update. I'm planning to call *** at ***. If they arrive before then, please page me and I'll come to the bedside.
```

### `.SCNOTHING`: Reviewed, no change
```
Thanks for letting me know. Reviewed: ***. No change in plan tonight. Please call if ***.
```

### `.SCPAGEFORMAT`: For charge nurse (helps pages arrive with what you need)
```
Hi, to help me respond faster overnight, pages are most useful with: patient name and room, current vitals, the concern, and what you need (order, bedside eval, FYI). Thank you!
```
