# Tutorial

This package is used to automatically create the necessary files that will allow you to visualize your datasets in OpenSpace.

## Introduction
There are two file types needed to visualize catalog data in Open Space: 

(1) an **asset file**, which, among other things, creates the object -- in this case a Renderable Billboards Cloud -- determines where in the GUI the data goes, initializes several other parameters, and points to the data and texture (image) which will be used to display your set, AND

(2) a **speck file**, which houses the actual information used to visualize your set. In a speck file, the first three columns must be x, y, and z positions, and then subsequent columns are used for any number of other parameters.

This package will automatically create an asset and speck file for your catalog data. With a small modification, it can also create and populate the necessary Open Space directories with your asset and speck and a few other necessary non-varying files. Below, we'll walk through the two main ways this package can be used to get your datasets into OpenSpace.

## Using the Package

#### 1. Starting with an Astropy Table

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
This will create an asset and speck file and save them in your current directory! You must give it two arguments: the name of your astropy table, and the desired name of your files. (file_name = 'test' will create test.asset and test.speck). You can also initialize it with GUI name, path, and data source. If you don't pass these arguments, then the program will ask for user input. GUI_path should be something like '/Universe/Galaxies'. 

This can be a lot of arguments to remember, so you can also run

```
files2ops.printArgs()
```
which  will return a list of createFiles's arguments. 

#### 2. Starting with a Vizier Catalog ID

The package can also create asset and speck files straight from a Vizier catalog (http://vizier.u-strasbg.fr/viz-bin/VizieR).

*(Note: This requires the astroquery.vizier module to be installed on your machine to remotely access Vizier. If you don't have astroquery, it can be easily pip or conda installed: https://astroquery.readthedocs.io/en/latest/)*

In this case, you import a module called viz2ops.

```
from data2ops import viz2ops as vz
```
And then you call the function OS_from_viz.

```
vz.OS_from_viz(viz_ID, file_name, extraCols = ['default'], GUI_name = 'default', GUI_path = 'default', use_redshift = False)
```
Again, this function has two necessary arguments and several optional arguments. **viz_ID** is, of course, the Vizier ID (something like 'VII/269/dr9q'), and **file_name** is again your desired name for your speck and asset files. 

**extraCols** is a list of any columns from the Vizier table BESIDES RA, Dec, and redshift or distance if available, that you would like to be included in your speck file. If no extraCols argument is passed, then it will prompt you for user input. 

If **use_redshift** is set to False, then if the program finds a redshift column but not a distance column, it will ask you if you'd like it to create a distance column from those redshifts. If you set it to True, then it will do so automatically.

Again, if you need a reminder of the module's arguments, you can run

```
vz.printArgs()
```
*Note: This code won't work with Python 2.7 or older, since it uses the command 'input', not 'raw_input' like older versions of Python. If you have an older Python version and don't want to update, replace every instance of 'input' with 'raw_input'.*

## Creating And Populating Directories

In the code in this repository, there is a file called put_in_dirs.py. If you'd like the package to automatically create directories in the right path in Open Space and fill them with your asset, speck, and other files, then you just need to follow these two steps:

1. Open put_in_dirs.py and edit 'start_path_OS' to Open Space's path on your machine. For example: 'C:/Users/your_name/Desktop/OpenSpace-0.12.0/'.

2. Open files2ops and un-comment out (delete the '#') in front of the command 'put_in_dirs.moveFiles(file_name)'.

Then, running either of the two modules above should automatically create and fill the Open Space directories. If you're having path issues, you can replace the variables in put_in_dirs that automatically scrape the paths with your machine's paths.

This should allow you to use the package to visualize your catalog data! If you're still having issues, check out the example notebooks in this repository or feel free to email me at archie.kinnane@gmail.com.

