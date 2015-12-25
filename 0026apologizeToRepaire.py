#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/decent.html
'''
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib

# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
	
# from_addr = 'luotengyang@outlook.com'
# password = ''
# to_addr = 'leopold.moz@pythonchallenge.com'
# smtp_sever = 'smtp-mail.outlook.com'

# msg = MIMEText('<html><body>Dear leopold.moz:' +
#     '<p>I am sorry.</p>' + 
#     '<p>yours luo</p>' + 
#     '</body></html>', 'html', 'utf-8')
# msg['From'] = _format_addr('Pythoner 骆<%s>' % from_addr)
# msg['To'] = _format_addr('Receive<%s>' % to_addr)
# msg['Subject'] = Header('Apologize', 'utf-8').encode()

# server = smtplib.SMTP(smtp_sever, 587)
# server.starttls()
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# Never mind that.
# Have you found my broken zip?
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
# Can you believe what one mistake can lead to?

import hashlib, struct
md5OK = "bbb8b499a0eef99b52c7f13f4e78c24b"
with open("mybroken.zip", 'rb') as bro:
    info = bro.read()
    for i in range(len(info)):
        for c in range(256):
            new = info[:i] + struct.pack("=B", c) + info[i + 1:]
            if hashlib.md5(new).hexdigest() == md5OK:
                with open("0026OK.zip", 'wb') as ok:
                    ok.write(new)
                break