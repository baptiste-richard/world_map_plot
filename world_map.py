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
                                  
                                  
# create the legend
CRS1 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[0], green_CRS[0], blue_CRS[0]))
CRS2 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[1], green_CRS[1], blue_CRS[1]))
CRS3 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[2], green_CRS[2], blue_CRS[2]))
CRS4 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[3], green_CRS[3], blue_CRS[3]))
CRS5 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[4], green_CRS[4], blue_CRS[4]))
CRS6 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[5], green_CRS[5], blue_CRS[5]))
CRS7 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[6], green_CRS[6], blue_CRS[6]))
CRS8 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[7], green_CRS[7], blue_CRS[7]))
CRS9 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[8], green_CRS[8], blue_CRS[8]))
CRS10 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[9], green_CRS[9], blue_CRS[9]))
CRS11 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[10], green_CRS[10], blue_CRS[10]))
CRS12 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[11], green_CRS[11], blue_CRS[11]))
CRS13 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[12], green_CRS[12], blue_CRS[12]))
CRS14 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[13], green_CRS[13], blue_CRS[13]))
CRS15 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[14], green_CRS[14], blue_CRS[14]))
CRS16 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[15], green_CRS[15], blue_CRS[15]))
CRS17 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[16], green_CRS[16], blue_CRS[16]))
CRS18 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[17], green_CRS[17], blue_CRS[17]))
CRS19 = mpatches.Rectangle((0, 0), 0.25, 0.25, facecolor=(red_CRS[18], green_CRS[18], blue_CRS[18]))
labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
plt.legend([CRS1, CRS2, CRS3, CRS4, CRS5, CRS6, CRS7, CRS8, CRS9, CRS10,CRS11, CRS12, CRS13, CRS14, CRS15, CRS16, CRS17, CRS18, CRS19], labels, loc=3,prop={'size':10}, ncol = 2, fancybox=True,title="CRS Scores")

# show plot
plt.show()

# more information on cartopy here: http://scitools.org.uk/cartopy/
