# Tutorial

This package is used to automatically create the necessary files that will allow you to visualize your datasets in OpenSpace.

### File Types
There are two file types needed to visualize catalog data in Open Space: 

(1) an **asset file**, which, among other things, creates the object -- in this case a Renderable Billboards Cloud -- determines where in the GUI the data goes, initializes several other parameters, and points to the data and texture (image) which will be used to display your set, AND

(2) a **speck file**, which houses the actual information used to visualize your set. In a speck file, the first three columns must be x, y, and z positions, and then subsequent columns are used for any number of other parameters.

This package will automatically create an asset and speck file for your catalog data. It can also create and populate the necessary Open Space directories with your asset and speck and a few other necessary non-varying files. Below, we'll walk through the two main ways this package can be used to get your datasets into OpenSpace.

### 1. STARTING WITH AN ASTROPY TABLE

The first way you can use the package is if your data is in an astropy table. 
```
from astropy.table import Table
table_name = Table(your_data)
```
Before calling the module,  you should make sure that the table only includes position columns (RA, Dec, and, if available, distance or redshift) and whatever parameters you want to be included in the speck file. It will automatically create a speck column for every additional column of your astropy table besides positional columns, so only leave the ones you want.

Once you have your table, you should import the module files2ops from data2ops. (If you're having path issues, an easy trick is to put the data2ops package in the same directory as something that you have no problem importing into python, like numpy.)

```
from data2ops import files2ops
```
Then, you want to call the function createFiles.
```
files2ops.createFiles(Table, file_name, GUI_name = 'default', GUI_path = 'default', source = 'default')
```
You must give it two arguments: the name of your astropy table, and the desired name of your files. (file_name = 'test' will create test.asset and test.speck). You can also initialize it with GUI name, path, and data source. If you don't pass these arguments, then the program will ask for user input. GUI_path should be something like '/Universe/Galaxies'. 

This can be a lot of arguments to remember, so you can also run

```
files2ops.printArgs()
```
