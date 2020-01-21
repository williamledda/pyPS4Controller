import struct


class Actions:
    """
    Actions are inherited in the Controller class.
    In order to bind to the controller events, subclass the Controller class and
    override desired action events in this class.
    """
    def __init__(self):
        pass

    def on_x_press(self):
        pass

    def on_x_release(self):
        pass

    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        pass

    def on_L2_release(self):
        pass

    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        pass

    def on_R2_release(self):
        pass

    def on_up_arrow_press(self):
        pass

    def on_up_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_down_arrow_release(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_right_arrow_release(self):
        pass

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_release(self):
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_release(self):
        pass

    def on_start_press(self):
        pass

    def on_start_release(self):
        pass


class Controller(Actions):

    EVENT_SIZE = struct.calcsize("LhBB")

    def __init__(self, interface):
        """
        Initiate controller instance that is capable of listening to all events on specified input interface
        :param interface: STRING aka /dev/input/js0 or any other PS4 Duelshock controller interface.
        """
        Actions.__init__(self)
        self.stop = False
        self.interface = interface

    def listen(self):

        while not self.stop:

            _file = open(self.interface, "rb")
            event = _file.read(Controller.EVENT_SIZE)
            while event:
                (tv_sec, value, button_type, button_id) = struct.unpack("LhBB", event)
                if button_id not in [6, 7, 8, 11, 12, 13]:
                    self.__event(button_id=button_id, button_type=button_type, value=value)
                event = _file.read(Controller.EVENT_SIZE)

    def __event(self, button_id, button_type, value):

        def L3_event():
            return button_type == 2 and button_id in [1, 0]

        def R3_event():
            return button_type == 2 and button_id in [5, 2]

        def L3_at_rest():
            return button_id in [1, 0] and value == 0

        def L3_up():
            return button_id == 1 and value < 0

        def L3_down():
            return button_id == 1 and value > 0

        def L3_left():
            return button_id == 0 and value < 0

        def L3_right():
            return button_id == 0 and value > 0

        def R3_at_rest():
            return button_id in [2, 5] and value == 0

        def R3_up():
            return button_id == 5 and value < 0

        def R3_down():
            return button_id == 5 and value > 0

        def R3_left():
            return button_id == 2 and value < 0

        def R3_right():
            return button_id == 2 and value > 0

        def circle_pressed():
            return button_id == 2 and button_type == 1 and value == 1

        def circle_released():
            return button_id == 2 and button_type == 1 and value == 0

        def x_pressed():
            return button_id == 1 and button_type == 1 and value == 1

        def x_release():
            return button_id == 1 and button_type == 1 and value == 0

        def triangle_pressed():
            return button_id == 3 and button_type == 1 and value == 1

        def triangle_released():
            return button_id == 3 and button_type == 1 and value == 0

        def square_pressed():
            return button_id == 0 and button_type == 1 and value == 1

        def square_released():
            return button_id == 0 and button_type == 1 and value == 0

        def start_pressed():
            return button_id == 9 and button_type == 2 and value == 1

        def start_released():
            return button_id == 9 and button_type == 2 and value == 0

        def L1_pressed():
            return button_id == 4 and button_type == 1 and value == 1

        def L1_released():
            return button_id == 4 and button_type == 1 and value == 0

        def R1_pressed():
            return button_id == 4 and button_type == 1 and value == 1

        def R1_released():
            return button_id == 4 and button_type == 1 and value == 0

        def L2_pressed():
            return button_id == 3 and button_type == 2 and value == 1

        def L2_released():
            return button_id == 3 and button_type == 2 and value == 0

        def R2_pressed():
            return button_id == 4 and button_type == 2 and value == 1

        def R2_released():
            return button_id == 4 and button_type == 2 and value == 0

        def up_arrow_press():
            return button_id == 10 and button_type == 1 and value < 0

        def up_arrow_release():
            return button_id == 10 and button_type == 1 and value == 0

        def down_arrow_press():
            return button_id == 10 and button_type == 1 and value > 0

        def down_arrow_release():
            return button_id == 10 and button_type == 1 and value == 0

        def left_arrow_press():
            return button_id == 9 and button_type == 1 and value < 0

        def left_arrow_release():
            return button_id == 9 and button_type == 1 and value == 0

        def right_arrow_press():
            return button_id == 9 and button_type == 1 and value > 0

        def right_arrow_release():
            return button_id == 9 and button_type == 1 and value == 0

        if R3_event():
            if R3_at_rest():
                self.on_R3_release()
            elif R3_right():
                self.on_R3_right(value)
            elif R3_left():
                self.on_R3_left(value)
            elif R3_up():
                self.on_R3_up(value)
            elif R3_down():
                self.on_R3_down(value)
        elif L3_event():
            if L3_at_rest():
                self.on_L3_release()
            elif L3_up():
                self.on_L3_up(value)
            elif L3_down():
                self.on_L3_down(value)
            elif L3_left():
                self.on_L3_left(value)
            elif L3_right():
                self.on_L3_right(value)
        elif circle_pressed():
            self.on_circle_press()
        elif circle_released():
            self.on_circle_release()
        elif x_pressed():
            self.on_x_press()
        elif x_release():
            self.on_x_release()
        elif triangle_pressed():
            self.on_triangle_press()
        elif triangle_released():
            self.on_triangle_release()
        elif square_pressed():
            self.on_square_press()
        elif square_released():
            self.on_square_release()
        elif L1_pressed():
            self.on_L1_press()
        elif L1_released():
            self.on_L1_release()
        elif L2_pressed():
            self.on_L2_press(value)
        elif L2_released():
            self.on_L2_release()
        elif R1_pressed():
            self.on_R1_press()
        elif R1_released():
            self.on_R1_release()
        elif R2_pressed():
            self.on_R2_press(value)
        elif R2_released():
            self.on_R2_release()
        elif start_pressed():
            self.on_start_press()
        elif start_released():
            self.on_start_release()
        elif left_arrow_press():
            self.on_left_arrow_press()
        elif left_arrow_release():
            self.on_left_arrow_release()
        elif right_arrow_press():
            self.on_right_arrow_press()
        elif right_arrow_release():
            self.on_right_arrow_release()
        elif up_arrow_press():
            self.on_up_arrow_press()
        elif up_arrow_release():
            self.on_up_arrow_release()
        elif down_arrow_press():
            self.on_down_arrow_press()
        elif down_arrow_release():
            self.on_down_arrow_release()


Controller(interface="/dev/input/js0").listen()
