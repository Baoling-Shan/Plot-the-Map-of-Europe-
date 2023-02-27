import numpy as np
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import MultiLineString, Polygon


### This the map only with border
# create a new map
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-15, 35, 35, 71], crs=ccrs.PlateCarree())

# add coastlines and borders
ax.coastlines(resolution='10m')
ax.add_feature(cartopy.feature.BORDERS)

# add a title
plt.title('Map of Europe')
# show the plot
plt.show()



# ### This is the
# # Set up the projection
# ax = plt.axes(projection=ccrs.PlateCarree())
#
# # Set the extent of the map
# ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())
#
# # Add land and ocean features
# ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')
# ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')
#
# # Add country borders
# ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=0.3)
#
# # Define a colormap
# cmap = plt.cm.get_cmap('OrRd')
#
# # Create a sample data array (replace with your own data)
# data = np.random.rand(10, 10)
#
# # Plot the data using pcolormesh
# im = ax.pcolormesh(data, cmap=cmap)
#
# # Plot the borders of each country
# for country in cartopy.feature.COASTLINE.geometries():
#     ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
#
# # # Highlight Poland with a different color
# # poland_lon = 19.0
# # poland_lat = 52.0
# # poland_color = 'red'
# # ax.plot(poland_lon, poland_lat, marker='o', markersize=10, color=poland_color, alpha=0.7, transform=ccrs.PlateCarree())
#
# # # Add a colorbar
# # cbar = plt.colorbar(im)
#
# # Add a title
# plt.title('Map of Europe')
#
# # Show the plot
# plt.show()

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import cartopy.io.shapereader as shapereader
import geopandas as gpd

# Set up the projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())

# Add land and ocean features
ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')  # #f5ede1
ax.add_feature(cartopy.feature.OCEAN, facecolor='none')

# Add country borders
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

# Define a colormap
cmap = plt.cm.get_cmap('OrRd')

# Create a sample data array (replace with your own data)
data = np.random.rand(10, 10)

# Plot the data using pcolormesh
im = ax.pcolormesh(data, cmap=cmap)

# Plot the borders of each country
for country in cfeature.COASTLINE.geometries():
    if isinstance(country, MultiLineString):
        for line in country:
            ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
    else:
        ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')

# Add a shapefile for Poland
shapefile_path = gpd.datasets.get_path('naturalearth_lowres')
gdf = gpd.read_file(shapefile_path)

