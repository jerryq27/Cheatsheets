# Linux

## File System

In Linux, everything is file. The Linux file system organizes these files
in some key directories by convention (depending on the flavor of Linux):

1. **/bin** - contains executable programs and core operating system commands. It is symbolically linked to `/usr/bin`.
1. **/boot** - contains the files needed by the boot loader. The initial RAM file system and kernel also live here.
1. **/dev** - contains device files that are dynamically created based on the various physical (and virtual) devices connected to the system.
1. **/etc** - contains critical configuration files and startup scripts.
1. **/home** - contians each user's home directory and user specific configuration files.
1. **/lib** - contains the shared libraries the system's programs will need. It is symbolically linked to `/usr/lib`. (lib32/ & lib64/ are also common, which are libraries for 32 and 64-bit systems).
1. **/lost+found** - contains chunks of broken files after a system crash.
1. **/media** - contians the mount points for file systems stored on removeable media.
1. **/mnt** - contains temporarily mounted devices like network storage. Some systems do permanently mount devices here.
1. **/opt** - containes optional software added on to the system, usually from some vendor. Rarely used with current systems.
1. **/proc** - contains pseudo files systems. Pseudo file systems are created on startup and destroyed on shutdown. This file system contains information about every running process with subdirectories for each.
1. **/root** - the root user's home directory.
1. **/run** - contains information about the system since boot time (like who's logged in and running daemons).
1. **/sbin** - contains files similar to /bin. Little practical difference between bin/ and sbin/ in most systems. Usually symbolically linked to `/usr/sbin`.
1. **/srv** - can be used as a folder for files served by servers such as a web server or file server. Depends on the flavor whether this is used or not.
1. **/sys** - contains informaiton about the devices, drivers, and kernel featurs running on the system. Often described as a better structured `/proc`.
1. **/tmp** - contians temporary files that won't be kept on the next reboot.
1. **/usr** - contians most programs and utilities the system will be running. Hence why `/bin`, `/sbin`, and `/lib` are usually symbolically linked here. Since this is where most programs and utilities live, it is shared between all users and read only except for root.
1. **/var** - contains system specific variable files, like logs, temporary message files, and spool files. May sometimes contain configuration files, or web server files.

> Running `man hier` also gives information about the Linux file system.

## Basic Navigation

* `CTRL + -> | <-` - Navigate by word.
* `CTRL + a` - Go to the beginning of the line.
* `CTRL + e` - Go to the end of the line.
* `CTRL + r` - Search history, use command again to cycle through matches.
* `$COMMAND &` - Runs a command in the background, giving control back to the terminal.

## Basic File I/O

* `$COMMAND > $FILE` - Overwrite `$FILE` with the output of the command.
* `$COMMAND >> $FILE` - Appends the command's output to `$FILE`.
* `sha1sum $FILE` - Generates a checksum hash of a file, usefule to compare it to the checksum of the file on a site.
* `tail -f $FILE` - Follow changes to a file, useful for logs.
* `whereis $COMMAND` - Displays the path where the executable is located.
* `sed` - stream editor.
  * `s/$SEARCH/$REPLACE/` - replaces the first occurance on each line.
  * `s/$SEARCH/$REPLACE/$N` - replaces $N occurances on each line.
  * `s/$SEARCH/$REPLACE/g` - replaces all occurances on each line.

## Permissions

Output from `ls -l`:

```bash
-rw-rw-r-- 1 jerry jerry 428 Oct  3 18:23 test.txt
# [?] [UUUGGGOOO(S)] [00] [UUUUUU] [GGGGGG] [####] [TTTT] [FFFF]
```

This output has 7 sections:

1. File or directory:
    * **-** = File
    * **d** = Directory
1. User/Group/Other permissions:
    * **r** = read
    * **w** = write
    * **x** = execute (or search in a directory)
1. The number of links the file has.
1. Owner.
1. Group.
1. File size in bytes.
1. Time stamp.
1. File name

`chmod`

Permissions can be changed with `chmod $REFERANCE $OPERATOR $PERMISSIONS $FILE`

Referances:

* **u** = owner (user) - The owner of the file.
* **g** = group - all users a part of the group.
* **o** = others - users who are neither the owner nor members of the file's group.
* **a** = all - All, same as **ugo**.

Operators:

* **+** - adds a permission.
* **-** - removes a permission.
* **=** - sets permissions equal what's specified.

Permissions:

* **4/r** = read
* **2/w** = write
* **1/x** = execute

> The reason for these numbers? Binary! (100 = read, 010 = write, 001 = execute)

## Users & Groups

* `adduser $USER` - creates a user in the system.
* `deluser $USER` - deletes a user in the system.
* `addgroup $GROUP` - creates a group in the system.
* `passwd` - change the password of the current user.

> user\* & group\* commands (useradd, userdel, usermod, groupadd) are lower level commands used in
their more user frendly commands.

## Processes

* `ps` - lists all the processes you own.
* `ps -ax` - lists all the processes.
* `kill $PID` - kills the specified process by its ID.
* `systemctl` - controller for **systemd** and service manager.
  * `start $PROCESS` - starts a process.
  * `status $PROCESS` - status information of the process.
  * `restart $PROCESS` - restarts the process.

## SSH

Provides a secure connection between computers.

### Client

`ssh $USER@$SERVER`

### Server

Config file: `/etc/ssh/sshd_config`.
Adding **public RSA keys** to `~/.ssh/authorized_keys` allows for public/private key authentication.

## Networking

* `ifconfig` - list network information.
* `ufw` - Uncomplicated Firewall, friendlier frontend for `iptables` commands.
  * `enable` - enables firewall.
  * `disable` - disables firewall.
  * `status` - shows firewall status.
  * `allow $RULE` - allows a service, or rule.
  * `deny $RULE` - denies a request, wait time before request gets rejected.
  * `reject $RULE` - rejects a request, no wait time.

## Other Commands

`chntpw`

1. Mount the Windows HDD if necessary, take note of the HD label.
    * `mount dev/sda2/ $MOUNT_DIRECTORY`
1. `cd /media/$HDD_LABEL/Windows/system32/config`
1. `sudo chntpw SAM`

## Research

* What are jobs?
  * jobs - list jobs
  * `fg %$JOB_NUMBER` - brings background process to the foreground
