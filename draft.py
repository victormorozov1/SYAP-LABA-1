import win32com.client as win32

word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open('C:\\Users\\danil\\Desktop\\сяп\\template.docx')

tb = doc.Shapes.AddTextbox(1, 400, 300, 100, 100)
tb.TextFrame.TextRange.Text = "Hello"
tb.TextFrame.MarginTop = 0
tb.TextFrame.MarginLeft = 0
tb.Fill.Visible = 0
tb.Line.Visible = 0

doc.SaveAs2("C:\\Users\\danil\\Desktop\\сяп\\Hello.docx")
doc.Close()
word.Application.Quit()