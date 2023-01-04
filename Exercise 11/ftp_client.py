"""
ftp_client.py
By: Abhinav Tyagi
Date: 02NOV22
"""

import ftplib
import settings.ftp as settings

#make connection
ftp=ftplib.FTP(settings.FTP['URL'])
#anonymous login
ftp.login()
#change to correct directory
ftp.cwd(settings.FTP["PATH"])
#retrieve file
ftp.retrbinary("RETR"+settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()