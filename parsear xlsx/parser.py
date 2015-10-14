from openpyxl import load_workbook

wb=load_workbook("files/CIRUGIA 2014.xlsx")
names=wb.get_sheet_names()
n=len(names)
for i in range(n):
	ws=wb.worksheets[i]
	archivo=open("CIRUGIA/"+names[i],"w")
	for row in ws.rows:
		for cell in row:
			try:
				res=str(cell.value)
				if res=="None":
					res='\t'
				else:
					res+='\t'
				archivo.write(res)
			except:
				pass
		archivo.write('\n')
	archivo.close()