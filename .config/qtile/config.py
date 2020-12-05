# -*- coding: utf-8 -*-
#  ____ _____
# |  _ \_   _|  Derek Taylor (DistroTube)
# | | | || |  	http://www.youtube.com/c/DistroTube
# | |_| || |  	http://www.gitlab.com/dwt1/
# |____/ |_|
#
# A customized config.py for Qtile window manager (http://www.qtile.org)
# Modified by Derek Taylor (http://www.gitlab.com/dwt1/ )
#
# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

##### IMPORTS #####

import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

##### DEFINING SOME WINDOW FUNCTIONS #####

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

##### LAUNCH APPS IN SPECIFIED GROUPS #####

def app_or_group(group, app):
    def f(qtile):
        if qtile.groupMap[group].windows:
            qtile.groupMap[group].cmd_toscreen()
        else:
            qtile.groupMap[group].cmd_toscreen()
            qtile.cmd_spawn(app)
    return f

##### KEYBINDINGS #####

def init_keys():
    keys = [
            Key(
                [mod], "Return",
                lazy.spawn(myTerm)                      # Open terminal
                ),
            Key(
                [mod], "Tab",
                lazy.next_layout()                      # Toggle through layouts
                ),
            Key(
                [mod, "shift"], "Tab",
                lazy.prev_layout()                      # Toggle through layouts
                ),
            Key(
                [mod, "shift"], "q",
                lazy.window.kill()                      # Kill active window
                ),
            Key(
                [mod, "shift"], "r",
                lazy.restart()                          # Restart Qtile
                ),
            Key(
                [mod, "shift"], "e",
                lazy.shutdown()                         # Shutdown Qtile
                ),
            Key([mod], "w",
                lazy.to_screen(2)                       # Keyboard focus screen(0)
                ),
            Key([mod], "e",
                lazy.to_screen(0)                       # Keyboard focus screen(1)
                ),
            Key([mod], "r",
                lazy.to_screen(1)                       # Keyboard focus screen(2)
                ),
            Key([mod, "control"], "k",
                lazy.layout.section_up()                # Move up a section in treetab
                ),
            Key([mod, "control"], "j",
                lazy.layout.section_down()              # Move down a section in treetab
                ),
            ### Window controls
            Key(
                [mod], "j",
                lazy.layout.down()                      # Switch between windows in current stack pane
                ),
            Key(
                [mod], "k",
                lazy.layout.up()                        # Switch between windows in current stack pane
                ),
            Key(
                [mod], "l",
                lazy.layout.right()                     # Move windows down in current stack
                ),
            Key(
                [mod], "h",
                lazy.layout.left()                      # Move windows down in current stack
                ),
            Key(
                [mod, "shift"], "j",
                lazy.layout.shuffle_down()              # Move windows down in current stack
                ),
            Key(
                [mod, "shift"], "k",
                lazy.layout.shuffle_up()                # Move windows up in current stack
                ),
            Key(
                [mod, "shift"], "l",
                lazy.layout.right()                     # Move windows down in current stack
                ),
            Key(
                [mod, "shift"], "h",
                lazy.layout.left()                      # Move windows down in current stack
                ),
            Key(
                [mod], "Up",
                lazy.layout.grow()                      # Grow size of current window (XmonadTall)
                ),
            Key(
                [mod], "Down",
                lazy.layout.shrink()                    # Shrink size of current window (XmonadTall)
                ),
            Key(
                [mod], "i",
                lazy.layout.increase_nmaster()          # Increase number in master pane (Tile)
                ),
            Key(
                [mod], "d",
                lazy.layout.decrease_nmaster()          # Decrease number in master pane (Tile)
                ),
            Key(
                [mod, "shift"], "Left",                 # Move window to workspace to the left
                window_to_prev_group
                ),
            Key(
                [mod, "shift"], "Right",                # Move window to workspace to the right
                window_to_next_group
                ),
            Key(
                [mod], "n",
                lazy.layout.normalize()                 # Restore all windows to default size ratios 
                ),
            Key(
                [mod], "m",
                lazy.layout.maximize()                  # Toggle a window between minimum and maximum sizes
                ),
            Key(
                [mod, "shift"], "space",
                lazy.window.toggle_floating()           # Toggle floating
                ),
            Key(
                [mod, "shift"], "Return",
                lazy.layout.flip()                      # Switch which side main pane occupies (XmonadTall)
                ),
            ### Stack controls
            Key(
                [mod], "space",
                lazy.layout.next()                      # Switch window focus to other pane(s) of stack
                ),
            Key(
                [mod, "control"], "Return",
                lazy.layout.toggle_split()              # Toggle between split and unsplit sides of stack
                ),

            ### Rofi Run Launcher
            Key(
                [mod], "x",
                lazy.spawn("rofi -show combi")
                ),
            ### Dmenu Run Launcher
            Key(
                [mod], "p",
                lazy.spawn("dmenu_run -fn 'UbuntuMono Nerd Font:size=10' -h 20 -nb '#191d2e' -nf '#a7a7a7' -sb '#404354' -sf '#d8dee9' -p 'dmenu:'")
                ),

            ### My applications launched with HYPER + KEY
            Key(
                ["mod3"], "space",
                lazy.spawn("pcmanfm")
                ),
            Key(
                ["mod3"], "n",
                lazy.spawn(myTerm+" -e newsboat")
                ),
            Key(
                ["mod3"], "t",
                lazy.spawn(myTerm+" -e tuir")
                ),
            Key(
                ["mod3"], "e",
                lazy.spawn(myTerm+" -e neomutt")
                ),
            Key(
                ["mod3"], "m",
                lazy.spawn(myTerm+" -e mocp")
                ),
            Key(
                ["mod3"], "w",
                lazy.spawn(myTerm+" -e weechat")
                ),
            Key(
                ["mod3"], "a",
                lazy.spawn(myTerm+" -e pulsemixer")
                ),
        ]
    return keys

