import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar


class PlotMap(QWidget):

    def __init__(self, array: np.array):
        super().__init__()

        # Create the plot.
        figure, axes = plt.subplots(1, 1)
        axes.imshow(array, interpolation='nearest')
        plot = FigureCanvas(figure)

        # Create the toolbar.
        toolbar = NavigationToolbar(plot, self)

        # Add it to layout.
        layout = QVBoxLayout()
        layout.addWidget(plot)
        layout.addWidget(toolbar)
        self.setLayout(layout)

