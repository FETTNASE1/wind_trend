import cdsapi
import xarray as xr

c = cdsapi.Client()

for year in range(1940,2024):
    filename = str(year) + '_' + 'wind_helgoland.nc'
    try:
        xr.open_dataset(filename)
        print("file ", filename, " exists\n")
    except:
        print("request file ", filename, "\n")
        c.retrieve(
                'reanalysis-era5-single-levels',
                {
                    'product_type': 'reanalysis',
                    'format': 'netcdf',
                    'variable': [
                        '10m_u_component_of_wind', '10m_v_component_of_wind',
                        ],
                    'year': str(year),
                    'month': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 
                    'day': [
                        '01', '02', '03',
                        '04', '05', '06',
                        '07', '08', '09',
                        '10', '11', '12',
                        '13', '14', '15',
                        '16', '17', '18',
                        '19', '20', '21',
                        '22', '23', '24',
                        '25', '26', '27',
                        '28', '29', '30',
                        '31',
                        ],
                    'time': [
                        '00:00', '01:00', '02:00',
                        '03:00', '04:00', '05:00',
                        '06:00', '07:00', '08:00',
                        '09:00', '10:00', '11:00',
                        '12:00', '13:00', '14:00',
                        '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00',
                        '21:00', '22:00', '23:00',
                        ],
                    'area': [
                        55, 7, 54,
                        8,
                        ],
                    },
                filename)
