# guided by https://tutorial.xarray.dev/fundamentals/03.2_groupby_with_xarray.html
import xarray as xr

# load ncdf file to xarray
ds = xr.open_mfdataset("data1/*_wind_helgoland.nc")# requires `pip install dask`

from numpy import sqrt
# add absolute wind speed
ds["windspeed"] = sqrt(ds.u10*ds.u10 + ds.v10*ds.v10)

xr.save_mfdataset([ds], ["data1/helgoland_wind.nc"], mode='w')