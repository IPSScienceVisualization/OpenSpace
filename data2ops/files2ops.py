from data2ops import asset_creator
from data2ops import speck_creator
from data2ops import put_in_dirs

# initialize with name of table and desired file name with NO extension. 
# e.g. a file_name of "test" will create "test.speck" and "test.asset"
def createFiles(Table, file_name, GUI_name = 'default', GUI_path = 'default', source = 'default'):
	asset_creator.makeAsset(file_name, GUI_name, GUI_path)
	speck_creator.makeSpeck(Table, file_name, source)
	#put_in_dirs.moveFiles(file_name)




