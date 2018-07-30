from data2ops import files2ops
from astropy.table import Table
global viz_key
viz_key = 0
global vizID

def printArgs():
    print("OS_from_viz(viz_ID, file_name, extraCols = ['default'], GUI_name = 'default', GUI_path = 'default', use_redshift = False)")

def OS_from_viz(viz_ID, file_name, extraCols = ['default'], GUI_name = 'default', GUI_path = 'default', use_redshift = False):
	from astroquery.vizier import Vizier
	v = Vizier()
	v.ROW_LIMIT = -1    
	Cats = v.get_catalogs(viz_ID)
	grbCat=Cats[0]
	grbAstroCat = Table(grbCat)
	global colNames 
	colNames = ["RAJ2000", "DEJ2000"]
	if extraCols == ['default']:
		otherCols(grbAstroCat)
	else:
		for i in range(len(extraCols)):
			colNames.append(extraCols[i])
	hasDistance(grbAstroCat, use_redshift)
	deleteCols(grbAstroCat)
#	global viz_key 
	viz_key= 1996
	global vizID
	vizID = viz_ID
	#guiforasset = GUI_name
	files2ops.createFiles(grbAstroCat, file_name, GUI_name, GUI_path, "Vizier:" + viz_ID)
        
#def RAandDec(TableName):
#    if 'RAJ2000' and 'DEJ2000' in TableName.colnames:
#        TableName.rename_column('RAJ2000', 'ra')
#        TableName.rename_column('DEJ2000', 'dec')
#    elif 'RAB1975' and 'DEB1975' in TableName.colnames:
#        from astropy.coordinates import SkyCoord, FK5
#        coordsCol=SkyCoord(TableName['RAB1975'],TableName['DEB1975'],unit=(u.degree, u.degree), distance = Distance(TableName['distance'], u.pc), frame='icrs')
        
        
        
def otherCols(TableName):
	upperCaseCols(TableName)
	print (TableName.colnames)
	global col_input
	col_input = 0
	while col_input != '1':
		col_input = input("Besides RA and Dec, what Vizier columns -- listed above -- would you like to retain? Type 1 if you are done. ")
		if col_input != '1':
			col_upper = str(col_input).upper()
			colNames.append(col_upper)
		print (colNames)
        
def upperCaseCols(TableName):
    for i in range(len(TableName.colnames)):
        if TableName.colnames[i] != str(TableName.colnames[i]).upper():
            newname = str(TableName.colnames[i]).upper()
            TableName.rename_column(TableName.colnames[i], newname)
        
def hasDistance(TableName, use_redshift):
    upperCaseCols(TableName)
    if 'DISTANCE' not in TableName.colnames and 'DIST' not in TableName.colnames:
        manual_distance = input('Distance column not found. If there is one, input name manually. Else, type 1. ')
        if manual_distance != '1':
            TableName.rename_column(manual_distance, 'DISTANCE')
        elif 'REDSHIFT' in TableName.colnames:
            if use_redshift == True:
                TableName.rename_column('REDSHIFT', 'Z')
                colNames.append('Z')
            else:
                q1 = input("Redshift found. Use to make distance column? (y/n) " )
                if q1 == 'y':
                    TableName.rename_column('REDSHIFT', 'Z')
                    colNames.append('Z')
                else:
                    print('Data placed at 100 Mpc.')      
        elif 'Z' in TableName.colnames:
            if use_redshift == True:
                colNames.append('Z')
            else:
                q1 = input("Redshift found. Use to make distance column? (y/n) " )
                if q1 == 'y':
                    colNames.append('Z')
                else:
                    print('Data placed at 100 Mpc.') 
        else:
            redshift_name = input("Redshift column also not found. If it exists, input name manually. Else, type 1 and all data will be placed at distance = 100 Mpc." )
            if redshift_name != '1':
                TableName.rename_column(str(redshift_name).upper(), 'Z')
                colNames.append('Z')
            else:
                good = 1
        
def deleteCols(TableName):
	for i in range(len(TableName.colnames) - 1, -1, -1):
		if TableName.colnames[i] not in colNames:
			TableName.remove_column(TableName.colnames[i])
            
class NameList(object):
    def __init__(self, names):
        self.names = names

    def __contains__(self, name): # implements `in`
        return name.lower() in (n.lower() for n in self.names)

    def add(self, name):
        self.names.append(name)