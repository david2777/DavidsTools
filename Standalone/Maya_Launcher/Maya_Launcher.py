#Stamdard
import os
import sys
import subprocess

#PyQt4
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_MayaLauncher import Ui_MayaLauncher

class MayaLauncher(QMainWindow, Ui_MayaLauncher):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.launch_PushButton.clicked.connect(self.launch)
        self.cancel_PushButton.clicked.connect(self.cancel)

        if not os.getenv("RedshiftPath", None):
            QMessageBox.warning(self, "Error", "Could not find RedshiftPath variable!")
            self.rs_ListWidget.setEnabled(False)

        defaultRs = self.get_default_rs_version()
        rsVersions = sorted(self.get_rsVersions())[::-1]
        if rsVersions:
            self.rs_ListWidget.addItems(rsVersions)
            try:
                idx = rsVersions.index(defaultRs)
                self.rs_ListWidget.setCurrentItem(self.rs_ListWidget.item(idx))
            except ValueError:
                pass

        mayaVersions = self.get_maya_versions()
        if mayaVersions:
            self.maya_ListWidget.addItems(mayaVersions)
            try:
                idx = mayaVersions.index("Maya2015")
                self.maya_ListWidget.setCurrentItem(self.maya_ListWidget.item(idx))
            except ValueError:
                pass

    def launch(self):
        mayaPath = self.get_maya_path(str(self.maya_ListWidget.selectedItems()[0].text()))
        if not mayaPath:
            QMessageBox.warning(self, "Error", "Could not find executeable for that version of Maya!")
            return None
 
        rsPath = self.get_rs_path(str(self.rs_ListWidget.selectedItems()[0].text()))
        if not rsPath:
            QMessageBox.warning(self, "Error", "Could not find that version of Redshift on the server!")
            return None

        self.launch_maya(rsPath, mayaPath)
        sys.exit(0)


    @staticmethod
    def cancel():
        sys.exit(0)

    @staticmethod
    def get_maya_versions():
        adsk_dir = r"C:\Program Files\Autodesk"
        return [x for x in os.listdir(adsk_dir) if x.startswith("Maya20")]

    @staticmethod
    def get_maya_path(maya_version):
        mayaPath = r"C:\Program Files\Autodesk\{}\bin\maya.exe".format(maya_version)
        if os.path.exists(os.path.abspath(mayaPath)):
            return mayaPath
        else:
            return None

    @staticmethod
    def get_rsVersions():
        rs_dir = r"\\rendersrv1\REDSHIFT_CORE\_VERSIONS"
        return os.listdir(rs_dir)

    @staticmethod
    def get_default_rs_version():
        ver_dir = r"\\rendersrv1\REDSHIFT_CORE"
        contents = os.listdir(ver_dir)
        vFiles = [x for x in contents if x.endswith(".Version")]
        if len(vFiles) == 1:
            version = vFiles[0].replace(".Version", "")
            return version
        else:
            return None

    @staticmethod
    def get_rs_path(rs_version):
        rs_dir = r"\\rendersrv1\REDSHIFT_CORE\_VERSIONS"
        rsPath = os.path.join(rs_dir, rs_version)
        if os.path.exists(os.path.abspath(rsPath)):
            return rsPath
        else:
            return None

    @staticmethod
    def launch_maya(rs_version, maya_version):
        if rs_version:
            os.environ["RedshiftPath"] = rs_version
        subprocess.Popen(maya_version)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MayaLauncher()

    window.show()
    retcode = app.exec_()
    sys.exit(retcode)
