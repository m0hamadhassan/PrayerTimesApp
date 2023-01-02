from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from ui import Ui_MainWindow
import sys

from datetime import date

from pyIslam.praytimes import PrayerConf, Prayer

from pyIslam.hijri import HijriDate


class MainWindowClass(QMainWindow, QTableWidgetItem, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Prayer")
        self.setWindowIcon(QIcon('icon.ico'))
        self.UpdateLabels()

    def UpdateLabels(self):
        PrayerTime = self.GetPrayerTime()
        self.label_fagr.setText(PrayerTime[0])
        self.label_duhr.setText(PrayerTime[1])
        self.label_asr.setText(PrayerTime[2])
        self.label_maghrib.setText(PrayerTime[3])
        self.label_ishaa.setText(PrayerTime[4])
        self.label_hijri.setText(HijriDate.today().format(1))
        self.label_miladi.setText(str(date.today()))

    def GetPrayerTime(self):
        longitude = 31.2268
        latitude = 30.0588
        timezone = 2
        fajr_isha_method = 3
        asr_fiqh = 1
        pconf = PrayerConf(longitude, latitude, timezone,
                           fajr_isha_method, asr_fiqh)
        pt = Prayer(pconf, date.today())
        return str(pt.fajr_time().strftime('%I:%M %p')), str(pt.dohr_time().strftime('%I:%M %p')),\
            str(pt.asr_time().strftime('%I:%M %p')), str(
                pt.maghreb_time().strftime('%I:%M %p')), str(pt.ishaa_time().strftime('%I:%M %p'))


def main():
    App = QApplication(sys.argv)
    MainWindowVar = MainWindowClass()
    MainWindowVar.show()
    App.exec_()


if __name__ == '__main__':
    main()
