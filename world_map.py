import matplotlib.pyplot as plt
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.patches as mpatches

# cd /Users/Baptiste/Documents/PROGRAMMING/Python/Cartopy
# load data
data = pd.read_csv('scores.csv', delimiter=',')

# create initial map shape and object ax
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.set_extent([-180, 180, -90, 90])

# choose type of map
shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

list_CRS = [x+1 for x in range(0,19)]
red_CRS = [0 for x in range(0,19)]
green_CRS = [0 for x in range(0,19)]
blue_CRS = [0 for x in range(0,19)]

# assign color to each country using ISO codes
for country in countries:
    for i in range(0,len(data)):
        for c in list_CRS:
            if (c>10):
                ind_1 = 0
                ind_2 = 1
            else:
                ind_1 = 1
                ind_2 = 0
            red_CRS[c-1] = (ind_1*(c-1)*(255/9) + ind_2*255)/255.
            green_CRS[c-1] = (ind_1*(100+(c-1)*(155/9)) + ind_2*(19-c)*(255/9))/255.
            blue_CRS[c-1] = 0/255.
            if (country.attributes['adm0_a3'] == data['ISO'].iloc[i] and data['dynamic_CRS'].iloc[i] == c):
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                                  facecolor=(red_CRS[c-1],green_CRS[c-1],blue_CRS[c-1]),
                                  label=country.attributes['adm0_a3'])
                                  
                                  
# create the legend using dynamic variable names for CRS01 ... CRS19
for i in range(1,20):
    exec("CRS%02d = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[i-1], green_CRS[i-1], blue_CRS[i-1]))" %i);  
labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
plt.legend([CRS01, CRS02, CRS03, CRS04, CRS05, CRS06, CRS07, CRS08, CRS09, CRS10, CRS11, CRS12, CRS13, CRS14, CRS15, CRS16, CRS17, CRS18, CRS19], labels, loc=3,prop={'size':10}, ncol = 2, fancybox=True,title="CRS Scores")

# show plot
plt.show()

# more information on cartopy here: http://scitools.org.uk/cartopy/
