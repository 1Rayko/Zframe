import requests, sys, os
_phone = sys.argv[1]
if _phone[0] == '+':
	_phone = _phone[1:]

while True:
	requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
	break
