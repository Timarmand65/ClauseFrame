# ClauseFrame
ClauseFrame: A Protocol for FAR 31.2 Compliance:  Most compliance tooling today is either interpretive or probabilistic - neither is enforceable/ trusted at audit time.  ClauseFrame changes that.  It’s the 1st  open-source, schema-driven logic engine for federal cost allowability under FAR 31.2 &amp; SF 1408— for audit readiness w/ clause citations.

# ClauseFrame v0.1

A self-validating audit logic engine for time-entry and cost validation in government compliance workflows.

## Contents

- `validator.py`: CLI tool for logic validation
- `validator_test.py`: Unit test suite
- `dcaa_audit_logic_engine_v0.1.yaml`: Core logic rules
- `test_set.yaml`: Sample inputs and expected outputs
- `assets/`: Flow diagram and badge graphics
- `.github/workflows/test-validator.yml`: GitHub Actions test runner

## Setup

Install Python 3.9+ and PyYAML.

```bash
pip install pyyaml
```

## Usage

Run the validator:

```bash
python3 validator.py "Employee claimed marketing cost"
```

