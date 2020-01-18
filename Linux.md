# Linux

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

> user* & group* commands (useradd, userdel, usermod, groupadd) are lower level commands used in
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
1. `cd /media/$HDD_LABEL/Windows/system32/config`
1. `sudo chntpw SAM`

## Research

* What are jobs?
  * jobs - list jobs
  * `fg %$JOB_NUMBER` - brings background process to the foreground
