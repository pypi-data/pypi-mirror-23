WinPET is a privilege escalation command line tester built on Python 2.7.
WinPET uses Click for command line functionality.
WinPET allows the user to determine whether a given Windows service is vulnerable to privilege escalation.
WinPET checks the Windows registry key for the given service and checks to see if the ImagePath is quoted.
The permissions to the path are then checked by piping the ICACLS command and retrieving the output.
Finally, the permissions for the registry key and service are checked.


