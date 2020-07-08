# Locale issue:

      sudo -i
      locale
      export LANGUAGE=en_US.UTF-8; export LANG=en_US.UTF-8; export LC_ALL=en_US.UTF-8; locale-gen en_US.UTF-8
      dpkg-reconfigure locales

# Swap Left Ctrl and Alt (seems not work well :( )

      Add ~/.Xmodmap
      
      clear control
      clear mod1
      keycode 37 = Alt_L Meta_L
      keycode 64 = Control_L
      add control = Control_L Control_R
      add mod1 = Alt_L Meta_L
      
      Then run xmodmap ~/.Xmodmap

# Disk usage:

     du -ahd1 | sort -h
note *d1* means max depth is 1. Don't use *chs*, it won't count hidden directories.
 
      
PyCharm issue:  Index file .PyCharmCE2017.3/system/caches/content.dat.storageData is too big.
Use File -> Invidate Caches to invaidate and restart.


# Use tmate to work remotely

Start tmate on server:

      tmate
      tmate detatch
      
Then you can connect to server:

      ssh ro-s8EGu5v1WessJXBuUj7SR2adg@sg2.tmate.io

Use transfer.sh to transfer file (no scp support in tmate):

      # Upload
      curl --upload-file ./hello.txt https://transfer.sh/hello.txt 
      # Download
      curl https://transfer.sh/66nb8/hello.txt -o hello.txt

# Use rsync to share folder between Mac and ubuntu

General options:

      az: archive and compress
      v: verbose
      rn: recursive and no-action (use to list which files will be transfer)
      --delete: delete file if not in source

From remote to local computer

      rsync --progress -azv user@remote.server:/folder/to/copy/ /local/folder
      
If you want to copy specific files, include it in the path.

      rsync --progress -v /path/to/file/file.ext user@remote.server:/remote/folder/

From local to remote computer

      rsync --progress -azv /folder/to/copy/ user@remote.server:/remote/folder

This will copy all files in /folder/to/copy/ to /remote/folder in the remote server, the folder copy itself will not be created in the remote computer, and only its contents will be copied, if you want the folder itself to also be created and then its contents copied inside the newly created copy folder, use this command.

      rsync --progress -azv /folder/to/copy user@remote.server:/remote/folder
      
# Config VNC server on 14.04
https://www.vultr.com/docs/how-to-install-vnc-desktop-on-ubuntu-14-04

Note: replace tightvncserver with vnc4server! Since tightvncserver doesn't support opengl which needs by opencv.

For 16.04, refer to https://linode.com/docs/applications/remote-desktop/install-vnc-on-ubuntu-16-04/

Start vncserver:

      vncserver :1 -geometry 1440x900 -depth 16 -pixelformat rgb565



# Command to view user of PID

      ps -u -p 1234
      
# Backup partition and restore
1) make a usb boot system

use ubuntu "Disks" gui tool, to restore the usb disk from a ubuntu iso.

2) download partclone debs

go to https://packages.ubuntu.com/ and search for partclone, download the deb and its dependency deb nilfs-tools

put the deb files in somewhere in the usb disk.

3) boot from usb disk

select "Try ubuntu without install"

use "sudo apt install ./xxxxx.deb" to install partclone and its dependencies.

4) using partclone to back up and restore

https://partclone.org/usage/

clone /dev/hda1 to hda1.img and display debug information.
   
      partclone.ext4 -c -d -s /dev/hda1 -o hda1.img

check part.img file is correct or not.
   
      partclone.chkimg -d -s partclone.img

restore /dev/hda1 from hda1.img and display debug information.
   
      partclone.ext4 -r -d -s hda1.img -o /dev/hda1


# Live CD boot
For omen880, need to add *acpi=off* in grub to boot.
For the 6850K machine, need to add *nomodeset* in grub to boot.

# Copy large file to usb disk
Stupid disk cache issue if you have large RAM.
https://unix.stackexchange.com/a/107722/94334

      sudo -i

      echo $((16*1024*1024)) > /proc/sys/vm/dirty_background_bytes
      echo $((48*1024*1024)) > /proc/sys/vm/dirty_bytes

To retore back:

      echo 0 > /proc/sys/vm/dirty_background_bytes
      echo 0 > /proc/sys/vm/dirty_bytes


## Find files exclude directory

      find . -path ./misc -prune -o -name '*.txt' -print

## Bash rename files
rename all xxx_h.png to xxx_half.png:

      for file in *.png; do mv "$file" "${file/_h.png/_half.png}"; done

## find and xargs

      find . [args] -print0 | xargs -0 -n1 [cmd]
      
-print0 Tells find to print all results to std, each separated with the ASCII NUL character ‘\000’    
-0 Tells xargs that the input will be separated with the ASCII NUL character ‘\000’    
   NUL charater separation is a way to escape files which also contain spaces in their filenames.    
-n1 Tells xarg to execute the command [cmd] with only one argument    

      tensorflow-master$ find . -regextype grep -regex ".*tensor.*[0-9]\{2\}.jpg"
      ./tensorflow/examples/tutorials/deepdream/pilatus800.jpg
      
-regextype to specify regex format
note it matches the whole path string, not only the filename.


## suspend and wakup

Sleep and wakeup after seconds:

      sudo rtcwake -m mem -s 3600 # try different -m options to see if it is supported
      
Sleep after some time:

      sleep 2h 45m 20s && systemctl suspend -i
      
## Yocto linux set static IP

Modify /etc/network/interfaces:

      auto eth0
      iface eth0 inet static
              address 192.168.1.100
              netmask 255.255.255.0
              network 192.168.1.0
              gateway 192.168.1.1
        
