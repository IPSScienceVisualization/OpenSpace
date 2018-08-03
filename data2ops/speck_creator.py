from astropy import units as u
from astropy.coordinates import SkyCoord, Distance
from astropy.table import Table, Column
from astropy.cosmology import Planck15
import numpy



# create speck file
def makeSpeck(Table, file_name, datasource = 'default'):
#	global datasource2
	if datasource == 'default':
		datasource = input("What is the data source? e.g. SDSS DR8 ") #getSpeckinfo()
#	else:
#		datasource = datasource
	fixColumns(Table)
	checkNegDist(Table)
	makeCoordsCol(Table)
	makeXYZcols()
	addDataCols(Table)
	from datetime import date
	today = str(date.today())
    
	f= open(file_name + ".speck","w+")
	f.write(
    "# File created using data from " + datasource + "\r\n" +
    "# Adler Planetarium \r\n" +
    "# Prepared on: " + today + "\r\n")
	for i in range(len(dataCols) - 3):
		f.write(
			"datavar %d "  %i + dataCols[i + 3].name + "\r\n"
		)

	for i in range(0, len(dataCols[0])):
		for j in range(len(dataCols)):
			if type(dataCols[j][i]) == str:
				f.write(str(dataCols[j][i]))
               # numpy.float64 or type(dataCols[i][j]) == numpy.float32 or type(dataCols[i][j]) == float:
			else:
				f.write("%.3f" %dataCols[j][i])
			if j != len(dataCols):
				f.write(" ")
		f.write("\r\n")

	f.close()
	

def getSpeckinfo():
#	global datasource2 
	datasource = input("What is the data source? e.g. SDSS DR8 ")

def upperCaseCols(TableName):
    for i in range(len(TableName.colnames)):
        newname = str(TableName.colnames[i]).upper()
        TableName.rename_column(TableName.colnames[i], newname)
    
#set column names     
def fixColumns(TableName):
    upperCaseCols(TableName)
    if 'RA' in TableName.colnames:
        good = 1
    elif 'RAJ2000' in TableName.colnames:
        TableName.rename_column('RAJ2000', 'RA')
    else:
        print('Could not find RA column')
    
    if 'DEC' in TableName.colnames:
        good = 1
    elif 'DECLINATION' in TableName.colnames:
        TableName.rename_column('DECLINATION', 'DEC')
    elif 'DEJ2000' in TableName.colnames:
        TableName.rename_column('DEJ2000', 'DEC')
    else:
        print('Could not find dec column')

    if 'DISTANCE' in TableName.colnames:
        good = 1
    elif 'DIST' in TableName.colnames:
        TableName.rename_column('DIST', 'DISTANCE')
    elif 'Z' in TableName.colnames:
        TableName.add_column(Column(Planck15.comoving_distance(TableName['Z']),name='DISTANCE'))
        TableName.remove_column('Z')
    elif 'REDSHIFT' in TableName.colnames:
        TableName.add_column(Column(Planck15.comoving_distance(TableName['REDSHIFT']),name='DISTANCE'))
        TableName.remove_column('REDSHIFT')
    else:
        TableName['DISTANCE'] = 100 * 10e6 * u.pc
        #.add_column(Column((TableName['ra']/TableName['ra']) * 100 * 10e6 * u.pc, name = 'distance'))
        print('Could not find distance or redshift column, placed all data at 100 Mpc')


def checkNegDist(TableName):
	for i in range(len(TableName) - 1, -1, -1):
		if TableName['DISTANCE'][i] < 0:
			TableName.remove_row(i)
            
#make SkyCoord
def makeCoordsCol(TableName):
	global coordsCol
	coordsCol=SkyCoord(TableName['RA'],TableName['DEC'],unit=(u.degree, u.degree),distance=Distance(TableName['DISTANCE'],u.pc),frame='icrs')
	

#make x, y, z columns using SkyCoord
def makeXYZcols():
	global dataCols 
	dataCols = [
		Column(coordsCol.galactic.cartesian.x/(1e6*u.pc), name = 'x'), # x coord in Mpc, galactic frame
		Column(coordsCol.galactic.cartesian.y/(1e6*u.pc), name = 'y'), # y coord in Mpc, galactic frame
		Column(coordsCol.galactic.cartesian.z/(1e6*u.pc), name = 'z') # z coord in Mpc, galactic frame
    ] 
		

# add rest of data       
def addDataCols(TableName):
	for i in range(len(TableName.colnames)):
		if TableName.colnames[i] != 'RA' and TableName.colnames[i] != 'DEC':
			dataCols.append(TableName[TableName.colnames[i]])

  
