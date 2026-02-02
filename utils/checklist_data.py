"""
==============================================================================
CHECKLIST DATA - Checklist Items and Comment Mappings
==============================================================================
File: utils/checklist_data.py
Purpose: Contains all checklist items organized by section, with mappings
         to relevant BB comments that should appear when "No" is selected.

Structure:
- CHECKLISTS: Dict of review types, each containing sections with items
- Each item has: description, applicable_to (review types), comment_ids
==============================================================================
"""

# Review types
REVIEW_TYPES = [
    "Transitional Lot",
    "Hillside Protection Lot", 
    "Standard Lot",
    "Pool Permit",
    "Fence Permit"
]

# Reviewers
REVIEWERS = ["KB", "JD", "JM", "RL", "PM", "JC", "SKT", "DB"]

# Checklist sections and items
# Format: section_id: {name, items: [{id, description, comment_ids, applies_to}]}
# applies_to: list of review types this item applies to (empty = all)

CHECKLIST_SECTIONS = {
    # =========================================================================
    # SECTION 0: GENERAL/PRELIMINARY (Quick exit for incomplete plans)
    # =========================================================================
    "general_preliminary": {
        "name": "0. General/Preliminary",
        "items": [
            {
                "id": "0.1",
                "description": "Plan complete enough for full review (Land Disturbance Plan requirements)",
                "comment_ids": ["BB-0011"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "0.2",
                "description": "Plan complete enough for full review (Transitional Lot requirements)",
                "comment_ids": ["BB-0013"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot"]
            },
            {
                "id": "0.3",
                "description": "Engineering review required (>800 sq ft additional impervious)",
                "comment_ids": ["BB-0018"],
                "applies_to": []  # All
            },
            {
                "id": "0.4",
                "description": "ROW/PUDE damage repair note provided",
                "comment_ids": ["BB-0024"],
                "applies_to": []  # All
            },
        ]
    },

    # =========================================================================
    # SECTION 1: PLAN DOCUMENTATION
    # =========================================================================
    "plan_documentation": {
        "name": "1. Plan Documentation",
        "items": [
            {
                "id": "1.1",
                "description": "Plans stamped and signed by TN PE or LA",
                "comment_ids": ["BB-0096"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Pool Permit"]
            },
            {
                "id": "1.2",
                "description": "Name and phone number of builder/owner shown on plan",
                "comment_ids": ["BB-0103"],
                "applies_to": []  # All
            },
            {
                "id": "1.3",
                "description": "Email address for design engineer or LA shown/submitted",
                "comment_ids": ["BB-0104"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Pool Permit"]
            },
            {
                "id": "1.4",
                "description": "Building footprint matches house plans",
                "comment_ids": ["BB-0105"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.5",
                "description": "Current field run topography with 2' contours and actual elevations based on benchmark",
                "comment_ids": ["BB-0083", "BB-0124"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "1.6",
                "description": "Limit to one page if possible, two pages if necessary",
                "comment_ids": ["BB-0106"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot"]
            },
            {
                "id": "1.7",
                "description": "Scale 1:20 standard, other engineering scales as necessary",
                "comment_ids": ["BB-0107"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot"]
            },
            {
                "id": "1.8",
                "description": "Vicinity map with legible street names",
                "comment_ids": ["BB-0108"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.9",
                "description": "Subdivision, lot number, and zoning in title block and labeled in plan view",
                "comment_ids": ["BB-0109"],
                "applies_to": []  # All
            },
            {
                "id": "1.10",
                "description": "Adjacent lot numbers and parcel data if available",
                "comment_ids": ["BB-0059"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.11",
                "description": "Label streets and show right-of-way width",
                "comment_ids": ["BB-0110"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.12",
                "description": "Include recorded plat book and page number in title block",
                "comment_ids": ["BB-0111"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.13",
                "description": "Dumpster location shown with accessible route by transport",
                "comment_ids": ["BB-0060"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "1.14",
                "description": "Concrete washout location shown with accessible route",
                "comment_ids": ["BB-0069"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 2: STANDARD DETAILS
    # =========================================================================
    "standard_details": {
        "name": "2. Standard Details",
        "items": [
            {
                "id": "2.1",
                "description": "Silt fence detail (TDEC approved)",
                "comment_ids": ["BB-0062", "BB-0025"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.2",
                "description": "Temporary construction entrance (12'W x 30'L, ASTM #1 stone, filter fabric)",
                "comment_ids": ["BB-0064", "BB-0132", "BB-0054"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.3",
                "description": "Tree protection detail (1.5 times larger than drip line)",
                "comment_ids": ["BB-0040"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.4",
                "description": "Retaining wall detail (if applicable) stamped by PE",
                "comment_ids": ["BB-0061", "BB-0036"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.5",
                "description": "Driveway ramp detail",
                "comment_ids": ["BB-0092"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "2.6",
                "description": "Typical drainage swale detail",
                "comment_ids": ["BB-0042"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.7",
                "description": "Underground drainage infrastructure detail",
                "comment_ids": ["BB-0130"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "2.8",
                "description": "Sidewalk detail (if applicable)",
                "comment_ids": ["BB-0070"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 3: PROPERTY & BOUNDARIES
    # =========================================================================
    "property_boundaries": {
        "name": "3. Property & Boundaries",
        "items": [
            {
                "id": "3.1",
                "description": "Property lines with bearings and distances (check against recorded plat)",
                "comment_ids": ["BB-0131", "BB-0001", "BB-0112"],
                "applies_to": []  # All
            },
            {
                "id": "3.2",
                "description": "Building setbacks shown, labeled and dimensioned",
                "comment_ids": ["BB-0125", "BB-0078", "BB-0063"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "3.3",
                "description": "Easements shown, labeled and dimensioned",
                "comment_ids": ["BB-0113"],
                "applies_to": []  # All
            },
            {
                "id": "3.4",
                "description": "All public utilities shown, labeled and dimensioned",
                "comment_ids": ["BB-0114"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 4: TOPOGRAPHY & GRADING
    # =========================================================================
    "topography_grading": {
        "name": "4. Topography & Grading",
        "items": [
            {
                "id": "4.1",
                "description": "Proposed contours labeled and distinguishable from existing",
                "comment_ids": ["BB-0051"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "4.2",
                "description": "Spot elevations shown where necessary, TW/BW for retaining walls",
                "comment_ids": ["BB-0075"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "4.3",
                "description": "Grades in excess of 3:1 labeled with method of stabilization noted",
                "comment_ids": ["BB-0055", "BB-0079"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "4.4",
                "description": "Off-site topography extended 25' beyond boundaries if grading within 20' of boundary",
                "comment_ids": ["BB-0028", "BB-0046"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 5: DRIVEWAYS
    # =========================================================================
    "driveways": {
        "name": "5. Driveways",
        "items": [
            {
                "id": "5.1",
                "description": "Driveway width labeled (Max 20', Min 10' unless >500' long then 12')",
                "comment_ids": ["BB-0115"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.2",
                "description": "Driveway slope (20% max hard surface, 10% gravel, 5% max cross slope)",
                "comment_ids": ["BB-0126"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.3",
                "description": "6\" rise in driveway from edge of pavement to R.O.W.",
                "comment_ids": ["BB-0116"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.4",
                "description": "Minimum 20' inside turning radius for curves, 14' overhead clearance",
                "comment_ids": ["BB-0117"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.5",
                "description": "Grade break from drive entrance passable for typical car",
                "comment_ids": ["BB-0118"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.6",
                "description": "30' driveway apron (or 24' with 10'x12' dovetail turnaround)",
                "comment_ids": ["BB-0057"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.7",
                "description": "Driveway 5' minimum from property line",
                "comment_ids": ["BB-0052"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "5.8",
                "description": "Driveway not impacting drainage inlet",
                "comment_ids": ["BB-0094"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 6: RETAINING WALLS
    # =========================================================================
    "retaining_walls": {
        "name": "6. Retaining Walls",
        "items": [
            {
                "id": "6.1",
                "description": "Max height 10' inside buildable area, 6' outside (measured on exposed face)",
                "comment_ids": ["BB-0036"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "6.2",
                "description": "Walls 4'+ require PE-stamped design (per code sec. 78-14)",
                "comment_ids": ["BB-0036", "BB-0041"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "6.3",
                "description": "Retaining wall design detail shown on plan",
                "comment_ids": ["BB-0061"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "6.4",
                "description": "Note that walls >4' must be inspected by licensed PE",
                "comment_ids": ["BB-0041"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "6.5",
                "description": "Guard rails/fencing required for grade change >30\" (attached to house)",
                "comment_ids": ["BB-0036", "BB-0102"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "6.6",
                "description": "Guard rails, fencing, or planted hedging for walls detached from house (>30\")",
                "comment_ids": ["BB-0036", "BB-0102"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 7: DRAINAGE
    # =========================================================================
    "drainage": {
        "name": "7. Drainage",
        "items": [
            {
                "id": "7.1",
                "description": "Drainage infrastructure designed by PE per Article 6.10 of Subdivision Regulations",
                "comment_ids": ["BB-0027", "BB-0080"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.2",
                "description": "Hydrologic and hydraulic data shown (pipe length, dimensions, acreage, flow, capacity, slope, material)",
                "comment_ids": ["BB-0027", "BB-0067"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.3",
                "description": "Drive culverts and pipe outlets require headwalls/endwalls and proper armament",
                "comment_ids": ["BB-0033", "BB-0073"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "7.4",
                "description": "Lot line swales designed and shown via contours or arrows",
                "comment_ids": ["BB-0042", "BB-0043"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.5",
                "description": "Swale calculations for velocities and stabilization",
                "comment_ids": ["BB-0021", "BB-0089"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.6",
                "description": "Check dams in areas of concentrated flow",
                "comment_ids": ["BB-0032", "BB-0038", "BB-0044"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.7",
                "description": "Downspout locations and outlet protection labeled",
                "comment_ids": ["BB-0034", "BB-0037"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "7.8",
                "description": "Positive drainage within right-of-way shown with contours/spot elevations",
                "comment_ids": ["BB-0082"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 8: EROSION CONTROL
    # =========================================================================
    "erosion_control": {
        "name": "8. Erosion Control",
        "items": [
            {
                "id": "8.1",
                "description": "Erosion control shown on plan with legend and/or annotations",
                "comment_ids": ["BB-0072"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "8.2",
                "description": "Silt fence properly designed per TDEC criteria",
                "comment_ids": ["BB-0025"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "8.3",
                "description": "Construction entrance detail with ROW protection notes",
                "comment_ids": ["BB-0064", "BB-0054"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "8.4",
                "description": "Limits of disturbance shown",
                "comment_ids": ["BB-0095"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "8.5",
                "description": "Brentwood Critical Erosion Control Notes provided",
                "comment_ids": ["BB-0031"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 9: TREES & LANDSCAPING
    # =========================================================================
    "trees_landscaping": {
        "name": "9. Trees & Landscaping",
        "items": [
            {
                "id": "9.1",
                "description": "Tree survey showing location, diameter, species of trees to remove/remain",
                "comment_ids": ["BB-0039", "BB-0065"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "9.2",
                "description": "Tree protection shown in plan view",
                "comment_ids": ["BB-0009"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "9.3",
                "description": "Tree protection detail (1.5 times drip line)",
                "comment_ids": ["BB-0040"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "9.4",
                "description": "Note: 25 caliper inches of trees per acre required",
                "comment_ids": ["BB-0121"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 10: UTILITIES
    # =========================================================================
    "utilities": {
        "name": "10. Utilities",
        "items": [
            {
                "id": "10.1",
                "description": "HVAC pad shown",
                "comment_ids": ["BB-0119"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "10.2",
                "description": "Water meter location shown",
                "comment_ids": ["BB-0120"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "10.3",
                "description": "Sewer stub-out shown (check FFE vs invert, grinder pump if applicable)",
                "comment_ids": ["BB-0068"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 11: SITE CALCULATIONS
    # =========================================================================
    "site_calculations": {
        "name": "11. Site Calculations",
        "items": [
            {
                "id": "11.1",
                "description": "Building coverage calculations (Max 25%)",
                "comment_ids": ["BB-0066"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "11.2",
                "description": "Green space coverage calculations (Min 40%)",
                "comment_ids": ["BB-0066"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "11.3",
                "description": "Basement coverage calculations (Min 50% perimeter covered)",
                "comment_ids": ["BB-0066"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 12: SITE ELEVATIONS
    # =========================================================================
    "site_elevations": {
        "name": "12. Site Elevations",
        "items": [
            {
                "id": "12.1",
                "description": "FFE shown for all structures",
                "comment_ids": ["BB-0127"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "12.2",
                "description": "Garage elevation shown",
                "comment_ids": ["BB-0128"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "12.3",
                "description": "Basement elevation shown (if applicable)",
                "comment_ids": ["BB-0129"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "12.4",
                "description": "Minimum LFE shown (if applicable)",
                "comment_ids": ["BB-0023"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "12.5",
                "description": "Grades adjacent to home (2% for 10', 8\" below FFE)",
                "comment_ids": ["BB-0071"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 13: SIGNATURES & NOTES
    # =========================================================================
    "signatures_notes": {
        "name": "13. Signatures & Notes",
        "items": [
            {
                "id": "13.1",
                "description": "Permit Holder Signature Block signed and dated",
                "comment_ids": ["BB-0049", "BB-0026"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Pool Permit"]
            },
            {
                "id": "13.2",
                "description": "Required general notes provided",
                "comment_ids": ["BB-0041"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot"]
            },
            {
                "id": "13.3",
                "description": "Driveway as-built survey note (for driveways over 15% slope)",
                "comment_ids": ["BB-0041"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 14: SPECIAL CONDITIONS
    # =========================================================================
    "special_conditions": {
        "name": "14. Special Conditions",
        "items": [
            {
                "id": "14.1",
                "description": "Open space/buffers noted as protected during construction",
                "comment_ids": ["BB-0035", "BB-0074"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "14.2",
                "description": "Water quality riparian buffer shown and labeled",
                "comment_ids": ["BB-0077"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "14.3",
                "description": "Floodplain requirements (if applicable)",
                "comment_ids": ["BB-0023", "BB-0010"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot", "Standard Lot", "Pool Permit"]
            },
            {
                "id": "14.4",
                "description": "Transitional lot checklist completed and submitted",
                "comment_ids": ["BB-0085", "BB-0086", "BB-0087"],
                "applies_to": ["Transitional Lot", "Hillside Protection Lot"]
            },
            {
                "id": "14.5",
                "description": "Hillside Protection compliance (if HP lot)",
                "comment_ids": ["BB-0012", "BB-0084"],
                "applies_to": ["Hillside Protection Lot"]
            },
            {
                "id": "14.6",
                "description": "Geotechnical inspection report required (HP lots)",
                "comment_ids": ["BB-0022"],
                "applies_to": ["Hillside Protection Lot"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 15: POOL PERMIT SPECIFIC
    # =========================================================================
    "pool_specific": {
        "name": "15. Pool Permit Specific",
        "items": [
            {
                "id": "15.1",
                "description": "Review is for grading only (Building & Codes handles pool decking)",
                "comment_ids": ["BB-0014"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.2",
                "description": "Fence/gate/pool/spa approval note (Building & Codes required)",
                "comment_ids": ["BB-0030"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.3",
                "description": "Pool fence location - not in PUDE or along property line issues",
                "comment_ids": ["BB-0017", "BB-0122", "BB-0123"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.4",
                "description": "Pool fence location - not in sewer or other easement",
                "comment_ids": ["BB-0122"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.5",
                "description": "Plan shows entire rear yard with grades",
                "comment_ids": ["BB-0097"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.6",
                "description": "Pool and decking shown within setbacks",
                "comment_ids": ["BB-0063", "BB-0093"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.7",
                "description": "Setbacks correct per approved plat",
                "comment_ids": ["BB-0078"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.8",
                "description": "Stormwater does not flow towards house",
                "comment_ids": ["BB-0071"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.9",
                "description": "Pool contractor limits of work clearly shown",
                "comment_ids": ["BB-0090", "BB-0098"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.10",
                "description": "Code compliant pool fence shown",
                "comment_ids": ["BB-0076"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.11",
                "description": "Pool deck paver detail (if applicable)",
                "comment_ids": ["BB-0047"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.12",
                "description": "Normal pool elevation at drain location",
                "comment_ids": ["BB-0015"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.13",
                "description": "Pool deck elevation not higher than home elevations",
                "comment_ids": ["BB-0016"],
                "applies_to": ["Pool Permit"]
            },
            {
                "id": "15.14",
                "description": "Floodplain steps completed (if applicable)",
                "comment_ids": ["BB-0099"],
                "applies_to": ["Pool Permit"]
            },
        ]
    },
    
    # =========================================================================
    # SECTION 16: FENCE PERMIT SPECIFIC
    # =========================================================================
    "fence_specific": {
        "name": "16. Fence Permit Specific",
        "items": [
            {
                "id": "16.1",
                "description": "Fence not in public right-of-way (3' from sidewalk/bikeway)",
                "comment_ids": ["BB-0122"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.2",
                "description": "Fence not in recorded easement without authorization",
                "comment_ids": ["BB-0122", "BB-0017"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.3",
                "description": "Fence does not create sight distance issues",
                "comment_ids": ["BB-0122"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.4",
                "description": "Fence location relative to PUDE reviewed",
                "comment_ids": ["BB-0017", "BB-0123"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.5",
                "description": "No trees planted in easements",
                "comment_ids": ["BB-0113"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.6",
                "description": "Fence over utility easement has proper gate for access",
                "comment_ids": ["BB-0123"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.7",
                "description": "Fence does not encompass drainage swale",
                "comment_ids": ["BB-0123"],
                "applies_to": ["Fence Permit"]
            },
            {
                "id": "16.8",
                "description": "Maximum 5' encroachment if no existing swale",
                "comment_ids": ["BB-0123"],
                "applies_to": ["Fence Permit"]
            },
        ]
    },
}


def get_checklist_for_review_type(review_type):
    """
    Get all applicable checklist sections and items for a given review type.
    
    Args:
        review_type: One of REVIEW_TYPES
    
    Returns:
        Dict of sections with their applicable items
    """
    applicable_checklist = {}
    
    for section_id, section_data in CHECKLIST_SECTIONS.items():
        applicable_items = []
        
        for item in section_data["items"]:
            # If applies_to is empty, it applies to all review types
            # Otherwise, check if the review type is in the list
            if not item["applies_to"] or review_type in item["applies_to"]:
                applicable_items.append(item)
        
        # Only include section if it has applicable items
        if applicable_items:
            applicable_checklist[section_id] = {
                "name": section_data["name"],
                "items": applicable_items
            }
    
    return applicable_checklist


def get_all_sections():
    """Get all section names"""
    return {sid: data["name"] for sid, data in CHECKLIST_SECTIONS.items()}
