#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtNetwork
from . import const
from .reply import Reply
from .message import Message


class Qonnection(QtCore.QObject):
    sigConnectedToSpec = QtCore.pyqtSignal()
    sigSpecReplyArrived = QtCore.pyqtSignal(object, object)
    sigError = QtCore.pyqtSignal(str)
    DelayAbort = 100  # ms
    StartingReconnectDelay = 500  # ms
    MaxReconnectDelay = 64000  # ms

    def __init__(self, address, reconnect=True):
        super().__init__()
        self._address = address
        self._connected = False
        self._aborting = False
        self._waiting = False
        self._reconnect_delay = self.StartingReconnectDelay
        self._reconnect = reconnect
        self._connect()

    def _connect(self):
        host, port = self._address
        self._host = host
        try:
            self._port = int(port)
        except ValueError:
            self._searching = True
            self._port = const.SPEC_MIN_PORT
            self._name = port
        else:
            self._name = ''
            self._searching = False
        self._connectToSpec()

    def _connectToSpec(self):
        self._message = Message()
        self._reply = Reply()
        self._setSocket()
        self._connectSignals()
        self._sock.connectToHost(self._host, self._port)

    def send(self, message):
        s = self._sock.state()
        if s == QtNetwork.QAbstractSocket.ConnectedState:
            self._sock.write(message)
        elif s == QtNetwork.QAbstractSocket.UnconnectedState and not self._connected and not self._searching:
            if self._reconnect:
                self._connectToSpec()
            else:
                self.sigError.emit(f'Lost connection to {self._name} at {self._host}:{self._port}')
        else:
            self.sigError.emit(f'Trying to send messages without established connection to {self._name}')

    def _setSocket(self):
        self._sock = QtNetwork.QTcpSocket(self)
        self._sock.setProxy(QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.NoProxy))

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self._sock.connected.connect(self._sayHello)
        self._sock.readyRead.connect(self._readResponse)
        self._sock.disconnected.connect(self._stopConnection)
        self._sock.error.connect(self._serverHasError)

    def _sayHello(self):
        self._waiting = False
        self.send(self._message.hello())

    def _readResponse(self):
        buf = bytes(self._sock.readAll())
        if self._searching and not self._connected:
            for header, answer in self._reply.unpack(buf):
                if header.cmd == const.HELLO_REPLY:
                    if answer == self._name:
                        self._connected = True
                        self._searching = False
                        self._address = self._host, self._port
                        self._reconnect_delay = self.StartingReconnectDelay
                        self.sigConnectedToSpec.emit()
                    else:
                        self._port += 1
                        if self._port >= const.SPEC_MAX_PORT:
                            self._connected = False
                            self._searching = False
                            self._reconnect_delay = self.StartingReconnectDelay
                            self.sigError.emit(f'Count not find {self._name} on the host {self._host}')
                            return
                        self._connectToSpec()
        else:
            for header, answer in self._reply.unpack(buf):
                if header.cmd == const.HELLO_REPLY:
                    self._connected = True
                    self._searching = False
                    self._name = answer
                    self._reconnect_delay = self.StartingReconnectDelay
                    self.sigConnectedToSpec.emit()
                else:
                    self.sigSpecReplyArrived.emit(header, answer)

    def _stopConnection(self):
        self._searching = False
        self._connected = False
        self.sigError.emit(f'The connection to {self._name} at {self._host}:{self._port} has been stopped')
        self.tryReconnect()

    def tryReconnect(self):
        if self._reconnect and not self._waiting:
            self._waiting = True
            if self._reconnect_delay < self.MaxReconnectDelay:
                self._reconnect_delay *= 2
            self.sigError.emit(f'Trying to reconnect in {self._reconnect_delay // 1000} seconds...')
            QtCore.QTimer.singleShot(self._reconnect_delay, self._sayHello)

    def _serverHasError(self):
        self._connected = False
        self._searching = False
        e = self._sock.errorString()
        self.sigError.emit(f'The server {self._name} at {self._host}:{self._port} has an error: {e}')
        self.tryReconnect()

    def close(self):
        self._stopConnection()
        self._sock.close()

    def __repr__(self):
        return f'<Qt SpecConnection to {self._name} running at {self._host}:{self._port}>'

    def isConnected(self):
        return not self._searching and self._connected and self._sock.ConnectedState == self._sock.state()

    def name(self):
        return self._name

    def message(self):
        return self._message

    def abort(self):
        if not self._aborting:
            self.send(self._message.abort())
            self._delay(self.DelayAbort)

    def _delay(self, msec):
        self._aborting = True
        dieTime = QtCore.QTime.currentTime().addMSecs(msec)
        while QtCore.QTime.currentTime() < dieTime:
            QtCore.QCoreApplication.processEvents()
        self._aborting = False
