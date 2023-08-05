## *************************************************************
## Licensed to the Apache Software Foundation (ASF) under one
## or more contributor license agreements.  See the NOTICE file
## distributed with this work for additional information
## regarding copyright ownership.  The ASF licenses this file
## to you under the Apache License, Version 2.0 (the
## "License"); you may not use this file except in compliance
## with the License.  You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing,
## software distributed under the License is distributed on an
## "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
## KIND, either express or implied.  See the License for the
## specific language governing permissions and limitations
## under the License.
## *************************************************************

## Author: Michael Nolde
## URL: http://www.flatpolar.org
## 2017/06

from osgeo import gdal, ogr, osr
import sys
import os
import math
import numpy
import logging
from scipy.spatial import Delaunay
import argparse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class ElevationMesh(object):
    
    def __init__(self):
        gdal.UseExceptions()
        pass


    def generate_mesh(self, dem, ortho, bound, dem_nodata=-9999, ortho_nodata=-9999, stepwidth=360, mesh_prefix='out', mesh_path='.', out_shape=False):
        
        
        in_dem_filename = dem
        in_ortho_filename = ortho
        in_boundaries_filename = bound
        in_dem_nodata_ext=dem_nodata
        in_ortho_nodata_ext=ortho_nodata
        out_mesh_filename_prefix=mesh_prefix
        out_mesh_path=mesh_path
        
        
        # this allows GDAL to throw Python Exceptions
        gdal.UseExceptions()
        
        
        out_triangles_filename_prefix = out_mesh_filename_prefix
        out_triangles_path = out_mesh_path
        
        indexed_colors = True
        coloring_mode = 'ortho'
        in_dem_format = 'tif'
        in_ortho_format = 'tif'
        
        
        
        
        in_dem = gdal.Open(in_dem_filename)
        in_ortho = gdal.Open(in_ortho_filename)
        
        
        for lon_min in range(-180, 180, stepwidth):
            for lat_min in range(-90, 90, stepwidth):
        
                #if lon_min == -95 and lat_min == 10:
                
                x_min_str = str(abs(int(lon_min)))
                y_min_str = str(abs(int(lat_min)))
        
        
                if len(x_min_str) == 1:
                    x_min_str = '00'+ x_min_str
                if len(x_min_str) == 2:
                    x_min_str = '0'+ x_min_str
        
                if len(y_min_str) == 1:
                    y_min_str = '00'+ y_min_str
                if len(y_min_str) == 2:
                    y_min_str = '0'+ y_min_str
        
        
                if lon_min < 0:
                    x_min_str = 'e'+ x_min_str
                else:
                    x_min_str = 'w'+ x_min_str
        
                if lat_min < 0:
                    y_min_str = 's'+ y_min_str
                else:
                    y_min_str = 'n'+ y_min_str
        
        
        
                if stepwidth < 360:
                    out_triangles_filename = os.path.join(out_triangles_path, out_triangles_filename_prefix + '_' + x_min_str + '_' + y_min_str + '.shp')
                    out_mesh_filename = os.path.join(out_mesh_path, out_mesh_filename_prefix + '_' + x_min_str + '_' + y_min_str + '.x3d')
                else:
                    out_triangles_filename = os.path.join(out_triangles_path, out_triangles_filename_prefix + '.shp')
                    out_mesh_filename = os.path.join(out_mesh_path, out_mesh_filename_prefix + '.x3d')
        
        
        
                
                ## Calculate triangles from boundary and DEM and write them into a Shape-File
                ## Open input boundaries layer
                in_boundaries_driver = ogr.GetDriverByName("ESRI Shapefile")
                in_boundaries = in_boundaries_driver.Open(in_boundaries_filename, 0)
                in_boundaries_layer = in_boundaries.GetLayer()
                in_boundaries_x_min, in_boundaries_x_max, in_boundaries_y_min, in_boundaries_y_max = in_boundaries_layer.GetExtent()
                in_boundaries_spatialref = in_boundaries_layer.GetSpatialRef()
        
        
                
                ## Open output vector shape
                out_triangles_driver = ogr.GetDriverByName("ESRI Shapefile")
                
                if os.path.exists(out_triangles_filename):
                    out_triangles_driver.DeleteDataSource(out_triangles_filename)
                
                out_triangles = out_triangles_driver.CreateDataSource(out_triangles_filename)
                #out_triangles_spatialref = ogr.osr.SpatialReference()
                out_triangles_spatialref = in_boundaries_spatialref
                
                out_triangles_field_a_x = ogr.FieldDefn("A_X", ogr.OFTReal)
                out_triangles_field_a_y = ogr.FieldDefn("A_Y", ogr.OFTReal)
                out_triangles_field_a_z = ogr.FieldDefn("A_Z", ogr.OFTReal)
                out_triangles_field_a_red = ogr.FieldDefn("A_RED", ogr.OFTReal)
                out_triangles_field_a_green = ogr.FieldDefn("A_GREEN", ogr.OFTReal)
                out_triangles_field_a_blue = ogr.FieldDefn("A_BLUE", ogr.OFTReal)
                out_triangles_field_a_alpha = ogr.FieldDefn("A_ALPHA", ogr.OFTReal)
                out_triangles_field_b_x = ogr.FieldDefn("B_X", ogr.OFTReal)
                out_triangles_field_b_y = ogr.FieldDefn("B_Y", ogr.OFTReal)
                out_triangles_field_b_z = ogr.FieldDefn("B_Z", ogr.OFTReal)
                out_triangles_field_b_red = ogr.FieldDefn("B_RED", ogr.OFTReal)
                out_triangles_field_b_green = ogr.FieldDefn("B_GREEN", ogr.OFTReal)
                out_triangles_field_b_blue = ogr.FieldDefn("B_BLUE", ogr.OFTReal)
                out_triangles_field_b_alpha = ogr.FieldDefn("B_ALPHA", ogr.OFTReal)
                out_triangles_field_c_x = ogr.FieldDefn("C_X", ogr.OFTReal)
                out_triangles_field_c_y = ogr.FieldDefn("C_Y", ogr.OFTReal)
                out_triangles_field_c_z = ogr.FieldDefn("C_Z", ogr.OFTReal)
                out_triangles_field_c_red = ogr.FieldDefn("C_RED", ogr.OFTReal)
                out_triangles_field_c_green = ogr.FieldDefn("C_GREEN", ogr.OFTReal)
                out_triangles_field_c_blue = ogr.FieldDefn("C_BLUE", ogr.OFTReal)
                out_triangles_field_c_alpha = ogr.FieldDefn("C_ALPHA", ogr.OFTReal)
                
                out_triangles_layer = out_triangles.CreateLayer('triangles', out_triangles_spatialref, geom_type=ogr.wkbPolygon)
                out_triangles_layer.CreateField(out_triangles_field_a_x)
                out_triangles_layer.CreateField(out_triangles_field_a_y)
                out_triangles_layer.CreateField(out_triangles_field_a_z)
                out_triangles_layer.CreateField(out_triangles_field_a_red)
                out_triangles_layer.CreateField(out_triangles_field_a_green)
                out_triangles_layer.CreateField(out_triangles_field_a_blue)
                out_triangles_layer.CreateField(out_triangles_field_a_alpha)
                out_triangles_layer.CreateField(out_triangles_field_b_x)
                out_triangles_layer.CreateField(out_triangles_field_b_y)
                out_triangles_layer.CreateField(out_triangles_field_b_z)
                out_triangles_layer.CreateField(out_triangles_field_b_red)
                out_triangles_layer.CreateField(out_triangles_field_b_green)
                out_triangles_layer.CreateField(out_triangles_field_b_blue)
                out_triangles_layer.CreateField(out_triangles_field_b_alpha)
                out_triangles_layer.CreateField(out_triangles_field_c_x)
                out_triangles_layer.CreateField(out_triangles_field_c_y)
                out_triangles_layer.CreateField(out_triangles_field_c_z)
                out_triangles_layer.CreateField(out_triangles_field_c_red)
                out_triangles_layer.CreateField(out_triangles_field_c_green)
                out_triangles_layer.CreateField(out_triangles_field_c_blue)
                out_triangles_layer.CreateField(out_triangles_field_c_alpha)
                
            
                    
                in_tile_ring = ogr.Geometry(ogr.wkbLinearRing)
                in_tile_ring.AddPoint(lon_min, lat_min)
                in_tile_ring.AddPoint(lon_min + stepwidth, lat_min)
                in_tile_ring.AddPoint(lon_min + stepwidth, lat_min + stepwidth)
                in_tile_ring.AddPoint(lon_min, lat_min + stepwidth)
                in_tile_ring.AddPoint(lon_min, lat_min)
                in_tile_bbox = ogr.Geometry(ogr.wkbPolygon)
                in_tile_bbox.AddGeometry(in_tile_ring)
        
        
                for in_boundaries_feat in in_boundaries_layer:
        
                    in_boundaries_geom = in_boundaries_feat.GetGeometryRef()
                    in_boundaries_geomtype = in_boundaries_geom.GetGeometryName()
        
                    in_geometry = in_tile_bbox.Intersection(in_boundaries_geom)
                    in_geometry_feature_defn = in_boundaries_layer.GetLayerDefn()
                                      
                    if in_geometry != None and str(in_geometry).upper() != 'GEOMETRYCOLLECTION EMPTY':
                        self.ogr_to_elevation_mesh(in_dem, in_ortho, in_geometry, in_boundaries_spatialref, in_geometry_feature_defn, in_dem_nodata_ext, in_ortho_nodata_ext, out_triangles_layer)
                        
                      
        
                out_triangles.Destroy()                    
                in_boundaries.Destroy()
        
                in_triangles_driver = ogr.GetDriverByName("ESRI Shapefile")
                in_triangles = in_triangles_driver.Open(out_triangles_filename, 0)
                in_triangles_layer = in_triangles.GetLayer()
        
                if in_triangles_layer.GetFeatureCount() > 0:
                    self.conv_triangle_shape_to_x3d(in_triangles_layer, out_mesh_filename, indexed_colors)
        
                in_triangles.Destroy()
        
                if out_shape == False:
                    ## Delete temporary shapefile (triangles)
                    if os.path.exists(out_triangles_filename):
                        in_triangles_driver.DeleteDataSource(out_triangles_filename)
                
        
        




    def parse_polygon(self, in_boundary_polygon, in_dem, in_ortho, out_triangles_layer, out_triangles_layer_feature_defn, in_dem_nodata_ext, in_ortho_nodata_ext, in_dem_res_x, in_dem_res_y, in_dem_extent_x_min, in_dem_extent_x_max, in_dem_extent_y_min, in_dem_extent_y_max, in_dem_cols, in_dem_rows,
            in_ortho_extent_x_min, in_ortho_extent_x_max, in_ortho_extent_y_min, in_ortho_extent_y_max, in_ortho_res_x, in_ortho_res_y, in_ortho_cols, in_ortho_rows, coloring_mode):



        triangle_cnt=0
        triangle_failed_cnt=0
        geom_linearring_cnt=0
        geom_polygon_cnt=0
        geom_multipolygon_cnt=0

        in_dem_clip_val_min = 0
        in_dem_clip_val_max = 8000
        

        in_boundary_polygon_geom_type = in_boundary_polygon.GetGeometryName()
        #logger.info("in_boundary_polygon_geom_type=%s", in_boundary_polygon_geom_type)
    
        (in_dem_clip_x_min, in_dem_clip_x_max, in_dem_clip_y_min, in_dem_clip_y_max) = in_boundary_polygon.GetEnvelope()
        (in_ortho_clip_x_min, in_ortho_clip_x_max, in_ortho_clip_y_min, in_ortho_clip_y_max) = in_boundary_polygon.GetEnvelope()
    
        # clip one cell/row more than needed
        in_dem_clip_x_min-=in_dem_res_x
        in_dem_clip_x_max+=in_dem_res_x
        in_dem_clip_y_min-=in_dem_res_y
        in_dem_clip_y_max+=in_dem_res_y
    
        in_ortho_clip_x_min-=in_dem_res_x
        in_ortho_clip_x_max+=in_dem_res_x
        in_ortho_clip_y_min-=in_dem_res_y
        in_ortho_clip_y_max+=in_dem_res_y
    
        ## get the cols and rows corresponding to the clip area
        in_dem_clip_col_min = int(math.floor((in_dem_clip_x_min - in_dem_extent_x_min) / in_dem_res_x))
        in_dem_clip_col_max = int(math.ceil((in_dem_clip_x_max - in_dem_extent_x_min) / in_dem_res_x))
        in_dem_clip_row_min = int(math.floor((in_dem_extent_y_max - in_dem_clip_y_max) / in_dem_res_y))
        in_dem_clip_row_max = int(math.ceil((in_dem_extent_y_max - in_dem_clip_y_min) / in_dem_res_y))

    
        in_ortho_clip_col_min = int(math.floor((in_ortho_clip_x_min - in_ortho_extent_x_min) / in_ortho_res_x))
        in_ortho_clip_col_max = int(math.ceil((in_ortho_clip_x_max - in_ortho_extent_x_min) / in_ortho_res_x))
        in_ortho_clip_row_min = int(math.floor((in_ortho_extent_y_max - in_ortho_clip_y_max) / in_ortho_res_y))
        in_ortho_clip_row_max = int(math.ceil((in_ortho_extent_y_max - in_ortho_clip_y_min) / in_ortho_res_y))


        if in_dem_clip_col_min < 0:
            in_dem_clip_col_min = 0
        if in_dem_clip_col_max > in_dem_cols:
            in_dem_clip_col_max = in_dem_cols
        if in_dem_clip_row_min < 0:
            in_dem_clip_row_min = 0
        if in_dem_clip_row_max > in_dem_rows:
            in_dem_clip_row_max = in_dem_rows


        if in_ortho_clip_col_min < 0:
            in_ortho_clip_col_min = 0
        if in_ortho_clip_col_max > in_ortho_cols:
            in_ortho_clip_col_max = in_ortho_cols
        if in_ortho_clip_row_min < 0:
            in_ortho_clip_row_min = 0
        if in_ortho_clip_row_max > in_ortho_rows:
            in_ortho_clip_row_max = in_ortho_rows
        

        #logger.info("in_dem_extent_x_min=%s, clip_x_min=%s, clip_col_min=%s", in_dem_extent_x_min, in_dem_clip_x_min, in_dem_clip_col_min)
        #logger.info("in_dem_extent_x_max=%s, clip_x_max=%s, clip_col_max=%s", in_dem_extent_x_max, in_dem_clip_x_max, in_dem_clip_col_max)
        #logger.info("in_dem_extent_y_min=%s, clip_y_min=%s, clip_row_min=%s", in_dem_extent_y_min, in_dem_clip_y_min, in_dem_clip_row_min)
        #logger.info("in_dem_extent_y_max=%s, clip_y_max=%s, clip_row_max=%s", in_dem_extent_y_max, in_dem_clip_y_max, in_dem_clip_row_max)
        
        #logger.info("in_dem_res_x=%s, in_dem_res_y=%s", in_dem_res_x, in_dem_res_x)
    
    
    
        if in_dem != None:

            in_dem_band = in_dem.GetRasterBand(1)
            
            in_dem_nodata = in_dem_nodata_ext
            
            #logger.info("dem_clip_array: %s %s %s %s", in_dem_clip_col_min, in_dem_clip_row_min, \
            #                        in_dem_clip_col_max - in_dem_clip_col_min, \
            #                        in_dem_clip_row_max - in_dem_clip_row_min)
    
            ## write the regarding cols and rows into an array
            in_dem_array_clip = in_dem_band.ReadAsArray(in_dem_clip_col_min, in_dem_clip_row_min, \
                                            in_dem_clip_col_max - in_dem_clip_col_min, \
                                            in_dem_clip_row_max - in_dem_clip_row_min)
            
        else:
            in_dem_array_clip = numpy.zeros((in_dem_clip_row_max - in_dem_clip_row_min,
                                            in_dem_clip_col_max - in_dem_clip_col_min))*0
            in_dem_nodata = in_dem_nodata_ext
    
    
    
    
    
        if in_ortho != None:
            
            in_ortho_band_red = in_ortho.GetRasterBand(1)
            in_ortho_band_green = in_ortho.GetRasterBand(2)
            in_ortho_band_blue = in_ortho.GetRasterBand(3)
            
            in_ortho_nodata = in_ortho_nodata_ext
    
            #logger.info("ortho_clip_array: %s %s %s %s", in_ortho_clip_col_min, in_ortho_clip_row_min, \
            #                        in_ortho_clip_col_max - in_ortho_clip_col_min, \
            #                        in_ortho_clip_row_max - in_ortho_clip_row_min)
    
            in_ortho_array_red_clip = in_ortho_band_red.ReadAsArray(in_ortho_clip_col_min, in_ortho_clip_row_min, \
                                              in_ortho_clip_col_max - in_ortho_clip_col_min, \
                                              in_ortho_clip_row_max - in_ortho_clip_row_min)
            in_ortho_array_green_clip = in_ortho_band_green.ReadAsArray(in_ortho_clip_col_min, in_ortho_clip_row_min, \
                                              in_ortho_clip_col_max - in_ortho_clip_col_min, \
                                              in_ortho_clip_row_max - in_ortho_clip_row_min)
            in_ortho_array_blue_clip = in_ortho_band_blue.ReadAsArray(in_ortho_clip_col_min, in_ortho_clip_row_min, \
                                              in_ortho_clip_col_max - in_ortho_clip_col_min, \
                                              in_ortho_clip_row_max - in_ortho_clip_row_min)
    
    
        else:
    
            in_ortho_array_red_clip = numpy.zeros((in_ortho_clip_row_max - in_ortho_clip_row_min,
                                              in_ortho_clip_col_max - in_ortho_clip_col_min))*0
    
            in_ortho_array_green_clip = numpy.zeros((in_ortho_clip_row_max - in_ortho_clip_row_min,
                                              in_ortho_clip_col_max - in_ortho_clip_col_min))*0
                                              
            in_ortho_array_blue_clip = numpy.ones((in_ortho_clip_row_max - in_ortho_clip_row_min,
                                              in_ortho_clip_col_max - in_ortho_clip_col_min))*127


            in_ortho_nodata = in_ortho_nodata_ext
                                              
    
    
        ## get the actual bounding box coords for the array (differing from the clip coords)
        in_dem_clip_col_min_x = in_dem_extent_x_min + (in_dem_clip_col_min * in_dem_res_x)
        in_dem_clip_col_max_x = in_dem_extent_x_min + (in_dem_clip_col_max * in_dem_res_x)
        in_dem_clip_row_min_y = in_dem_extent_y_max - (in_dem_clip_row_max * in_dem_res_y)
        in_dem_clip_row_max_y = in_dem_extent_y_max - (in_dem_clip_row_min * in_dem_res_y)
    
        in_ortho_clip_col_min_x = in_ortho_extent_x_min + (in_ortho_clip_col_min * in_ortho_res_x)
        in_ortho_clip_col_max_x = in_ortho_extent_x_min + (in_ortho_clip_col_max * in_ortho_res_x)
        in_ortho_clip_row_min_y = in_ortho_extent_y_max - (in_ortho_clip_row_max * in_ortho_res_y)
        in_ortho_clip_row_max_y = in_ortho_extent_y_max - (in_ortho_clip_row_min * in_ortho_res_y)
    
    
    

    
    
    
        ## get center of actual bounding box
        in_dem_clip_col_center_x = in_dem_clip_col_min_x + ((in_dem_clip_col_max_x - in_dem_clip_col_min_x) / 2)
        in_dem_clip_row_center_y = in_dem_clip_row_min_y + ((in_dem_clip_row_max_y - in_dem_clip_row_min_y) / 2)
    



        in_dem_array_rows = in_dem_array_clip.shape[0]
        in_dem_array_cols = in_dem_array_clip.shape[1]
    
    
        for row in range(0, in_dem_array_rows):
    
            for col in range(0, in_dem_array_cols):
                
    
                


                ## in case the current pixel is a nodata pixel, use an average height value
                #if int(round(in_dem_array_clip[row,col],0)) == in_dem_nodata:
                #    in_dem_array_clip[row,col] = -32768
    
    
    
                point_upperleft_x = in_dem_clip_col_min_x + ((col) * in_dem_res_x) + (0.5 * in_dem_res_x)
                point_upperleft_y = in_dem_clip_row_max_y - ((row) * in_dem_res_y) - (0.5 * in_dem_res_y)
                point_upperleft_z = in_dem_array_clip[row,col]
    
    
                if row < in_dem_array_rows-1 and col < in_dem_array_cols-1:
    
                    point_upperright_x = in_dem_clip_col_min_x + ((col+1) * in_dem_res_x) + (0.5 * in_dem_res_x)
                    point_upperright_y = in_dem_clip_row_max_y - ((row) * in_dem_res_y) - (0.5 * in_dem_res_y)
                    point_upperright_z = in_dem_array_clip[row,col+1]
                    point_lowerleft_x = in_dem_clip_col_min_x + ((col) * in_dem_res_x) + (0.5 * in_dem_res_x)
                    point_lowerleft_y = in_dem_clip_row_max_y - ((row+1) * in_dem_res_y) - (0.5 * in_dem_res_y)
                    point_lowerleft_z = in_dem_array_clip[row+1,col]
                    point_lowerright_x = in_dem_clip_col_min_x + ((col+1) * in_dem_res_x) + (0.5 * in_dem_res_x)
                    point_lowerright_y = in_dem_clip_row_max_y - ((row+1) * in_dem_res_y) - (0.5 * in_dem_res_y)
                    point_lowerright_z = in_dem_array_clip[row+1,col+1]
    

                    if int(round(point_upperleft_z,0)) == in_dem_nodata_ext:
                        point_upperleft_z = numpy.nan
                    if int(round(point_upperright_z,0)) == in_dem_nodata_ext:
                        point_upperright_z = numpy.nan
                    if int(round(point_lowerleft_z,0)) == in_dem_nodata_ext:
                        point_lowerleft_z = numpy.nan
                    if int(round(point_lowerright_z,0)) == in_dem_nodata_ext:
                        point_lowerright_z = numpy.nan

                    if numpy.isnan(point_upperleft_z):
                        point_upperleft_z = numpy.nanmean([point_upperleft_z,point_upperright_z,point_lowerleft_z,point_lowerright_z])
                    if numpy.isnan(point_upperright_z):
                        point_upperright_z = numpy.nanmean([point_upperleft_z,point_upperright_z,point_lowerleft_z,point_lowerright_z])
                    if numpy.isnan(point_lowerleft_z):
                        point_lowerleft_z = numpy.nanmean([point_upperleft_z,point_upperright_z,point_lowerleft_z,point_lowerright_z])
                    if numpy.isnan(point_lowerright_z):
                        point_lowerright_z = numpy.nanmean([point_upperleft_z,point_upperright_z,point_lowerleft_z,point_lowerright_z])
    
    
                    point_upperleft = (point_upperleft_x, point_upperleft_y, point_upperleft_z)
                    point_upperright = (point_upperright_x, point_upperright_y, point_upperright_z)
                    point_lowerleft = (point_lowerleft_x, point_lowerleft_y, point_lowerleft_z)
                    point_lowerright = (point_lowerright_x, point_lowerright_y, point_lowerright_z)
    
    
    
                    for triangle_id in range(0,2):
    
    
                        triangle_ring = ogr.Geometry(ogr.wkbLinearRing)
                        nodata_point_z = False
    
                        if triangle_id == 0:                        
                            triangle_ring.AddPoint(point_lowerleft_x, point_lowerleft_y)
                            triangle_ring.AddPoint(point_upperleft_x, point_upperleft_y)
                            triangle_ring.AddPoint(point_upperright_x, point_upperright_y)
                            triangle_ring.AddPoint(point_lowerleft_x, point_lowerleft_y)
                            
                            triangle_a = (point_lowerleft_x, point_lowerleft_y, point_lowerleft_z)
                            triangle_b = (point_upperleft_x, point_upperleft_y, point_upperleft_z)
                            triangle_c = (point_upperright_x, point_upperright_y, point_upperright_z)
                            
                            if point_lowerleft_z == 0 or point_upperleft_z == 0 or point_upperright_z == 0:
                                nodata_point_z = True
    
    
                        if triangle_id == 1:                        
                            triangle_ring.AddPoint(point_lowerleft_x, point_lowerleft_y)
                            triangle_ring.AddPoint(point_upperright_x, point_upperright_y)
                            triangle_ring.AddPoint(point_lowerright_x, point_lowerright_y)
                            triangle_ring.AddPoint(point_lowerleft_x, point_lowerleft_y)
    
                            triangle_a = (point_lowerleft_x, point_lowerleft_y, point_lowerleft_z)
                            triangle_b = (point_upperright_x, point_upperright_y, point_upperright_z)
                            triangle_c = (point_lowerright_x, point_lowerright_y, point_lowerright_z)
    
                            if point_lowerleft_z == 0 or point_upperright_z == 0 or point_lowerright_z == 0:
                                nodata_point_z = True

    
    
                        triangle_polygon = ogr.Geometry(ogr.wkbPolygon)
                        triangle_polygon.AddGeometry(triangle_ring)
                        triangle_abc = (triangle_a, triangle_b, triangle_c)
    
                        
                        if nodata_point_z == True:
                            break

        
                        ## Clip the triangle resulting from the in_dem with the in_boundary polygon
                        intersec_in_boundary_triangle = in_boundary_polygon.Intersection(triangle_polygon)
    
                        ## Only calculate output if triangle and in_boundary overlap, at least partly
                        if intersec_in_boundary_triangle:
                            
                            ## loop over the geometries in the resulting feature
                            for geom_id in range(0, intersec_in_boundary_triangle.GetGeometryCount()):
    
                                geom = intersec_in_boundary_triangle.GetGeometryRef(geom_id)
                                
                                if geom.GetGeometryName().upper() == 'LINEARRING': geom_linearring_cnt+=1
                                if geom.GetGeometryName().upper() == 'POLYGON': geom_polygon_cnt+=1
                                if geom.GetGeometryName().upper() == 'MULTIPOLYGON': geom_multipolygon_cnt+=1
                                
    
                                geom_points=[]
                                del geom_points[:]
    
    
                                if geom.GetGeometryName().upper() == 'LINEARRING':
                                    for i in range(0, geom.GetPointCount()):
                                        geom_point = (geom.GetPoint(i)[0], geom.GetPoint(i)[1])
                                        geom_points.append(geom_point)
    
                                if geom.GetGeometryName().upper() == 'POLYGON':
                                    geom2=geom.GetGeometryRef(0)
                                    for i in range(0, geom2.GetPointCount()):
                                        geom_point = (geom2.GetPoint(i)[0], geom2.GetPoint(i)[1])
                                        geom_points.append(geom_point)
    
    
                                if len(geom_points) > 0:
                                    
                                    try:

                                        triangulated_points = Delaunay(geom_points, qhull_options='QJ Pp')
        
                                        for a, b, c in triangulated_points.vertices:
                
                
                                            triangle_ring_splint = ogr.Geometry(ogr.wkbLinearRing)
                                            triangle_ring_splint.AddPoint(geom_points[a][0], geom_points[a][1])
                                            triangle_ring_splint.AddPoint(geom_points[b][0], geom_points[b][1])
                                            triangle_ring_splint.AddPoint(geom_points[c][0], geom_points[c][1])
                                            triangle_ring_splint.AddPoint(geom_points[a][0], geom_points[a][1])
                                            triangle_polygon_splint = ogr.Geometry(ogr.wkbPolygon)
                                            triangle_polygon_splint.AddGeometry(triangle_ring_splint)
                
            
                                            intersec_in_boundary_triangle_splint = in_boundary_polygon.Intersection(triangle_polygon_splint)
                                            
                                            if str(intersec_in_boundary_triangle_splint).upper() != 'GEOMETRYCOLLECTION EMPTY':
        
                                                geom_splint = intersec_in_boundary_triangle.GetGeometryRef(0)
                                    
                                                if geom_splint.GetGeometryName().upper() == 'LINEARRING':
                                                    geom_splint_area=geom_splint.GetArea()
        
                                                elif geom_splint.GetGeometryName().upper() == 'POLYGON':
                                                    geom_splint2=geom_splint.GetGeometryRef(0)                
                                                    geom_splint_area=geom_splint2.GetArea()
                                                else:
                                                    pass
                                                    
                                                if str(geom_splint).upper() != 'GEOMETRYCOLLECTION EMPTY':
        
        
                                                    point_a_x = geom_points[a][0]
                                                    point_a_y = geom_points[a][1]
                                                    point_a_z = self.get_z_coord_of_point((geom_points[a][0], geom_points[a][1]), triangle_abc)
        
                                                    point_b_x = geom_points[b][0]
                                                    point_b_y = geom_points[b][1]
                                                    point_b_z = self.get_z_coord_of_point((geom_points[b][0], geom_points[b][1]), triangle_abc)
                                                    
                                                    point_c_x = geom_points[c][0]
                                                    point_c_y = geom_points[c][1]
                                                    point_c_z = self.get_z_coord_of_point((geom_points[c][0], geom_points[c][1]), triangle_abc)
                                                    
    
                                                   
                                                    ## write output to shape
                                                    out_triangles_feature = ogr.Feature(out_triangles_layer_feature_defn)
                                                    out_triangles_feature.SetGeometry(triangle_polygon_splint)
    
                                                    out_triangles_feature.SetField("A_X", round(point_a_x,16))
                                                    out_triangles_feature.SetField("A_Y", round(point_a_y,16))
                                                    out_triangles_feature.SetField("A_Z", round(point_a_z,16))
                                                    out_triangles_feature.SetField("B_X", round(point_b_x,16))
                                                    out_triangles_feature.SetField("B_Y", round(point_b_y,16))
                                                    out_triangles_feature.SetField("B_Z", round(point_b_z,16))
                                                    out_triangles_feature.SetField("C_X", round(point_c_x,16))
                                                    out_triangles_feature.SetField("C_Y", round(point_c_y,16))
                                                    out_triangles_feature.SetField("C_Z", round(point_c_z,16))
        
        
                                                    
                                                    if coloring_mode == 'height':
                                                           
                                                        out_triangles_feature.SetField("A_RED", ((point_a_z - in_dem_clip_val_min) * 100 / (in_dem_clip_val_max - in_dem_clip_val_min)) / 100.0)
                                                        out_triangles_feature.SetField("A_GREEN", 0.0)
                                                        out_triangles_feature.SetField("A_BLUE", 0.0)
                                                        out_triangles_feature.SetField("A_ALPHA", 0.5)
                                                        out_triangles_feature.SetField("B_RED", ((point_b_z - in_dem_clip_val_min) * 100 / (in_dem_clip_val_max - in_dem_clip_val_min)) / 100.0)
                                                        out_triangles_feature.SetField("B_GREEN", 0.0)
                                                        out_triangles_feature.SetField("B_BLUE", 0.0)
                                                        out_triangles_feature.SetField("B_ALPHA", 0.5)
                                                        out_triangles_feature.SetField("C_RED", ((point_c_z - in_dem_clip_val_min) * 100 / (in_dem_clip_val_max - in_dem_clip_val_min)) / 100.0)
                                                        out_triangles_feature.SetField("C_GREEN", 0.0)
                                                        out_triangles_feature.SetField("C_BLUE", 0.0)
                                                        out_triangles_feature.SetField("C_ALPHA", 0.5)
        
        
                                                    if coloring_mode == 'ortho':
        
                                                        in_ortho_col_a = int(math.floor((point_a_x - in_ortho_clip_col_min_x) / in_ortho_res_x))
                                                        in_ortho_row_a = int(math.floor((in_ortho_clip_row_max_y - point_a_y) / in_ortho_res_y))
                                                        in_ortho_col_b = int(math.floor((point_b_x - in_ortho_clip_col_min_x) / in_ortho_res_x))
                                                        in_ortho_row_b = int(math.floor((in_ortho_clip_row_max_y - point_b_y) / in_ortho_res_y))
                                                        in_ortho_col_c = int(math.floor((point_c_x - in_ortho_clip_col_min_x) / in_ortho_res_x))
                                                        in_ortho_row_c = int(math.floor((in_ortho_clip_row_max_y - point_c_y) / in_ortho_res_y))
        
        
                                                         
        
                                                        if in_ortho_row_a < in_ortho_array_red_clip.shape[0] and in_ortho_col_a < in_ortho_array_red_clip.shape[1]:
                                                            red_a = in_ortho_array_red_clip[in_ortho_row_a, in_ortho_col_a]
                                                            green_a = in_ortho_array_green_clip[in_ortho_row_a, in_ortho_col_a]
                                                            blue_a = in_ortho_array_blue_clip[in_ortho_row_a, in_ortho_col_a]
                                                        else:
                                                            red_a, green_a, blue_a = 255,255,255
        
                                                        if in_ortho_row_b < in_ortho_array_red_clip.shape[0] and in_ortho_col_b < in_ortho_array_red_clip.shape[1]:
                                                            red_b = in_ortho_array_red_clip[in_ortho_row_b, in_ortho_col_b]
                                                            green_b = in_ortho_array_green_clip[in_ortho_row_b, in_ortho_col_b]
                                                            blue_b = in_ortho_array_blue_clip[in_ortho_row_b, in_ortho_col_b]
                                                        else:
                                                            red_b, green_b, blue_b = 255,255,255
        
                                                        if in_ortho_row_c < in_ortho_array_red_clip.shape[0] and in_ortho_col_c < in_ortho_array_red_clip.shape[1]:
                                                            red_c = in_ortho_array_red_clip[in_ortho_row_c, in_ortho_col_c]
                                                            green_c = in_ortho_array_green_clip[in_ortho_row_c, in_ortho_col_c]
                                                            blue_c = in_ortho_array_blue_clip[in_ortho_row_c, in_ortho_col_c]
                                                        else:
                                                            red_c, green_c, blue_c = 255,255,255
        
                                                        
                                                        #red_a_perc = round((red_a * 100.0 / 255.0) / 100.0,2)
        
                                                        out_triangles_feature.SetField("A_RED", (red_a * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("A_GREEN", (green_a * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("A_BLUE", (blue_a * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("A_ALPHA", 0.5)
                                                        out_triangles_feature.SetField("B_RED",  (red_b * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("B_GREEN",  (green_b * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("B_BLUE",  (blue_b * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("B_ALPHA", 0.5)
                                                        out_triangles_feature.SetField("C_RED",  (red_c * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("C_GREEN",  (green_c * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("C_BLUE",  (blue_c * 100.0 / 255.0) / 100.0)
                                                        out_triangles_feature.SetField("C_ALPHA", 0.5)
        
        
                                                    out_triangles_layer.CreateFeature(out_triangles_feature)
                                                    out_triangles_feature.Destroy
        
        
                                                    triangle_cnt+=1

                                    except:
                                        pass
    
        return out_triangles_layer
                                                    
                                               


    
    def calculate_ecef_from_lla(self, lon, lat, h):

        ## convert LLA (latitude/longitude/altitude) to ECEF (earth-centered/earth-fixed)
        
        a = 6378137
          
        ## Ellipsoid 
        f = 1/298.257224
        c =  1 / (math.sqrt( math.cos(math.radians(lat))**2 + ((1-f)**2 * math.sin(math.radians(lat))**2) ))
        s = (1-f)**2 * c
            
        x = (a * c + h) * math.cos(math.radians(lat)) * math.cos(math.radians(lon))
        y = (a * c + h) * math.cos(math.radians(lat)) * math.sin(math.radians(lon))
        z = (a * s + h) * math.sin(math.radians(lat)) 


        ## Sphere
        """
        x = (a + h) * math.cos(math.radians(lat)) * math.cos(math.radians(lon))
        y = (a + h) * math.cos(math.radians(lat)) * math.sin(math.radians(lon))
        z = (a + h) * math.sin(math.radians(lat)) 
        """
        


        return x,y,z


    
    def get_z_coord_of_point(self, searchpoint, triangle_abc):
        ## Get a z-coordinate of a point within a triangle
        ## http://math.stackexchange.com/questions/851742/calculate-coordinate-of-any-point-on-triangle-in-3d-plane
    
    
        triangle_a, triangle_b, triangle_c = triangle_abc
    
        triangle_a_x, triangle_a_y, triangle_a_z = triangle_a
        triangle_b_x, triangle_b_y, triangle_b_z = triangle_b
        triangle_c_x, triangle_c_y, triangle_c_z = triangle_c
    
        searchpoint_x, searchpoint_y = searchpoint
    
    
    
    
        numerator1 = (triangle_b_x - triangle_a_x) * (triangle_c_z - triangle_a_z) - (triangle_c_x - triangle_a_x) * (triangle_b_z - triangle_a_z)
        denominator1 = (triangle_b_x - triangle_a_x) * (triangle_c_y - triangle_a_y) - (triangle_c_x - triangle_a_x) * (triangle_b_y - triangle_a_y)
        fraction1 = numerator1 / denominator1
    
        numerator2 = (triangle_b_y - triangle_a_y) * (triangle_c_z - triangle_a_z) - (triangle_c_y - triangle_a_y) * (triangle_b_z - triangle_a_z )
        denominator2 = (triangle_b_x - triangle_a_x) * (triangle_c_y - triangle_a_y) - (triangle_c_x - triangle_a_x) * (triangle_b_y - triangle_a_y)
        fraction2 = numerator2 / denominator2
    
    
        searchpoint_z = triangle_a_z + (fraction1 * (searchpoint_y - triangle_a_y)) - (fraction2 * (searchpoint_x - triangle_a_x)) 
    
        return searchpoint_z
        

    


    def ogr_to_elevation_mesh(self, in_dem, in_ortho, in_geometry, in_boundaries_spatialref, in_geometry_feature_defn, in_dem_nodata_ext, in_otho_nodata_ext, out_triangles_layer, indexed_colors=True, coloring_mode='ortho'):
        
        

        out_triangles_layer_feature_defn = out_triangles_layer.GetLayerDefn()

        if in_dem != None:
           
            in_dem_res_x = float(in_dem.GetGeoTransform()[1])
            in_dem_res_y = float(abs(in_dem.GetGeoTransform()[5]))
            in_dem_cols = in_dem.RasterXSize
            in_dem_rows = in_dem.RasterYSize
            in_dem_extent_x_min = float(in_dem.GetGeoTransform()[0])
            in_dem_extent_y_max = float(in_dem.GetGeoTransform()[3])
            in_dem_extent_x_max = float(in_dem_extent_x_min + (in_dem_cols * in_dem_res_x))
            in_dem_extent_y_min = float(in_dem_extent_y_max - (in_dem_rows * in_dem_res_y))

        else:

            in_dem_extent_x_min, in_dem_extent_x_max, in_dem_extent_y_min, in_dem_extent_y_max = in_boundary_layer.GetExtent()
            in_dem_cols = 144
            in_dem_rows = 72
            in_dem_res_x = (in_dem_extent_x_max - in_dem_extent_x_min) / in_dem_cols
            in_dem_res_y = (in_dem_extent_y_max - in_dem_extent_y_min) / in_dem_rows

       

        
        if in_ortho != None:
            
            in_ortho_res_x = float(in_ortho.GetGeoTransform()[1])
            in_ortho_res_y = float(abs(in_ortho.GetGeoTransform()[5]))
            in_ortho_cols = in_ortho.RasterXSize
            in_ortho_rows = in_ortho.RasterYSize
            in_ortho_extent_x_min = float(in_ortho.GetGeoTransform()[0])
            in_ortho_extent_y_max = float(in_ortho.GetGeoTransform()[3])
            in_ortho_extent_x_max = float(in_ortho_extent_x_min + (in_ortho_cols * in_ortho_res_x))
            in_ortho_extent_y_min = float(in_ortho_extent_y_max - (in_ortho_rows * in_ortho_res_y))

        else:

            in_ortho_extent_x_min, in_ortho_extent_x_max, in_ortho_extent_y_min, in_ortho_extent_y_max = in_boundary_layer.GetExtent()
            in_ortho_cols = 144
            in_ortho_rows = 72
            in_ortho_res_x = (in_ortho_extent_x_max - in_ortho_extent_x_min) / in_ortho_cols
            in_ortho_res_y = (in_ortho_extent_y_max - in_ortho_extent_y_min) / in_ortho_rows
        
            
     
        
    


        in_geometry_geom_type = in_geometry.GetGeometryName()

        if in_geometry_geom_type.upper() == "POLYGON":
            out_triangles_layer = self.parse_polygon(in_geometry, in_dem, in_ortho, out_triangles_layer, out_triangles_layer_feature_defn, in_dem_nodata_ext, in_otho_nodata_ext, in_dem_res_x, in_dem_res_y, in_dem_extent_x_min, in_dem_extent_x_max, in_dem_extent_y_min, in_dem_extent_y_max, in_dem_cols, in_dem_rows,
                    in_ortho_extent_x_min, in_ortho_extent_x_max, in_ortho_extent_y_min, in_ortho_extent_y_max, in_ortho_res_x, in_ortho_res_y, in_ortho_cols, in_ortho_rows, coloring_mode)


        if in_geometry_geom_type.upper() == "MULTIPOLYGON":

            for in_geometry_polygon_id, in_geometry_polygon in enumerate(in_geometry):
                
                if in_geometry_polygon_id > -1:

                    out_triangles_layer = self.parse_polygon(in_geometry_polygon, in_dem, in_ortho, out_triangles_layer, out_triangles_layer_feature_defn, in_dem_nodata_ext, in_otho_nodata_ext, in_dem_res_x, in_dem_res_y, in_dem_extent_x_min, in_dem_extent_x_max, in_dem_extent_y_min, in_dem_extent_y_max, in_dem_cols, in_dem_rows,
                            in_ortho_extent_x_min, in_ortho_extent_x_max, in_ortho_extent_y_min, in_ortho_extent_y_max, in_ortho_res_x, in_ortho_res_y, in_ortho_cols, in_ortho_rows, coloring_mode)


        
        elevation_minmax = [0,0]

        

    







    def conv_triangle_shape_to_x3d(self, in_triangles_layer, out_mesh_filename, indexed_colors=True):
      
        in_triangles_feature_count = in_triangles_layer.GetFeatureCount()
        logger.info('feature_count: %s', in_triangles_feature_count)
               
        out_mesh = open(out_mesh_filename, 'w')
        logger.info(out_mesh_filename)
        
        coords_array_x = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        coords_array_y = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        coords_array_z = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        
        coords_array_lut_x = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        coords_array_lut_y = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        coords_array_lut_z = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        
        
        colors_array_red = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        colors_array_green = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        colors_array_blue = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        colors_array_alpha = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        
        colors_array_lut_red = numpy.empty(in_triangles_feature_count*3)* numpy.nan
        colors_array_lut_green = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        colors_array_lut_blue = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        colors_array_lut_alpha = numpy.empty(in_triangles_feature_count*3) * numpy.nan
       
        
        nodecoords_array = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        nodecolors_array = numpy.empty(in_triangles_feature_count*3) * numpy.nan
        
        
        
        triangles_x_min_total, triangles_x_max_total, triangles_y_min_total, triangles_y_max_total = in_triangles_layer.GetExtent()




        ## Loop through triangle-features and write every
        ## x,y, and z - coordinate into one distinct numpy array
      
        
        for in_triangles_feature_id,in_triangles_feature in enumerate(in_triangles_layer):
            in_triangles_polygon = in_triangles_feature.GetGeometryRef()
            geom_firstlevel = in_triangles_polygon.GetGeometryRef(0)
            point_a_x = in_triangles_feature.GetField("A_X")
            point_a_y = in_triangles_feature.GetField("A_Y")
            point_a_z = in_triangles_feature.GetField("A_Z")
            point_b_x = in_triangles_feature.GetField("B_X")
            point_b_y = in_triangles_feature.GetField("B_Y")
            point_b_z = in_triangles_feature.GetField("B_Z")
            point_c_x = in_triangles_feature.GetField("C_X")
            point_c_y = in_triangles_feature.GetField("C_Y")
            point_c_z = in_triangles_feature.GetField("C_Z")
            
            point_a_red = in_triangles_feature.GetField("A_RED")
            point_a_green = in_triangles_feature.GetField("A_GREEN")
            point_a_blue = in_triangles_feature.GetField("A_BLUE")
            point_a_alpha = in_triangles_feature.GetField("A_ALPHA")
            point_b_red = in_triangles_feature.GetField("B_RED")
            point_b_green = in_triangles_feature.GetField("B_GREEN")
            point_b_blue = in_triangles_feature.GetField("B_BLUE")
            point_b_alpha = in_triangles_feature.GetField("B_ALPHA")
            point_c_red = in_triangles_feature.GetField("C_RED")
            point_c_green = in_triangles_feature.GetField("C_GREEN")
            point_c_blue = in_triangles_feature.GetField("C_BLUE")
            point_c_alpha = in_triangles_feature.GetField("C_ALPHA")
            
       
              
            coords_array_x[(in_triangles_feature_id*3) + 0] = round(point_a_x,16)
            coords_array_y[(in_triangles_feature_id*3) + 0] = round(point_a_y,16)
            coords_array_z[(in_triangles_feature_id*3) + 0] = round(point_a_z,16)
        
            coords_array_x[(in_triangles_feature_id*3) + 1] = round(point_b_x,16)
            coords_array_y[(in_triangles_feature_id*3) + 1] = round(point_b_y,16)
            coords_array_z[(in_triangles_feature_id*3) + 1] = round(point_b_z,16)
        
            coords_array_x[(in_triangles_feature_id*3) + 2] = round(point_c_x,16)
            coords_array_y[(in_triangles_feature_id*3) + 2] = round(point_c_y,16)
            coords_array_z[(in_triangles_feature_id*3) + 2] = round(point_c_z,16)
        
              
            colors_array_red[(in_triangles_feature_id*3) + 0] = round(point_a_red,2)
            colors_array_green[(in_triangles_feature_id*3) + 0] = round(point_a_green,2)
            colors_array_blue[(in_triangles_feature_id*3) + 0] = round(point_a_blue,2)
            colors_array_alpha[(in_triangles_feature_id*3) + 0] = round(point_a_alpha,2)

            colors_array_red[(in_triangles_feature_id*3) + 1] = round(point_b_red,2)
            colors_array_green[(in_triangles_feature_id*3) + 1] = round(point_b_green,2)
            colors_array_blue[(in_triangles_feature_id*3) + 1] = round(point_b_blue,2)
            colors_array_alpha[(in_triangles_feature_id*3) + 1] = round(point_b_alpha,2)
        
            colors_array_red[(in_triangles_feature_id*3) + 2] = round(point_c_red,2)
            colors_array_green[(in_triangles_feature_id*3) + 2] = round(point_c_green,2)
            colors_array_blue[(in_triangles_feature_id*3) + 2] = round(point_c_blue,2)
            colors_array_alpha[(in_triangles_feature_id*3) + 2] = round(point_c_alpha,2)

        
        #logger.info('assign colors')
        
        ## Loop through the x,y, and z - numpy arrays, search for duplicates and replace
        ## them by NAN, write the found unique coord combinations in x,y,z, lists and the node id in another list
        unique_nodecoords_cnt=0
        unique_nodecolors_cnt=0
        
        if indexed_colors == False:
        
            for coord_id in range(0,len(coords_array_x)):
                #logger.info coord_id, '(', len(coords_array_x), ')'
                
                coord_x, coord_y, coord_z = coords_array_x[coord_id], coords_array_y[coord_id], coords_array_z[coord_id]
                color_red, color_green, color_blue, color_alpha = colors_array_red[coord_id], colors_array_green[coord_id], colors_array_blue[coord_id], colors_array_alpha[coord_id]
                
            
                if not numpy.isnan(coord_x):
                
                    coord_locations = numpy.where(  ( coords_array_x[:] == round(coord_x,16) ) &
                                                    ( coords_array_y[:] == round(coord_y,16) ) &
                                                    ( coords_array_z[:] == round(coord_z,16) ) )
            
                    for coord_location in coord_locations:
                        coords_array_x[coord_location] = numpy.nan
                        coords_array_y[coord_location] = numpy.nan
                        coords_array_z[coord_location] = numpy.nan
            
                        nodecoords_array[coord_location] = unique_nodecoords_cnt
            
                    coords_array_lut_x[unique_nodecoords_cnt] = coord_x
                    coords_array_lut_y[unique_nodecoords_cnt] = coord_y
                    coords_array_lut_z[unique_nodecoords_cnt] = coord_z
            
                    colors_array_lut_red[unique_nodecoords_cnt] = color_red
                    colors_array_lut_green[unique_nodecoords_cnt] = color_green
                    colors_array_lut_blue[unique_nodecoords_cnt] = color_blue
                    colors_array_lut_alpha[unique_nodecoords_cnt] = color_alpha
            
                    unique_nodecoords_cnt+=1
                
        
        
        if indexed_colors == True:
        
            for coord_id in range(0,len(coords_array_x)):
                #logger.info coord_id, '(', len(coords_array_x), ')'
        
                coord_x, coord_y, coord_z = coords_array_x[coord_id], coords_array_y[coord_id], coords_array_z[coord_id]
                color_red, color_green, color_blue, color_alpha = colors_array_red[coord_id], colors_array_green[coord_id], colors_array_blue[coord_id], colors_array_alpha[coord_id]
                
            
                if not numpy.isnan(coord_x):
                
                    coord_locations = numpy.where(  ( coords_array_x[:] == round(coord_x,16) ) &
                                                    ( coords_array_y[:] == round(coord_y,16) ) &
                                                    ( coords_array_z[:] == round(coord_z,16) ) )
            
                    #for coord_location in coord_locations:
                    #    coords_array_x[coord_location] = numpy.nan
                    #    coords_array_y[coord_location] = numpy.nan
                    #    coords_array_z[coord_location] = numpy.nan
                    #
                    #    nodecoords_array[coord_location] = unique_nodecoords_cnt

                    if len(coord_locations[0]) > 0:

                        coords_array_x[coord_locations] = numpy.nan
                        coords_array_y[coord_locations] = numpy.nan
                        coords_array_z[coord_locations] = numpy.nan
            
                        nodecoords_array[coord_locations] = unique_nodecoords_cnt
            
            
                        coords_array_lut_x[unique_nodecoords_cnt] = coord_x
                        coords_array_lut_y[unique_nodecoords_cnt] = coord_y
                        coords_array_lut_z[unique_nodecoords_cnt] = coord_z
            
                        unique_nodecoords_cnt+=1
            
            
            
                if not numpy.isnan(color_red):
            
                    color_locations = numpy.where(  ( colors_array_red[:] == round(color_red,2) ) &
                                                    ( colors_array_green[:] == round(color_green,2) ) &
                                                    ( colors_array_blue[:] == round(color_blue,2) ) & 
                                                    ( colors_array_alpha[:] == round(color_alpha,2) ) )



                    if len(color_locations[0]) > 0:

                        colors_array_red[color_locations] = numpy.nan
                        colors_array_green[color_locations] = numpy.nan
                        colors_array_blue[color_locations] = numpy.nan
                        colors_array_alpha[color_locations] = numpy.nan
            
                        nodecolors_array[color_locations] = unique_nodecolors_cnt

            
                        colors_array_lut_red[unique_nodecoords_cnt] = color_red
                        colors_array_lut_green[unique_nodecoords_cnt] = color_green
                        colors_array_lut_blue[unique_nodecoords_cnt] = color_blue
                        colors_array_lut_alpha[unique_nodecoords_cnt] = color_alpha

                        unique_nodecolors_cnt+=1
        

        
        coords_array_lut_x_clean = coords_array_lut_x[numpy.logical_not(numpy.isnan(coords_array_lut_x))]
        coords_array_lut_y_clean = coords_array_lut_y[numpy.logical_not(numpy.isnan(coords_array_lut_y))]
        coords_array_lut_z_clean = coords_array_lut_z[numpy.logical_not(numpy.isnan(coords_array_lut_z))]

        colors_array_lut_red_clean = colors_array_lut_red[numpy.logical_not(numpy.isnan(colors_array_lut_red))]
        colors_array_lut_green_clean = colors_array_lut_green[numpy.logical_not(numpy.isnan(colors_array_lut_green))]
        colors_array_lut_blue_clean = colors_array_lut_blue[numpy.logical_not(numpy.isnan(colors_array_lut_blue))]
        colors_array_lut_alpha_clean = colors_array_lut_alpha[numpy.logical_not(numpy.isnan(colors_array_lut_alpha))]

        ## Just a precaution: If the reference to to color list is higher than the number of colors contained in that list, 
        ## set the reference to the last list item.
        nodecolors_false_values = numpy.where(nodecolors_array[:] > len(colors_array_lut_red_clean)-1)
        if len(nodecolors_false_values[0]) > 0:
            nodecolors_array[nodecolors_false_values] = len(colors_array_lut_red_clean)-1


        nodecoords_array_clean = nodecoords_array[numpy.logical_not(numpy.isnan(nodecoords_array))]
        nodecolors_array_clean = nodecolors_array[numpy.logical_not(numpy.isnan(nodecolors_array))]


        coords_arrays_lut_clean = [coords_array_lut_x_clean, coords_array_lut_y_clean, coords_array_lut_z_clean]
        colors_arrays_lut_clean = [colors_array_lut_red_clean, colors_array_lut_green_clean, colors_array_lut_blue_clean, colors_array_lut_alpha_clean]
        
        
        
        
        elevation_minmax = [0,1]
        triangles_z_min_total, triangles_z_max_total = elevation_minmax
        
        bbox3d = [triangles_x_min_total, triangles_x_max_total, triangles_y_min_total, triangles_y_max_total, triangles_z_min_total, triangles_z_max_total]
        center_scale_coords=True
        
        self.write_x3d(nodecoords_array_clean, coords_arrays_lut_clean, nodecolors_array_clean, colors_arrays_lut_clean, out_mesh, out_mesh_filename, bbox3d, center_scale_coords, indexed_colors)
        
        
        out_mesh.close()

    
    
    def write_x3d(self, nodecoords_array, coords_arrays_lut, nodecolors_array, colors_arrays_lut, out_mesh, out_mesh_filename, bbox3d, center_scale_coords, indexed_colors):
        exaggeration_z = 1.0
        
        coords_array_lut_x, coords_array_lut_y, coords_array_lut_z = coords_arrays_lut
        colors_array_lut_red, colors_array_lut_green, colors_array_lut_blue, colors_array_lut_alpha = colors_arrays_lut
    
    
        triangles_x_min_total, triangles_x_max_total, triangles_y_min_total, triangles_y_max_total, triangles_z_min_total, triangles_z_max_total = bbox3d
        
        
        
        if center_scale_coords==True:
            triangles_x_center_total = (triangles_x_min_total + triangles_x_max_total) / 2
            triangles_y_center_total = (triangles_y_min_total + triangles_y_max_total) / 2
            triangles_z_center_total = (triangles_z_min_total + triangles_z_max_total) / 2
            
            if round(triangles_x_center_total - triangles_x_min_total, 2) != 0.00:
                scale_x = 8 / (triangles_x_center_total - triangles_x_min_total)
            else:
                scale_x = 0.1
                
            if (triangles_y_center_total - triangles_y_min_total) != 0.00:
                scale_y = 8 / (triangles_y_center_total - triangles_y_min_total)
            else:
                scale_y = 0.1
            
            scale_xy = min(scale_x, scale_y)
            scale_z = scale_xy * exaggeration_z
        
        else:
            triangles_x_center_total=0
            triangles_y_center_total=0
            triangles_z_center_total=0
            scale_xy = 1.0
            scale_z = scale_xy * exaggeration_z
    
        #logger.info("triangles_z_center_total=%s, scale_xy=%s, scale_z=%s", triangles_z_center_total, scale_xy, scale_z)
    
        out_mesh.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
        out_mesh.write('<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 3.0//EN" "http://www.web3d.org/specifications/x3d-3.0.dtd">' + '\n')
        out_mesh.write('<X3D version="3.0" profile="Immersive" xmlns:xsd="http://www.w3.org/2001/XMLSchema-instance" xsd:noNamespaceSchemaLocation="http://www.web3d.org/specifications/x3d-3.0.xsd">' + '\n')
        out_mesh.write('    <head>' + '\n')
        out_mesh.write('        <meta name="filename" content="' + out_mesh_filename + '" />' + '\n')
        out_mesh.write('        <meta name="generator" content="geoTriMesh 0.9" />' + '\n')
        out_mesh.write('    </head>' + '\n')
        out_mesh.write('    <Scene>' + '\n')
        out_mesh.write('        <NavigationInfo headlight="false"' + '\n')
        out_mesh.write('                        visibilityLimit="0.0"' + '\n')
        out_mesh.write('                        type=' + "'" + '"EXAMINE", "ANY"' + "'" + '\n')
        out_mesh.write('                        avatarSize="0.25, 1.75, 0.75"' + '\n')
        out_mesh.write('                        />' + '\n')
        out_mesh.write('        <Background DEF="WO_World"' + '\n')
        out_mesh.write('                    groundColor="0.051 0.051 0.051"' + '\n')
        out_mesh.write('                    skyColor="0.051 0.051 0.051"' + '\n')
        out_mesh.write('                    />' + '\n')
        out_mesh.write('        <Transform DEF="Cube_TRANSFORM"' + '\n')
        out_mesh.write('                   translation="0.000000 0.000000 0.000000"' + '\n')
        out_mesh.write('                   scale="1.000000 1.000000 1.000000"' + '\n')
        out_mesh.write('                   rotation="0.000000 0.707107 0.707107 3.141593"' + '\n')
        out_mesh.write('                   >' + '\n')
        out_mesh.write('            <Transform DEF="Cube_ifs_TRANSFORM"' + '\n')
        out_mesh.write('                       translation="0.000000 0.000000 0.000000"' + '\n')
        out_mesh.write('                       scale="1.000000 1.000000 1.000000"' + '\n')
        out_mesh.write('                       rotation="1.000000 0.000000 0.000000 0.000000"' + '\n')
        out_mesh.write('                       >' + '\n')
        out_mesh.write('                <Group DEF="group_ME_Cube">' + '\n')
        out_mesh.write('                    <Shape>' + '\n')
        out_mesh.write('                        <Appearance>' + '\n')
        out_mesh.write('                            <Material DEF="MA_Material"' + '\n')
        out_mesh.write('                                      diffuseColor="0.800 0.800 0.800"' + '\n')
        out_mesh.write('                                      specularColor="0.401 0.401 0.401"' + '\n')
        out_mesh.write('                                      emissiveColor="0.000 0.000 0.000"' + '\n')
        out_mesh.write('                                      ambientIntensity="0.333"' + '\n')
        out_mesh.write('                                      shininess="0.098"' + '\n')
        out_mesh.write('                                      transparency="0.0"' + '\n')
        out_mesh.write('                                      />' + '\n')
        out_mesh.write('                        </Appearance>' + '\n')
        out_mesh.write('                        <IndexedFaceSet solid="false"' + '\n')
    
        out_mesh.write('                                        coordIndex="')
        for nodecoord_id, nodecoord in enumerate(nodecoords_array):
    
            out_mesh.write(str(int(nodecoord)) + ' ')
    
            if nodecoord_id > 0 and (nodecoord_id +1) % 3 == 0:
                out_mesh.write('-1' + ' ')
                    
     
        out_mesh.write('"' + '\n')
    
    
    
        ## if indexed colors (equivalent to indexed coords are not supported by the viewer,
        ## output all the colors as a sequence so that each vertex matches a color. Creates
        ## unneccessary big files compared with the advised setting (indexed_colors=True).
    
        if indexed_colors == True:
    
            out_mesh.write('                                        colorIndex="')

            logger.info('Highest color reference: %s', numpy.amax(nodecolors_array))
    
            for nodecolor_id, nodecolor in enumerate(nodecolors_array):

                if not numpy.isnan(nodecolor):

                    """
                    ##Blender-bug (<=v2.78a): nolor aray starts at 1 instead of 0
                    if int(nodecolor) > 0:
                        out_mesh.write(str(int(nodecolor)) + ' ')
                    else:
                        out_mesh.write(str(int(nodecolor+1)) + ' ')
                    """
                    out_mesh.write(str(int(nodecolor)) + ' ')
                
                
                    if nodecolor_id > 0 and (nodecolor_id +1) % 3 == 0:
                        out_mesh.write('-1' + ' ')

    
     
            out_mesh.write('"' + '\n')
           
    
        out_mesh.write('                                        colorPerVertex="true"' + '\n')
        out_mesh.write('                                        >' + '\n')
        
        out_mesh.write('                            <Coordinate DEF="coords_ME_Cube"' + '\n')
        out_mesh.write('                                        point="')
    
        for coord_lut_id, (coord_lut_x, coord_lut_y, coord_lut_z) in enumerate(zip(coords_array_lut_x, coords_array_lut_y, coords_array_lut_z)):
    
            if not numpy.isnan(coord_lut_x):
               
   
                x_out,y_out,z_out = self.calculate_ecef_from_lla(coord_lut_x, coord_lut_y, coord_lut_z)
                
                scale_xy=0.000001
                scale_z =0.000001
               
                out_mesh.write(str(x_out * scale_xy) + ' ' + str(y_out * scale_xy) + ' ' + str(z_out * scale_z) + ' ')

            else:
                break
    
    
        out_mesh.write('"' + '\n')
    
        out_mesh.write('                                        />' + '\n')
    
        
        
        out_mesh.write('                                        <ColorRGBA color="')



        logger.info('Number of unique colors: %s %s %s %s', len(colors_array_lut_red), len(colors_array_lut_green), len(colors_array_lut_blue), len(colors_array_lut_alpha))

        for color_lut_id, (color_lut_red, color_lut_green, color_lut_blue, color_lut_alpha) in enumerate(zip(colors_array_lut_red, colors_array_lut_green, colors_array_lut_blue, colors_array_lut_alpha)):
    
            if not numpy.isnan(color_lut_red):
            
                out_mesh.write(str(color_lut_red) + ' ' + str(color_lut_green) + ' ' + str(color_lut_blue) + ' ' + str(color_lut_alpha) + ' ' )
    
            else:
                break
    
        out_mesh.write('"' + '\n')
    
        out_mesh.write('                                        />' + '\n')
        
        
        out_mesh.write('                        </IndexedFaceSet>' + '\n')
        out_mesh.write('                    </Shape>' + '\n')
        out_mesh.write('                </Group>' + '\n')
        out_mesh.write('            </Transform>' + '\n')
        out_mesh.write('        </Transform>' + '\n')
        out_mesh.write('        <Transform DEF="Lamp_TRANSFORM"' + '\n')
        out_mesh.write('                   translation="-4.076245 5.903862 1.005454"' + '\n')
        out_mesh.write('                   scale="1.000000 1.000000 1.000000"' + '\n')
        out_mesh.write('                   rotation="-0.498084 -0.762016 -0.413815 1.513875"' + '\n')
        out_mesh.write('                   >' + '\n')
        out_mesh.write('            <PointLight DEF="LA_Lamp"' + '\n')
        out_mesh.write('                        ambientIntensity="0.0000"' + '\n')
        out_mesh.write('                        color="1.0000 1.0000 1.0000"' + '\n')
        out_mesh.write('                        intensity="0.5714"' + '\n')
        out_mesh.write('                        radius="30.0000" ' + '\n')
        out_mesh.write('                        location="-0.0000 -0.0000 0.0000"' + '\n')
        out_mesh.write('                        />' + '\n')
        out_mesh.write('        </Transform>' + '\n')
        out_mesh.write('        <Transform DEF="Camera_TRANSFORM"' + '\n')
        out_mesh.write('                   translation="-7.481132 5.343665 -6.507640"' + '\n')
        out_mesh.write('                   scale="1.000000 1.000000 1.000000"' + '\n')
        out_mesh.write('                   rotation="-0.093039 -0.968741 -0.229967 2.347036"' + '\n')
        out_mesh.write('                   >' + '\n')
        out_mesh.write('            <Viewpoint DEF="CA_Camera"' + '\n')
        out_mesh.write('                       centerOfRotation="0 0 0"' + '\n')
        out_mesh.write('                       position="0.00 0.00 -0.00"' + '\n')
        out_mesh.write('                       orientation="-0.00 0.00 0.00 0.00"' + '\n')
        out_mesh.write('                       fieldOfView="0.858"' + '\n')
        out_mesh.write('                       />' + '\n')
        out_mesh.write('        </Transform>' + '\n')
        out_mesh.write('    </Scene>' + '\n')
        out_mesh.write('</X3D>' + '\n')
    
    
