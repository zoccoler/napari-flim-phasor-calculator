# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:11:43 2022

@author: mazo260d
"""

import napari
from magicgui import magicgui
from napari_flim_phasor_calculator._widget import make_flim_label_layer
import types
viewer = napari.Viewer()
viewer.open("C:/Users/mazo260d/Desktop/Conni_BiA_PoL/copied_for_Marcelo/single_image/raw_FLIM_data/single_FLIM_image.ptu",
            plugin="napari-flim-phasor-calculator")

# image = viewer.layers[0].data[:, 120:130, 260:290]

# viewer.add_image(image, metadata = viewer.layers[0].metadata)

# viewer.layers.pop()
# viewer.layers.pop()



widget = make_flim_label_layer()

viewer.window.add_dock_widget(widget)
# Run make labels layer
widget()

# dw_plotter_widget, plotter_widget = viewer.window.add_plugin_dock_widget('napari-clusters-plotter',
#                                       widget_name='Plotter Widget')

# plotter_widget.update_axes_list()
# plotter_widget.plot_x_axis.setCurrentText('G')
# plotter_widget.plot_y_axis.setCurrentText('S')



# def add_phasor_circle(ax):
#     '''
#     Generate FLIM universal semi-circle plot
#     '''
#     import numpy as np
#     import matplotlib.pyplot as plt
#     angles = np.linspace(0, np.pi, 180)
#     x =(np.cos(angles) + 1) / 2
#     y = np.sin(angles) / 2
#     ax.plot(x,y, 'yellow', alpha=0.3)
#     return ax

# add_phasor_circle(plotter_widget.graphics_widget.axes)

# plotter_widget.run(viewer.layers[-1].features,'G','S')
# print('plotted')

# plotter_widget.graphics_widget.fig.canvas.draw()

