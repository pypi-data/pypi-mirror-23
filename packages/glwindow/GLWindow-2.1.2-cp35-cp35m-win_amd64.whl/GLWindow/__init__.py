'''
    OpenGL Window

    Examples:

        A Simple window::

            import GLWindow

            wnd = GLWindow.create_window()

            # Initialize Scene

            while wnd.update():
                # Render Scene
'''

# pylint: disable=using-constant-test

import os
from typing import Tuple, List

try:
    from . import glwnd

except ImportError:

    if os.environ.get('READTHEDOCS') == 'True':
        from .mock import glwnd

    else:
        _IMPORT_ERROR = '\n'.join([
            'No implementation found for GLWindow',
            'Are you sure the source code is compiled properly?',
            'Hint: python3 setup.py build_ext -b .',
        ])

        raise ImportError(_IMPORT_ERROR) from None

from . import keys


__all__ = [
    'Window', 'create_window', 'get_window', 'keys',
]

__version__ = '0.2.2'


class Window:
    '''
        Window
    '''

    def __init__(self):
        self.wnd = None
        raise Exception('Call create_window()')

    def clear(self, red=0.0, green=0.0, blue=0.0, alpha=0.0) -> None:
        '''
            set the window to clear mode
        '''

        self.wnd.clear(red, green, blue, alpha)

    def fullscreen(self) -> None:
        '''
            set the window to fullscreen mode
        '''

        self.wnd.fullscreen()

    def windowed(self, width, height) -> None:
        '''
            set the window to windowed mode
        '''

        self.wnd.windowed(width, height)

    def update(self) -> None:
        '''
            process window events
            swap buffers
            update key states
        '''

        return self.wnd.update()

    def make_current(self) -> None:
        '''
            activate the opengl context associated with the window
        '''

        self.wnd.make_current()

    def keys(self, key) -> List[str]:
        '''
            keys down
        '''

        return [keys.KEY_NAME.get(i, '%02X' % i) for i in range(256) if self.key_down(i)]

    def key_pressed(self, key) -> bool:
        '''
            Is the key pressed?

            Args:
                key (int or str): The key or keycode.

            Returns:
                bool: True if the key is pressed, otherwise False
        '''

        return self.wnd.key_pressed(key)

    def key_down(self, key) -> bool:
        '''
            Is the key down?

            Args:
                key (int or str): The key or keycode.

            Returns:
                bool: True if the key is down, otherwise False
        '''

        return self.wnd.key_down(key)

    def key_released(self, key) -> bool:
        '''
            Is the key released?

            Args:
                key (int or str): The key or keycode.

            Returns:
                bool: True if the key is released, otherwise False
        '''

        return self.wnd.key_released(key)

    def key_up(self, key) -> bool:
        '''
            Is the key up?

            Args:
                key (int or str): The key or keycode.

            Returns:
                bool: True if the key is up, otherwise False
        '''

        return self.wnd.key_up(key)

    def set_icon(self, filename):
        '''
            set the window icon
            to set the small icon use :py:meth:`~Window.set_small_icon` instead
        '''

        self.wnd.set_icon(filename)

    def set_small_icon(self, filename):
        '''
            set the small window icon
            to set the large icon use :py:meth:`~Window.set_icon` instead
        '''

        self.wnd.set_small_icon(filename)

    def grab_mouse(self, grab):
        '''
            lock the mouse to the center of the window
            use the :py:attr:`mouse` or :py:attr:`mouse_delta` to get the mouse position
        '''

        self.wnd.grab_mouse(grab)

    @property
    def mouse(self) -> Tuple[int, int]:
        '''
            tuple: The mouse of the window.
        '''

        return self.wnd.mouse

    @property
    def mouse_delta(self) -> Tuple[int, int]:
        '''
            tuple: The mouse_delta of the window
        '''

        return self.wnd.mouse_delta

    @property
    def size(self) -> Tuple[int, int]:
        '''
            tuple: size of the window
        '''

        return self.wnd.size

    @property
    def ratio(self) -> float:
        '''
            float: the ratio of the window
        '''

        return self.wnd.size[0] / self.wnd.size[1]

    @property
    def viewport(self) -> Tuple[int, int, int, int]:
        '''
            tuple: viewport of the window
        '''

        return self.wnd.viewport

    @property
    def title(self) -> str:
        '''
            str: title of the window
        '''

        raise NotImplementedError()

    @title.setter
    def title(self, value):
        self.wnd.title = value

    @property
    def vsync(self) -> bool:
        '''
            bool: vsync
        '''

        return self.wnd.vsync

    @vsync.setter
    def vsync(self, value):
        self.wnd.vsync = value

    @property
    def time(self) -> float:
        '''
            float: time
        '''

        return self.wnd.time

    @property
    def text_input(self) -> str:
        '''
            str: text_input
        '''

        return self.wnd.text_input


def create_window(width=None, height=None, samples=16, *, fullscreen=False, title=None, threaded=True) -> Window:
    '''
        create the main window
    '''

    if samples < 0 or (samples & (samples - 1)) != 0:
        raise Exception('Invalid number of samples: %d' % samples)

    if (width is None) ^ (height is None):
        raise Exception('Error width = %r and height = %r' % (width, height))

    window = Window.__new__(Window)
    window.wnd = glwnd.create_window(width, height, samples, fullscreen, title, threaded)
    return window


def get_window() -> Window:
    '''
        Returns the main window.
    '''

    return glwnd.get_window()
