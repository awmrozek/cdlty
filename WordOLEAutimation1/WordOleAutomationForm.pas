unit WordOleAutomationForm;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ComObj;

type
  TForm1 = class(TForm)
    Button1: TButton;
    MemoInfo: TMemo;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var
  WordApp, Doc, Range, Table: Variant;
  i, j: Integer;
begin
  try
    WordApp := CreateOleObject('Word.Application');
    WordApp.Visible := True;

    Doc := WordApp.Documents.Add;

    // Add title
    Doc.Content.Text := 'Sales Report' + #13#10;
    Doc.Content.Font.Size := 16;
    Doc.Content.Font.Bold := True;

    // Move to end and add table
    Range := Doc.Content;
    Range.Collapse(0); // wdCollapseEnd
    Range.InsertAfter(#13#10);

    // Create table
    Range := Doc.Content;
    Range.Collapse(0);
    Table := Doc.Tables.Add(Range, 4, 3);

    // Add headers
    Table.Cell(1, 1).Range.Text := 'Month';
    Table.Cell(1, 2).Range.Text := 'Sales';
    Table.Cell(1, 3).Range.Text := 'Target';

    // Add data
    Table.Cell(2, 1).Range.Text := 'January';
    Table.Cell(2, 2).Range.Text := '$25,000';
    Table.Cell(2, 3).Range.Text := Edit1.Text;

    Table.Cell(3, 1).Range.Text := 'February';
    Table.Cell(3, 2).Range.Text := '$28,000';
    Table.Cell(3, 3).Range.Text := Edit2.Text;

    Table.Cell(4, 1).Range.Text := 'March';
    Table.Cell(4, 2).Range.Text := '$32,000';
    Table.Cell(4, 3).Range.Text := Edit3.Text;

    // Format table
    Table.Rows.Item(1).Range.Font.Bold := True;
    Table.Borders.Enable := True;
    Table.AutoFitBehavior(1); // wdAutoFitContent

  except
    on E: Exception do
      ShowMessage('Error: ' + E.Message);
  end;
end;

end.
