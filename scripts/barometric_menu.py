#!/usr/bin/python3
# Code for the pressure level menu
# Joseph E. Rener
# UCAR
# Boulder, CO USA
# Email: jrener@ucar.edu
# Developed at COMET at University Corporation for Atmospheric Research and the Research Applications Laboratory at the National Center for Atmospheric Research (NCAR)

import wx, helper_functions

class ChangeBarometric(wx.Dialog):
    def __init__(self, parent):
        super(ChangeBarometric, self).__init__(parent)
        inputs = helper_functions.getArguments()
        self.record_interval = str(inputs[0])
        self.chords_interval = str(inputs[1])
        self.chords_toggle = str(inputs[2])
        self.chords_id = str(inputs[3])
        self.chords_link = str(inputs[4])
        self.pressure_level = str(inputs[5])
        self.test_toggle = str(inputs[6])
        self.altitude = str(inputs[7])
        self.InitUI()
        self.SetTitle("Pressure Level Menu")


    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        # Set alert if the custom input is bad (also add saveButton so it can be referenced later)
        self.saveButton = wx.Button(panel, label='Save')
        self.alert = wx.StaticText(panel, label="")
        self.alert.SetForegroundColour(wx.Colour(255,0,0))
        # Add explanation text
        vbox.Add(wx.StaticText(panel, label="By default, pressure level is set to 1013.25"), flag=wx.LEFT|wx.TOP|wx.RIGHT, border=15)
        vbox.Add(wx.StaticText(panel, label="and altitude set to 100000 (to ensure the "), flag=wx.LEFT|wx.RIGHT, border=15)
        vbox.Add(wx.StaticText(panel, label="value is changed, which you can do here.)"), flag=wx.LEFT|wx.BOTTOM|wx.RIGHT, border=15)
        # Make a horizontal line
        line = wx.StaticLine(panel)
        vbox.Add(line, flag=wx.LEFT|wx.BOTTOM|wx.RIGHT|wx.EXPAND, border=7)

        """
        # Add default option
        rb1 = wx.RadioButton(panel, label='1013.25', style=wx.RB_GROUP)
        rb1.Bind(wx.EVT_RADIOBUTTON, self.OnPressureToggle, rb1)
        vbox.Add(rb1, flag=wx.LEFT, border=80)
        self.selected_pressure = rb1
        # Add custom pressure level input (and disable input if it isn't the selected option)
        custom_pl_section = wx.BoxSizer(wx.HORIZONTAL)
        rb2 = wx.RadioButton(panel, label='Custom')
        rb2.Bind(wx.EVT_RADIOBUTTON, self.OnPressureToggle, rb2)
        custom_pl_section.Add(rb2, wx.BOTTOM, border=5) 
        custom_pl_section.Add(wx.StaticText(panel, label=""), flag=wx.RIGHT, border=5)
        self.custom_input = wx.TextCtrl(panel, style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_TEXT, self.OnEdit, self.custom_input)
        if self.pressure_level == "1013.25":
            self.custom_input.Enable(False)
        else:
            rb2.SetValue(True)
            self.custom_input.SetValue(self.pressure_level)
        custom_pl_section.Add(self.custom_input, flag=wx.TOP, border=-4)
        vbox.Add(custom_pl_section, flag=wx.LEFT, border=80)
        """


        # Add pressure level input
        pl_section = wx.BoxSizer(wx.HORIZONTAL)
        pl_section.Add(wx.StaticText(panel, label=""), flag=wx.RIGHT, border=-10)
        pl_section.Add(wx.StaticText(panel, label="Pressure"), flag=wx.ALL, border=10)
        self.pressure_input = wx.TextCtrl(panel, style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_TEXT, self.pressureEdit, self.pressure_input)
        self.pressure_input.SetValue(self.pressure_level)
        pl_section.Add(self.pressure_input, flag=wx.TOP, border=3)
        vbox.Add(pl_section, flag=wx.LEFT, border=75)
        # Add atmosphere input
        at_section = wx.BoxSizer(wx.HORIZONTAL)
        at_section.Add(wx.StaticText(panel, label="Altitude"), flag=wx.ALL, border=10)
        self.altitude_input = wx.TextCtrl(panel, style=wx.ALIGN_LEFT)
        self.Bind(wx.EVT_TEXT, self.altitudeEdit, self.altitude_input)
        self.altitude_input.SetValue(self.altitude)
        at_section.Add(self.altitude_input, flag=wx.ALIGN_CENTER|wx.ALL, border=8)
        vbox.Add(at_section, flag=wx.LEFT, border=75)


        # Make a horizontal line
        line = wx.StaticLine(panel)
        vbox.Add(line, flag=wx.LEFT|wx.TOP|wx.RIGHT|wx.EXPAND, border=7)
        # Place alert
        vbox.Add(self.alert, flag=wx.LEFT, border=10)
        # Add save and cancel buttons
        #TODO there seems to be an issue with these buttons
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.saveButton.Bind(wx.EVT_BUTTON, self.OnSave)
        hbox2.Add(self.saveButton, flag=wx.RIGHT, border=5)
        self.cancelButton = wx.Button(panel, label='Cancel')
        self.cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
        hbox2.Add(self.cancelButton)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)
        # Adjust window size to fit content
        panel.SetSizer(vbox)
        vbox.Fit(self)
    

    def pressureEdit(self, e):
        value = self.pressure_input.GetValue()
        try:
            float(value)
            self.alert.SetLabel("")
            self.saveButton.Enable(True)
            self.pressure_level = value
        except (ValueError, TypeError):
            self.alert.SetLabel("Pressure must be a number.")
            self.saveButton.Enable(False)


    def altitudeEdit(self, e):
        value = self.altitude_input.GetValue()
        try:
            float(value)
            self.alert.SetLabel("")
            self.saveButton.Enable(True)
            self.altitude = value
        except (ValueError, TypeError):
            self.alert.SetLabel("Altitude must be a number.")
            self.saveButton.Enable(False)


    def OnSave(self, e):
        with open("/home/pi/Desktop/variables.txt", 'w') as file:
            file.write(self.record_interval + "," + self.chords_interval + "," + self.chords_toggle + "," + self.chords_id + "," + self.chords_link + "," + str(self.pressure_level) + "," + self.test_toggle + "," + str(self.altitude))
        self.Destroy()


    def OnCancel(self, e):
        self.Destroy()
