# Week 6: Testing & CI/CD

**Goal:** Automate quality gates with tests and GitHub Actions.

**Time:** ~12 hours

## Objectives

- Build a test pyramid: code → data → model
- Add pre-commit hooks for formatting
- Run CI on every pull request
- Define merge quality gates

## Readings

- [pytest](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Labs

### Lab 1: Test suites (3h)

```
tests/
  code/     # unit tests
  data/     # schema & distribution tests
  model/    # behavioral & performance floors
```

### Lab 2: Pre-commit (1h)

Add black, isort, and flake8 hooks.

### Lab 3: GitHub Actions CI (4h)

Create `.github/workflows/ci.yaml` that runs code and data tests on every PR.

### Lab 4: Quality gates doc (2h)

Write `docs/quality-gates.md`: what must pass before merge and deploy.

## Deliverable

- [ ] All test suites green locally
- [ ] CI passing on your repo
- [ ] Quality gates documented

## Next

[Week 7: Orchestration](week-07-orchestration.md)
