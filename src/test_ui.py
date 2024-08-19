from PySide6.QtWidgets import (QApplication, QDialog, QWidget, QVBoxLayout, QHBoxLayout,
                               QRadioButton, QSpinBox, QLabel, QButtonGroup,
                               QTabWidget, QFileDialog, QLineEdit, QPushButton,
                               QCheckBox
                               )

class StepLabel(QWidget):
    def __init__(self, widget, text):
        super().__init__()
        main_layout = QVBoxLayout()
        
        # 在传入的widget上方添加一个label标明步骤说明
        main_layout.addWidget(QLabel(text))
        main_layout.addWidget(widget)
        
        self.setLayout(main_layout)

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        
        # 创建文本框
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("请选择 .rdc 文件")
        
        # 创建浏览按钮
        browse_button = QPushButton("...")
        browse_button.clicked.connect(self.browse_file)

        # 将部件添加到布局中
        main_layout.addWidget(self.file_input)
        main_layout.addWidget(browse_button)

        self.setLayout(main_layout)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择 RDC 文件", "", "RDC Files (*.rdc)")
        if file_name:
            self.file_input.setText(file_name)

class RDCDataExtractor(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        
        # 创建文本框
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("请选择输出文件夹")
        # 创建浏览按钮
        browse_button = QPushButton("...")
        browse_button.clicked.connect(self.browse_folder)
        # 创建用于存放输出路径的水平布局
        output_path_layout = QHBoxLayout()
        output_path_layout.addWidget(self.output_path)
        output_path_layout.addWidget(browse_button)
        
        start_eid = QSpinBox()
        
        # 创建多选按钮
        input_texure_checkbox = QCheckBox("输入纹理")
        output_texture_checkbox = QCheckBox("输出纹理")
        # 创建多选按钮的水平布局
        check_layout = QHBoxLayout()
        check_layout.addWidget(input_texure_checkbox)
        check_layout.addWidget(output_texture_checkbox)
        
        # 创建单选按钮
        input_mesh_radio = QRadioButton("输入网格数据")
        output_mesh_radio = QRadioButton("输出网格数据")

        # 创建按钮组，确保单选行为
        button_group = QButtonGroup(self)
        button_group.addButton(input_mesh_radio)
        button_group.addButton(output_mesh_radio)
        # 创建单选按钮的水平布局
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(input_mesh_radio)
        radio_layout.addWidget(output_mesh_radio)
        
        extract_data_button = QPushButton("保存数据")
        
        main_layout.addLayout(output_path_layout)
        main_layout.addLayout(check_layout)
        main_layout.addLayout(radio_layout)
        main_layout.addWidget(extract_data_button)

        self.setLayout(main_layout)
        
        # 初始状态
        input_texure_checkbox.setChecked(True)
        output_texture_checkbox.setChecked(False)
        input_mesh_radio.setChecked(False)
        output_mesh_radio.setChecked(True)
        
    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "选择输出文件夹")
        if folder_path:
                self.output_path.setText(folder_path)
                
class CSVAttributeMapper(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        
        label = QLabel("CSVAttributeMapper")
        main_layout.addWidget(label)
        
        self.setLayout(main_layout)
        
class PositionReconstructor_VSIn(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        
        label = QLabel("PositionReconstructor_VSIn")
        main_layout.addWidget(label)
        
        self.setLayout(main_layout)
        
class PositionReconstructor_VSOut(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        
        label = QLabel("PositionReconstructor_VSOut")
        main_layout.addWidget(label)
        
        self.setLayout(main_layout)
        
class PositionReconstructor(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        
        vsin_radio = QRadioButton("从输入网格CSV数据重建")
        vsout_radio = QRadioButton("从输出网格CSV数据重建")
        
        button_group = QButtonGroup(self)
        button_group.addButton(vsin_radio)
        button_group.addButton(vsout_radio)
        
        self.vsin_widget = PositionReconstructor_VSIn()
        self.vsout_widget = PositionReconstructor_VSOut()
        
        main_layout.addWidget(vsin_radio)
        main_layout.addWidget(vsout_radio)
        main_layout.addWidget(self.vsin_widget)
        main_layout.addWidget(self.vsout_widget)
        
        self.setLayout(main_layout)
        
        # 初始状态
        vsin_radio.setChecked(False)
        vsout_radio.setChecked(True)
        self.vsin_widget.hide()
        self.vsout_widget.show()

class RDCToCSVToFBX(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        
        file_selector = StepLabel(FileSelector(), "step1: 选择.rdc文件")
        rdc_data_extractor = StepLabel(RDCDataExtractor(), "step2: 保存纹理与网格CSV数据")
        csv_attr_mapper = StepLabel(CSVAttributeMapper(), "step3: 选择需要从网格CSV数据中提取的属性")
        pos_reconstructor = StepLabel(PositionReconstructor(), "step4: 重建顶点位置")
        
        main_layout.addWidget(file_selector)
        main_layout.addWidget(rdc_data_extractor)
        main_layout.addWidget(csv_attr_mapper)
        main_layout.addWidget(pos_reconstructor)

        self.setLayout(main_layout)

class RDCToCSV(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("这是RDC_To_CSV的页面"))
        self.setLayout(main_layout)
        
class CSVToFBX(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("这是CSV_To_FBX的页面"))
        self.setLayout(main_layout)
        
class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rdc文件批量资源提取工具")
        
        main_tab_widget = QTabWidget()

        rdc_to_csv_to_fbx_layout = RDCToCSVToFBX()
        rdc_to_csv = RDCToCSV()
        csv_to_fbx = CSVToFBX()
        
        main_tab_widget.addTab(rdc_to_csv_to_fbx_layout, "RDC_To_CSV_To_FBX")
        main_tab_widget.addTab(rdc_to_csv, "RDC_To_CSV")
        main_tab_widget.addTab(csv_to_fbx, "CSV_To_FBX")
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(main_tab_widget)
        
        self.setLayout(main_layout)
        self.resize(600, 400)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()