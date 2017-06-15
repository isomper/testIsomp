;谷歌证书弹出框
$hWnd = WinWait("使用确认请求", "", 10)
WinActivate($hWnd)
For $i=1 To 3
	Send("{TAB}")
	Sleep(500)
Next
;Send("{Tab 3}")
Send("{ENTER}")