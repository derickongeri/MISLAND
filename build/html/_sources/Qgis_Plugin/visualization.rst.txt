Visualization tools
===================

.. raw:: html

    <div style="border: 1px solid; margin-bottom: 2em; box-shadow: 2px 3px #888888; overflow: hidden; max-width: 100%; height: auto;">
        <video style="width: 100%; height: 100%;" controls>
            <source src="https://res.cloudinary.com/acemobile/video/upload/v1613914435/MISLAND/visualization_tools.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

.. image:: ../_static/common/plugin_toolbar_visualize.png
   :align: center


To view the "Visualization Tools", select the report icon highlighted above. This will open up 
the "Visualization tools" dialog box:

.. image:: ../_static/documentation/reporting_tool/image065.png
   :align: center

Here there are two options: "Add Basemap" or "Create Print Map". The first allows users to add a Basemap for a first or second level administrative boundary. The second option brings up the Composer window in QGIS to design and export a static map. 
   
.. image:: ../_static/documentation/reporting_tool/image066.png
   :align: center

By selecting "Add Basemap", the user can select the first or second level administrative boundary. The first level is the country boundary. The second level will be the first sub-division that the country is divided into and will be dependent on the country selected. For example, in the United States of America, the second level will provide a drop down of states. In Kenya, the second level will display provinces.    
Please note the disclaimer in the window. Natural Earth provides the spatial layers contained within the dropdown. These boundaries are not official endorsed by CI or other partner organizations and contributors.
After selecting the dropdown, for the first level and second level if applicable, select "Ok".
   
After submitting the above message will appear within the QGIS Desktop window. This shows that the Basemap is loading. DO NOT select cancel or attempt another function in QGIS until the Basemap has loaded. The time it takes to load will depend on your Internet connection and computer processor.
   
If you have a map layer within your QGIS Desktop window, you will now see the Basemap with the administrative level selected clipped out to view the underlying map layer.
