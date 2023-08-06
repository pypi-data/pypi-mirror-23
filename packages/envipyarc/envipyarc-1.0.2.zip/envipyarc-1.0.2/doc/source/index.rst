.. _envipyarc:

******************
ENVI Py for ArcGIS
******************

.. include:: <isonum.txt>

ENVI Py for ArcGIS  provides a Python client library, named envipyarc, to run ENVI analytics provided by ENVI Desktop through ArcMap and ArcGIS Pro.

See http://www.harrisgeospatial.com/ for more details on product offerings.

Usage
=====

ENVI Py for ArcGIS allows users to generate an ArcGIS Python Toolbox containing 
geoprocessing tools (GPTools) associated with tasks provided by ENVI Desktop.

There are three ways to create an ArcGIS Python Toolbox:  

* Through a ENVI Python Toolbox provided as a system toolbox from ArcMap.
* Through a ENVI Python Toolbox provided as a project template from ArcGIS Pro.
* Through a command-line tool, named creategptoolbox, provided in the Python scripts directory.
* Through Python using the Python package, envipyarc.


Python Toolbox
==============

From ArcMap
-----------

Once the Python package is installed, the ENVI Python toolbox becomes available as a system toolbox.

* Launch ArcMap
* Navigate in the Catalog window to Toolboxes |rarr| System Toolboxes |rarr| ENVIManagementTools.pyt |rarr| Create ENVI Toolbox.  Note: If ENVIManagementTools.pyt does not appear in System Toolboxes, connect to the folder located at C:\\Python27\\ArcGIS10.x\\Lib\\site-packages\\envipyarc\\esri\\toolboxes\\ and ENVIManagementTools.pyt can be run from there.
* Double-click on Create ENVI Toolbox, and the tool appears with two required input parameters.
* The first parameter is used to specify the names of one or more ENVI tasks to be wrapped in a GPTool. The second parameter is the location where the toolbox is created. 

.. image:: images/create_envi_toolbox.png

* Click OK, and when the tool finishes generating the new toolbox, navigate to the location specified in Output Toolbox. 
* Double-click on Spectral Index, and the tool appears with two required input parameters. 

.. image:: images/spectral_index.png

* Select an input raster dataset for the first input parameter and an index to run for the second input parameter.

.. image:: images/spectral_index_input.png

* Click OK, and when the tool finishes processing, the result appear in ArcGIS.



From ArcGIS Pro
---------------

Once the Python package is installed, the ENVI Management Tools toolbox can be added to a project in ArcGIS Pro. 

* Launch ArcGIS Pro
* Select or create new project to work with ENVI Tasks
* To setup for the display of results, select the Insert tab and click on New Map
* In Project pane, select Toolboxes, right-click and select Add Toolbox
* Navigate to C:\\Python34\\Lib\\site-packages\\envipyarc\\esri\\toolboxes, and select ENVIManagementTools.pyt
* Expand the ENVI Management Tools toolbox, and double-click on Create ENVI Toolbox.
* The tool appears with two required input parameters. The first parameter is used to specify the names of one or more ENVI tasks to be wrapped in a GPTool. The second parameter is the location where the toolbox will be created.

.. image:: images/create_envi_toolbox_arcgispro.png

* Click run and when the tool finishes generating a new toolbox, navigate in the Project tab to the location specified in Output Toolbox. 
* Double-click on Spectral Index. The tool will appear with two required parameters, and one optional parameter. 

.. image:: images/spectral_index_arcgispro.png

* Select an input raster dataset for the first input parameter and an index to run for the second input parameter. 

.. image:: images/spectral_index_input_arcgispro.png

* Click Run, and when the tool finishes processing, a result will appear in ArcGIS Pro when a basemap is enabled.


From Command-line
=================

createenvitoolbox.py is a command-line tool in the envipyarc package used to create a Python toolbox that wraps ENVI tasks.

For ArcMap the script is located at C:\\Python27\\ArcGIS10.x\\scripts.

