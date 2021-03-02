Calculate Vegetation Loss/Gain indicators
==========================================

To compute vegetation loss/gain on the service platform,

1. On the services menu, select the 'VEGETATION GAIN/LOSS' option 

.. figure:: ../_static/Images/vegetation_gain_loss.png
    :width: 790
    :align: center
    :height: 45
    :alt: Vegetation gain/loss service
    :figclass: align-center

    Finding the forest change service

2. If the selected region is a large area, the user will be prompted to select a smaller region. Select a smaller region on the 'Select Country' dialog on the top left conner of the dashboard

.. figure:: ../_static/Images/vegetation_gain_loss1.png
    :width: 780
    :align: center
    :height: 206
    :alt: select country
    :figclass: align-center

    seleting a region to compute vegetation gain/loss

.. note::
   Selection of a smaller regin optimizes the computation time and ensures that the service does not time-out. If a large area is selected, users will be notifed by a pop up on the top right conner of the site. Computation of large ares is still under development and will be available in later versions of the service.

.. figure:: ../_static/Images/vegetation_gain_loss2.png
    :width: 360
    :align: center
    :height: 99
    :alt: warning
    :figclass: align-center

    Pop-up notification when large area is selected.

3. Next, select the start and end period for which the vegetation loss and gain will be computed.

.. figure:: ../_static/Images/vegetation_gain_loss3.png
    :width: 350
    :align: center
    :height: 115
    :alt: vegetation gain/loss
    :figclass: align-center

    Vegetation gain/loss outputs

To compute vegetation indices using Landsat derived vegetation indices, 

1. On the services menu, select the 'VEGETATION GAIN/LOSS' option, and under the 'Source' dropdown menu, select Landsat 7 option

.. figure:: ../_static/Images/Service/landsat.png
    :width: 400
    :align: center
    :height: 187
    :alt: Vegetation gain/loss service
    :figclass: align-center

    Selecting the Landsat-derived vegetation index option

2. On the 'Veg index' dropdown, select the vegetation index to compute and select the start and end period

.. figure:: ../_static/Images/Service/vegindex.png
    :width: 428
    :align: center
    :height: 195
    :alt: select vegetation index
    :figclass: align-center

    Choosing the vegetation index to compute

The map and computed statistics will be displayed on the map panel and summary pannel respectively.

.. figure:: ../_static/Images/Service/landsat_vegetation_loss.png
    :width: 712
    :align: center
    :height: 332
    :alt: register
    :figclass: align-center

    Landsat derived vegetation loss and gain output

.. toctree::
   :maxdepth: 3