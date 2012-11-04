# ---------------------------------------------------------------------------
# build_b2_ne_50m_admin_0_units.py
# Created on: Sun Nov 04 2012 03:08:26 AM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
ne_50m_admin_0_map_units_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_units_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_subunits_test_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_subunits_test_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_subunits_test_shp__5_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_units_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_subunits_test_shp__7_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_admin_0_details_level_3_map_units_dbf = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\ne_admin_0_details_level_3_map_units.dbf"
ne_50m_admin_0_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_scale_rank.shp"
Output_Feature_Class = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"
ne_10m_admin_0_map_units_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_2d0d0_rc4\\50m_cultural\\ne_50m_admin_0_map_units.shp"

# Process: Dissolve...
gp.Dissolve_management(ne_50m_admin_0_scale_rank_shp, ne_50m_admin_0_map_units_shp, "sr_gu_a3", "scalerank MIN", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Field (2)...
gp.AddField_management(ne_50m_admin_0_map_units_shp, "scalerank", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__4_, "scalerank", "[MIN_scaler]", "VB", "")

# Process: Add Field...
gp.AddField_management(ne_10m_admin_0_map_subunits_test_shp__5_, "featurecla", "TEXT", "", "", "30", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__3_, "featurecla", "\"Admin-0 map unit\"", "VB", "")

# Process: Delete Field...
gp.DeleteField_management(ne_10m_admin_0_map_units_shp__2_, "MIN_scaler")

# Process: Repair Geometry...
gp.RepairGeometry_management(ne_10m_admin_0_map_subunits_test_shp__7_, "DELETE_NULL")

# Process: Join Field...
gp.JoinField_management(Output_Feature_Class, "sr_gu_a3", ne_admin_0_details_level_3_map_units_dbf, "SU_A3", "")

# Process: Delete Field (2)...
gp.DeleteField_management(ne_10m_admin_0_map_units_shp__4_, "sr_gu_a3;MIN_scaler")