For ArcGIS Pro the script is located at C:\\Python34\\scripts.

To display the help, navigate to the scripts directory and run the --help option::

    $ createenvitoolbox.py --help

To create a Python toolbox with the ENVI Tasks SpectralIndex and ISODATAClassification, run this command.::

    $ createenvitoolbox.py SpectralIndex ISODATAClassification --output C:\\ENVITasks.pyt

The toolbox name is the same as the engine name if no option is provided.
The output directory defaults to the current directory if no option is provided.


From Python
===========

The create_toolbox member method is the first way to create a toolbox from a Python module::

    >>> from envipyengine import Engine
    >>> engine = Engine('ENVI')

Now, construct a list of tasks to add to the toolbox::

    >>> task_list = [engine.task('SpectralIndex'), engine.task('ISODATAClassification')]

Next, instantiate a GPToolbox class for creating a toolbox::

    >>> from envipyengine import GPToolbox
    >>> envi_toolbox = GPToolbox()
    >>> toolbox_file = envi_toolbox.create_toolbox(task_list, 'c:\\my_envi_tools')

The create_toolbox method returns the filename of the toolbox, which can then be used by arcpy to import the toolbox::

    >>> import arcpy
    >>> arcpy.ImportToolbox(toolbox_file)
	
Run the toolbox.

    >>> input_raster = 'C:/Program Files/Harris/ENVI54/data/qb_boulder_msi'
    >>> index = 'Normalized Difference Vegetation Index'
    >>> result = arcpy.SpectralIndex_ENVI(input_raster,index)
    >>> print(result)


Configure ENVI Environment Tool
===============================

In order to run toolbox tools, you must configure ENVI Py to be able to run ENVI.

From ArcMap
-----------

* Launch ArcMap
* Navigate in the Catalog window to Toolboxes |rarr| System Toolboxes |rarr| ENVIManagementTools.pyt |rarr| Create ENVI Toolbox.  Note: If ENVIManagementTools.pyt does not appear in System Toolboxes, connect to the folder located at C:\\Python27\\ArcGIS10.x\\Lib\\site-packages\\envipyarc\\esri\\toolboxes\\ and ENVI Management Tools.pyt can be run from there.
* Double-click on Configure ENVI Environment, and a tool is opened that you can use to configure ENVI Py

.. image:: images/configure_envi_environment.png

* The first field - Engine Location - is required. This must be the full path of the 'taskengine.exe' in your ENVI distribution. This file is located at <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe
* Next, you may specify whether ENVI will have the ability to compile .pro files. This will depend on what you ENVI license allows. If this is not checked, the ENVI code you wish to run must be packaged as .sav files.
* Finally, if you wish to specify one or more directories that contain custom ENVI code, you can do so here. If you wish to specify more than one directory be sure to use a semi-colon to separate the individual directory paths.

From ArcPro
-----------

* Launch ArcGIS Pro
* Select or create new project to work with ENVI Tasks
* To setup for the display of results, select the Insert tab and click on New Map
* In Project pane, select Toolboxes, right-click and select Add Toolbox
* Navigate to C:\\Python34\\Lib\\site-packages\\envipyarc\\esri\\toolboxes, and select ENVIManagementTools.pyt
* Expand the ENVI Management Tools toolbox, and double-click on Configure ENVI Environment tool.

.. image:: images/configure_envi_environment_arcgispro.png

* The first field - Engine Location - is required. This must be the full path of the 'taskengine.exe' in your ENVI distribution. This file is located at <ENVI_INSTALL_DIR>\\IDLXX\\bin\\bin.x86_64\\taskengine.exe
* Next, you may specify whether ENVI will have the ability to compile .pro files. This will depend on what you ENVI license allows. If this is not checked, the ENVI code you wish to run must be packaged as .sav files.
* Finally, if you wish to specify one or more directories that contain custom ENVI code, you can do so here. If you wish to specify more than one directory be sure to use a semi-colon to separate the individual directory paths.



API Documentation
=================

.. toctree::
   :maxdepth: 2

   api




