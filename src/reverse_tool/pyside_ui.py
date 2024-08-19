from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QTableWidget,
                               QTableWidgetItem,
                               QLineEdit,
                               QVBoxLayout,
                               QHBoxLayout,
                               QWidget,
                               QTabWidget,
                               QLabel,
                               QGridLayout,
                               QProgressBar,
                               QCheckBox
                               )

from PySide6.QtCore import Slot, Signal

import os
import csv
from collections import defaultdict
from .fbx_utils import batch_csv_to_fbx

class CustomProgressBar(QWidget):
    def __init__(self, parent=None):
        super(CustomProgressBar, self).__init__(parent)
        # 创建一个QGridself.layout作为布局
        self.layout = QVBoxLayout(self)

        # 创建一个QLabel显示描述
        self.prog = QProgressBar()
        self.layout.addWidget(self.prog)

class MatrixWidget(QWidget):
    def __init__(self, parent=None):
        super(MatrixWidget, self).__init__(parent)

        # 创建一个QGridself.layout作为布局
        self.layout = QGridLayout(self)

        # 创建一个QLabel显示描述
        label = QLabel("投影矩阵")
        self.layout.addWidget(label, 0, 0, 1, 4)

        # 手动创建一个4x4的QLineEdit数组
        self.edit00 = QLineEdit("1.13")
        self.layout.addWidget(self.edit00, 1, 0)
        self.edit01 = QLineEdit("0")
        self.layout.addWidget(self.edit01, 1, 1)
        self.edit02 = QLineEdit("0")
        self.layout.addWidget(self.edit02, 1, 2)
        self.edit03 = QLineEdit("0")
        self.layout.addWidget(self.edit03, 1, 3)

        self.edit10 = QLineEdit("0")
        self.layout.addWidget(self.edit10, 2, 0)
        self.edit11 = QLineEdit("2.32")
        self.layout.addWidget(self.edit11, 2, 1)
        self.edit12 = QLineEdit("0")
        self.layout.addWidget(self.edit12, 2, 2)
        self.edit13 = QLineEdit("0")
        self.layout.addWidget(self.edit13, 2, 3)

        self.edit20 = QLineEdit("0")
        self.layout.addWidget(self.edit20, 3, 0)
        self.edit21 = QLineEdit("0")
        self.layout.addWidget(self.edit21, 3, 1)
        self.edit22 = QLineEdit("0")
        self.layout.addWidget(self.edit22, 3, 2)
        self.edit23 = QLineEdit("1")
        self.layout.addWidget(self.edit23, 3, 3)

        self.edit30 = QLineEdit("0")
        self.layout.addWidget(self.edit30, 4, 0)
        self.edit31 = QLineEdit("0")
        self.layout.addWidget(self.edit31, 4, 1)
        self.edit32 = QLineEdit("1")
        self.layout.addWidget(self.edit32, 4, 2)
        self.edit33 = QLineEdit("0")
        self.layout.addWidget(self.edit33, 4, 3)

    def get_projection_matrix(self):
        # 获取QLineEdit的内容，转换为浮点数，然后返回二维列表
        matrix = []
        matrix_01 = [float(self.edit00.text()), float(self.edit01.text()), float(self.edit02.text()), float(self.edit03.text())]
        matrix_02 = [float(self.edit10.text()), float(self.edit11.text()), float(self.edit12.text()), float(self.edit13.text())]
        matrix_03 = [float(self.edit20.text()), float(self.edit21.text()), float(self.edit22.text()), float(self.edit23.text())]
        matrix_04 = [float(self.edit30.text()), float(self.edit31.text()), float(self.edit32.text()), float(self.edit33.text())]
        matrix.append(matrix_01)
        matrix.append(matrix_02)
        matrix.append(matrix_03)
        matrix.append(matrix_04)
        return matrix

