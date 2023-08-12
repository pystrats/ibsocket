from PyQt5.QtWidgets import (QMessageBox, QLabel, QDialogButtonBox, QPushButton, QDesktopWidget, QVBoxLayout, QWidget,
                    QScrollArea, QGridLayout, QApplication, QLineEdit, QShortcut, QComboBox, QCheckBox, QSpinBox, QHBoxLayout)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QPoint, pyqtSignal

from copy import deepcopy
import os
import json


class Settings(QWidget):

    success = pyqtSignal(bool)
    timeframe_error = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.close)

        self.shortcut_esc = QShortcut(QKeySequence('Esc'), self)
        self.shortcut_esc.activated.connect(self.close)

        self.width = 600
        self.widthSpacing = 100

        self.settings = {"connection": {"port": 4002, "clientId": 1}, "sockets": {"host": "127.000.000.001", "port": 3490}, "database": {"exchange_id": 8}, "data": {"only_rth": True}}

        fileName = path = '{}{}{}'.format( os.path.dirname(os.path.abspath(__file__)), '/config/', 'settings.json')
        if os.path.isfile(fileName):
            with open(fileName) as f:
                self.settings = json.load(f)

        w = QWidget()
        l = QVBoxLayout()
        self.setLayout(l)


        scroll = QScrollArea(w)
        l.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollLayout.setAlignment(Qt.AlignTop)
        scrollContent.setLayout(scrollLayout)
        _w = QWidget()
        _l = QGridLayout()
        _l.setHorizontalSpacing(15)
        _l.setVerticalSpacing(10)
        _w.setLayout(_l)
        scrollLayout.addWidget(_w)
        scroll.setWidget(scrollContent)

        title = QLabel('Settings')
        title.setStyleSheet('QLabel{color:"#aaaaaa"; font-size:16px; font-weight: normal; margin-bottom: 15px;}')

        strategy = QLabel('Strategy')
        strategy_separator = QWidget()
        strategy_separator.setFixedSize(self.width - self.widthSpacing, 1)
        strategy_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        connection = QLabel('Connection')
        connection.setStyleSheet("QLabel{margin-top: 25px;}")

        separator = QWidget()
        separator.setFixedSize(self.width - self.widthSpacing, 1)
        separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        port_name = QLabel('Port')
        self.port_value = QLineEdit( str(self.settings['connection']['port']) )
        self.port_value.setMaxLength(4)
        self.port_value.setAlignment(Qt.AlignLeft)
        self.port_value.setFixedSize(75,28)
        self.port_value.setTextMargins(10, 1, 10, 1)

        clientID_n = QLabel('Client ID')
        self.clientID_v = QLineEdit( str(self.settings['connection']['clientId']) )
        self.clientID_v.setMaxLength(10)
        self.clientID_v.setAlignment(Qt.AlignLeft)
        self.clientID_v.setFixedSize(75,28)
        self.clientID_v.setTextMargins(10, 1, 10, 1)

        socket = QLabel('Socket')
        socket.setStyleSheet("QLabel{margin-top: 25px;}")
        socket_separator = QWidget()
        socket_separator.setFixedSize(self.width - self.widthSpacing, 1)
        socket_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        socket_host = QLabel('Host')
        self.socket_host = QLineEdit( str(self.settings['sockets']['host']) )
        self.socket_host.setAlignment(Qt.AlignLeft)
        self.socket_host.setFixedSize(150,28)
        self.socket_host.setTextMargins(10, 1, 10, 1)
        self.socket_host.setInputMask( "000.000.000.000" )

        socket_port = QLabel('Port')
        self.socket_port = QLineEdit( str(self.settings['sockets']['port']) )
        self.socket_port.setMaxLength(4)
        self.socket_port.setAlignment(Qt.AlignLeft)
        self.socket_port.setFixedSize(75,28)
        self.socket_port.setTextMargins(10, 1, 10, 1)

        db = QLabel('Database')
        db.setStyleSheet("QLabel{margin-top: 25px;}")
        db_separator = QWidget()
        db_separator.setFixedSize(self.width - self.widthSpacing, 1)
        db_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        exchange_id = QLabel('EXCHANGE_ID')
        self.exchange_id = QLineEdit( str(self.settings['database']['exchange_id']) )
        self.exchange_id.setMaxLength(4)
        self.exchange_id.setAlignment(Qt.AlignLeft)
        self.exchange_id.setFixedSize(75,28)
        self.exchange_id.setTextMargins(10, 1, 10, 1)

        data = QLabel('Data')
        data.setStyleSheet("QLabel{margin-top: 25px;}")
        data_separator = QWidget()
        data_separator.setFixedSize(self.width - self.widthSpacing, 1)
        data_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        rthonly = QLabel('Only RTH')
        self.use_only_RTH_data = QCheckBox()
        self.use_only_RTH_data.setChecked( self.settings['data']['only_rth'] )


        clientID_n = QLabel('Client ID')
        self.clientID_v = QLineEdit( str(self.settings['connection']['clientId']) )
        self.clientID_v.setMaxLength(10)
        self.clientID_v.setAlignment(Qt.AlignLeft)
        self.clientID_v.setFixedSize(75,28)
        self.clientID_v.setTextMargins(10, 1, 10, 1)

        server = QLabel('Server')
        server.setStyleSheet("QLabel{margin-top: 25px;}")
        server_separator = QWidget()
        server_separator.setFixedSize(self.width - self.widthSpacing, 1)
        server_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')


        """
        timeframe = QLabel('Timeframe')
        self.timeframe_spinbox = QSpinBox()
        self.timeframe_spinbox.setRange(1,59)
        self.timeframe_spinbox.setMaximum(59)
        self.timeframe_spinbox.setFixedWidth(100)
        self.timeframe_spinbox.setValue( self.settings['strategy']['timeframe'] )
        self.timeframe_spinbox.setSuffix(" min")

        onlyRTH_history = QLabel('Only RTH data in analyses')
        self.use_only_RTH_data = QCheckBox()
        self.use_only_RTH_data.setChecked( self.settings['strategy']['onlyRTH_history'] )

        onlyRTH_trading = QLabel('Trade only during regular hours')
        self.use_only_RTH_trading = QCheckBox()
        self.use_only_RTH_trading.setChecked( self.settings['strategy']['onlyRTH_trading'] )

        trade_all = QLabel('Apply all presets to a new instrument')
        self.trade_all = QCheckBox()
        self.trade_all.setChecked( self.settings['strategy']['trade_all'] )

        flatten_eod = QLabel('Go flat EOD')
        self.flatten_eod = QCheckBox()
        self.flatten_eod.setChecked( self.settings['strategy']['flatten_eod'] )

        flatten_eod_seconds = QLabel('Go flat at T = Closing Bell minus')
        self.flatten_eod_seconds = QSpinBox()
        self.flatten_eod_seconds.setRange(5,3000)
        self.flatten_eod_seconds.setMaximum(3000)
        self.flatten_eod_seconds.setFixedWidth(100)
        self.flatten_eod_seconds.setValue( self.settings['strategy']['flatten_eod_seconds'] )
        self.flatten_eod_seconds.setSuffix(" sec")

        hist_excess = QLabel('History excess to download')
        self.hist_excess = QSpinBox()
        self.hist_excess.setRange(10,1000)
        self.hist_excess.setMaximum(1000)
        self.hist_excess.setFixedWidth(100)
        self.hist_excess.setValue( self.settings['strategy']['hist_excess'] )
        self.hist_excess.setSuffix(" %")

        default_pos_size = QLabel('Default position size')
        self.default_pos_size = QSpinBox()
        self.default_pos_size.setRange(0,1000000)
        self.default_pos_size.setMaximum(1000000)
        self.default_pos_size.setFixedWidth(100)
        self.default_pos_size.setValue( self.settings['strategy']['pos_size'] )
        self.default_pos_size.setPrefix("$ ")

        server_address = QLabel('Address')
        self.server_value = QLineEdit(self.settings['server']['address'])
        self.server_value.setInputMask( "000.000.000.000" )
        # port_value.setMaxLength(4)
        self.server_value.setAlignment(Qt.AlignLeft)
        self.server_value.setFixedSize(150,28)
        self.server_value.setTextMargins(10, 1, 10, 1)

        auth = QLabel('Authentication Key')
        self.auth_value = QLineEdit(self.settings['server']['key'])
        self.auth_value.setAlignment(Qt.AlignLeft)
        self.auth_value.setFixedSize(150,28)
        self.auth_value.setTextMargins(10, 1, 10, 1)

        role = QLabel('Role')
        self.role_value = QComboBox()
        if self.settings['server']['role'] == 'Client':
            self.role_value.setCurrentIndex(0)
        else: self.role_value.setCurrentIndex(1)
        self.role_value.addItem('Client')
        self.role_value.addItem('Manager')
        # self.role_value.setFixedWidth(100)

        margin = QLabel('Margin')
        margin.setStyleSheet("QLabel{margin-top: 25px;}")
        margin_separator = QWidget()
        margin_separator.setFixedSize(self.width - self.widthSpacing, 1)
        margin_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        intraday_margin = QLabel('Intraday Margin')
        self.intraday_margin = QSpinBox()
        self.intraday_margin.setRange(1,100)
        self.intraday_margin.setMaximum(100)
        self.intraday_margin.setValue( self.settings['margin']['intraday'] )
        self.intraday_margin.setSuffix('%')

        overnight_margin = QLabel('Overnight Margin')
        self.overnight_margin = QSpinBox()
        self.overnight_margin.setRange(1,100)
        self.overnight_margin.setMaximum(100)
        self.overnight_margin.setValue( self.settings['margin']['overnight'] )
        self.overnight_margin.setSuffix('%')

        common = QLabel('Common')
        common.setStyleSheet("QLabel{margin-top: 25px;}")
        common_separator = QWidget()
        common_separator.setFixedSize(self.width - self.widthSpacing, 1)
        common_separator.setStyleSheet('QWidget{background-color: "#aaaaaa"; text-align: left; width:100%;}')

        check_updates = QLabel('Check for updates on startup')
        self.check_updates_checkbox = QCheckBox()
        self.check_updates_checkbox.setChecked( self.settings['common']['checkUpdates'] )

        default_risk = QLabel('Default risk per trade')
        self.default_risk = QSpinBox()
        self.default_risk.setRange(0,10000)
        self.default_risk.setMaximum(10000)
        self.default_risk.setValue( self.settings['common']['risk'] )
        self.default_risk.setPrefix("$ ")

        """

        button_panel = QHBoxLayout()
        button_panel.setContentsMargins(0, 50, 0, 0)
        cancelBtn = QPushButton('Cancel')
        cancelBtn.setFixedSize(100, 30)
        cancelBtn.clicked.connect(self.cancel)
        cancelBtn.setEnabled(True)
        padding = QLabel('')
        saveBtn = QPushButton('Save')
        saveBtn.setFixedSize(100, 30)
        saveBtn.setStyleSheet("QPushButton {background-color: #f39c12; color: #2a2a2a; font-weight: bold; border: 1px solid #2a2a2a;}")
        saveBtn.clicked.connect(self.save)
        saveBtn.setEnabled(True)
        button_panel.addWidget(cancelBtn)
        button_panel.addWidget(padding)
        button_panel.addWidget(saveBtn)

        _l.addWidget(title, 0, 0, 1, 2, alignment=Qt.AlignTop|Qt.AlignRight)

        _l.addWidget(connection, 1, 0, 1, 2, alignment=Qt.AlignBottom|Qt.AlignLeft)
        _l.addWidget(separator, 2, 0, 1, 2, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(port_name, 3, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.port_value, 3, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(clientID_n, 4, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.clientID_v, 4, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)

        _l.addWidget(socket, 5, 0, 1, 2, alignment=Qt.AlignBottom|Qt.AlignLeft)
        _l.addWidget(socket_separator, 6, 0, 1, 2, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(socket_host, 7, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.socket_host, 7, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(socket_port, 8, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.socket_port, 8, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)

        _l.addWidget(db, 9, 0, 1, 2, alignment=Qt.AlignBottom|Qt.AlignLeft)
        _l.addWidget(db_separator, 10, 0, 1, 2, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(exchange_id, 11, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.exchange_id, 11, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)

        _l.addWidget(data, 12, 0, 1, 2, alignment=Qt.AlignBottom|Qt.AlignLeft)
        _l.addWidget(data_separator, 13, 0, 1, 2, alignment=Qt.AlignVCenter|Qt.AlignLeft)
        _l.addWidget(rthonly, 14, 0, alignment=Qt.AlignVCenter|Qt.AlignRight)
        _l.addWidget(self.use_only_RTH_data, 14, 1, alignment=Qt.AlignVCenter|Qt.AlignLeft)

        _l.addLayout(button_panel, 28, 1, alignment=Qt.AlignVCenter|Qt.AlignRight)

        self.setWindowTitle("Settings")


        self.screen = QApplication.primaryScreen()
        self.screenWidth = self.screen.size().width()
        self.screenHeight = self.screen.size().height()
        self.move(int(self.screenWidth/2. - self.width/2.), int(self.screenHeight/7.))

        self.setFixedWidth(self.width)
        # self.setMinimumWidth(500)
        self.setFixedHeight(int(self.screenHeight*.75))

        # qtRectangle = self.frameGeometry()
        # centerPoint = QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.move(qtRectangle.topLeft())

    def cancel(self):
        self.close()

    def save(self):
        self.settings = {}

        self.settings['connection'] = {}
        self.settings['connection']['port'] = int(self.port_value.text())
        self.settings['connection']['clientId'] = int(self.clientID_v.text())

        self.settings['sockets'] = {}
        self.settings['sockets']['host'] = str(self.socket_host.text())
        self.settings['sockets']['port'] = int(self.socket_port.text())

        self.settings['database'] = {}
        self.settings['database']['exchange_id'] = int(self.exchange_id.text())

        self.settings['data'] = {}
        self.settings['data']['only_rth'] = self.use_only_RTH_data.isChecked()

        if True:
            try:
                path = '{}{}'.format( os.path.dirname(os.path.abspath(__file__)), '/config/' )
                if not os.path.isdir(path): os.mkdir(path)
                fileName = '{}{}'.format(path, 'settings.json')
                with open(fileName, 'w') as f:
                    f.write(json.dumps(self.settings))
                self.success.emit(True)
            except: self.success.emit(False)
            self.close()
