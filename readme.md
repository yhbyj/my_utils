#My Python Utils  
测试环境： anaconda3      
## 文本处理（text_editors.py）
### 大小写互换(shift_text)
```text
abc123XYZ#
-->
ABC123xyz#
```
## 电子表格处理（excel_editors.py）
### 无损xls转xlsx(convert_xls_to_xlsx)
```text
*.xls
-->
*.xlsx
```
### 就地修改(edit_in_place)
```text
修改电子表格的值，不改变格式！
```
### 创建群邮件(create_mails)
```text
从电子表格中提取邮件地址，提取内容并格式化！
```
## 邮件处理（email_editors.py）
### 测试邮件发送(test_mail_sending)
```text
smtp.qq.com
```
### 群发邮件(send_mails)
```text
sendmail(sender, [m['receiver'], ], m['message'])
```