##### BAR COLORS #####

def init_colors():
    return [["#191d2e", "#191d2e"], # panel background
            ["#434758", "#434758"], # background for current screen tab
            ["#D0D0D0", "#D0D0D0"], # font color for group names
            ["#CC6666", "#CC6666"], # color for layout widget
            ["#000000", "#000000"], # background for other screen tabs
            ["#8ABEB7", "#8ABEB7"], # color for window widget
            ["#B5BD68", "#B5BD68"], # color for network widget
            ["#B294BB", "#B294BB"], # color for pacman widget
            ["#81A2BE", "#81A2BE"], # color for memory widget
            ["#393D4E", "#393D4E"], # background color for clock widget
            ["#434758", "#434758"]] # background color for systray widget

##### GROUPS #####

def init_group_names():
    return [("TERM", {'label': '', 'layout': 'monadtall'}),
            ("WWW", {'label': '', 'layout': 'max'}),
            ("SYS", {'label': '', 'layout': 'monadtall'}),
            ("DOC", {'label': '', 'layout': 'monadtall'}),
            ("VBOX", {'label': '', 'layout': 'floating'}),
            ("CHAT", {'label': '', 'layout': 'matrix'}),
            ("MAIL", {'label': '', 'layout': 'monadtall'}),
            ("MEDIA", {'label': '', 'layout': 'monadtall'}),
            ("GFX", {'label': '', 'layout': 'monadtall'})]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

##### LAYOUTS #####

def init_floating_layout():
    return layout.Floating(border_focus="#3B4022")

def init_layout_theme():
    return {"border_width": 2,
            "single_border_width": 0,
            "single_margin": 0,
            "margin": 3,
            "ratio": .517,
            "border_focus": "6B82AB",
            "border_normal": "2E3036"
           }

def init_border_args():
    return {"border_width": 2}

