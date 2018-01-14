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
