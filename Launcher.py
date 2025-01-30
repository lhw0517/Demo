# lastet edit time: 2025-1-28
# Editor: HanWen_lu
# Designer: DogeBoy2
# Copyright HrotonStudio 2025

from Main import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QWidget
from qframelesswindow import FramelessWindow,AcrylicWindow
from qfluentwidgets import SplitFluentWindow,fluent_window
import sys

class Window(FramelessWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法，确保父类的初始化逻辑被执行
        self.setupUi(self)  # 调用setupUi方法，这个方法通常用于设置窗口的用户界面，比如添加按钮、标签等控件
        self.titleBar.maxBtn.deleteLater() # 移除最大化按钮
        self.titleBar.minBtn.deleteLater() # 移除标题栏中的最小化按钮
        self.titleBar.closeBtn.deleteLater() # 移除标题栏中的关闭按钮
        self.titleBar._isDoubleClickEnabled = False # 禁用标题栏的双击放大功能，通过设置_isDoubleClickEnabled属性为False来实现


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Window()
    start.show()
    app.exec()