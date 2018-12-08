# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import ComboBox


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent, param_kat):
        self.parameter_kategori = param_kat
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(936, 638), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook3 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_notebook3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        self.Training_page = wx.Panel(self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_judul = wx.StaticText(self.Training_page, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_judul.Wrap(-1)
        bSizer9.Add(self.m_judul, 0, wx.ALL, 5)

        self.m_training_judul = wx.TextCtrl(self.Training_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer9.Add(self.m_training_judul, 0, wx.ALL | wx.EXPAND, 5)

        self.m_topik = wx.StaticText(self.Training_page, wx.ID_ANY, u"Kategori", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_topik.Wrap(-1)
        bSizer9.Add(self.m_topik, 0, wx.ALL, 5)

        self.choices = self.parameter_kategori
        self.m_training_topik = ComboBox.PromptingComboBox(self.Training_page, "", self.choices, style=wx.CB_SORT)
        bSizer9.Add(self.m_training_topik, 0, wx.ALL | wx.EXPAND, 5)

        self.m_abstrak = wx.StaticText(self.Training_page, wx.ID_ANY, u"Abstrak", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_abstrak.Wrap(-1)
        bSizer9.Add(self.m_abstrak, 0, wx.ALL, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_training_abstrak = wx.TextCtrl(self.Training_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, wx.TE_MULTILINE)
        bSizer10.Add(self.m_training_abstrak, 1, wx.ALL | wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.Add_training = wx.Button(self.Training_page, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.Add_training, 0, wx.ALL, 5)

        self.proses_training = wx.Button(self.Training_page, wx.ID_ANY, u"proses training", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer13.Add(self.proses_training, 0, wx.ALL, 5)

        bSizer10.Add(bSizer13, 0, 0, 5)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        self.Training_page.SetSizer(bSizer9)
        self.Training_page.Layout()
        bSizer9.Fit(self.Training_page)
        self.m_notebook3.AddPage(self.Training_page, u"Training", True)

        bSizer3.Add(self.m_notebook3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.m_notebook31 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_notebook31.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        self.Training_page1 = wx.Panel(self.m_notebook31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        bSizer91 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText21 = wx.StaticText(self.Training_page1, wx.ID_ANY, u"Judul", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        bSizer91.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_ctrl_test_judul = wx.TextCtrl(self.Training_page1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer91.Add(self.m_ctrl_test_judul, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self.Training_page1, wx.ID_ANY, u"Abstrak", wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_MULTILINE)
        self.m_staticText11.Wrap(-1)
        bSizer91.Add(self.m_staticText11, 0, wx.ALL, 5)

        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        self.m_judul_text_abstrak = wx.TextCtrl(self.Training_page1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        bSizer101.Add(self.m_judul_text_abstrak, 1, wx.ALL | wx.EXPAND, 5)

        self.proses_testing = wx.Button(self.Training_page1, wx.ID_ANY, u"Process", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        bSizer101.Add(self.proses_testing, 0, wx.ALL, 5)

        bSizer91.Add(bSizer101, 1, wx.EXPAND, 5)

        self.Training_page1.SetSizer(bSizer91)
        self.Training_page1.Layout()
        bSizer91.Fit(self.Training_page1)
        self.m_notebook31.AddPage(self.Training_page1, u"Testing", False)

        bSizer1.Add(self.m_notebook31, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem_training = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Data Training", wx.EmptyString,
                                               wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem_training)

        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, u"Option")

        self.About_Menu = wx.Menu()
        self.m_menubar1.Append(self.About_Menu, u"About")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass




###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(601, 284), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap7 = wx.StaticBitmap(self.m_panel4, wx.ID_ANY, wx.ICON(wx.ICON_WARNING), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer9.Add(self.m_bitmap7, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer9)
        self.m_panel4.Layout()
        bSizer9.Fit(self.m_panel4)
        bSizer8.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dataViewList_number = self.m_dataViewListCtrl1.AppendTextColumn(u"No")
        self.m_dataViewList_kategori = self.m_dataViewListCtrl1.AppendTextColumn(u"Kategori")
        self.m_dataViewList_jumlah = self.m_dataViewListCtrl1.AppendTextColumn(u"Jumlah")
        bSizer12.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button4_exit = wx.Button(self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button4_exit, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


# class MyFrame3(wx.Frame):
#
#     def __init__(self, parent):
#         wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
#                           size=wx.Size(423, 745), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
#
#         self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
#         self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
#
#         bSizer12 = wx.BoxSizer(wx.VERTICAL)
#
#         self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
#         self.m_panel4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
#
#         bSizer13 = wx.BoxSizer(wx.VERTICAL)
#
#         self.m_staticText6 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0)
#         self.m_staticText6.Wrap(-1)
#         bSizer13.Add(self.m_staticText6, 0, wx.ALL, 5)
#
#         self.m_judul_result = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
#                                           wx.TE_READONLY)
#         bSizer13.Add(self.m_judul_result, 0, wx.ALL | wx.EXPAND, 5)
#
#         self.m_staticText7 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Abstrak", wx.DefaultPosition, wx.DefaultSize, 0)
#         self.m_staticText7.Wrap(-1)
#         bSizer13.Add(self.m_staticText7, 0, wx.ALL, 5)
#
#         self.m_abstrak_result = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
#                                             wx.Size(-1, -1), wx.TE_MULTILINE | wx.TE_READONLY)
#         self.m_abstrak_result.SetMinSize(wx.Size(-1, 200))
#
#         bSizer13.Add(self.m_abstrak_result, 0, wx.ALL | wx.EXPAND, 5)
#
#         self.m_staticText8 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Hasil Stemming dan Tokenisasi",
#                                            wx.DefaultPosition, wx.DefaultSize, 0)
#         self.m_staticText8.Wrap(-1)
#         bSizer13.Add(self.m_staticText8, 0, wx.ALL, 5)
#
#         self.m_stem_result = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
#                                          wx.TE_MULTILINE | wx.TE_READONLY)
#         self.m_stem_result.SetMinSize(wx.Size(-1, 200))
#
#         bSizer13.Add(self.m_stem_result, 0, wx.ALL | wx.EXPAND, 5)
#
#         self.m_result = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 150),
#                                     wx.TE_MULTILINE | wx.TE_READONLY | wx.ALWAYS_SHOW_SB)
#         self.m_result.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
#         bSizer13.Add(self.m_result, 1, wx.ALL | wx.EXPAND, 5)
#
#         #=================================================#
#
#         self.m_dataViewList_result = wx.dataview.DataViewListCtrl(self.m_panel4, wx.ID_ANY, wx.DefaultPosition,
#                                                                   wx.DefaultSize, 0)
#         self.m_dataViewList_result.SetMinSize(wx.Size(-1, 100))
#
#         self.m_dataViewListColumn4 = self.m_dataViewList_result.AppendTextColumn(u"Ket")
#         self.m_dataViewListColumn5 = self.m_dataViewList_result.AppendTextColumn(u"Presicion")
#         self.m_dataViewListColumn6 = self.m_dataViewList_result.AppendTextColumn(u"Recall")
#         self.m_dataViewListColumn7 = self.m_dataViewList_result.AppendTextColumn(u"F1-Score")
#         self.m_dataViewListColumn8 = self.m_dataViewList_result.AppendTextColumn(u"Support")
#         bSizer13.Add(self.m_dataViewList_result, 0, wx.ALL | wx.EXPAND, 5)
#
#
#         #=================================================#
#
#         bSizer14 = wx.BoxSizer(wx.HORIZONTAL)
#
#         self.m_button_exit_result = wx.Button(self.m_panel4, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0)
#         bSizer14.Add(self.m_button_exit_result, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
#
#         bSizer13.Add(bSizer14, 0, wx.ALIGN_RIGHT, 5)
#
#         self.m_panel4.SetSizer(bSizer13)
#         self.m_panel4.Layout()
#         bSizer13.Fit(self.m_panel4)
#         bSizer12.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)
#
#         self.SetSizer(bSizer12)
#         self.Layout()
#
#         self.Centre(wx.BOTH)
#
#     def __del__(self):
#         pass

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(936, 712), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"Judul", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer13.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_judul_result = wx.TextCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_READONLY)
        bSizer13.Add(self.m_judul_result, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"Abstrak", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer13.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_abstrak_result = wx.TextCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(-1, -1), wx.TE_MULTILINE | wx.TE_READONLY | wx.ALWAYS_SHOW_SB)
        self.m_abstrak_result.SetMinSize(wx.Size(-1, 150))

        bSizer13.Add(self.m_abstrak_result, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"Preprocessing", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer13.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_stem_result = wx.TextCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY | wx.ALWAYS_SHOW_SB)
        self.m_stem_result.SetMinSize(wx.Size(-1, 150))

        bSizer13.Add(self.m_stem_result, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText81 = wx.StaticText(self.m_scrolledWindow2, wx.ID_ANY, u"Result", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        bSizer13.Add(self.m_staticText81, 0, wx.ALL, 5)

        self.m_result = wx.TextCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(-1, 100),
                                    wx.TE_MULTILINE | wx.TE_NO_VSCROLL | wx.TE_READONLY | wx.ALWAYS_SHOW_SB)
        self.m_result.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer13.Add(self.m_result, 1, wx.ALL | wx.EXPAND, 5)

        self.m_dataViewList_result = wx.dataview.DataViewListCtrl(self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition,
                                                                  wx.DefaultSize, 0)
        self.m_dataViewList_result.SetMinSize(wx.Size(-1, 100))

        self.m_dataViewListColumn4 = self.m_dataViewList_result.AppendTextColumn(u"Ket")

        self.m_dataViewListColumn5 = self.m_dataViewList_result.AppendTextColumn(u"Presicion")
        self.m_dataViewListColumn6 = self.m_dataViewList_result.AppendTextColumn(u"Recall")
        self.m_dataViewListColumn7 = self.m_dataViewList_result.AppendTextColumn(u"F1-Score")
        self.m_dataViewListColumn8 = self.m_dataViewList_result.AppendTextColumn(u"Support")
        bSizer13.Add(self.m_dataViewList_result, 0, wx.ALL | wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button5_ext = wx.Button(self.m_scrolledWindow2, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        bSizer14.Add(self.m_button5_ext, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer13.Add(bSizer14, 0, wx.ALIGN_RIGHT, 5)

        self.m_scrolledWindow2.SetSizer(bSizer13)
        self.m_scrolledWindow2.Layout()
        bSizer13.Fit(self.m_scrolledWindow2)
        bSizer12.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
