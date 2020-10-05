from FileTools import FileTool

defter = FileTool(r"Ibrahim\telDefter",["Adı","Soyadı","Tel"])

banka  = FileTool(r"Ibrahim\banka",["Hesap","Tutar","Tip"])

defter.menu()
banka.menu()