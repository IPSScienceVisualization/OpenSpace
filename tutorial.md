# Tutorial

This package is used to automatically create the necessary files that will allow you to visualize your datasets in OpenSpace.

### File Types
There are two file types needed to visualize catalog data in Open Space: 
(1) an **asset file**, which, among other things, creates the object -- in this case a Renderable Billboards Cloud -- determines where in the GUI the data goes, initializes several other parameters, and points to the data and texture (image) which will be used to display your set, AND
(2) a **speck file**, which houses the actual information used to visualize your set. In a speck file, the first three columns must be x, y, and z positions, and then subsequent columns are used for any number of other parameters.

This package will automatically create an asset and speck file for your catalog data. It can also create and populate the necessary Open Space directories with your asset and speck and a few other necessary non-varying files. Below, we'll walk through the two main ways this package can be used to get your datasets into OpenSpace.

### 1. STARTING WITH AN ASTROPY TABLE

The first way you can use the package is if your data is in an astropy table.
