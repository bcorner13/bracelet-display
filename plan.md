# Bracelet Display Parametric Implementation Plan

**Project:** Parametric bracelet display for product photography  
**Target:** Support-free printing on Creality K2 Plus  
**Standards:** CAD_STANDARDS.md compliance  
**Status:** Ready for execution  

---

## Phase 0: Documentation Discovery ✅

### Allowed APIs (from MCP schema analysis)
- **Document Management:** `mcp__freecad__create_document`, `mcp__freecad__save_document`, `mcp__freecad__recompute_document`
- **Object Creation:** `mcp__freecad__create_object` (for VarSet), `mcp__freecad__create_partdesign_body`
- **Sketching:** `mcp__freecad__create_sketch`, `mcp__freecad__add_sketch_*` family
- **Features:** `mcp__freecad__pad_sketch`, `mcp__freecad__pocket_sketch`, `mcp__freecad__chamfer_edges`
- **Python Execution:** `mcp__freecad__execute_python` (for constraints, expressions, VarSet properties only)

### Validated Parametric System
**BaseGeometry Group:**
- `BaseWidth`: 80mm (70-90mm tested range)
- `BaseDepth`: 60mm (50-70mm range)
- `BaseHeight`: 18mm (15-25mm range)
- `WallThickness`: 2.5mm (2-4mm range)

**DisplayGeometry Group:**
- `DisplayHeight`: 105mm (90-120mm range)
- `DisplayAngle`: 50° (40-60° range)
- `ArmWidth`: 15mm at base, 8mm at top
- `BraceletRestDiameter`: 28mm (20-35mm range)

**Aesthetics Group:**
- `BaseChamfer`: 3mm (edge finishing)
- `ArmChamfer`: 2mm (edge finishing)
- `RestChamfer`: 1.5mm (comfort edge)

### Copy-Ready Implementation Patterns

**VarSet Creation Pattern:**
```python
vs.addProperty("App::PropertyLength", "BaseWidth", "BaseGeometry", "Base platform width")
vs.BaseWidth = "80mm"
```

**Parametric Binding Pattern:**
```python
pad.setExpression('Length', '<<Params>>#VarSet.BaseWidth')
```

**Angular Constraint Pattern:**
```python
constraint.setExpression('Angle', '<<Params>>#VarSet.DisplayAngle')
```

---

## Phase 1: Core Document Structure

### Step 1.1: Create Params Document
```python
# Create parameter document
doc_params = mcp__freecad__create_document("Params")

# Create VarSet for all parameters
vs = mcp__freecad__create_object("App::VarSet", "VarSet", "Params")
```

### Step 1.2: Setup BaseGeometry Parameters
```python
# Base platform parameters
vs.addProperty("App::PropertyLength", "BaseWidth", "BaseGeometry", "Base platform width")
vs.addProperty("App::PropertyLength", "BaseDepth", "BaseGeometry", "Base platform depth")
vs.addProperty("App::PropertyLength", "BaseHeight", "BaseGeometry", "Base platform height")
vs.addProperty("App::PropertyLength", "WallThickness", "BaseGeometry", "Wall thickness throughout")

# Set initial values
vs.BaseWidth = "80mm"
vs.BaseDepth = "60mm" 
vs.BaseHeight = "18mm"
vs.WallThickness = "2.5mm"
```

### Step 1.3: Setup DisplayGeometry Parameters
```python
# Display arm parameters
vs.addProperty("App::PropertyLength", "DisplayHeight", "DisplayGeometry", "Total display height")
vs.addProperty("App::PropertyAngle", "DisplayAngle", "DisplayGeometry", "Display arm angle from vertical")
vs.addProperty("App::PropertyLength", "ArmWidthBase", "DisplayGeometry", "Arm width at base")
vs.addProperty("App::PropertyLength", "ArmWidthTop", "DisplayGeometry", "Arm width at top")
vs.addProperty("App::PropertyLength", "BraceletRestDiameter", "DisplayGeometry", "Bracelet rest diameter")

# Set initial values
vs.DisplayHeight = "105mm"
vs.DisplayAngle = "50deg"
vs.ArmWidthBase = "15mm"
vs.ArmWidthTop = "8mm"
vs.BraceletRestDiameter = "28mm"
```

### Step 1.4: Setup Aesthetics Parameters
```python
# Finishing parameters
vs.addProperty("App::PropertyLength", "BaseChamfer", "Aesthetics", "Base edge chamfer")
vs.addProperty("App::PropertyLength", "ArmChamfer", "Aesthetics", "Arm edge chamfer") 
vs.addProperty("App::PropertyLength", "RestChamfer", "Aesthetics", "Rest edge chamfer")

# Set initial values
vs.BaseChamfer = "3mm"
vs.ArmChamfer = "2mm"
vs.RestChamfer = "1.5mm"
```

---

## Phase 2: Main Model Creation

### Step 2.1: Create Main Document
```python
# Create main display document
doc_main = mcp__freecad__create_document("BraceletDisplay")

# Create main body
body = mcp__freecad__create_partdesign_body("DisplayBody", "BraceletDisplay")
```

