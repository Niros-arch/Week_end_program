# Linux Fundamental
 - Linux is a free and open-source operating system kernel first released on September 17, 1991, by **Linus Trovalds**  
 - Also Linux is a Kernel 
 - Linux is renowned for its **flexibility, stability, security, and performance**, and it powers a vast range of devices
## Linux File System 
- Linux Uses a tree-like structure with critical directories 
![[Pasted image 20260316143846.png]]   
   1. / (root or The top-level directory is the root filesystem and contains all of the files required to boot the operating system before other filesystems are mounted, as well as the files required to boot the other filesystems. After boot, all of the other filesystems are mounted at standard mount points as subdirectories of the root)
   2. /bin, /sbin (essential binaries)
   3. /etc (configuration file)
   4. /home (user directories) 
   5. /var (variable data like logs )
   6. tmp (temporary files)
   7. /boot (Consists of the static bootloader, kernel executable, and files required to boot the Linux OS.)
   8. /dev (Contains device files to facilitate access to every hardware device attached to the system)
   9. /mnt (Temporary mount point for regular file systems)
   10. /opt  (Optional files such as third-party tools can be saved here)
   11. /usr (Contains executables, libraries, man files, etc)
   12. /boot (Consists of the static bootloader, kernel executable, and files required to boot the Linux OS)
## Command line interface
 - command line interface is a text based interface that can give you the control of your computer by using a command on a **Shell or Terminal**
 - A Linux terminal, also called a `shell` or command line, provides a text-based input/output (I/O) interface between users and the kernel for a computer system. The term console is also typical but does not refer to a window but a screen in text mode. In the terminal window, commands can be executed to control the system.
### Basic Linux Commands And There Uses 
#### PWD 
 **pwd** We can find out where we are with this  command
```
$ pwd
/home/prolon
```
#### LS
**ls** to list all the contents inside a directory
     - an it has an option
         - **-l** option to display more information on those directories and files.
         - **-a** to list the hidden files 
#### cd
The **cd** command changes directory:
```
$ pwd
/home/prolon
$ cd /opt
$ pwd
/opt
```
#### clear
**clear** to clear the terminal 
#### touch
**touch** to create an empty file 
#### echo
 **echo** to print  what we right 
    - > to add a text to a file 
    - >> to append output to a file 
 #### su
 The **su** command switches to another user on the machine. You must know their password.
```
su Yemariyam 
```
   - If no username is provided, `su` will attempt to login as root:
```
su
```
#### grep
- **grep** is an incredibly useful command that allows searching the contents of files and the outputs of terminal commands.

**Grepping a File**
```
$ grep [SEARCH_TERM] /path/to/file
```
**or, using pipe (`|`):**
```
$ cat /path/to/file | grep [SEARCH_TERM]
```
**Grepping Terminal Output**
- You can use the pipe operator to run `grep` on the output of any command. A common use case is searching the output of a directory.
```
$ ls -la | grep [SEARCH_TERM]
```
#### awk

- **awk** can be used for manipulating structured text and extracting specific fields. Think of it as a way of selecting a specific column from a load of structured data.

For example, a list of employee names:
```
$ cat name
Nahom Tadesse
Firaol Bulcha 
Barok Yeshiber
```
`awk` could be used to extract the first names of these employees:
```
$ cat employees
Nahom Tadesse
Firaol Bulcha 
Barok Yeshiber
$ cat employees | awk -F ':' '{print $1}'
Nahom 
Firaol  
Barok 
```