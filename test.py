# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:28:08 2021

@author: Pamit
"""

import numpy as np
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist  
from matplotlib import pyplot as plt
from skimage import exposure
#%%
img = rasterio.open("data/phr_xs_osr_mipy.tif"); 

#No. of bands the image has
num_bands = img.count 
print('Number of bands in image: {n}\n'.format(n=num_bands)) 
#No. of rows and columns
rows, cols= img.shape 
print('Image size is: {r} rows x {c} columns\n'.format(r=rows, c=cols))
#%%
#Using histogram tool
show_hist( img, bins=256, lw=0.0 , stacked=False, alpha=0.3, 
histtype='stepfilled',title="Histogram",label=("BLUE","GREEN","RED","NIR"))

#Extracting Each Spectracl Band
blue= img.read(1).astype(float) 
green= img.read(2).astype(float)
red= img.read(3).astype(float) 
nir = img.read(4).astype(float)

#%%
#Statistics for the diﬀerent bands
band_mean = np.mean(nir) 
band_min = np.amin(nir) 
band_max = np.amax(nir) 
band_stddev = np.std(nir) 
print("nir")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))

#Plotting the Different Bands
plt.imshow(nir, cmap='gray') 
#%%
#Statistics for the diﬀerent bands
band_mean = np.mean(red) 
band_min = np.amin(red) 
band_max = np.amax(red) 
band_stddev = np.std(red) 
print("red")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))

#Plotting the Different Bands
plt.imshow(red, cmap='gray') 
#%%
#Statistics for the diﬀerent bands
band_mean = np.mean(green) 
band_min = np.amin(green) 
band_max = np.amax(green) 
band_stddev = np.std(green) 
print("green")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))

#Plotting the Different Bands
plt.imshow(green, cmap='gray') 
#%%
#Statistics for the diﬀerent bands
band_mean = np.mean(blue) 
band_min = np.amin(blue) 
band_max = np.amax(blue) 
band_stddev = np.std(blue) 
print("blue")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))

#Plotting the Different Bands
#plt.imshow(blue, cmap='gray') 

#%%
#Nir
p2, p98 = np.percentile(nir, (2, 98))
rescaled_nir = exposure.rescale_intensity(nir, in_range=(p2, p98))

band_mean = np.mean(rescaled_nir) 
band_min = np.amin(rescaled_nir) 
band_max = np.amax(rescaled_nir) 
band_stddev = np.std(rescaled_nir) 
print("rescaled_nir")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))
plt.title('Histogram NIR')
plt.hist(rescaled_nir.ravel(), 256, [0, 1])
plt.show()

#%%

#Red
p2, p98 = np.percentile(nir, (2, 98))
rescaled_red = exposure.rescale_intensity(red, in_range=(p2, p98))

band_mean = np.mean(rescaled_red) 
band_min = np.amin(rescaled_red) 
band_max = np.amax(rescaled_red) 
band_stddev = np.std(rescaled_red) 
print("rescaled_red")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))
plt.title('Histogram Red')
plt.hist(rescaled_red.ravel(), 256, [0, 1])
plt.show()

#%%

#Green
p2, p98 = np.percentile(nir, (2, 98))
rescaled_green = exposure.rescale_intensity(green, in_range=(p2, p98))

band_mean = np.mean(rescaled_green) 
band_min = np.amin(rescaled_green) 
band_max = np.amax(rescaled_green) 
band_stddev = np.std(rescaled_green) 
print("rescaled_green")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))
plt.title('Histogram Green')
plt.hist(rescaled_green.ravel(), 256, [0, 1])
plt.show()

#%%

#blue
p2, p98 = np.percentile(nir, (2, 98))
rescaled_blue = exposure.rescale_intensity(blue, in_range=(p2, p98))

band_mean = np.mean(rescaled_blue) 
band_min = np.amin(rescaled_blue) 
band_max = np.amax(rescaled_blue) 
band_stddev = np.std(rescaled_blue) 
print("rescaled_blue")
print('Band range: {minimum} - {maximum}'.format(maximum=band_max,minimum=band_min))
print('Band mean, stddev: {m}, {s}\n'.format(m=band_mean,s=band_stddev))
plt.title('Histogram Blue')
plt.hist(rescaled_blue.ravel(), 256, [0, 1])
plt.show()

#%%


