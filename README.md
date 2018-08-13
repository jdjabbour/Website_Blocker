# Website_Blocker
This is a simple application that blocks the specified websites during a specified time.  

To add more sites, append your sites to the "website_list" variable.  Once running, if during working hours those sites will be written to the "hosts" file in your system and thus blocking them.

Currently, the application is set with a dummy variable called "hosts_temp" that will call the included sample hosts file.  When ready to implement the application, you will need to change the variable to "hosts_path".  Depending on the OS the application should change the variable to the correct path to your system's hosts file.  Before going live ALWAYS MAKE A BACKUP OF YOUR FILES!!  Once live, you will need to run this application either as an administrator or as sudo, depending on your OS.

There is a file included called "startup_scheduling.txt" that explains how to set this application up to run upon booting your system.
