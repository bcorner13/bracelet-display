#!/usr/bin/env python3
"""
Parametric system audit for bracelet display.
Validates all constraints and parameter bindings.
"""

import FreeCAD
import sys
import os

def audit_parameters():
    """Audit parameter document and bindings."""
    results = []

    # Check if Params document exists
    params_doc = FreeCAD.getDocument("Params1")
    if not params_doc:
        results.append("ERROR: Params document not found")
        return results

    # Check VarSet exists
    varset = params_doc.getObject("VarSet")
    if not varset:
        results.append("ERROR: VarSet object not found in Params document")
        return results

    # Expected parameters
    expected_params = [
        "BaseWidth", "BaseDepth", "BaseHeight", "WallThickness",
        "DisplayHeight", "DisplayAngle", "ArmWidth", "BraceletRestDiameter",
        "BaseChamfer", "ArmChamfer", "RestChamfer"
    ]

    # Check each parameter exists
    for param in expected_params:
        if param not in varset.PropertiesList:
            results.append(f"ERROR: Missing parameter {param}")
        else:
            value = getattr(varset, param)
            results.append(f"OK: {param} = {value}")

    return results

def audit_constraints():
    """Audit constraint bindings in main document."""
    results = []

    # Check if BraceletDisplay document exists
    display_doc = FreeCAD.getDocument("BraceletDisplay")
    if not display_doc:
        results.append("ERROR: BraceletDisplay document not found")
        return results

    # Check parameter bindings
    constraint_checks = 0
    for obj in display_doc.Objects:
        if hasattr(obj, 'ExpressionEngine'):
            for expr in obj.ExpressionEngine:
                if '<<Params>>#VarSet.' in expr[1]:
                    results.append(f"OK: {obj.Label}.{expr[0]} = {expr[1]}")
                    constraint_checks += 1

    if constraint_checks == 0:
        results.append("WARNING: No parameter bindings found")

    return results

def main():
    """Run parametric audit."""
    print("=== Bracelet Display Parametric Audit ===\n")

    # Audit parameters
    print("Parameter Check:")
    param_results = audit_parameters()
    for result in param_results:
        print(f"  {result}")

    print("\nConstraint Check:")
    constraint_results = audit_constraints()
    for result in constraint_results:
        print(f"  {result}")

    # Count errors
    all_results = param_results + constraint_results
    errors = [r for r in all_results if r.startswith("ERROR")]
    warnings = [r for r in all_results if r.startswith("WARNING")]

    print(f"\n=== Audit Summary ===")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nFailed - Fix errors before proceeding")
        sys.exit(1)
    else:
        print("\nPassed - Parametric system is valid")

if __name__ == "__main__":
    main()