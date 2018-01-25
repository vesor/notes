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


# Config p4merge as external git diff tool

      git config --global diff.tool p4merge
      git config --global difftool.p4merge.cmd "~/Applications/p4v/bin/p4merge \$LOCAL \$REMOTE"

Changes are made to your ~/.gitconfig:

      [diff]
          tool = p4merge
      [difftool "p4merge"]
          cmd = ~/Applications/p4v/bin/p4merge $LOCAL $REMOTE
          
Note you can't just run git diff myfile.txt you need to run git difftool myfile.txt

# Use rsync to share folder between Mac and ubuntu
From remote to local computer

      rsync --progress --partial -avz user@remote.server:/folder/to/copy/ /local/folder
      
If you want to copy specific files, include it in the path.

      rsync --progress --partial -v /path/to/file/file.ext user@remote.server:/remote/folder/

From local to remote computer

      rsync --progress --partial -avz /folder/to/copy/ user@remote.server:/remote/folder

This will copy all files in /folder/to/copy/ to /remote/folder in the remote server, the folder copy itself will not be created in the remote computer, and only its contents will be copied, if you want the folder itself to also be created and then its contents copied inside the newly created copy folder, use this command.

      rsync --progress --partial -avz /folder/to/copy user@remote.server:/remote/folder
      
# Config VNC server on 14.04
https://www.vultr.com/docs/how-to-install-vnc-desktop-on-ubuntu-14-04
Note: replace tightvncserver with vnc4server! Since tightvncserver doesn't support opengl which needs by opencv.

Start vncserver:

      vncserver :1 -geometry 1440x900 -depth 16 -pixelformat rgb565

# Command to view user of PID

      ps -u -p 1234
      
# Backup partition and restore
1) make a usb boot system

copy all files from ubuntu iso to a usb disk.

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

