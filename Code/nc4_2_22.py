#Import data
import netCDF4 as nc
#Copy the path from the file 
fn = '/Users/justinpratama/Desktop/Groundwater_Research/Data/GRACEDADM_CLSM0125US_7D.A20230220.020.nc4'
#Obtain the dataset
ds = nc.Dataset(fn)
#print the dataset
print(ds)