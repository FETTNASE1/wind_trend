# guided by https://tutorial.xarray.dev/fundamentals/03.2_groupby_with_xarray.html
import xarray as xr

# load ncdf file to xarray
ds = xr.open_mfdataset("data1/*_wind_helgoland.nc")# requires `pip install dask`

from numpy import sqrt
# add absolute wind speed
ds["windspeed"] = sqrt(ds.u10*ds.u10 + ds.v10*ds.v10)

# use of xarray.polyfit: https://stackoverflow.com/a/60517358
import numpy as np

lat = 54
lon = 7.5

x = np.array([t.item() for t in ds.time.values])# t.item() will cast numpy.datetime64 to datetime.datetime https://stackoverflow.com/a/69804526
y = ds.windspeed.sel(latitude=lat, longitude=lon, method="nearest").values

pf = np.polyfit(x,y,1)# fit polynomial of degree 1

from matplotlib import pyplot as plt

plt.scatter(x, y, label="Data")
plt.plot(x, pf[0]*x + pf[1], "r-", label="lin. Fit")

plt.legend()

plt.savefig("lat" + str(lat) + "lon" + str(lon) + "linFit.pdf", bbox_inches="tight")