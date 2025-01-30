import sys
import os
import math
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QFileDialog
from PyQt6.QtCore import QObject, QThreadPool, QRunnable, pyqtSlot, pyqtSignal
import traceback
from tkinter import messagebox
import numpy as np
import re
from interface_2 import Ui_Form
import time
from time import sleep
import Lockin_SR_class as Lockin_class
import PI_class as Stage_class
import pyqtgraph as pg
from random import seed
from random import random
# seed random number generator
seed(1)
uiclass, baseclass = pg.Qt.loadUiType("interface.ui")


# 2 next classes for multithreading

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):
    # used for LIA and XPS initialization
    '''
    Worker thread for any function
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    taken from https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        # set parameters of GUI
        self.setWindowTitle('2D scan')
        # create an instance of Ui_Form
        self.ui = Ui_Form()

        # initialization of GUI
        self.ui.setupUi(self)

        # plot blank images
        # self.ui.Image_view_X.ui.histogram.hide()
        # self.ui.plotWidget.ui.roiBtn.hide()
        # self.ui.plotWidget.ui.menuBtn.hide()
        # # Set a custom color map
        # colors = [
        #     (0, 0, 0),
        #     (4, 5, 61),
        #     (84, 42, 55),
        #     (15, 87, 60),
        #     (208, 17, 141),
        #     (255, 255, 255)
        # ]
        # # color map
        # cmap = pg.ColorMap(pos=np.linspace(0.0, 1.0, 6), color=colors)
        cm = pg.colormap.get('CET-L9')
        # setting color map to the image view
        self.ui.Image_view_X.setColorMap(cm)
        self.scene = QGraphicsScene()
        self.show()

        # set functions for buttons
        self.ui.folderButton.clicked.connect(self.show_folder_dialog)
        self.ui.connectLIAandPIbutton.clicked.connect(self.lia_pi_init)
        self.ui.StopButton.clicked.connect(self.stop_button)
        self.ui.StartButton.clicked.connect(self.start_button_press)
        self.ui.Go2StartButton.clicked.connect(self.go2start)

        # folder and file names
        self.folder_path = self.ui.folder_edit.text()
        # variable for stopping main loop
        self.isStop = True
        # setup thread pool
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def lia_pi_init(self):
        # Pass the function to execute
        worker = Worker(self.connect_LIA_PI)  # Any other args, kwargs are passed to the run function
        # Execute
        self.threadpool.start(worker)

    def connect_LIA_PI(self):
        # connect LIA
        # self.lockin_id = self.ui.LockIn.text()  # set lock-in address
        # self.lia = Lockin_class.Lockin(self.lockin_id)
        # self.ui.liaStatuslabel.setText(self.lia.state)
        # connect PI stages
        self.piX_sn = self.ui.PI_X_sn_lineEdit.text()
        self.stage_X = Stage_class.Pi(serial_number=self.piX_sn, stage='M-126.CG1', controller='C-863', refmodes='FNL', show=True)
        self.stage_X.connect()
        self.stage_X.set_velocity(0.6)
        self.piY_sn = self.ui.PI_Y_sn_lineEdit.text()
        self.stage_Y = Stage_class.Pi(serial_number=self.piY_sn, stage='M-126.CG1', controller='C-863', refmodes='FNL', show=True)
        self.stage_Y.connect()
        self.stage_Y.set_velocity(0.6)
        self.ui.PIStatuslabel.setText("PIs are connected")

    # def getPIposition(self):
    #     self.currDLposition = self.delay_line.get_position()
    #     self.ui.currentDLposituionlabel.setText(f"Current delay pos: {self.currDLposition} mm")

    def go2start(self):
        startX = self.ui.Ystart_doubleSpinBox.value()
        self.stage_X.set_absolute_position(startX)
        self.ui.Xposition_doubleSpinBox.setValue(self.stage_X.get_current_position())
        startY = self.ui.Ystart_doubleSpinBox.value()
        self.stage_Y.set_absolute_position(startY)
        self.ui.Yposition_doubleSpinBox.setValue(self.stage_Y.get_current_position())

    def closeEvent(self, e):
        if hasattr(self, 'stage_X'):
            self.stage_X.disconnect()
        if hasattr(self, 'stage_Y'):
            self.stage_Y.disconnect()
        e.accept()

    def stop_button(self):
        self.isStop = True

    def start_button_press(self):
        # Pass the function to execute
        worker = Worker(self.start_button_thread)  # Any other args, kwargs are passed to the run function
        # Execute
        self.threadpool.start(worker)

    def start_button_thread(self):
        # start main measurements
        # if not hasattr(self, 'lia'):
        #     messagebox.showerror("Error", "Lock-in is not connected!")
        #     return
        #
        if not hasattr(self, 'stage_X'):
            messagebox.showerror("Error", "PI X is not connected!")
            return

        if not hasattr(self, 'stage_Y'):
            messagebox.showerror("Error", "PI Y is not connected!")
            return

        # prepare measurements
        self.isStop = False
        self.go2start()

        # load the parameters of measurements
        startX = self.ui.Xstart_doubleSpinBox.value()
        stepX = self.ui.Xstep_doubleSpinBox.value()
        endX = self.ui.Xlength_doubleSpinBox.value()+stepX
        arrayX = np.arange(startX, startX+endX, stepX)
        startY = self.ui.Ystart_doubleSpinBox.value()
        stepY = self.ui.Ystep_doubleSpinBox.value()
        endY = self.ui.Ylength_doubleSpinBox.value() + stepY
        arrayY = np.arange(startY, startY+endY, stepY)
        signalX = np.zeros( (len(arrayX), len(arrayY)) )
        signalY = np.zeros( (len(arrayX), len(arrayY)) )

        all_steps = len(arrayX) * len(arrayY)
        counter = 0

        # save protocol
        folder = self.ui.folder_edit.text()
        filename = self.ui.FileName.text()
        # save reference image
        fullpath = os.path.join(folder, filename)
        self.save_mainwindow_screenshot(fullpath + "_protocol.png")

        # main loop of measurements
        for x, posX in enumerate(arrayX):
            if not self.isStop:
                self.stage_X.set_absolute_position(posX)
                self.ui.Xposition_doubleSpinBox.setValue(self.stage_X.get_current_position() - startX)
                # self.ui.progressBar.setValue(progress)
            for y, posY in enumerate(arrayY):
                if not self.isStop:
                    self.stage_Y.set_absolute_position(posY)
                    self.ui.Yposition_doubleSpinBox.setValue(self.stage_Y.get_current_position() - startY)
                    sleep(self.ui.AccTime_spinBox.value()*0.001)
                    # sigX, sigY = get_data, get_data
                    signalX[x, y] = self.get_data()
                    signalY[x, y] = self.get_data()
                    self.update_frame(signalX, self.ui.Image_view_X)
                    self.update_frame(signalY, self.ui.Image_view_Y)
                    counter += 1
                    progress = int(math.floor(100 * counter / all_steps))

        np.savetxt(fullpath + '_chX.dat', signalX)
        np.savetxt(fullpath + '_chY.dat', signalY)
        np.savetxt(fullpath + 'arrayX.dat', arrayX)
        np.savetxt(fullpath + 'arrayY.dat', arrayY)
        # save screenshots
        self.ui.Image_view_X.export(fullpath + "_chX.png")
        self.ui.Image_view_Y.export(fullpath + "_chY.png")

        self.ui.progressBar.setValue(progress)
        messagebox.showinfo("Done", "Measurements are done.")

    def get_data(self):
        return random()

    def pi_move(self, position):
        return

    def show_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.ui.folder_edit.setText(folder_path + "/")
            self.folder_path = self.ui.folder_edit.text()

    def update_frame(self, frame, widget):
        image_data = frame
        # Get the number of rows and columns
        num_rows, num_columns = image_data.shape
        # Get the central subarray
        central_subarray = image_data[num_rows // 4: num_rows * 3 // 4, num_columns // 4: num_columns * 3 // 4]
        # Compute the maximum and minimum values
        max_value = np.max(central_subarray)
        min_value = np.min(central_subarray)
        # View image
        widget.setImage(image_data)
        widget.setLevels(min_value, max_value)  # Set min_value and max_value according to your desired range
        widget.show()

    def save_snap(self, image, fullname, format='%d'):
        # saving one image
        folder = self.ui.folder_edit.text()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Folder does not exist!")
            return
        # if not filename:
        #     messagebox.showerror("Error", "Please enter a file name")
        #     return
        # fullname = os.path.join(folder, filename)
        if os.path.exists(fullname):
            overwrite = messagebox.askyesno('File already exists', 'File already exists. Overwrite?')
            if overwrite:
                with open(fullname, "w") as file:
                    np.savetxt(file, image, fmt=format)
                    # messagebox.showinfo("Save", "File saved successfully.")
            else:
                self.isStop = True
        else:
            dir_name = os.path.dirname(os.path.abspath(fullname))
            Path(dir_name).mkdir(parents=True, exist_ok=True)
            with open(fullname, "w") as file:
                np.savetxt(file, image, fmt=format)
                messagebox.showinfo("Save", "File saved successfully.")
        return

    def save_images(self, delay_pwr="0"):
        base_folder = self.ui.folder_edit.text()
        file_base_name = self.ui.FileName.text()
        # save reference image
        folder = base_folder + f"ref_{file_base_name}"
        if not os.path.isdir(folder):
            os.makedirs(folder)
        filename = f"{delay_pwr}.dat"
        fullname = os.path.join(folder, filename)
        self.save_snap(self.reference_img, fullname=fullname)
        # save screenshot
        self.ui.referenceImage_view.export(fullname + ".png")

    def save_mainwindow_screenshot(self, fullpath):
        # Get the primary screen
        screen = QApplication.primaryScreen()
        # Capture the entire main window
        pixmap = screen.grabWindow(self.winId())
        # Save the screenshot to a file
        pixmap.save(fullpath, 'png')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainForm()
    sys.exit(app.exec())
