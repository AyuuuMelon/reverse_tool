from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Widget Loading")

        # 主布局
        self.layout = QVBoxLayout(self)

        # Step 1
        self.step1_label = QLabel("Step 1: 选择需要的数据", self)
        self.layout.addWidget(self.step1_label)

        self.step1_combo = QComboBox(self)
        self.step1_combo.addItems(["Option 1", "Option 2"])
        self.step1_combo.currentIndexChanged.connect(self.update_dynamic_area)
        self.layout.addWidget(self.step1_combo)

        # 动态加载的区域
        self.dynamic_area = QVBoxLayout()
        self.layout.addLayout(self.dynamic_area)

    def update_dynamic_area(self):
        # 清除动态区域的内容
        for i in reversed(range(self.dynamic_area.count())):
            widget = self.dynamic_area.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # 根据选择动态加载新的组件
        selected_option = self.step1_combo.currentText()
        step2_label = QLabel(f"Step 2: 选择.rdc文件 (based on {selected_option})", self)
        self.dynamic_area.addWidget(step2_label)

        # 添加更多组件
        # ...

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()