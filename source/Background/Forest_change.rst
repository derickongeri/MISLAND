Forest Change
=============

Forest Gain/Loss
_________________
The quantification of the forest gain/loss hotspots will be based on pre-existing high-resolution global maps derived from Hansen Global Forest change dataset that can be accessed using `Google Earth Engine API`_. 

    .. _Google Earth Engine API: https://earthenginepartners.appspot.com/science-2013-global-forest

The maps are produced from time-series analysis of Landsat images characterizing forest extent and change over time.

Forest Carbon Emission
________________________



Forest Fire Risk
_________________



Forest Fires
_____________
Burnt areas and forest fires will be highlighted and mapped out form remotely sensed Landsat/Sentinel data using the Normalized Burn Ratio (NBR). NBR is designed to highlight burned areas and estimate burn severity. It uses near-infrared (NIR) and shortwave-infrared (SWIR) wavelengths. Before fire events, healthy vegetation has very high NIR reflectance and a low SWIR reflectance. In contrast, recently burned areas show low reflectance in the NIR and high reflectance in the SWIR band.

The NBR will be calculated for Landsat/Sentinel images before the fire (pre-fire NBR) and after the fire (post-fire NBR). The difference between the pre-fire NBR and the post-fire NBR referred to as delta NBR (dNBR) is computed to highlight the areas of forest disturbance by fire event.

Classification of the dNBR will be used for burn severity assessment, as areas with higher dNBR values indicate more severe damage whereas areas with negative dNBR values might show increased vegetation productivity. dNBR will be classified according to burn severity ranges proposed by the United States Geological Survey(USGS)

.. figure:: ../_static/Images/Forest_fires.png
    :width: 700
    :align: center
    :height: 500
    :alt: Forest fires methodology
    :figclass: align-center

    Sammury methodology for conputing Burnt Areas

.. toctree::
   :maxdepth: 3
