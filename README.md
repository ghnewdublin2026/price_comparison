# Price Comparison

Below is a **complete, end-to-end project blueprint** you could hand to:

# 1️⃣ Full Project File & Folder Structure

This is a **minimum viable, regulator-ready layout**.

```
supermarket-price-comparison/
│
├── README.md
├── config/
│   ├── system.yaml
│   ├── models.yaml
│   └── thresholds.yaml
│
├── prompts/
│   ├── v1.0-mvp/
│   │   ├── 00_global_rules.md
│   │   ├── 01_requirements.md
│   │   ├── 02_data_sources.md
│   │   ├── 03_architecture.md
│   │   ├── 04_schema.md
│   │   ├── 05_implementation.md
│   │   ├── 06_validation.md
│   │   └── 07_release_review.md
│   └── CHANGELOG.md
│
├── orchestrator/
│   ├── orchestrator.py
│   ├── stage_runner.py
│   ├── approval_gate.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── validated/
│   └── rejected/
│
├── ingestion/
│   ├── sources/
│   │   ├── tesco.py
│   │   ├── aldi.py
│   │   └── lidl.py
│   ├── fetch.py
│   └── normalize.py
│
├── backend/
│   ├── api/
│   │   ├── prices.py
│   │   ├── products.py
│   │   └── stores.py
│   ├── models.py
│   ├── services/
│   │   └── comparison.py
│   └── main.py
│
├── validation/
│   ├── sanity_checks.py
│   ├── outliers.py
│   ├── confidence.py
│   └── reports.py
│
├── frontend/
│   ├── pages/
│   ├── components/
│   └── ui_copy.md
│
├── logs/
│   ├── ai_runs.jsonl
│   ├── ingestion.log
│   ├── validation.log
│   └── release.log
│
├── governance/
│   ├── data_sources_registry.md
│   ├── risk_register.md
│   ├── audit_trail.md
│   └── incident_response.md
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_validation.py
│   └── test_comparison.py
│
└── releases/
    ├── v1.0/
    │   ├── release_notes.md
    │   └── approval_record.md
    └── v1.1/
```

---

# 2️⃣ What Each Major Area Is Responsible For

### 🔐 `config/`

**Immutable system controls**

* AI behavior
* Thresholds
* Risk tolerances

Regulators will read this.

---

### 🧠 `prompts/`

**Versioned AI behavior**

* Treated as *code*
* Never edited without review
* Fully auditable

---

### ⚙️ `orchestrator/`

**The brain**

* Executes stages
* Enforces order
* Requires human approval
* Writes logs

---

### 📦 `ingestion/`

**Data acquisition**

* No inference
* Source-specific logic
* Fully logged

---

### 🧪 `validation/`

**Trust layer**

* Sanity checks
* Outlier detection
* Confidence scoring

---

### 🏛 `governance/`

**Regulator survival kit**

* Proof of diligence
* Decision records
* Incident playbooks

---

# 3️⃣ Stage-by-Stage Execution Steps

This is the **actual operating procedure**.

---

## 🟢 Stage 0 — Global Rules (Once)

**Files**

* `config/system.yaml`
* `prompts/00_global_rules.md`

**Steps**

1. Define non-negotiable rules:

   * No inferred prices
   * Provenance required
2. Hash & lock file
3. Require legal/compliance sign-off

✅ **AI role:** None
✅ **Human role:** Full ownership

---

## 🟢 Stage 1 — Requirements (Product Owner)

**Files**

* `prompts/01_requirements.md`
* Output → `governance/requirements.md`

**Steps**

1. Run Requirements prompt
2. Generate:

   * User stories
   * Acceptance criteria
   * Non-goals
3. Human PO reviews
4. Freeze scope for sprint

❌ No code allowed
❌ No data assumptions allowed

---

## 🟢 Stage 2 — Data Sources & Legal Risk

**Files**

* `prompts/02_data_sources.md`
* Output → `governance/data_sources_registry.md`

**Steps**

1. AI proposes sources
2. Classifies legal risk
3. Flags ToS issues
4. Human approves or rejects each source
5. Registry updated + signed

🚨 If no legal source → feature blocked

---

## 🟢 Stage 3 — Architecture & Schema

**Files**

* `prompts/03_architecture.md`
* `prompts/04_schema.md`
* Output → `backend/models.py`

**Steps**

1. Generate architecture
2. Generate schema
3. Human dev reviews
4. Lock schema version

🔒 Schema changes require migration + review

---

## 🟢 Stage 4 — Implementation

**Files**

* `prompts/05_implementation.md`
* `backend/`
* `ingestion/`

**Steps**

1. AI writes code per approved schema
2. No new data sources allowed
3. Human reviews PR
4. Tests must pass

❌ No business logic changes
❌ No silent refactors

---

## 🟢 Stage 5 — Validation & QA

**Files**

* `prompts/06_validation.md`
* `validation/`
* `logs/validation.log`

**Steps**

1. Run sanity checks
2. Run outlier detection
3. Assign confidence scores
4. Generate validation report

⚠️ Any failed hard rule blocks release

---

## 🟢 Stage 6 — Release Review

**Files**

* `prompts/07_release_review.md`
* `releases/vX.Y/approval_record.md`

**Steps**

1. AI summarizes risks
2. AI lists unresolved issues
3. Human signs release
4. Archive logs

🚨 AI can recommend — never approve

---

# 4️⃣ Daily / Ongoing Operations (Post-Launch)

### 🕒 Nightly price updates

* Ingestion → Validation → Logging
* No AI autonomy changes

### 🚨 Incident response

* Trigger `governance/incident_response.md`
* Freeze comparisons
* Notify users if needed

---

# 5️⃣ What This Gives You (Practically)

✅ Trustworthy prices
✅ Explainable comparisons
✅ Regulator-defensible AI usage
✅ Scalable supermarket onboarding
✅ Clear accountability

---

# 6️⃣ One Sentence That Matters

> **This project structure ensures that AI can move fast —
> but never move silently.**