### Step 2.2: Base Platform Sketch
```python
# Create base platform sketch on XY plane
base_sketch = mcp__freecad__create_sketch("BaseSketch", "BraceletDisplay")

# Create rounded rectangle base
# Center rectangle
mcp__freecad__add_sketch_rectangle(
    sketch_name="BaseSketch",
    document_name="BraceletDisplay",
    start_x="-40mm",  # Half BaseWidth
    start_y="-30mm",  # Half BaseDepth
    end_x="40mm",
    end_y="30mm"
)

# Add corner radius fillets (8mm radius for professional look)
# Constrain rectangle to parameters
```

### Step 2.3: Base Platform Feature
```python
# Pad base platform
base_pad = mcp__freecad__pad_sketch(
    sketch_name="BaseSketch",
    document_name="BraceletDisplay",
    length="18mm"  # Will be parametrically bound
)

# Bind to parameter
base_pad.setExpression('Length', '<<Params>>#VarSet.BaseHeight')
```

### Step 2.4: Display Arm Sketch
```python
# Create display arm sketch on XZ plane (side view)
arm_sketch = mcp__freecad__create_sketch("ArmSketch", "BraceletDisplay")

# Create tapered arm profile
# Start point: (0, BaseHeight)
# End point: (calculated from angle and height, DisplayHeight)
# Taper from ArmWidthBase to ArmWidthTop

# Mathematical relationships:
# arm_length = DisplayHeight / cos(DisplayAngle)
# top_x = DisplayHeight * tan(DisplayAngle)
```

### Step 2.5: Display Arm Feature
```python
# Pad display arm
arm_pad = mcp__freecad__pad_sketch(
    sketch_name="ArmSketch", 
    document_name="BraceletDisplay",
    length="15mm"  # Will be parametrically bound to ArmWidthBase
)

# Bind to parameter
arm_pad.setExpression('Length', '<<Params>>#VarSet.ArmWidthBase')
```

### Step 2.6: Bracelet Rest Feature
```python
# Create bracelet rest at top of arm
rest_sketch = mcp__freecad__create_sketch("RestSketch", "BraceletDisplay")

# Create circle for bracelet rest
mcp__freecad__add_sketch_circle(
    sketch_name="RestSketch",
    document_name="BraceletDisplay", 
    center_x="calculated_x",  # From arm geometry
    center_y="calculated_y",  # From arm geometry
    radius="14mm"  # Half BraceletRestDiameter
)

# Revolve to create cylindrical rest
```

---

## Phase 3: Finishing Operations

### Step 3.1: Edge Chamfers
```python
# Chamfer base edges
mcp__freecad__chamfer_edges(
    object_name="BaseFeature",
    document_name="BraceletDisplay", 
    size="3mm"  # Bound to BaseChamfer parameter
)

# Chamfer arm edges  
mcp__freecad__chamfer_edges(
    object_name="ArmFeature",
    document_name="BraceletDisplay",
    size="2mm"  # Bound to ArmChamfer parameter
)

# Chamfer rest edges
mcp__freecad__chamfer_edges(
    object_name="RestFeature", 
    document_name="BraceletDisplay",
    size="1.5mm"  # Bound to RestChamfer parameter
)
```

---

## Phase 4: Validation & Export

### Step 4.1: Geometric Validation
```python
# Recompute all features
mcp__freecad__recompute_document("BraceletDisplay")

# Verify no geometry errors
# Check manifold status
# Verify all constraints satisfied
```

### Step 4.2: Print Validation
- All overhangs < 45° (no supports required)
- Maximum height ≤ 120mm
- Centered at origin (0,0,0)
- Wall thickness ≥ 2mm everywhere

### Step 4.3: Export STL
```python
# Export final STL for printing
mcp__freecad__export_stl(
    object_name="DisplayBody",
    document_name="BraceletDisplay",
    file_path="./stls/bracelet_display_v1.stl"
)
```

---

## Phase 5: Parametric Testing

### Step 5.1: Parameter Range Testing
Test critical parameters within design ranges:
- `BaseWidth`: 70mm, 80mm, 90mm
- `DisplayHeight`: 90mm, 105mm, 120mm  
- `DisplayAngle`: 40°, 50°, 60°
- `BraceletRestDiameter`: 20mm, 28mm, 35mm

### Step 5.2: Bracelet Size Validation
Verify design works with common bracelet sizes:
- Small: 15-18cm circumference
- Medium: 18-20cm circumference  
- Large: 20-23cm circumference

### Step 5.3: Photography Angle Testing
Confirm optimal viewing angles for product photography:
- Front view (0°)
- Three-quarter view (45°)
- Side profile (90°)

---

## Success Criteria

✅ **Parametric:** All dimensions driven by VarSet parameters  
✅ **Print-ready:** No supports required, manifold geometry  
✅ **Professional:** Smooth curves, chamfered edges, stable base  
✅ **Flexible:** Accommodates various bracelet sizes  
✅ **Photography-optimized:** Multiple viewing angles, elegant presentation  

---

## File Structure (Post-Implementation)

```
bracelet_display/
├── cad_files/
│   ├── Params.FCStd           # Parameter document
│   └── BraceletDisplay.FCStd  # Main model
├── stls/
│   └── bracelet_display_v1.stl
├── macros/
│   ├── setup_varset.FCMacro   # Parameter setup
│   └── create_display.FCMacro # Main geometry
└── renders/
    └── display_angles.png     # Photography reference
```