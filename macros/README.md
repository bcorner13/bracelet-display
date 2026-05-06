# FreeCAD Macros

Macros for automating the bracelet display creation and modification:

- `setup_varset.FCMacro` - Creates and configures the parameter VarSet
- `create_display.FCMacro` - Builds the main display geometry
- `export_stl.FCMacro` - Exports final STL with validation

## Usage

1. Copy macros to `~/Library/Application Support/FreeCAD/v1-1/Macro/` (symlinks recommended)
2. Run via **Macro → Macros...** in FreeCAD
3. Macros are designed to be idempotent (safe to re-run)