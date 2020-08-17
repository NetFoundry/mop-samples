# Overview

  This guide will help you understand the cloud vendor specific rules and guideline for remotely accessing
  the "NetFoundry Zero Trust Network" image once it's instantiated.

{!common/ssh-authentication-important.md!}

{!common/root-ssh-disabled-important.md!}

{!common/nfadmin-ssh.md!}

# AliCloud Specifics

* Username Allowed: nfadmin
* Root Allowed: No
* Password Authentication: Yes

The AliCloud image username is "nfadmin". Please assign an ssh key when launching the instance, if you wish to access this machine post deployment.

!!! Note
    **Password Reset**: In order for the password reset function to work, you must reboot the machine afterward the procedure is complete for the password to take effect.


Read more on the AliCloud documentation [Here](https://www.alibabacloud.com/help/doc-detail/71529.htm)



