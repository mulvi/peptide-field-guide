# Peptide Field Guide

A free, single-page web app: an evidence-graded peptide library, a "what fits me" finder, and a reconstitution, dose and schedule calculator. Educational only, not medical advice.

## Files

- `index.html` is the live site (served by GitHub Pages).
- `src/app.html` is the same app without the page wrapper, used for previews.

To change the app, edit `src/app.html`, then rebuild `index.html` by wrapping it in the doctype, head and body tags found at the top and bottom of the current `index.html`.

## Waitlist

The Pro sign-up form posts to a Supabase table (`pro_waitlist`). The key in the page is a publishable key that can only add rows, never read them.