# Filter the dataframe to only include Poland, Plot the geometry for Poland
# poland = gdf[gdf['name'] == 'Poland']
# ax.add_geometries(poland['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Portugal = gdf[gdf['name'] == 'Portugal']
ax.add_geometries(Portugal['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Norway = gdf[gdf['name'] == 'Norway']
ax.add_geometries(Norway['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Greece = gdf[gdf['name'] == 'Greece']
ax.add_geometries(Greece['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Czechia = gdf[gdf['name'] == 'Czechia']
ax.add_geometries(Czechia['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

England = gdf[gdf['name'] == 'United Kingdom']
ax.add_geometries(England['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Italy = gdf[gdf['name'] == 'Italy']
ax.add_geometries(Italy['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Sweden = gdf[gdf['name'] == 'Sweden']
ax.add_geometries(Sweden['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')

Romania = gdf[gdf['name'] == 'Romania']
ax.add_geometries(Romania['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='red')


# ax.text(-8.5, 38, 'Portugal', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(9, 62,    'Norway', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(23.5, 39, 'Greece', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(15, 49,  'Czechia', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(-3, 54,   'UK',      horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(12.5, 42, 'Italy', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(17.5, 62,   'Sweden', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())
# ax.text(26.5, 46, 'Romania', horizontalalignment='center', fontsize=10, color='black', fontweight='bold', transform=ccrs.PlateCarree())



# Add the country name for each highlighted country
ax.annotate('Portugal', xy=(-8, 38), xytext=(-10, 43), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='red', arrowstyle='-|>'))
ax.annotate('Norway', xy=(9, 65), xytext=(4, 65), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='red', arrowstyle='-|>'))
ax.annotate('Greece', xy=(23, 38), xytext=(21, 35.5), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='red', arrowstyle='-|>'))
ax.annotate('Czechia', xy=(15, 50), xytext=(13, 51), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='red', arrowstyle='-|>'))
ax.annotate('United Kingdom', xy=(-2, 54), xytext=(-7, 58), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='red', arrowstyle='-|>'))
ax.annotate('Italy', xy=(14, 42), xytext=(11, 40), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='blue', arrowstyle='-|>'))
ax.annotate('Sweden', xy=(19, 64), xytext=(20, 66), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='blue', arrowstyle='-|>'))
ax.annotate('Romania', xy=(27, 46), xytext=(23, 48), color='black',  fontsize=10, fontweight='bold',)
            # arrowprops=dict(facecolor='blue', arrowstyle='-|>'))


# Add a title
plt.title('Map of Europe')

# Show the plot
plt.show()




import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import cartopy.io.shapereader as shapereader
import geopandas as gpd

# Set up the projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())

# Add land and ocean features
ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')
ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')

# Add country borders
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

# Define a colormap
cmap = plt.cm.get_cmap('OrRd')

# Create a sample data array (replace with your own data)
data = np.random.rand(10, 10)

# Plot the data using pcolormesh
im = ax.pcolormesh(data, cmap=cmap)

# Plot the borders of each country
for country in cfeature.COASTLINE.geometries():
    if isinstance(country, MultiLineString):
        for line in country:
            ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
    else:
        ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')

# Add a shapefile for Europe
shapefile_path = shapereader.natural_earth(resolution='10m', category='cultural', name='admin_0_countries')
gdf = gpd.read_file(shapefile_path)

# Plot the geometry and name of each country
for country_name, edgecolor, xy_position, text_position in [('Portugal', '#0D1130', (-8.5, 38), (-7, 43)),
                                               ('Norway', '#0D1130', (9, 62),  (7, 65)),
                                               ('Greece', '#0D1130', (23.5, 39), (22, 36),),
                                               ('Czechia', '#0D1130', (15, 49), (15, 52),),
                                               ('United Kingdom', '#0D1130', (-3, 54), (-4, 60),),
                                               ('Italy', '#0D1130', (12.5, 42), (13, 40),),
                                               ('Sweden', '#0D1130', (18, 62), (22, 66),),
                                               ('Romania', '#0D1130', (26.5, 46), (27, 49))]:
    country = gdf[gdf['NAME'] == country_name]
    ax.add_geometries(country['geometry'], crs=ccrs.PlateCarree(), facecolor='#0072BB', edgecolor=edgecolor)
    ax.annotate(country_name, xy=xy_position, xytext=text_position, ha='center', va='center', fontsize=10, color='red', fontweight='bold')

ax.text(-9, 39, 'D1',            bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(8, 62,    'D2',          bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(22, 38,'D4,B2,I5',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(13, 48, 'D3,C4,B3,I4',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-3, 54,   'D5,C5,B4',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(12, 42,   'C1,B5,I2',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(16, 62,   'C3,B1,I3',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(25, 46, 'C2,I1',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))




# Add a title
plt.title('Map of Period 1')
plt.axis('off')

# Show the plot
plt.show()


# import cartopy.crs as ccrs
# import cartopy.feature as cfeature
# import matplotlib.pyplot as plt
# import numpy as np
# import cartopy.io.shapereader as shapereader
# import geopandas as gpd
#
# # Set up the projection
# ax = plt.axes(projection=ccrs.PlateCarree())
#
# # Set the extent of the map
# ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())
#
# # Add land and ocean features
# ax.add_feature(cartopy.feature.LAND, facecolor='none')  # #f5ede1
# ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')
#
# # Add country borders
# ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)
#
# # Define a colormap
# cmap = plt.cm.get_cmap('OrRd')
#
# # Create a sample data array (replace with your own data)
# data = np.random.rand(10, 10)
#
# # Plot the data using pcolormesh
# im = ax.pcolormesh(data, cmap=cmap)
#
# # Plot the borders of each country
# for country in cfeature.COASTLINE.geometries():
#     if isinstance(country, MultiLineString):
#         for line in country:
#             ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
#     else:
#         ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
#
# # Add a shapefile for countries
# shapefile_path = gpd.datasets.get_path('naturalearth_lowres')
# gdf = gpd.read_file(shapefile_path)
#
# # Add Russia
# russia = gdf[gdf['name'] == 'Russia']
# ax.add_geometries(russia['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='green')
#
# # Add Belarus
# belarus = gdf[gdf['name'] == 'Belarus']
# ax.add_geometries(belarus['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='green')
#
# # Add Germany
# germany = gdf[gdf['name'] == 'Germany']
# ax.add_geometries(germany['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='green')
#
# # Add text for Russia
# ax.text(56, 64, 'Russia', horizontalalignment='center', fontsize=8, transform=ccrs.PlateCarree())
#
# # Add text for Belarus
# ax.text(28, 54, 'Belarus', horizontalalignment='center', fontsize=8, transform=ccrs.PlateCarree())
#
# # Add text for Germany
# ax.text(10, 50, 'Germany', horizontalalignment='center', fontsize=8, transform=ccrs.PlateCarree())
#
# # Add a title
# plt.title('Map of Europe')
#
# # Show the plot
# plt.show()

###########################################
#This is period 2

# Set up the projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())

# Add land and ocean features
ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')
ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')

# Add country borders
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

# Define a colormap
cmap = plt.cm.get_cmap('OrRd')

# Create a sample data array (replace with your own data)
data = np.random.rand(10, 10)

# Plot the data using pcolormesh
im = ax.pcolormesh(data, cmap=cmap)

# Plot the borders of each country
for country in cfeature.COASTLINE.geometries():
    if isinstance(country, MultiLineString):
        for line in country:
            ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
    else:
        ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')

# Add a shapefile for Europe
shapefile_path = shapereader.natural_earth(resolution='10m', category='cultural', name='admin_0_countries')
gdf = gpd.read_file(shapefile_path)

# Plot the geometry and name of each country
for country_name, edgecolor, xy_position, text_position in [('Italy', '#0D1130', (12.5, 42), (13, 40),),
                                                            ('Russia', '#0D1130', (32, 64), (32, 63)),
                                                            ('Sweden', '#0D1130', (18, 62), (22, 66),),
                                                            ('Greece', '#0D1130', (23.5, 39), (22, 36),),
                                                            ('Romania', '#0D1130', (26.5, 46), (27, 49)),
                                                            ('Belarus', '#0D1130', (28, 54),  (27, 56)),
                                                            ('Germany', '#0D1130', (10, 50), (10, 53),),
                                                            ('United Kingdom', '#0D1130', (-3, 54), (-4, 60),)]:
    country = gdf[gdf['NAME'] == country_name]
    ax.add_geometries(country['geometry'], crs=ccrs.PlateCarree(), facecolor='#0072BB', edgecolor=edgecolor)
    ax.annotate(country_name, xy=xy_position, xytext=text_position, ha='center', va='center', fontsize=10, color='red', fontweight='bold')

ax.text(12, 42,   'D1,C2,B1',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(30, 60,   'D2,I1',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(16, 62,   'D3,C4,B5',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(22, 38,   'D4,B2,I4',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(24, 46, 'D5,C3,I3',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(26, 53, 'C1,B4,I5',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(9, 50, 'C5,I2',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-3, 54,   'B3',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))



# Add a title
plt.title('Map of Period 2')
plt.axis('off')

# Show the plot
plt.show()


############################################
#This is Period 3
# Set up the projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())

# Add land and ocean features
ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')
ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')

# Add country borders
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

# Define a colormap
cmap = plt.cm.get_cmap('OrRd')

# Create a sample data array (replace with your own data)
data = np.random.rand(10, 10)

# Plot the data using pcolormesh
im = ax.pcolormesh(data, cmap=cmap)

# Plot the borders of each country
for country in cfeature.COASTLINE.geometries():
    if isinstance(country, MultiLineString):
        for line in country:
            ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
    else:
        ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')

# Add a shapefile for Europe
shapefile_path = shapereader.natural_earth(resolution='10m', category='cultural', name='admin_0_countries')
gdf = gpd.read_file(shapefile_path)

# Plot the geometry and name of each country
for country_name, edgecolor, xy_position, text_position in [('Romania', '#0D1130', (26.5, 46), (27, 48.5)),
                                                            ('Netherlands', '#0D1130', (4.5, 52.5), (4.5, 55.5),),
                                                            ('Germany', '#0D1130', (2.5, 47.5), (10.5, 53),),
                                                            ('France', '#0D1130', (2, 47), (2, 48)),
                                                            ('Spain', '#0D1130', (-5, 40), (-5, 42),),
                                                            ('Hungary', '#0D1130', (20, 47.5), (20, 44.5),),
                                                            ('Poland', '#0D1130', (20, 53),  (20, 55)),
                                                            ('United Kingdom', '#0D1130', (-3, 54), (-4, 60),),
                                                            ('Italy', '#0D1130', (12.5, 42), (13, 40),)]:
    country = gdf[gdf['NAME'] == country_name]
    ax.add_geometries(country['geometry'], crs=ccrs.PlateCarree(), facecolor='#0072BB', edgecolor=edgecolor)
    ax.annotate(country_name, xy=xy_position, xytext=text_position, ha='center', va='center', fontsize=10, color='red', fontweight='bold')

ax.text(25.0, 46,   'D1,C1,I5',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(2.0, 52.5,   'D2,I2',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(9.0, 50.5,   'D3,B4',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-1, 45,   'D4,C5,B1',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-7, 39, 'D5,B2,I1',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(18, 46.5, 'C2,I4',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(18, 52, 'C3,I3',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-3.5, 55,   'B3',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(12, 42,   'B5',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))



# Add a title
plt.title('Map of Period 3')
plt.axis('off')

# Show the plot
plt.show()

###################################################
#This is Period4

# Set up the projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map
ax.set_extent([-11, 35, 35, 71], crs=ccrs.PlateCarree())

# Add land and ocean features
ax.add_feature(cartopy.feature.LAND, facecolor='#f5ede1')
ax.add_feature(cartopy.feature.OCEAN, facecolor='#d4edf4')

# Add country borders
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=0.5)

# Define a colormap
cmap = plt.cm.get_cmap('OrRd')

# Create a sample data array (replace with your own data)
data = np.random.rand(10, 10)

# Plot the data using pcolormesh
im = ax.pcolormesh(data, cmap=cmap)

# Plot the borders of each country
for country in cfeature.COASTLINE.geometries():
    if isinstance(country, MultiLineString):
        for line in country:
            ax.add_geometries([line], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')
    else:
        ax.add_geometries([country], ccrs.PlateCarree(), facecolor='none', edgecolor='gray')

# Add a shapefile for Europe
shapefile_path = shapereader.natural_earth(resolution='10m', category='cultural', name='admin_0_countries')
gdf = gpd.read_file(shapefile_path)

# Plot the geometry and name of each country
for country_name, edgecolor, xy_position, text_position in [('United Kingdom', '#0D1130', (-3, 54), (-4, 60),),
                                                            ('Germany', '#0D1130', (2.5, 47.5), (10.5, 53),),
                                                            ('Hungary', '#0D1130', (20, 47.5), (18, 44.5),),
                                                            ('Spain', '#0D1130', (-5, 40), (-5, 42),),
                                                            ('Italy', '#0D1130', (12.5, 42), (13, 40),),
                                                            ('France', '#0D1130', (2, 47), (2, 48)),
                                                            ('Romania', '#0D1130', (26.5, 46), (27, 49))]:
    country = gdf[gdf['NAME'] == country_name]
    ax.add_geometries(country['geometry'], crs=ccrs.PlateCarree(), facecolor='#0072BB', edgecolor=edgecolor)
    ax.annotate(country_name, xy=xy_position, xytext=text_position, ha='center', va='center', fontsize=10, color='red', fontweight='bold')

ax.text(-3.5, 55,   'D1, C3',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(9.0, 50.5,   'D2,B5,C3',  bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(15, 46.5, 'D3,B5,I3',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-7, 39, 'D4,B4,C4',      bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(11, 42,   'D5,C2,I2',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(-1, 45,   'C1,B2,I4',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))
ax.text(25.5, 46,   'B1,I1',    bbox=dict(facecolor='#FEB729', edgecolor='#FEB729'))


# Add a title
plt.title('Map of Period 4')
plt.axis('off')

# Show the plot
plt.show()