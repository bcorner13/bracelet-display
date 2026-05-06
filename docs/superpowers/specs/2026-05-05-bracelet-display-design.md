# Bracelet Display Design Specification

**Date:** 2026-05-05  
**Project:** bracelet_display  
**Status:** Approved  
**Implementation:** Parametric FreeCAD model via MCP tools  

## Overview

A parametric bracelet display stand designed for product photography, optimized for support-free FDM printing on Creality K2 Plus. The design enables professional bracelet presentation for marketing materials while maintaining parametric flexibility for various bracelet sizes and photography requirements.

## Requirements

### Functional Requirements
- **Primary Use:** Display bracelets for product photography
- **Stability:** Secure tabletop placement during photography setup
- **Flexibility:** Accommodate bracelet sizes from 8-9 inches (20.3-22.9 cm length)
- **Professional Aesthetics:** Clean, elegant appearance suitable for marketing

### Manufacturing Requirements
- **Printer:** Creality K2 Plus (350mm x 350mm x 350mm build volume)
- **Material:** PLA/ASA, optimized for Silk filaments (Gold/Copper)
- **Support-Free:** All overhangs under 45° for clean printing
- **Wall Thickness:** 2.5mm minimum for strength and premium feel
- **Print Orientation:** Upright without rotation required

### Parametric Requirements
- **Fully Parametric:** All dimensions driven by VarSet parameters
- **Range Validation:** Each parameter tested across specified ranges
- **Constraint Strategy:** Single point of truth for all measurements
- **Version Control:** Parameter changes tracked and documented

## Architecture

### Component Breakdown

**1. Base Platform**
- **Geometry:** Rounded rectangular platform (120mm x 100mm x 25mm)
- **Purpose:** Provides stability for taller display and houses weight distribution
- **Features:** Chamfered edges (3mm) for premium appearance
- **Constraints:** Platform center anchored to origin (0,0,0)

**2. Display Arm**
- **Geometry:** Elegant curved arm extending from base at 15° angle (more vertical for hanging display)
- **Profile:** Wider at base (20mm), maintaining width (18mm) for strength with taller design
- **Height:** 200mm total display height (ample room for 8-9" bracelet to hang)
- **Features:** 2mm edge chamfers for smooth finish

**3. Bracelet Rest**
- **Geometry:** Cylindrical post for hanging bracelets
- **Diameter:** 25mm (optimal for 8-9 inch bracelet draping without stretching)
- **Integration:** Seamlessly blended with arm geometry
- **Features:** 1.5mm comfort chamfer to prevent bracelet snagging

### Parametric System Design

**Parameter Groups:**

```
BaseGeometry:
├── BaseWidth: 120mm (100-150mm range)
├── BaseDepth: 100mm (80-120mm range)
├── BaseHeight: 25mm (20-35mm range)
└── WallThickness: 2.5mm (2-4mm range)

DisplayGeometry:
├── DisplayHeight: 200mm (180-250mm range)
├── DisplayAngle: 15° (10-25° range, more vertical for hanging)
├── ArmWidth: 20mm (15-25mm range, consistent for strength)
└── BraceletRestDiameter: 25mm (20-35mm range, optimized for 8-9" bracelets)

Aesthetics:
├── BaseChamfer: 3mm (2-4mm range)
├── ArmChamfer: 2mm (1-3mm range)
└── RestChamfer: 1.5mm (1-2mm range)
```

## Implementation Strategy

### Phase 1: Parameter System Setup
1. Create `Params.FCStd` document with VarSet object
2. Define all 12 parameters with appropriate types and ranges
3. Group parameters by functional category
4. Set initial values per design specification

### Phase 2: Base Geometry Creation
1. Create `BraceletDisplay.FCStd` main document
2. Create PartDesign body for unified feature tree
3. Sketch rounded rectangular base on XY plane
4. Constrain base dimensions to BaseGeometry parameters
5. Pad base to BaseHeight with parametric binding

### Phase 3: Display Arm Construction
1. Create arm profile sketch on XZ plane (side view)
2. Define tapered arm geometry from base to rest position
3. Calculate arm endpoint using trigonometry (DisplayAngle, DisplayHeight)
4. Constrain all arm dimensions to DisplayGeometry parameters
5. Pad arm with parametric width binding

### Phase 4: Bracelet Rest Feature
1. Create rest sketch at calculated arm endpoint
2. Define circular rest profile (BraceletRestDiameter)
3. Integrate rest with arm geometry via revolution or pad
4. Apply parametric constraints for all rest dimensions

### Phase 5: Finishing Operations
1. Apply chamfers to all visible edges per Aesthetics parameters
2. Verify all constraints satisfied and model recomputes cleanly
3. Validate geometry meets print requirements (no overhangs >45°)
4. Export STL centered at origin for K2 Plus compatibility

## Validation Criteria

### Geometric Validation
- All features recompute without errors across parameter ranges
- No invalid geometry or self-intersections at any parameter combination
- All constraints properly applied and driving geometry
- Model remains manifold (watertight) for all parameter values

### Print Validation
- Maximum overhang angle ≤ 45° for support-free printing
- Wall thickness ≥ 2mm everywhere for structural integrity
- Overall dimensions fit within 350×350×350mm K2 Plus build volume
- Model centered at (0,0,0) for proper bed placement

### Functional Validation
- Bracelet rest diameter accommodates target bracelet size ranges
- Display angle provides optimal photography viewing angles
- Base provides adequate stability for desktop photography setup
- Aesthetics meet commercial product presentation standards

## Risk Mitigation

### Parametric Risks
- **Risk:** Parameter changes breaking downstream constraints
- **Mitigation:** Comprehensive constraint validation across full parameter ranges
- **Validation:** Automated parameter sweep testing in implementation

### Manufacturing Risks  
- **Risk:** Support requirements due to excessive overhangs
- **Mitigation:** All geometry designed with ≤45° overhang constraint
- **Validation:** Slicer preview testing with actual print settings

### Aesthetic Risks
- **Risk:** Poor surface finish on visible surfaces
- **Mitigation:** Optimized orientation and chamfer strategy for Silk filaments
- **Validation:** Test prints with target material and settings

## Success Metrics

1. **Parametric Flexibility:** Model adapts across full parameter ranges without manual intervention
2. **Print Quality:** Support-free printing with excellent surface finish on first attempt  
3. **Photography Performance:** Provides stable, attractive bracelet presentation for marketing materials
4. **Commercial Viability:** Meets $36-45 price target with professional appearance

## Implementation Dependencies

- **FreeCAD 1.1:** MCP tool compatibility for automated model creation
- **Parameter Document:** `Params.FCStd` with properly configured VarSet
- **CAD Standards Compliance:** All geometry follows CAD_STANDARDS.md requirements
- **Validation Framework:** Parametric audit script for constraint verification

This design provides a robust foundation for creating a professional, parametric bracelet display that meets all functional, manufacturing, and commercial requirements while maintaining the flexibility needed for various bracelet sizes and photography setups.