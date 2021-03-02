.. ossldmsdocumentation documentation master file, created by
   sphinx-quickstart on Thu Oct 15 11:15:20 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
MISLAND North Africa - Monitoring Integrated Service for Land Degradation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	.. image:: ../source/_static/Images/LDMS.png
	   :height: 277
	   :width: 550
	   :alt: LocateIT

MISLAND-North Africa is an operational instrument relying on the international standards for reporting SDG 15.3.1 and technical approaches allowing the delivery of regular information on vegetation cover gain/loss to decision makers and environmental agencies at the first place.

The core-service provides land degradation indicators for six North African Countries at two levels:

	- At the regional level(North Africa action zone) where low and medium resolution EO are used.

	- At the pilot site level, where(customized indicators) can be developed, using medium resoultion data(landsat time series imagery and derived vegetation indices, combined with different satellite-derived climate data)

.. note::

   You can download the `PDF Version of this doucument`_ here.

   .. _PDF Version of this doucument: https://locateit-oss-ldms.readthedocs.io/_/downloads/en/latest/pdf/

.. toctree::
   :maxdepth: 3
   :caption: About

   /Introduction/general_information
   /Introduction/data
   /Introduction/Layers

.. toctree::
   :maxdepth: 4
   :caption: Background

   Background/LD_indicators
   Background/SDG_indicators
   Background/Forest_Change

.. toctree::
   :maxdepth: 3
   :caption: Web Service Guide

   Service/Service_Guide
   Service/Calculate_SDG
   Service/Calculate_vegetationloss
   Service/Calculate_Forestloss
   Service/Calculate_Medalus
   Service/Download_results
   Service/Download_data

.. toctree::
   :maxdepth: 3
   :caption: Qgis Plugin Guide

   Qgis_Plugin/plugin_development
   Qgis_Plugin/before_installing
   Qgis_Plugin/installing
   Qgis_Plugin/Registration
   Qgis_Plugin/Calculate_sdg15
   Qgis_Plugin/Calculate_vegetation
   Qgis_Plugin/Calculate_forest
   Qgis_Plugin/Calculate_medalus
   Qgis_Plugin/gee_tasks
   Qgis_Plugin/load_data
   Qgis_Plugin/Download_data
   Qgis_Plugin/visualization

.. toctree::
   :maxdepth: 3
   :caption: QGIS Plugin Training Material

   Qgis_Plugin/sdg_15_training
   Qgis_Plugin/vegetation_degradation_training

==================
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

