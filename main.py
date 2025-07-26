from modules.application import Main
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "venv\\Lib\\site-packages\\PyQt5\\Qt5\\plugins"

if __name__ == "__main__":
    app = QApplication([])
    app.setAttribute(Qt.ApplicationAttribute.AA_DisableWindowContextHelpButton)
    main = Main()
    main.run(app)