class MainWindow(QMainWindow):

    # 定义一个自定义信号
    valueChanged = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("rdc->csv->fbx批量转换工具")
        
        # 创建一个文本输入框，输入rdc文件路径
        self.rdc_path_input = QLineEdit(self)
        self.rdc_path_input.setPlaceholderText("请输入或选中rdc文件")
        
        self.texture_checkbox_layout = QHBoxLayout()
        self.texture_input = QCheckBox("导出输入纹理")
        self.texture_input.setChecked(True)
        self.texture_output = QCheckBox("导出输出纹理")
        self.texture_output.setChecked(False)
        self.texture_checkbox_layout.addWidget(self.texture_input)
        self.texture_checkbox_layout.addWidget(self.texture_output)
        
        self.mesh_checkbox_layout = QHBoxLayout()
        self.mesh_data_input = QCheckBox("导出输入顶点数据")
        self.mesh_data_input.setChecked(False)
        self.mesh_data_output = QCheckBox("导出输出顶点数据")
        self.mesh_data_output.setChecked(True)
        self.mesh_checkbox_layout.addWidget(self.mesh_data_input)
        self.mesh_checkbox_layout.addWidget(self.mesh_data_output)
        
        # 创建一个按钮，用于转换rdc文件
        self.rdc2csv_button = QPushButton("RDC转CSV", self)
        self.rdc2csv_button.setMinimumHeight(40)
        # self.rdc2csv_button.clicked.connect()

        # 创建一个文本输入框，输入csv文件夹路径
        self.folder_path_input = QLineEdit(self)
        self.folder_path_input.setPlaceholderText("请输入csv文件夹路径")

        self.progress_bar = QProgressBar(self)
        
        # 创建一个按钮
        self.start_button = QPushButton("CSV文件分批", self)
        self.start_button.setMinimumHeight(40)
        self.start_button.clicked.connect(self.start_filter)

        self.matrix_widget = MatrixWidget()

        # 批量转换
        self.convert_button = QPushButton("CSV to FBX", self)
        self.convert_button.setMinimumHeight(40)
        self.convert_button.clicked.connect(self.start_convert)

        # 创建一个标签页部件
        self.tab_widget = QTabWidget(self)

        # 创建一个布局
        layout = QVBoxLayout()
        layout.addWidget(self.rdc_path_input)
        layout.addLayout(self.texture_checkbox_layout)
        layout.addLayout(self.mesh_checkbox_layout)
        layout.addWidget(self.rdc2csv_button)
        layout.addWidget(self.folder_path_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.tab_widget)
        layout.addWidget(self.matrix_widget)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.progress_bar)

        # 创建一个窗口部件，设置布局
        widget = QWidget()
        widget.setLayout(layout)

        # 设置主窗口的中心部件
        self.setCentralWidget(widget)

    def start_convert(self):
        # 获取tab的数量
        tab_count = self.tab_widget.count()

        # 获取每个tab的文本
        test = {}
        self.progress_bar.setValue(0)
        pro_id = 1
        total_num = tab_count
        for i in range(tab_count):
            tab_text = self.tab_widget.tabText(i)
            tab_widget = self.tab_widget.widget(i)

            # 获取所有的子组件
            children = tab_widget.children()

            # 打印所有的子组件
            for child in children:
                if isinstance(child, QLineEdit):
                    value = child.text() or 0
                    if child.objectName() == 'uv':
                        value = [int(i) for i in child.text().split(" ")]
                        test[child.objectName()] = value
                    else:
                        test[child.objectName()] = int(value)


            dir_path = self.folder_path_input.text()
            draw_id_start = int(tab_text.split("-")[0])
            draw_id_end = int(tab_text.split("-")[1])
            position_id = test["position"]
            normal_id = test["normal"]
            uv_ids = test["uv"]
            matrix_list = self.matrix_widget.get_projection_matrix()
            batch_csv_to_fbx(dir_path, draw_id_start, draw_id_end, position_id, normal_id, uv_ids, matrix_list=matrix_list)

            value = (pro_id / total_num) * 100
            self.progress_bar.setValue(value)
            pro_id += 1

    def load_csv(self, table_widget, file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row_index, row in enumerate(reader):
                if row_index < 5:  # 只读取前5行
                    table_widget.insertRow(row_index)
                    table_widget.setColumnCount(len(row))  # 设置列数
                    for column_index, cell in enumerate(row):
                        if row_index > 0:
                            cell = float(cell)
                            cell = round(cell, 7)
                            print(cell)
                            
                        self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell)))
        headers = [str(i-1) for i in range(1, table_widget.columnCount()+1)]
        table_widget.setHorizontalHeaderLabels(headers)
        table_widget.setVerticalHeaderLabels(headers)

        return table_widget
    
    @Slot()
    def start_filter(self):
        folder_path = self.folder_path_input.text()
        # 创建一个默认字典来存储具有相同行数的文件
        files_by_column_count = defaultdict(list)

        # 遍历文件夹及其子文件夹
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 检查文件是否为 csv 文件
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    # 打开 csv 文件并计算行数
                    with open(file_path, 'r') as csv_file:
                        reader = csv.reader(csv_file)

                        # 检查文件是否为空
                        if not csv_file.read(1):
                            print(f'File {file_path} is empty. Skipping...')
                            continue
                        else:
                            # 回到文件的开始
                            csv_file.seek(0)
                            first_row = next(reader)
                            column_count = len(first_row)
                            row_count = sum(1 for row in reader)
                            if row_count == 1:
                                print(f'File {file_path} has 1 row. Skipping...')
                                continue
                    # 将文件添加到具有相同行数的文件列表中
                    
                    files_by_column_count[column_count].append(file_path)

        # 清空标签页部件
        self.tab_widget.clear()

        # 为每个键创建一个标签页
        pro_id = 1
        total_num = len(files_by_column_count)
        for column_count, files in files_by_column_count.items():
            # 创建一个布局
            print(column_count)
            self.table_widget = QTableWidget(self)
            grid_layout = QGridLayout()

            self.table_widget = self.load_csv(self.table_widget, files[0])

            grid_layout.addWidget(self.table_widget, 0, 0, 1,-1)

            # 创建三个标签和三个文本输入框
            for i, label_text in enumerate(["position", "normal", "uv"]):
                label = QLabel(label_text)
                line_edit = QLineEdit()
                line_edit.setObjectName(label_text)
                grid_layout.addWidget(label, i+1, 0)
                grid_layout.addWidget(line_edit, i+1, 1)

            # 创建一个窗口部件，设置布局
            widget = QWidget()
            widget.setLayout(grid_layout)

            file_names = [os.path.basename(file) for file in files]
            tab_name = file_names[0]+"-"+file_names[-1]
            tab_name = tab_name.replace(".csv", "")

            # 添加标签页
            self.tab_widget.addTab(widget, str(tab_name))

            value = (pro_id / total_num) * 100
            self.progress_bar.setValue(value)
            pro_id += 1

def main():
    # 创建应用实例
    app = QApplication([])

    # 创建主窗口
    window = MainWindow()
    if os.path.exists(r"style.qss"):
        with open(r"style.qss", "r") as f:
            window.setStyleSheet(f.read())
    window.show()  # 显示窗口

    # 运行应用，并监听事件
    app.exec()