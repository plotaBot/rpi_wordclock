import gi
import subprocess
import shlex
from datetime import datetime

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class time_manipulator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Time Manipulator")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Reset")
        button.connect("clicked", self.on_reset_clicked)
        hbox.pack_start(button, False, False, 0)

        policy = Gtk.SpinButtonUpdatePolicy.IF_VALID

        #create hour Spinner
        hour_adj = Gtk.Adjustment(value=0, lower=0, upper=23, step_increment=1, page_increment=1, page_size=0)
        self.hour = Gtk.SpinButton.new(hour_adj, 0, 0)
        self.hour.set_update_policy(policy)
        self.hour.set_numeric(True)
        self.hour.set_wrap(True)
        self.hour.connect("value-changed", self.on_hour_changed)
        hbox.pack_start(self.hour, False, False, 0)

        # create minute Spinner
        minute_adj = Gtk.Adjustment(value=0, lower=0, upper=59, step_increment=5, page_increment=1, page_size=0)
        self.minute = Gtk.SpinButton.new(minute_adj, 0, 0)
        self.minute.set_update_policy(policy)
        self.minute.set_numeric(True)
        self.minute.set_wrap(True)
        self.minute.connect("value-changed", self.on_minute_changed)
        hbox.pack_start(self.minute, False, False, 0)

        self.displayTime()

    def on_hour_changed(self, button):
        setTime(hour=int(button.get_value()))

    def on_minute_changed(self, button):
        setTime(minute=int(button.get_value()))

    def on_reset_clicked(self, button):
        self.displayTime()
        #reset time to the one from the system's ntp server
        subprocess.call(shlex.split("timedatectl set-ntp true"))

    def displayTime(self):
        now = datetime.now()
        self.hour.props.value = now.hour
        self.minute.props.value = now.minute

def setTime(hour=None, minute=None):
    now = datetime.now()
    hour = hour if type(hour) is int else now.hour
    minute = minute if type(minute) is int else now.minute

    new = now.replace(hour=hour, minute=minute)

    time_string = new.isoformat()

    subprocess.call(shlex.split("timedatectl set-ntp false"))  # May be necessary
    subprocess.call(shlex.split("date -s '%s'" % time_string))
    #subprocess.call(shlex.split("hwclock -w"))


win = time_manipulator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
