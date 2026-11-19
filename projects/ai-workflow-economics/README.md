# When does an AI workflow pay for itself?

**Stage:** Synthetic model complete. Field trial proposed.

Measure the cost of producing an accepted deliverable. Faster drafting could lower cost, while extra review, rework, and tooling could offset that gain. The relevant comparison is the full workflow for an equivalent output.

## Synthetic result

From the repository root, run `python3 projects/ai-workflow-economics/model.py`. The model uses only the Python standard library.

At $60 per labor hour, a 30-minute manual workflow costs $30. A 10-minute AI-assisted draft with a $2 tool charge reaches $30 after another 18 minutes of review and rework. Under these assumptions, 10 minutes of review and rework saves $8 per task and 25 minutes costs $7 more than the manual workflow. These scenarios assume equal output quality and equal hourly labor costs. They exclude fixed deployment costs, downstream error losses, and the question of whether time saved is redeployed.

## Proposed pilot

- Select one recurring task with de-identified or synthetic inputs and define a rubric covering accuracy, completeness, and material errors.
- Use 24 comparable tasks arranged into 12 pairs by anticipated difficulty. Randomly assign one task per pair to AI assistance and the other to the manual workflow. Balance execution order where feasible. Use independent reviewers blinded to assignment where feasible.
- Record drafting, review, rework, tool cost, and acceptance for every assigned task. Report cost per accepted output by arm as all assigned costs divided by accepted outputs. If there are zero accepted outputs in an arm, report that rate and leave its unit cost undefined. Also report first-pass acceptance and material-error rates.
- Stop after the pre-specified 24 tasks. Keep assigned failures in the record. Report missing timings, reasons, and sensitivity to plausible timing bounds. Treat this as a feasibility pilot and use its variability to design a larger trial.
- Expand the trial if the assisted workflow lowers cost per accepted output and meets the pre-specified quality requirements. Document the tool and version, assignment, scoring rubric, raw timing schema, and any protocol deviations before reporting results.

[Blog, social post, and policy memo drafts](drafts.md)
