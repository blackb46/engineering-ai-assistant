"""
==============================================================================
COMMENTS DATABASE - Standard Review Comments
==============================================================================
File: utils/comments_database.py
Purpose: Contains all standard BB comments for plan reviews

All comments are stored in a dictionary with Comment_ID as key.
Comments BB-0001 through BB-0102 are from the original template.
Comments BB-0103 through BB-0123 are new additions.
==============================================================================
"""

# Dictionary of all standard comments
# Format: "BB-XXXX": "Comment text"

COMMENTS = {
    "BB-0001": "Grading extends beyond property line",
    
    "BB-0002": "Add note: As-built surveys and certifications will be required for detention ponds, storm infrastructure, and cut/fill on lots and building areas, prior to release of certificates of occupancy",
    
    "BB-0003": "Add note: As-built surveys and certifications will be required for detention ponds, storm infrastructure, and cut/fill on lots and building areas, prior to release of final plat",
    
    "BB-0004": "Additional BMPs are necessary to properly address EPSC. Drainage areas for silt fence provided exceed 1/4 acre per 100 foot of silt fence. There are also multiple areas of concentrated flow without appropriate BMPs proposed.",
    
    "BB-0005": "Provide callouts for outfalls on all EPSC sheets",
    
    "BB-0006": "Provide detailed pond conversion plan from sediment basin to detention and schedule of completion.",
    
    "BB-0007": "Adjustments to these plans will likely result in additional comments based on changes required for plan set.",
    
    "BB-0008": "Add note that use of J-Hook method is required when crossing contours",
    
    "BB-0009": "Show tree protection on grading plan.",
    
    "BB-0010": "Pursuant to FEMA TN No-Rise Guidance Document: No encroachments including fill material or other development including structures shall be located within an area of at least equal to twice the width of the stream, measured from the top of each stream bank, unless certification by a Tennessee registered professional engineer is provided demonstrating that the cumulative effect of the proposed development, when combined with all other existing and anticipated development, will not increase the water surface elevation of the base flood more than one (1) foot at any point within the locality. The width of the stream is approximately 15', therefore no encroachments shall be located 30' on both sides of the TOB without a no-rise certification. An Effective Model (if one is not available from FEMA) can be created alongside an Existing & Proposed Conditions models that can have up to 1' rise.",
    
    "BB-0011": "Provide revised plan set in compliance with all elements of the Land Disturbance Plan provided in the City of Brentwood Zoning Code Chapter 56, Article 1, Subdivision 1, Sec. 56-13. - Land disturbance plan",
    
    "BB-0012": "Provide revised plan set in compliance with all elements of the Hillside Protection provided in the City of Brentwood Zoning Code Chapter 78, Article 3, Division 14.",
    
    "BB-0013": "Provide revised plan set in compliance with all elements of the Transitional Lot Checklist.",
    
    "BB-0014": "This review is only for the grading. The pool decking review will be required by the Building and Codes department. Building and Codes to confirm this will not be required with their review of the submittal.",
    
    "BB-0015": "Confirm whether normal pool elevation is at drain location. If so, provide alternate design.",
    
    "BB-0016": "Pool deck elevation is higher than adjacent elevations shown for the home such as the covered porch.",
    
    "BB-0017": "The installation of a fence within a P.U.D.E. does not relieve the current or future property owner from the responsibility and cost of having to remove or replace the fence in the future, if the City of Brentwood or any other utility owner were to need access to any portion of the P.U.D.E. for routine maintenance or utility relocation.",
    
    "BB-0018": "Since the total additional impervious surface is less than 800 square feet, a grading plan is not required. However, the proposed construction shall be required to comply with the erosion control requirements set forth in subsection 56-13(3) of the Brentwood City Code.",
    
    "BB-0019": "Provide underdrains in accordance with Article 6.5 of the subdivision regulations. Refer to Appendix Two, Drawings 6 and 7 of the Subdivision Regulations for underdrain detail. Update standard detail to show underdrains and provide notation on plans where underdrains are necessary.",
    
    "BB-0020": "Please review this and determine if adequately accommodated",
    
    "BB-0021": "Provide swale calculations including velocities to ensure final stabilization is maintained.",
    
    "BB-0022": "Provide geotechnical inspection report for review prior to CO to Codes department",
    
    "BB-0023": "Surveyor must show location of 100 year as it crosses lot by ground elevation and it's relationship to all improvements. Plan must also show BFE, flood map number and date. All must be stamped by a TN licensed surveyor.",
    
    "BB-0024": "Provide a note on the plans stating: Any damage to the ROW and/or PUDE shall be repaired to pre-construction conditions",
    
    "BB-0025": """Most if not all silt fence shown in the plans must be adjusted to meet the silt fence design criteria as follows per TDEC:

Silt fence should be installed along the contour, never up or down a slope. This is essential to ensure that the fence will not accidentally concentrate stormwater flows, thus creating worse erosion problems.

Silt fence can be installed without backing or with wire backing.

- The maximum drainage area for a continuous fence without backing shall be 1/4 acre per 100 linear feet of fence length, up to a maximum area of 2 acres. The maximum slope length behind the fence on the upslope side should be 110 feet (as measured along the ground surface).

- The maximum drainage area for a continuous silt fence with backing shall be 1 acre per 150 linear feet of fence length. The slope length above the silt fence with backing should be no more than 300 feet.""",
    
    "BB-0026": "Provide completed transitional lot checklist and provide signature.",
    
    "BB-0027": """Provide drainage calculations supporting proposed swales, channel drains, and pipe sizing. Drainage design must provide the following:
- Hydrologic and hydraulic data should be shown on the plan (e.g., pipe/culvert length and section dimensions, acreage entering, design flow, flow capacity, slope, material, etc.)
- All pipes and culverts (entrances/outlets) require proper armament at discharge.""",
    
    "BB-0028": "Revise the plan to include off-site existing topographic conditions extended to a minimum of 25 feet beyond the boundaries of the subject tract if grading is designed to be within 20 feet of any boundary line.",
    
    "BB-0029": "There is significant concern with the colluvial soils on site particularly in the areas where the building is being proposed.",
    
    "BB-0030": "SW2xxx-xxx Approval of the fence/gate details, pool, spa and structures is required by the Building and Codes Department. Release of the grading plan does not constitute approval of these items.",
    
    "BB-0031": """Provide the following notes on the plans:
BRENTWOOD CRITICAL EROSION CONTROL NOTES:
1) STABILIZATION MEASURES MUST BE PERFORMED WITHIN THREE(3) DAYS IN PORTIONS OF THE SITE WHERE CONSTRUCTION ACTIVITIES HAVE TEMPORARILY OR PERMANENTLY CEASED, WITHIN FIFTEEN (15) DAYS AFTER FINAL GRADING, OR PRIOR TO FINAL INSPECTION (STABILIZATION PRACTICES MAY INCLUDE: TEMPORARY OR PERMANENT SEEDING WITH MULCH, MATTING, OR SOD STABILIZATION.)

2) INSPECTIONS OF ALL CONTROL MEASURES AND DISTURBED AREAS MUST BE PERFORMED AT LEAST TWICE WEEKLY. INSPECTIONS MUST BE DOCUMENTED AND INCLUDE THE DATE OF THE INSPECTION AND MAJOR OBSERVATIONS.

3) BASED ON THE RESULTS OF INSPECTIONS, ANY INADEQUATE CONTROL MEASURES OR CONTROL MEASURES IN DISREPAIR MUST BE REPLACED OR MODIFIED, OR REPAIRED AS NECESSARY, WITHIN ONE DAY AFTER THE NEED IS IDENTIFIED.""",
    
    "BB-0032": "Concentrated flow in the proposed swales will require check dams. Indicate locations and provide check dam details.",
    
    "BB-0033": "Provide inverts at each end of proposed culvert. Indicate the total amount of cover for the pipe to ensure the driveway is built to accommodate the required 18\" minimum pipe. Determine if additional grading is needed or increased elevation of the driveway is needed to provide sufficient cover and properly convey stormwater through the pipe without creating low spots that could hold water",
    
    "BB-0034": "Label all downspout locations and indicate type of outfall protection for each. If pipes (french drains) are used, indicate type of outlet protection proposed for each such as river rock, concrete apron, or pop-ups.",
    
    "BB-0035": "Label all buffers and provide note that the buffers must be protected with no disturbance during construction.",
    
    "BB-0036": "Label top and bottom of all retaining walls. Provide retaining wall detail. All walls 4-feet and higher are required to be designed and inspected by a TN licensed PE and a separate retaining wall permit is required. All walls with 30-inches or more in grade difference require a code compliant barrier.",
    
    "BB-0037": "Show locations of downspouts for proposed home. For unconnected downspouts indicate each having proper splash guards. For downspouts connected to underground \"french\" drains, detail pipe information and provide proper outlet protection (river rock apron, concrete apron, or pop-ups)",
    
    "BB-0038": "Provide check dams or equivalent measures with proper spacing along swales and in areas of concentrated stormwater flow (TYP)",
    
    "BB-0039": "Provide a tree survey of the lot showing location, diameter, and species of all trees on site to be removed and trees to remain. For all trees to remain, provide adequate tree protection fencing located at 1.5 times the radius of the drip line.",
    
    "BB-0040": "Provide tree protection detail showing fence location placed at 1.5 times the dripline radius of each tree.",
    
    "BB-0041": """Provide the following general notes on the plans:
• Builder to call Brentwood Engineering Department for initial erosion control inspection (615-371-0080) prior to issuance of a permit.
• All retaining walls greater than 4-ft will be designed and inspected by a licensed professional engineer and certified in writing prior to issuance of a Certificate of Occupancy
• A Temporary Certificate of Occupancy will not be given for grading and drainage related issues.
• All retaining walls with height in excess of 30-in require safety rail or barrier as per Brentwood code.
• The maximum grade of any portion of a driveway shall not exceed 20% for paved surfaces and 10% for unpaved surfaces, with a maximum cross slope of 5%
• All driveways with 15% or greater longitudinal slopes and/or 5% or greater cross-slopes shall be profiled and sectioned by a TN R.L.S. and approved by the City Engineer prior to issuance of a certificate of occupancy.""",
    
    "BB-0042": "Provide swale detail on plans showing minimum 1-ft deep with 3:1 side slopes for all swales. Minimum width of swale should be 6 feet wide.",
    
    "BB-0043": "All proposed drainage swales shown on site must be a minimum of 1 foot depth and 6 feet wide with max side slopes of 3:1. As shown, swales do not meet this condition. If alternate swale designs are desired, provide supporting stormwater calculations for all proposed swales.",
    
    "BB-0044": "For swale slopes greater than 3%, it is suggested to provide permanent check dams, level spreader, or equivalent to prevent erosion and promote infiltration.",
    
    "BB-0045": "Please resubmit to kevin.blackburn@brentwoodtn.gov and upload documents to ON LAMA once revised site plan is completed.",
    
    "BB-0046": "Prior to issuing grading permit, applicant must provide confirmation that notification has been provided to adjacent land owner explaining disturbance within the PUDE and that no disturbance will extend beyond the PUDE on their property.",
    
    "BB-0047": "Provide paver detail for pool deck. If designed for infiltration, soil testing of native soil under paver gravel is required to infiltrate at 0.5 inches per hour. If an underdrain system is proposed, show drainage pipe network and provide proper outlet protection for all pipes.",
    
    "BB-0048": "Post Planning Commission Approval submit final construction documents to Engineering Department for review and approval of a Grading Permit.",
    
    "BB-0049": "Provide signatures and dates for the acknowledgement form and other areas of the plans reserved for signatures that are blank.",
    
    "BB-0050": "Since the total additional impervious surface is less than 800 square feet, a grading plan is not required. However, the proposed construction shall be required to comply with the erosion control requirements set forth in subsection 56-13(3) of the Brentwood City Code. If total additional impervious exceeds 800 square feet, additional plans and reviews will be required in accordance with Brentwood Code.",
    
    "BB-0051": "Clearly display existing and proposed contours on the grading plans. As shown, it is difficult to determine the proposed grading.",
    
    "BB-0052": "Per City Code, driveways and parking areas and structures shall be located a minimum of five feet away from any adjoining property line.",
    
    "BB-0053": "Pending approval of application, further engineering review will be required prior to issuance of required permits.",
    
    "BB-0054": "There are concerns with providing construction access over existing curb and gutter, grass strip, and sidewalk. Provide a note on the plans stating that the curb and gutter, sidewalk and grass strip shall be protected during construction. Also provide a note stating the contractor is responsible for any and all repairs to damages within the right-of-way and will be inspected by the City prior to issuance of a certificate of occupancy.",
    
    "BB-0055": "Indicate on plans the proposed permanent stabilization methods of all disturbed areas. If different stabilization methods are proposed for steeper slopes, indicate or shade these areas on the plans to discern the difference in stabilization method proposed.",
    
    "BB-0056": "This plan was reviewed assuming all proposed items and site work will be completed as shown. Separate permits are required for the pool, retaining walls, fence, and pool house and include all requirements from the BOZA review. Should any proposed item on this plan be adjusted or removed, a new overall grading plan will be necessary for review to ensure all proposed modifications are properly planned and coordinated.",
    
    "BB-0057": "A 30-ft driveway apron is required in front of the garage. If 30-ft cannot be provided, a minimum of 24-ft apron can be provided if a 10-ft wide by 12-ft long dovetail is provided as a turnaround.",
    
    "BB-0058": "The total amount of additional impervious surface proposed for the lot exceeds 800 square feet which by Code is defined as a substantial rebuild and requires a grading permit based on conditions stated under Section 56-12 (3). Provide a complete plan set in compliance with all elements of the Land Disturbance Plan provided in the City of Brentwood Zoning Code Chapter 56, Article 1, Subdivision 1, Sec. 56-13. - Land disturbance plan. Below is a link to the code section: https://library.municode.com/tn/brentwood/codes/code_of_ordinances?nodeId=PTIICOOR_CH56STMAERCOFLDAPR_ARTISTMAERCO_SDIGRPE_S56-13LADIPL",
    
    "BB-0059": "Label adjacent lots with parcel data on plans.",
    
    "BB-0060": "Show dumpster location on plans and ensure it is placed in an accessible route by transport.",
    
    "BB-0061": "Provide retaining wall detail on the plans.",
    
    "BB-0062": "Provide silt fence detail on the plans.",
    
    "BB-0063": "As built required prior to final due to proximity to setbacks.",
    
    "BB-0064": "Provide construction track out measures. This can be done with a FODS mat (or equivalent), gravel pads using ASTM #1 stone (standard construction entrance 12' wide x 30' long), wheel wash station, or shaker racks.",
    
    "BB-0065": "Label all trees on site to be removed and those to be saved. For trees to be saved within 50 feet of limits of disturbance, provide tree protection fencing.",
    
    "BB-0066": """Provide the following on the plans:
- Building coverage calculations (Max 25%)
- Green space coverage calculations (Min 40%)
- Basement coverage calculations (Percentage of perimeter covered by adjacent turf above 1/2 of basement height. Min. = 50%.) Coverage to be calculated as follows: Linear Feet of basement perimeter covered / Linear Feet of total perimeter of basement, shown in percentage. Walls interior of building footprint considered covered.""",
    
    "BB-0067": "State the design storm for the culvert calculation. The design year the culvert must pass is the 10 year but the 100 year also must be checked to ensure no structures surrounding the area are impacted. Please update calcs to show this.",
    
    "BB-0068": "Show sewer stub-out on plans (check FFE vs invert; if grinder pump, show pump location and service line alignment to main).",
    
    "BB-0069": "Show dumpster and concrete washout on EPSC plan and ensure both are accessible by transport. Provide concrete washout detail on the plans as well.",
    
    "BB-0070": "Replace sidewalk detail with the City Standard Detail provided here: https://www.brentwoodtn.gov/home/showpublisheddocument/6937/638011581480270000",
    
    "BB-0071": "Check all grades adjacent to home. Ensure proper slope from home is provided which should be at least 2% for first 10 feet from home. Adjacent grade must be at least 8 inches below FFE. Provide callouts showing these conditions are met.",
    
    "BB-0072": """Provide the following details on the site plan:
- Silt fence or other appropriate erosion control BMPs (e.g., check dams – TDEC-approved details)
- Temporary construction entrance: ASTM #1 stone with filter fabric underneath. Minimum dimensions: 12' W x 30' L (acceptable for single lot)
- Tree protection: 1.5 times larger than the drip line
- Retaining wall (if applicable) stamped by a P.E.
- Driveway ramp
- Typical drainage swale
- Underground drainage infrastructure
- Others as necessary""",
    
    "BB-0073": "Provide calculated design flow rate of ditch along roadway on plans. If 10 year flow exceeds 5 CFS energy dissipaters are required to be added to the headwall. A toe is required to be added to headwall if flow is in excess of 10 CFS.",
    
    "BB-0074": "Provide a note on the plans stating that open space shall be protected without disturbance during construction.",
    
    "BB-0075": "Provide spot elevations around the home on the plans. The spot elevations should show proper slope away from the structures proposed with a minimum 2% slope for the first 10 feet away from home. All adjacent grades must be at least 8 inches below the FFE of all structures.",
    
    "BB-0076": """Show proposed code compliant pool fence on the plans.
Proposed fence to comply with Williamson County Swimming pool fence specification:
• Min 4' high
• Bottom of fence to be no more than 4" from ground
• Openings in fence shall not permit the passage of a 4" sphere
• Fence to encompass the pool area to prevent unauthorized entry""",
    
    "BB-0077": "Per Brentwood Code Section 56-31, Show and label water quality riparian buffer on the plan set. Identify the boundary and note it as a buffer that shall be protected. Provide a note on the plans stating the following \"There shall be no clearing, grading, construction or disturbance of vegetation within the water quality riparian buffer, except as permitted by the City of Brentwood\". The buffer shall be staked and labeled as part of a construction layout survey prior to commencement of construction, using a combination of stakes and flagging to ensure adequate visibility.",
    
    "BB-0078": "Add note: An as-built survey will be required prior to footing inspection due to proximity of building to setbacks to confirm building is within the revised plat setbacks.",
    
    "BB-0079": "On the plans, please label the proposed permanent stabilization method for all disturbed areas and denote where additional measures are needed such as staked sod or erosion control matting for swales, steep slopes, or areas with concentrated flow.",
    
    "BB-0080": "Stormwater report is sufficient for preliminary plan approval only. Approval of the grading permit will require additional analysis of the proposed drainage system on site per City Subdivision Regulations Article 6.",
    
    "BB-0081": "Geotechnical report is sufficient for preliminary plan approval only. Approval of the grading permit will require additional analysis of the proposed roadway and individual proposed structures on each lot. Details of the required report will be verified by applicant with City Staff prior to grading permit submittal.",
    
    "BB-0082": "The contractor is responsible to provide positive drainage within the right-of-way. Proposed contours spot elevations are required on the plans to clearly show how drainage is being properly conveyed within the right-of-way.",
    
    "BB-0083": "Per City Code a recent/current field run survey with topography, 2-ft contours, and actual elevations based on a benchmark is required. Survey provided is dated nearly 10 years ago. At a minimum, provide a new survey of the area of the new addition and at least 50 feet in all directions to ensure conditions shown on the site plan match with the older survey provided. If the conditions do not match at the 50 foot distance, additional survey is required either until the new and old surveys match or the survey extends to all property lines.",
    
    "BB-0084": """Designate the lot as a Transitional Lot and also a Hillside Protection Lot on the plans. Use an asterisk " * " for transitional lot and "HP" to identify the lot on the plat within the property boundaries. Also provide the following note on the plat and reference to the note from the asterisk and HP designation on the lot:

This lot contains slopes greater than 15% and is considered a Transitional Lot. Prior to issuance of a building permit, a site plan prepared by a licensed professional engineer shall be submitted and approved by the City Engineer in accordance with the City's Transitional Lot requirements. No tree clearing or grading is permitted until the site plan is approved. This lot is also a Hillside Protection lot and must also comply with the Hillside Protection standards outlined in Chapter 78, Article III, Division 14 of the Brentwood Municipal Code.""",
    
    "BB-0085": "This is a transitional lot and therefore the plans must address all items on the transitional lot checklist. Revise plans and submit a completed transitional lot checklist with resubmittal. The transitional lot checklist can be found at the following link: https://www.brentwoodtn.gov/files/assets/city/v/1/engineering/jc-files/transitional-lot-checklist-071224.pdf",
    
    "BB-0086": "This is a transitional lot and therefore a completed and signed transitional lot checklist is required with resubmittal. The transitional lot checklist can be found at the following link: https://www.brentwoodtn.gov/files/assets/city/v/1/engineering/jc-files/transitional-lot-checklist-071224.pdf",
    
    "BB-0087": "Provide completed transitional lot checklist and provide signature. The transitional lot checklist can be found at the following link: https://www.brentwoodtn.gov/files/assets/city/v/1/engineering/jc-files/transitional-lot-checklist-071224.pdf",
    
    "BB-0088": "Post Planning Commission Approval submit final construction documents to Engineering Department for review. Further engineering review will be required prior to issuance of required permits.",
    
    "BB-0089": "For all swales with long slope lengths and grades exceeding 5%, sod alone is not considered sufficient for permanent stabilization under TDEC and City of Brentwood standards. Please provide additional permanent stabilization measures such as turf reinforcement matting, erosion control blankets, check dams, staked sod, or other approved methods in these areas to control erosion both during and after construction. The specific locations and types of stabilization should be selected based on the swale design and documented flow calculations, demonstrating that the measures are adequate for the site's expected velocities and slope conditions",
    
    "BB-0090": "Clearly designate and outline the pool construction work areas and areas of disturbance, making sure they are distinguished from the overall site work and home construction. Include a note on the plan that specifies exactly which portions of the project the pool contractor is responsible for. As currently presented, the plan incorrectly suggests that the pool contractor is also responsible for lot grading, retaining walls, the driveway, and other unrelated site work. The plan must clearly show and label the pool contractor's limits of work and scope of responsibility.",
    
    "BB-0091": """Provide the following note in the notes section of the plat.
IN ACCORDANCE WITH THE REQUIREMENTS OF SECTION 78-14 OF THE MUNICIPAL CODE, LOTS DESIGNATED WITH (*) HAVE NATURAL SLOPES OF GREATER THAN 15%. PRIOR TO THE ISSUANCE OF A BUILDING PERMIT FOR A RESIDENTIAL LOT WITH A SLOPE OF 15% OR GREATER, A PLAN SHALL BE PREPARED BY A LICENSED PROFESSIONAL ENGINEER FOR APPROVAL BY THE CITY ENGINEER SHOWING EXISTING TOPOGRAPHIC INFORMATION FROM FIELD RUN SURVEY DATA, BOUNDARY AND SETBACK LINES, UTILITY AND DRAINAGE EASEMENTS, EXISTING AND PROPOSED DRAINAGE PIPES, DITCHES AND SWALES TO BE CONNECTED TO PUBLIC DRAINAGE LINES AND/OR TO DIRECT OR RE-DIRECT STORMWATER RUNOFF, THE PROPOSED BUILDING FOOTPRINT AND THE DRIVEWAY PLAN, INCLUDING THE FINISHED FLOOR ELEVATIONS AND FINISHED GRADES OF PAVEMENTS AND GROUND LINES, IDENTIFICATION OF EXISTING TREES IN EXCESS OF FOUR-INCH CALIPER AND TREES TO BE PRESERVED, AND THE LOCATION AND TIMING OF INSTALLATION OF EROSION CONTROL FEATURES. NO CLEAR CUTTING OF TREES OR GRADING OF THE LOT SHALL BE PERMITTED UNTIL APPROVAL OF THE SITE PLAN BY THE CITY ENGINEER.""",
    
    "BB-0092": "Provide driveway ramp detail on the plans. Use City Standard driveway ramp detail or equivalent. City standard detail is provided here: https://www.brentwoodtn.gov/files/assets/city/v/1/engineering/jc-files/cob-std-dwg5.pdf",
    
    "BB-0093": """Through discussions with Floodplain Administrator in Planning, the following steps are required prior to pool permit:
- Submit for a grading permit showing the proposed grading needed for the pool and other site work showing the compensatory cut as shown and the location of the revised BFE line outside the improvement locations.
- Submit an as-built survey from a TN licensed surveyor showing the grading matches the proposed plan and shows the BFE line which will serve as the revised setback line on the lot.
- Submit a revised final plat to Brentwood Planning Commission showing the revised setback line based on the graded area and revised BFE contour line.
- Submit this revised pool permit for review once the final plat is recorded (this is because the pool and pool deck cannot be located outside the building setbacks which based on the current plat is shown right up to the back of the existing home).""",
    
    "BB-0094": "Adjust driveway to terminate at least 3 feet from any curb inlet. As shown, driveway impacts the drainage inlet.",
    
    "BB-0095": "Provide and label a limits of disturbance line on the plans to clearly show the proposed work area.",
    
    "BB-0096": """By City Code, the proposed project qualifies as a substantial rebuild and requires a grading permit based on conditions stated under Section 56-12 (3). This includes the requirement that the plans be signed and sealed by a TN licensed Landscape Architect or Professional Engineer.

Provide a complete plan set in compliance with all elements of the Land Disturbance Plan provided in the City of Brentwood Zoning Code Chapter 56, Article 1, Subdivision 1, Sec. 56-13. - Land disturbance plan. Below is a link to the code section: https://library.municode.com/tn/brentwood/codes/code_of_ordinances?nodeId=PTIICOOR_CH56STMAERCOFLDAPR_ARTISTMAERCO_SDIGRPE_S56-13LADIPL

Once a Code-compliant submittal is provided, further review will commence.""",
    
    "BB-0097": "Plan shows grading for entire lot and home. For the pool permit, only show proposed grading needed for the pool. Show grading and work for the home and other lot improvements already complete as existing grade and existing structure.",
    
    "BB-0098": "Show limits of disturbance needed to only do the work associated with this permit. As shown, the entire lot is within the limits. The plan needs to clearly show the limits of disturbance and area the pool contractor is responsible for.",
    
    "BB-0099": """The following steps are required prior to pool permit:
- Submit for a grading permit showing the proposed grading needed for the pool and other site work showing the compensatory cut as shown and the location of the revised BFE line outside the improvement locations.
- Submit an as-built survey from a TN licensed surveyor showing the grading matches the proposed plan and shows the BFE line which will serve as the revised setback line on the lot.
- Submit a revised final plat to Brentwood Planning Commission showing the revised setback line based on the graded area and revised BFE contour line.
- Submit this revised pool permit for review once the final plat is recorded (this is because the pool and pool deck cannot be located outside the building setbacks which based on the current plat is shown right up to the back of the existing home).""",
    
    "BB-0100": """The following steps are required prior to signing the final plat:
- Based on notes on the submittal, grading is proposed on the site. Submit for and obtain a grading permit from the City showing the proposed grading needed to adjust to the proposed BFE for the lot as shown. The grading plan must show and provide calculations of any fill and required compensatory cut within the floodplain.
- Submit an as-built survey from a TN licensed surveyor showing the grading matches the proposed plan and shows the BFE line which will also serve as the revised setback line on the lot.
- Should the as-built survey after site grading differ from the submitted plat, a revised final plat will be required to be submitted to Brentwood Planning Commission showing the revised setback line based on the graded area and revised BFE contour line.""",
    
    "BB-0101": "Add note: All designated Stormwater Management facilities to be maintained in accordance with the recorded Stormwater Management Agreement BK____ , PG ____ by Home Owner's Association (HOA).",
    
    "BB-0102": "If retaining wall is over 60 inches, it has to be a rail barrier. For under 60 inches, provide plant species, spacing and height.",

    # =========================================================================
    # NEW COMMENTS (BB-0103 through BB-0123)
    # =========================================================================
    
    "BB-0103": "Provide name and phone number of the builder and owner (if other than builder) on the plan.",
    
    "BB-0104": "Provide email address for design engineer or landscape architect on the plan or submit to City Engineer.",
    
    "BB-0105": "Building footprint shown on site plan does not match the house plans. Revise to match.",
    
    "BB-0106": "Limit plans to one page if possible, two pages maximum.",
    
    "BB-0107": "Use standard engineering scale of 1:20. Other scales acceptable for unique sites with blow-ups on second page if necessary.",
    
    "BB-0108": "Provide vicinity map with legible street names.",
    
    "BB-0109": "Include subdivision name, lot number, and zoning in title block and label in plan view.",
    
    "BB-0110": "Label all streets and show right-of-way width on plans.",
    
    "BB-0111": "Include recorded plat book and page number in title block.",
    
    "BB-0112": "Property lines with bearings and distances do not match recorded plat. Explain any differences.",
    
    "BB-0113": "Show all easements labeled and dimensioned on plans.",
    
    "BB-0114": "Show all public utilities labeled and dimensioned on plans.",
    
    "BB-0115": "Label driveway width on plans. Maximum 20', minimum 10' (12' if over 500' long).",
    
    "BB-0116": "Provide 6-inch rise in driveway from edge of pavement to right-of-way.",
    
    "BB-0117": "Minimum inside turning radius for driveway curves = 20 feet. Minimum overhead clearance = 14 feet.",
    
    "BB-0118": "Grade break from drive entrance to driveway must be passable for typical car.",
    
    "BB-0119": "Show HVAC pad location on plans.",
    
    "BB-0120": "Show water meter location on plans.",
    
    "BB-0121": "Add note: Prior to issuance of Certificate of Occupancy, this residential lot shall have a minimum of 25 caliper inches of trees per acre.",
    
    "BB-0122": """City Code Section 78-10 (8)
Prohibited areas:
a. Public right-of-way. Fences shall be prohibited on any street or public right-of-way. In addition, any fence constructed or erected after June 1, 2005 must be placed a minimum of three feet away from any public sidewalk or bikeway.
b. Easements. No fence may be placed within any section of a recorded public utility, drainage or detention pond easement, unless authorized in writing by the city engineer, in accordance with section 58-6 of this Code, as the same may be amended or replaced.
c. Sight distance limitations. No fence shall be placed on private property near an intersection and/or driveway entrance in a manner that creates a visual obstruction or safety hazard for vehicular traffic and pedestrians.""",
    
    "BB-0123": """Any acceptance of a fence encroachment comes with the following conditions:
• It is the property owner's or fence contractor's responsibility to locate property lines and utilities prior to fence installation and to ensure the fence is installed per the approved plan and any other conditions mentioned above or herein.
• City approval does not constitute, supersede, or replace HOA approval, if required.
• This approval of a fence to be installed in a P.U.D.E. does not relieve the current or future property owner from the responsibility and cost of having to remove or replace the fence in the future, if the City of Brentwood or any other utility owner were to need full access to any of the P.U.D.E. for routine maintenance or utility relocation.
• A fence cannot encompass or encumber a common lot drainage swale.
• If this location is out of the service limits of Brentwood Water Department, the Owner is responsible for contacting Metro Water Services for location of any possible underground sewer locations, and Nolensville/College Grove for location of any possible underground water lines within the affected PUDE's.""",
}


def get_comment(comment_id):
    """Get a single comment by ID"""
    return COMMENTS.get(comment_id, f"Comment {comment_id} not found")


def get_comments(comment_ids):
    """Get multiple comments by their IDs"""
    return {cid: COMMENTS.get(cid, f"Comment {cid} not found") for cid in comment_ids}


def get_all_comments():
    """Get all comments"""
    return COMMENTS.copy()


def search_comments(search_term):
    """Search comments containing a term"""
    search_term = search_term.lower()
    results = {}
    for cid, text in COMMENTS.items():
        if search_term in text.lower():
            results[cid] = text
    return results
