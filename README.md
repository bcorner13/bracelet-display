# Bracelet Display - Parametric 3D Model

A parametric bracelet display stand designed for product photography, optimized for support-free FDM printing.

## Project Overview

**Purpose:** Professional bracelet display for marketing photography  
**Printer:** Creality K2 Plus (120mm x 140mm build area)  
**Material:** PLA/ASA (optimized for Silk filaments - Gold/Copper)  
**Print Requirements:** No supports required, printable upright  

## Key Features

- **Fully Parametric:** 12 key parameters for customization
- **Support-Free:** All overhangs under 45°
- **Professional Aesthetics:** Chamfered edges, smooth curves
- **Stable Base:** Weighted base for tabletop photography
- **Size Flexible:** Accommodates various bracelet sizes (20-35mm)

## Quick Start

1. **Design Phase:** Review `intent.md` and `plan.md`
2. **Implementation:** Follow `plan.md` phases using FreeCAD MCP tools
3. **Validation:** Run parametric tests across size ranges
4. **Export:** Generate STL files in `stls/` directory

## File Structure

```
bracelet_display/
├── cad_files/          # FreeCAD documents (.FCStd)
├── stls/               # Exported STL files
├── macros/             # FreeCAD automation macros  
├── renders/            # CAD renders and photography refs
├── docs/               # Design specs and documentation
├── intent.md           # Project requirements
├── plan.md             # Implementation roadmap
├── CAD_STANDARDS.md    # Design standards and constraints
└── CLAUDE.md           # Workflow and execution rules
```

## Parameters

| Parameter | Default | Range | Purpose |
|-----------|---------|--------|---------|
| BaseWidth | 80mm | 70-90mm | Platform stability |
| BaseDepth | 60mm | 50-70mm | Desk footprint |
| DisplayHeight | 105mm | 90-120mm | Total height |
| DisplayAngle | 50° | 40-60° | Photography angle |
| BraceletRestDiameter | 28mm | 20-35mm | Bracelet accommodation |
| WallThickness | 2.5mm | 2-4mm | Print quality & strength |

## Development Workflow

1. **Intent** → Defined in `intent.md`
2. **Plan** → Documented in `plan.md` 
3. **Execution** → Using FreeCAD MCP tools
4. **Validation** → Parametric testing and print validation

## Standards Compliance

- ✅ CAD_STANDARDS.md requirements
- ✅ Manifold geometry (watertight)
- ✅ Origin-centered for K2 Plus
- ✅ Commercial pricing target ($36-45)
- ✅ Silk filament optimization