# Assessment and Plan Style Guide

Target: academic and specific, but short. A reader should know what you think, why, and what happens next in 15 seconds per problem.

## The two failure modes

**Too wordy** (copy-forward bloat):
> #Sepsis. Patient presented to the ED with fevers and was found to have elevated WBC and lactate and was started on broad spectrum antibiotics in the ED and blood cultures were drawn. Patient was admitted to medicine. Today patient is feeling better. Will continue antibiotics. Will follow cultures. Will continue to monitor. Appreciate ID recs. Will continue IV fluids as needed.

**Too sparse:**
> #Sepsis: abx, f/u cx

Neither tells the next doctor the source, the organism, the day, the response, or the endpoint.

**Target:**
> **#Sepsis with AKI due to E. coli pyelonephritis, improving**
> Afebrile 24 h, lactate 3.8 to 1.4, Cr 2.1 to 1.6. BCx 1/2 E. coli (pan-S except ampicillin).
> - Narrow cefepime to ceftriaxone 1 g daily (day 3 of 7, stop 11/14)
> - No repeat BCx needed (no persistent bacteremia risk factors)
> - Transition to PO cephalexin once tolerating diet 24 h

## The format (4 parts, 3 to 6 lines per active problem)

```
#[Specific diagnosis: acuity + type + severity + cause], [trajectory]
[Evidence: the 1 to 3 data points that support it, with trend arrows or "to"]
[Reasoning, only if not obvious: leading alternative and why less likely]
- [Verb + specific action + dose/target]
- [Endpoint: what defines done, or the stop date]
```

## Rules

1. **The problem title is the diagnosis, as specific as you'd want it coded.** Acuity (acute, acute on chronic), type (HFrEF, hypoxic), severity (KDIGO stage, septic shock), cause (due to ___). This one line also does the CDI work.
2. **One trajectory word:** improving, worsening, unchanged, resolved. Readers scan for it.
3. **Evidence is trends, not dumps.** "Cr 2.1 to 1.6" beats pasting the BMP. Raw data belongs in the objective section.
4. **Reasoning only when it adds something.** One line on the differential when the diagnosis is uncertain or the plan is non-obvious ("Favor type 2 MI given flat delta and sepsis; no ischemic ECG changes"). This is where "academic" lives, and it's what separates your note from a template.
5. **Plan bullets start with a verb and include the number.** "Furosemide 80 mg IV BID, goal net negative 1 to 2 L" not "continue diuresis."
6. **Every plan has an endpoint.** Antibiotic stop date, diuresis target weight, the Hgb that triggers a transfusion, the criteria for discharge.
7. **No filler phrases.** Delete: "will continue to monitor", "appreciate recs", "patient is a pleasant", "as needed" without a trigger, "will follow" without what you'll do with the result.
8. **Consultant recs as decisions, not deference.** "Per cardiology: no ischemic evaluation inpatient; outpatient stress test" (and name them in the MDM data line, `.JCMDM`).
9. **Chronic stable problems: one line each, grouped at the bottom.**
   > Chronic, stable: HTN (amlodipine held for soft BP), T2DM (A1c 7.9, basal-bolus, BG 120s to 180s), HLD (atorvastatin 40), GERD (pantoprazole).
10. **Resolved problems collapse to one line** under the hospital course, then get deleted after a day.
11. **Edit the copy-forward every day.** Read each line and ask "is this still true today?" If you didn't verify it, delete it.

## Worked examples

**Heart failure**
> **#Acute on chronic HFrEF (EF 25%), NYHA IV on admission, improving**
> Weight 92.1 to 88.4 kg (dry ~86), net -5.2 L, still 2+ edema, JVP 10 cm. Trigger: dietary sodium plus missed doses.
> - Furosemide 80 mg IV BID, goal net -1.5 L/day; BMP/Mg daily
> - GDMT: continue metoprolol succinate 50; start sacubitril/valsartan 24/26 once Cr stable 24 h; add empagliflozin 10 before discharge
> - Discharge when euvolemic on PO diuretic x24 h; HF clinic within 7 days

**Troponin elevation**
> **#Type 2 MI due to septic shock, resolved**
> hs-troponin 48 to 310 to 280 ng/L; ECG (my read) sinus tachycardia, no new ST changes; TTE no new wall motion abnormality.
> Favor supply-demand mismatch over type 1 given concurrent shock, no anginal symptoms, and plateau with recovery.
> - No inpatient ischemic evaluation (discussed with cardiology)
> - Continue atorvastatin 40; outpatient risk stratification with PCP

**AKI**
> **#AKI, KDIGO stage 2, prerenal from GI losses, improving**
> Cr 1.0 baseline to 2.3 peak to 1.7; FENa 0.4%; UOP 0.6 mL/kg/h.
> - LR 75 mL/h until tolerating PO; hold lisinopril and spironolactone
> - Renally dose antibiotics (reviewed); avoid NSAIDs and contrast
> - Resume ACEi when Cr at or near baseline

## Discharge summary hospital course (same rules)

One paragraph per problem: diagnosis, what happened, what was done, status at discharge, what follow-up needs to do. Lead with the principal diagnosis.

> **Acute on chronic HFrEF:** Admitted with 8 kg weight gain after missed diuretic doses. Diuresed 5.8 L with IV furosemide to a dry weight of 86.2 kg. Started sacubitril/valsartan and empagliflozin. Discharged on furosemide 40 mg PO daily. **PCP/HF clinic:** BMP in 1 week; uptitrate GDMT.

## Quick self-check before signing
- Could a stranger act on this A/P tonight without opening another note?
- Does every active problem have a trajectory word and an endpoint?
- Did I delete everything I didn't verify today?
