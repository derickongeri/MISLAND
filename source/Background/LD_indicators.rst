===========================
Land Degradation Indicators
===========================

.. contents::

-------------------
SDG15.3.1 Indicator
-------------------

As part of the Sustainable development Goals(SDGs), SDG 15 is to: “Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forest, combat desertification, and halt and reverse land degradation and halt biodiversity loss”

Target 15.3 aims to: “By 2030, combat desertification, restore degraded land and soil, including land affected by desertification, drought, floods, and strive to achieve land degradation-neutral world”

The indicator used to assess the progress of each SDG target is the 15.3.1 indicator: “Proportion of land that is degraded over total land area’’

The basic land degradation indicators include three main sub-indicators of the SDG target 15.3.1 (proportion of land that is degraded over the total land area). As the custodian agency of SDG 15.3, the United Nations Convention to Combat Desertification (UNCCD) has developed recommendations/Good practice guide on how to compute SDG indicator 15.3.1  from 3 sub-indicators:

	- Vegetation productivity
	- Landcover
	- Soil Organic carbon


.. figure:: ../_static/Images/sdg.png
    :width: 500
    :align: center
    :height: 300
    :alt: sdg 15.3.1 sub-indicators
    :figclass: align-center

    SDG 15.3.1 Indicators

-------------------------
SDG 15.3.1 Sub-indicators
-------------------------

Productivity
------------
Land productivity is the biological productive capacity of the land (i.e. the ability to produce food, fibre and fuel that sustain life). For easy interpretation the annual mean NDVI values at the pixel level will be used to assess three measures of change as summarized below:

.. figure:: ../_static/Images/sdgmethodology.png
    :width: 700
    :align: center
    :height: 500
    :alt: sdg 15.3.1 Land Productivity
    :figclass: align-center

    Sammury methodology for conputing Land Productivity

Landcover
---------
Monitoring of Land Use and Land Cover Changes (LULCCs) at both regional and local scales presents a major opportunity for identifying areas threatened by land degradation where mitigation measures should be taken. Traditionally, LULCCs have been interpreted by distinguishing between two transformation types: conversion and modification.

.. figure:: ../_static/Images/lulc.png
    :width: 700
    :align: center
    :height: 500
    :alt: sdg 15.3.1 Land Cover change
    :figclass: align-center

    Sammary methodology for computing land cover change

Carbon-stocks
-------------

These sub-inidcators represent a minimum that are complemented by other indicators for compresensive assesment of land degradation. 

-----------------------------
Vegetation Loss/Gain hotspots
-----------------------------

Land degradation hotsports (LDH) are produced via the analysis of time-series vegetation indices data and are used to characterize areas of different sizes, where the vegetation cover and the soil types are severely degraded.

Vegetation loss/gain hotspots will be calculated based on time series observation of selected suit of vegetation indices depending on the climatic zones and terrain morphology of the North African countries. The selected indices derived from Landsat data are as listed below:

	-NDVI for humid zones, sub-humid and semi-arid zones
	-MSAVI2 for arid and stepic zones
	-SAVI for desert areas


----------------------------
Forest degradation hotspots
----------------------------

Forest Cover Change
-------------------
The quantification of the forest change will be based on pre-existing high-resolution global maps derived from Hansen Global Forest change dataset that can be accessed using `Google Earth Engine API`_. 

	.. _Google Earth Engine API: https://earthenginepartners.appspot.com/science-2013-global-forest

The maps are produced from time-series analysis of Landsat images characterizing forest extent and change over time.

Forest Fires
------------
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
