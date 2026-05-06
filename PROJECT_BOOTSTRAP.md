# Project Bootstrap Standard (MANDATORY)

This document defines how ALL new CAD projects must be created under:

~/Documents/3dPrinting/Commercial License

---

# Goal

Ensure every project is:

* structurally identical
* repeatable
* compatible with MCP + CLAUDE.md + CAD_STANDARDS.md

---

# Step 1 — Project Creation

When a new project is requested:

* Create directory:
  `<ProjectName>/`

Example:
HexVase/

---

# Step 2 — Required Folder Structure

Every project MUST contain:

<ProjectName>/
├── CLAUDE.md
├── intent.md
├── plan.md
├── CAD_STANDARDS.md (copied from root)
├── models/
├── logs/
├── cad_files/
├── stls/
├── renders/

If any folder/file is missing:
→ abort and fix before proceeding

---

# Step 3 — Required Files

## intent.md (HUMAN INPUT)

Defines the goal only.

Example:
Goal:
Parametric hex-pattern vase

Constraints:

* Must follow CAD_STANDARDS.md
* Printable without supports
* Target price $36–$45

---

## plan.md (AI GENERATED — REQUIRED BEFORE EXECUTION)

Must include:

PARAMETERS:

* Name
* Type
* Default value

FEATURE TREE:

* Ordered modeling steps

CONSTRAINT STRATEGY:

* How sketches will be constrained

VALIDATION:

* How model will be verified

Execution is FORBIDDEN until plan.md is complete and approved

---

## CLAUDE.md

* Copy project-specific CLAUDE.md template
* Must be present before any CAD operation

---

## CAD_STANDARDS.md

* Copy from root Commercial License folder
* Must not be modified

---

# Step 4 — Environment Validation

Before any modeling:

* Confirm MCP FreeCAD connection
* Confirm GUI mode
* Confirm working document:
  `<ProjectName>/temp_work`

If not valid:
→ abort

---

# Step 5 — Execution Flow

1. Read intent.md
2. Generate plan.md
3. WAIT for approval
4. Execute using CLAUDE.md rules
5. Validate against CAD_STANDARDS.md

---

# Step 6 — Save Policy

* NEVER save automatically
* Only save after human approval
* Save into:
  models/<ProjectName>_vX.Y.Z.FCStd

---

# Step 7 — Failure Behavior

If ANY of the following occur:

* Missing files
* Invalid structure
* Plan not approved
* MCP unavailable

THEN:
→ STOP immediately
→ return error

DO NOT proceed

---

# Core Principle

Projects are NOT created ad hoc.

They are instantiated from this standard and must remain compliant at all times.

