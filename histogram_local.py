# guided by https://tutorial.xarray.dev/fundamentals/03.2_groupby_with_xarray.html
import xarray as xr

# load ncdf file to xarray
ds = xr.open_mfdataset("data1/*_wind_helgoland.nc")# requires `pip install dask`

from numpy import sqrt
ds["windspeed"] = sqrt(ds.u10*ds.u10 + ds.v10*ds.v10)

# example coordinates: Helgoland lat=54.1825 lon=7.885278, select nearest points
lat=54.25
lon=8

# plot histogram of wind speeds
import matplotlib.pyplot as plt

beaufort = [0,0.3,1.6,3.4,5.5,8.0,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
ds.windspeed.sel(latitude=lat, longitude=lon, method="nearest").plot.hist(bins=beaufort,edgecolor="k")

plt.savefig("histogram.pdf")