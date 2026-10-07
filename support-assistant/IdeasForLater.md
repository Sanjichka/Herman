# Ideas for Later

## FAQ synthetic document layer

Write a small document with common user questions phrased in everyday language, paired with complete step-by-step answers. Ingest it as a separate source alongside the manual. No chunker changes needed — each Q&A pair becomes its own chunk and scores well because the question wording matches how real users ask.

Useful when you know a question is being asked but the manual never phrases it directly (e.g. "How do I link a VAT percentage to a product?").

## Merge small orphan chunks

The chunker splits on every heading, producing very small chunks (under ~200 tokens) that are too brief to stand alone as answers. Change the chunking strategy to merge a child section into its parent when the child falls below a minimum token threshold. This keeps related steps together and reduces the chance that the answer is split across chunks that never get retrieved together.

## Threshold and k tuning

After any chunking changes, re-run the VAT/declaration code question and check scores. The "adding price matrix records" chunk likely scores below threshold today partly because it never mentions VAT. A merged chunk (see above) may score higher. If not, consider lowering the threshold slightly (e.g. 0.35 → 0.30) and raising k (e.g. 5 → 8) to cast a wider net — then measure whether precision drops.
