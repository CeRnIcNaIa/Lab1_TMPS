from abc import ABC, abstractmethod

class StatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def  create(self): pass

class MainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass

class MainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass

class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created status bar for {self._system}')

class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created main menu for {self._system}')

class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created Main Window for {self._system}')

class AndroidStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Android")

    def create(self):
        print(f'Created status bar for {self._system}')

class AndroidMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Android")

    def create(self):
        print(f'Created main menu for {self._system}')

class AndroidMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Android")

    def create(self):
        print(f'Creater main window for {self._system}')

class GuiAbstractFactory(ABC):
    @abstractmethod
    def getStatusBar(self) -> StatusBar: pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu: pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow: pass

class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()

class AndroidGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return AndroidStatusBar()

    def getMainMenu(self) -> MainMenu:
        return AndroidMainMenu()

    def getMainWindow(self) -> MainWindow:
        return AndroidMainWindow()

class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        main_window = self._gui_factory.getMainWindow()
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        main_window.create()
        status_bar.create()
        main_menu.create()

def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Android": AndroidGuiFactory
    }
    return factory_dict[system_name]()

if __name__ == "__main__":
    system_name = "Android"
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()