def init_layouts():
    return [layout.MonadTall(**layout_theme),
            layout.MonadWide(**layout_theme),
            layout.Max(**layout_theme),
            layout.Floating(**layout_theme),
            layout.Matrix(**layout_theme),
            layout.RatioTile(**layout_theme),
            layout.VerticalTile(**layout_theme),
            #layout.Bsp(**layout_theme),
            layout.TreeTab(
                font = "Ubuntu",
                fontsize = 10,
                sections = ["FIRST", "SECOND"],
                section_fontsize = 11,
                bg_color = "141414",
                active_bg = "90C435",
                active_fg = "000000",
                inactive_bg = "384323",
                inactive_fg = "a0a0a0",
                padding_y = 5,
                section_top = 10,
                panel_width = 320,
                **layout_theme
                ),
            #layout.Slice(side="left", width=192, name="gimp", role="gimp-toolbox",
            #    fallback=layout.Slice(side="right", width=256, role="gimp-dock",
            #    fallback=layout.Stack(num_stacks=1, **border_args))),
            #layout.Stack(stacks=2, **layout_theme),
            #layout.Columns(**layout_theme),
            #layout.Zoomy(**layout_theme),
            layout.Tile(
                shift_windows=True,
                **layout_theme
                )]

##### WIDGETS #####

def init_widgets_defaults():
    return dict(font="Hack",
                fontsize = 9,
                padding = 2,
                background=colors[2])

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 22,
                        margin_y = 2,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 1,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_method = "block",
                        this_current_screen_border = colors[1],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        font="Ubuntu Mono",
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(font="Ubuntu",
                        fontsize = 11,
                        foreground = colors[5],
                        background = colors[0],
                        padding = 5
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  ☵",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.CurrentLayout(
                        foreground = colors[3],
                        background = colors[0],
                        padding = 5
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  |",
                        padding = 5,
                        foreground=colors[9],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  ",
                        foreground=colors[2],
                        background=colors[0],
                        padding = 0,
                        fontsize=18
                        ),
               widget.GenPollText(
                        foreground=colors[6],
                        background=colors[0],
                        fmt = ' {} ',
                        update_interval=60,
                        func = lambda: subprocess.check_output("/home/geir/.local/bin/ip.sh").decode("utf-8").replace('\n', '')
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  |",
                        padding = 5,
                        foreground=colors[9],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text=" ⟳",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.CheckUpdates(
                        colour_no_updates = colors[7],
                        colour_have_updates = colors[7],
                        background = colors[0],
                        distro = "Arch",
                        custom_command = "pacman -Qu"
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="   |",
                        padding = 5,
                        foreground=colors[9],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  ",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.GenPollText(
                        update_interval=60,
                        fmt = ' {} ',
                        func = lambda: subprocess.check_output("/home/geir/.local/bin/disk.sh").decode("utf-8").replace('\n', ''),
                        foreground=colors[5],
                        background=colors[0]
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  |",
                        padding = 5,
                        foreground=colors[9],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="  ",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.Memory(
                        foreground=colors[8],
                        background=colors[0]
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="   |",
                        padding = 5,
                        foreground=colors[9],
                        background=colors[0],
                        fontsize=14
                        ),
               widget.TextBox(
                        font="Ubuntu Bold",
                        text="   ",
                        foreground=colors[2],
                        background=colors[0],
                        padding = 5,
                        fontsize=14
                        ),
               widget.Clock(
                        foreground = colors[2],
                        background = colors[0],
                        format="%A, %d %B - %H:%M"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 5,
                        foreground = colors[2],
                        background = colors[0]
                        ),
              ]
    return widgets_list

##### SCREENS #####

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), opacity=0.95, size=20))]

##### FLOATING WINDOWS #####

@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True

def init_mouse():
    return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front

##### DEFINING A FEW THINGS #####

if __name__ in ["config", "__main__"]:
    mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
    myTerm = "st"                                    # My terminal of choice
    myConfig = "/home/geir/.config/qtile/config.py"    # Qtile config file location 

    colors = init_colors()
    keys = init_keys()
    mouse = init_mouse()
    group_names = init_group_names()
    groups = init_groups()
    floating_layout = init_floating_layout()
    layout_theme = init_layout_theme()
    border_args = init_border_args()
    layouts = init_layouts()
    widget_defaults = init_widgets_defaults()
    widgets_list = init_widgets_list()
    screens = init_screens()

##### SETS GROUPS KEYBINDINGS #####

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))          # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))   # Send current window to another group

##### STARTUP APPLICATIONS #####

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

##### NEEDED FOR SOME JAVA APPS #####

#wmname = "LG3D"
wmname = "qtile"
