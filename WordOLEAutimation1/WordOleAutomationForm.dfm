object Form1: TForm1
  Left = 253
  Top = 585
  BorderStyle = bsDialog
  Caption = 'Word Automation Example'
  ClientHeight = 267
  ClientWidth = 310
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 8
    Top = 88
    Width = 43
    Height = 13
    Caption = 'Target 1:'
  end
  object Label2: TLabel
    Left = 8
    Top = 112
    Width = 43
    Height = 13
    Caption = 'Target 2:'
  end
  object Label3: TLabel
    Left = 8
    Top = 136
    Width = 43
    Height = 13
    Caption = 'Target 3:'
  end
  object Button1: TButton
    Left = 80
    Top = 168
    Width = 145
    Height = 65
    Caption = 'Create Word Document'
    TabOrder = 0
    OnClick = Button1Click
  end
  object MemoInfo: TMemo
    Left = 8
    Top = 8
    Width = 289
    Height = 65
    BorderStyle = bsNone
    Lines.Strings = (
      'This example demonstrates how to automate Word with '
      'Delphi. Click this button to create a document and fill it with '
      'contents. In the fields below, you can choose what will '
      'appear in the Word document.')
    ParentColor = True
    ReadOnly = True
    TabOrder = 1
  end
  object Edit1: TEdit
    Left = 64
    Top = 80
    Width = 121
    Height = 21
    TabOrder = 2
    Text = '25.000'
  end
  object Edit2: TEdit
    Left = 64
    Top = 104
    Width = 121
    Height = 21
    TabOrder = 3
    Text = '30.000'
  end
  object Edit3: TEdit
    Left = 64
    Top = 128
    Width = 121
    Height = 21
    TabOrder = 4
    Text = '45.000'
  end
end
