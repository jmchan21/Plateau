# Plateau Vent Trainer

Mechanical ventilation training for ICU clinicians: ventilator simulator, bedside cases, board-style questions, and spaced review, cited to current guidelines with PMIDs.

**Use it:** https://jmchan21.github.io/plateau/ (on iPhone: open in Safari, tap Share, then Add to Home Screen)

## Layout
- `src/index.html`: the app (same file published as the claude.ai artifact).
- `tools/build.py`: builds the installable home-screen version into `docs/` (served by GitHub Pages).
- `tools/icon.svg`: app icon source.

To update: edit `src/index.html`, bump `CONTENT_VERSION` and `REVIEWED`, run `python3 tools/build.py`, commit, push.

For education only. Not medical advice.

## Shift Prep (separate tool)
`shift-prep/`: per diem hospitalist and intensivist workflow for Epic. `PLAYBOOK.md` covers the 5-minute chart review, quality measure checklist, and billing/RVU cheat sheet. `SMARTPHRASES.md` has copy-paste note templates.
