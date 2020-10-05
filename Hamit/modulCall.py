from FileTools import FileTool

defter = FileTool(r"Hamit\telDefter",["Adı","Soyadı","Tel"])

banka  = FileTool(r"Hamit\banka",["Hesap","Tutar","Tip"])

defter.menu()
banka.menu()