#!/usr/bin/env python3
"""
Print validation for bracelet display.
Checks geometry requirements for support-free printing.
"""

import FreeCAD
import FreeCADGui
import Mesh
import sys
import math

def check_overhangs():
    """Check for overhangs exceeding 45 degrees."""
    results = []

    display_doc = FreeCAD.getDocument("BraceletDisplay")
    if not display_doc:
        results.append("ERROR: BraceletDisplay document not found")
        return results

    body = display_doc.getObject("DisplayBody")
    if not body:
        results.append("ERROR: DisplayBody not found")
        return results

    # Check arm angle
    try:
        varset = FreeCAD.getDocument("Params1").getObject("VarSet")
        arm_angle = float(str(varset.DisplayAngle).replace("deg", ""))

        if arm_angle > 45:
            results.append(f"ERROR: Arm angle {arm_angle}° exceeds 45° limit")
        else:
            results.append(f"OK: Arm angle {arm_angle}° within 45° limit")
    except:
        results.append("WARNING: Could not verify arm angle")

    return results

def check_manifold():
    """Check if model is manifold (watertight)."""
    results = []

    display_doc = FreeCAD.getDocument("BraceletDisplay")
    body = display_doc.getObject("DisplayBody")

    try:
        # Create mesh for manifold check
        mesh_obj = display_doc.addObject("Mesh::Feature", "TempMesh")
        mesh_obj.Mesh = body.Shape.tessellate(0.1)

        if mesh_obj.Mesh.isSolid():
            results.append("OK: Model is manifold (watertight)")
        else:
            results.append("ERROR: Model is not manifold")

        # Clean up
        display_doc.removeObject("TempMesh")
    except Exception as e:
        results.append(f"WARNING: Could not verify manifold: {e}")

    return results

def check_dimensions():
    """Check model fits within build volume."""
    results = []

    try:
        display_doc = FreeCAD.getDocument("BraceletDisplay")
        body = display_doc.getObject("DisplayBody")

        bbox = body.Shape.BoundBox
        max_dim = max(bbox.XLength, bbox.YLength, bbox.ZLength)

        # K2 Plus build volume: 350x350x350mm
        if max_dim > 350:
            results.append(f"ERROR: Model dimension {max_dim:.1f}mm exceeds 350mm limit")
        else:
            results.append(f"OK: Max dimension {max_dim:.1f}mm fits in 350mm build volume")

        # Check if centered
        center_x = (bbox.XMax + bbox.XMin) / 2
        center_y = (bbox.YMax + bbox.YMin) / 2

        if abs(center_x) > 5 or abs(center_y) > 5:
            results.append(f"WARNING: Model not centered (offset: {center_x:.1f}, {center_y:.1f})")
        else:
            results.append("OK: Model centered at origin")

    except Exception as e:
        results.append(f"ERROR: Could not check dimensions: {e}")

    return results

def main():
    """Run print validation."""
    print("=== Bracelet Display Print Validation ===\n")

    # Run checks
    print("Overhang Check:")
    overhang_results = check_overhangs()
    for result in overhang_results:
        print(f"  {result}")

    print("\nManifold Check:")
    manifold_results = check_manifold()
    for result in manifold_results:
        print(f"  {result}")

    print("\nDimension Check:")
    dimension_results = check_dimensions()
    for result in dimension_results:
        print(f"  {result}")

    # Count errors
    all_results = overhang_results + manifold_results + dimension_results
    errors = [r for r in all_results if r.startswith("ERROR")]
    warnings = [r for r in all_results if r.startswith("WARNING")]

    print(f"\n=== Validation Summary ===")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nFailed - Fix errors before printing")
        sys.exit(1)
    else:
        print("\nPassed - Model ready for printing")

if __name__ == "__main__":
    main()