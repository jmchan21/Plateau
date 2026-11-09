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

### `.JCRECON`: Messy chart reconstruction (Sticky Note, not in the chart)
```
WHY HERE: ***
DONE (dates): ***
WORKING / NOT: ***
WAITING FOR: ***
RISK NEXT 24H: ***
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

## Assessment and plan blocks (format from `AP-STYLE.md`)

Each block: specific diagnosis plus trajectory, evidence as trends, reasoning only if needed, verb-first plan, endpoint. Delete lines that don't apply.

### `.JCSEPSIS`
```
#Sepsis {without organ dysfunction/with *** (acute organ dysfunction)/septic shock} due to *** (organism ***), {improving/worsening/unchanged}
Tmax *** ; lactate *** to *** ; WBC *** to *** ; cultures: ***
- Antibiotics: *** (day *** of ***, stop ***); narrow to *** per cultures
- Source control: ***
- Pressors: {none/norepinephrine *** mcg/min, MAP goal 65}
- Endpoint: afebrile 48 h, hemodynamically stable, PO transition to ***
SEP-1 (day 1): lactate ***, BCx before abx at ***, abx at ***, fluids *** mL/kg {/less due to ***}, reassessment at ***
```

### `.JCAHRF`
```
#Acute {hypoxic/hypercapnic/hypoxic and hypercapnic} respiratory failure due to ***, {improving/worsening/unchanged}
{SpO2 *** on ***/P:F ***/pH *** PaCO2 ***}; RR ***; work of breathing ***
- ***
- Wean O2 to SpO2 {92 to 96%/88 to 92% (hypercapnia)}
- Endpoint: room air or home O2 *** L at rest and ambulation
```

### `.JCHF`
```
#Acute on chronic {HFrEF (EF ***%)/HFpEF (EF ***%)/HFmrEF}, NYHA ***, {improving/worsening/unchanged}
Weight *** to *** kg (dry ~***), net ***; JVP ***; edema ***. Trigger: ***
- {Furosemide/bumetanide} *** IV ***, goal net -*** L/day; BMP/Mg daily
- GDMT: BB ***; ARNI/ACEi/ARB ***; MRA ***; SGLT2i ***
- Endpoint: euvolemic on PO diuretic x24 h; HF follow-up within 7 days
```

### `.JCAKI`
```
#AKI, KDIGO stage ***, {prerenal/ATN/obstructive/***} from ***, {improving/worsening/unchanged}
Cr baseline *** to peak *** to today ***; UOP *** mL/kg/h; {FENa/FEUrea} ***
- ***
- Hold ***; renally dose meds (reviewed); avoid NSAIDs and contrast
- Endpoint: Cr at or near baseline; resume *** then
```

### `.JCTROP`
```
#{Type 1 NSTEMI/Type 2 MI due to ***/Non-ischemic myocardial injury, {acute/chronic}}, {improving/resolved}
hs-troponin *** to *** to *** ng/L; ECG (my read): ***; TTE: ***
{Favor *** over *** given ***.}
- ***
```

### `.JCENCEPH`
```
#Acute {metabolic/toxic/toxic-metabolic} encephalopathy due to ***, {improving/worsening/unchanged}
CAM {+/-}; baseline per *** is ***
- Treat cause: ***; stop or avoid ***
- Delirium bundle: sleep, glasses/hearing aids, mobilize, family at bedside
- Endpoint: back to baseline per ***
```

### `.JCNA`
```
#Hyponatremia, {hypovolemic/euvolemic (SIADH from ***)/hypervolemic}, {acute/chronic}, {improving/worsening}
Na *** to *** ; Sosm *** ; Uosm *** ; UNa ***
- ***
- Correction limit 8 mEq/L per 24 h; Na q*** h; DDAVP clamp if overcorrecting
- Endpoint: Na above *** and stable on discharge regimen
```

### `.JCAWS`
```
#Alcohol withdrawal, {mild/moderate/severe}, last drink ***, {seizure/DT history/no complicated history}, {improving/worsening}
CIWA max *** ; ***
- {Phenobarbital/symptom-triggered lorazepam} ***
- Thiamine *** before glucose; Mg/Phos repletion
- Addiction medicine {consulted/declined}; discuss naltrexone or acamprosate at discharge
```

### `.JCGIB`
```
#{Upper/Lower} GI bleed {from ***/source unknown}, {improving/worsening/unchanged}
Hgb *** to *** ; Glasgow-Blatchford *** ; hemodynamics ***
- Transfuse for Hgb below {7/8 (ACS)}; type and screen active
- {Pantoprazole 40 mg IV BID/***}; GI: ***
- Antithrombotics: hold ***, plan to resume ***
- Endpoint: Hgb stable x24 h, tolerating diet
```

### `.JCCHRONIC`
```
Chronic, stable: ***
```

### `.JCDCCOURSE`: discharge summary, one paragraph per problem
```
**{Principal diagnosis}:** Admitted with ***. Treated with ***. Course notable for ***. At discharge: ***. **Follow-up needs to:** ***.
```

---

## Attestation add-in lines (paste inside the department attestation)

You already use the department attestations for residents, APPs, and procedures. These lines make them specific, since "seen and agree" alone does not support the billed level.

### `.JCATTKEY`: What you personally did
```
My key findings: ***. I personally reviewed {CXR/CT/ECG} images: ***. My assessment differs from or adds to the resident's as follows: ***. Today's key decisions: ***.
```

### `.JCATTCCTIME`: Critical care time (residents present)
```
My personal critical care time: *** minutes, excluding teaching time, resident time without my presence, and separately billable procedures. Critical illness: ***. My interventions: ***.
```

### `.JCSPLIT`: Split/shared with APP
```
I performed the substantive portion of this visit by {spending more than half of total time (*** of *** min)/making the medical decision-making: ***}.
```

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

### `.SCDISPO`: Case management, morning
```
Good morning, I'm covering *** today. Likely discharge candidates: ***. Potential barriers: ***. Anything you need from me early?
```

### `.SCPRIOR`: Prior attending, quick clarification
```
Hi, I'm covering *** today. Quick question so I don't miss anything: what's your main concern and what's the endpoint for ***? Thanks!
```

### `.SCNOTHING`: Reviewed, no change
```
Thanks for letting me know. Reviewed: ***. No change in plan tonight. Please call if ***.
```

### `.SCPAGEFORMAT`: For charge nurse (helps pages arrive with what you need)
```
Hi, to help me respond faster overnight, pages are most useful with: patient name and room, current vitals, the concern, and what you need (order, bedside eval, FYI). Thank you!
```
