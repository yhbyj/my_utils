import win32com.client as win32
from openpyxl import load_workbook 
from faker import Faker

def convert_xls_to_xlsx(ifname, ofname=None):
    """无损xls转xlsx"""
    if ofname is None:
        ofname = ifname + 'x'
        
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(ifname)
    wb.SaveAs(ofname, FileFormat = 51)  # 56 is for .xls extension
    wb.Close()
    excel.Application.Quit()

def edit_in_place(fname):
    """在原表修改值，不改变格式！"""
    myfake = Faker(locale='zh_CN')
    
    wb = load_workbook(fname)
    ws = wb.active

    title = '2012年7月{}工资清单'.format(myfake.company_prefix())
    ws['A1'] = title
    
    for x in range(3, 105):
        _ = ws.cell(row=x, column=2, value=myfake.name())
        _ = ws.cell(row=x, column=3, value=myfake.ssn())
    wb.save(fname)
    

if __name__ == '__main__':
    import os, shutil

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DOCUMENTS_DIR = os.path.join(BASE_DIR, 'documents')
    
    BACKUP_DIR = os.path.join(DOCUMENTS_DIR, 'backup')
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    ifnames = []
    for item in os.listdir(DOCUMENTS_DIR):
        if item.endswith('.xls'):
            file = os.path.join(DOCUMENTS_DIR, item)
            shutil.copy(file, BACKUP_DIR)
            ifnames.append(file)

    for ifname in ifnames:
        print('Converting...', ifname)
        convert_xls_to_xlsx(ifname)
        print('Done!')

    in_place_file = os.path.join(DOCUMENTS_DIR, 'salary-12-07.xlsx')
    if os.path.exists(in_place_file):
        print('Editing...', in_place_file)
        edit_in_place(in_place_file)
        print('Done!')
        
        
    
