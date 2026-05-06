## CLAUDE.md — CAD Execution Standard (FreeCAD 1.1)

---

# Core Objective

Operate as a deterministic FreeCAD operator that:

1. Generates a correct parametric design plan
2. Executes that plan using MCP tools
3. Produces a stable, printable model

---

# Workflow (MANDATORY)

1. Intent
2. Plan
3. Execution
4. Validation

Execution is **FORBIDDEN** until plan is complete.

---

# Intent Resolution (STRICT)

During Plan phase:

1. If user provides intent → use it
2. ELSE IF `intent.md` exists → use it (MANDATORY)
3. ELSE → ask for clarification

If `intent.md` exists:

* DO NOT ask questions
* DO NOT delay
* Proceed immediately to plan generation

---

# Intent Override Rule (MANDATORY)

If `intent.md` exists:

* It is the complete and sufficient source of intent
* The agent MUST NOT request clarification
* The agent MUST generate the plan immediately

This overrides all default behaviors requiring clarification.

---

# Planning Memory Reset

During Plan phase:

* Ignore previous implementations
* Ignore macros
* Ignore prior parametric systems

Plan must be generated fresh from:

* intent.md
* CAD_STANDARDS.md
* user prompt (if provided)

---

# Plan Phase Rules

## Allowed Inputs

* intent.md
* CAD_STANDARDS.md
* user prompt

## Forbidden

* MCP tools
* execute_python
* Bash / shell
* filesystem exploration beyond allowed files

---

# Plan Output Contract (STRICT)

Return ONLY the following:

PARAMETERS:

* list of all driving parameters

FEATURE TREE:

1. ordered modeling steps

DEPENDENCIES:

* parameter relationships
* feature dependencies
* NO face-based references

VALIDATION:

* how model correctness will be verified

---

## Plan Requirements

* Fully parametric design
* Single source of truth for dimensions
* No redundant constraints
* No dependency on generated faces
* Must support variation without breaking

If plan cannot meet these:
→ return error

---

# Execution Rules

* Follow plan exactly
* NO improvisation
* NO adding features not in plan

If something is missing:
→ STOP and return error

---

# Tool Usage

* ALWAYS use MCP tools
* execute_python is LAST RESORT ONLY

Forbidden for Python:

* object creation
* sketches
* constraints
* parameter systems
* document structure

---

# Type Safety (MANDATORY)

ALWAYS validate object.TypeId

Required:

* VarSet → App::VarSet
* Sketch → Sketcher::SketchObject
* Body → PartDesign::Body

If mismatch:
→ DO NOT reuse
→ create correct object

---

# Parameter Rules

Valid containers:

* App::VarSet
* Spreadsheet::Sheet

NEVER:

* use generic DocumentObject as parameter store

All geometry must be driven by parameters

---

# Constraint Rules

Each sketch must include:

* 1 anchor constraint
* 1 driving dimension
* 1 orientation constraint

Prefer:

* Equal constraints
* External geometry

---

# Persistence Rules

After any modification:

1. doc.recompute()
2. doc.save()

---

# Validation (MANDATORY)

Before success:

* Objects exist
* Types correct
* Parameters valid
* Constraints applied
* Model recomputes
* No geometry errors

Failure:
→ return error

---

# Failure Behavior

If ANY occur:

* Type mismatch
* Invalid parameter system
* Missing plan step
* Tool misuse

THEN:

* STOP immediately
* return error
* DO NOT recover

---

# Human Approval Required For

* Saving to disk
* Deleting objects
* Overwriting main document

---

# Core Principle

Correct model state > task completion

If uncertain → STOP, not guess

