# Week 2: Data Engineering & Quality

**Goal:** Treat data as a first-class product with validation and profiling.

**Time:** ~12 hours

## Objectives

- Profile a dataset for imbalance, nulls, and outliers
- Implement schema validation with Great Expectations
- Write data tests that run in CI
- Document a data contract

## Readings

- [Great Expectations — Getting started](https://docs.greatexpectations.io/docs/guides/setup/configuring_metadata_stores/)
- [Pandas profiling basics](https://pandas.pydata.org/docs/)

## Key concepts

Validation layers: **schema** → **distribution** → **content** → **pipeline parity**

## Labs

### Lab 1: Data profiling (3h)

Load your dataset. Report class balance, null rates, and feature statistics.

### Lab 2: Great Expectations suite (4h)

Define expectations for column types, allowed values, and null constraints. Save the suite to your repo.

### Lab 3: Data tests (3h)

Add pytest tests that fail when data violates your contract. Run locally before every training job.

### Lab 4: Data contract (2h)

Write `data/schema.yaml` documenting columns, types, and allowed values.

## Deliverable

- [ ] Profiling notes
- [ ] Great Expectations suite passing
- [ ] Data contract YAML

## Next

[Week 3: Modeling](week-03-modeling.md)
