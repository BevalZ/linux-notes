
  ## <center>Linux notes</center>
  #### archlinux fcitx
  1. ~$:# fcitx
     export GTK_IM_MODULE=fcitx
     export QT_IM_MODULE=fcitx
     export XMODIFIERS="@im=fcitx"
     </a>
  2. ~$: vim ~/.xinitrc
  >export LC_ALL=zh_CN.UTF-8
  export GTK_IM_MODULE=fcitx
  export QT_IM_MODULE=fcitx
  export XMODIFIERS=“@im=fcitx”
  #### ubuntu tips
  1. auto find the best mirror base on your location (deb mirror)
  just add the code below to the top of your /etc/apt/sources
  <br>
  >
  deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted universe multiverse
  deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted universe multiverse
  deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted universe multiverse
  deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted universe multiverse
  2. locale
  > ~$: vim /etc/defalut/locale
  > ~$: locale-gen
  > ~$: locale -a
  > ~$: locale
  > ~$: sudo /usr/share/locales/install-language-pack en_US
  #### enviromental variables
  1. declare (create a  variables )
  > ~$: declare { variables }
  2. set (show all  variables  of current shell)
  > ~$: set
  2. env(show  variables  related to current user)
  > ~$: env
  3. export (export  variables )
  > ~$: export
  4. location to save variables to make them permanent
   /etc/bashrc   
   /etc/profile
   5. **☆**path
   > ~$: echo $path
   > ~$: PATH=$PATH:/home/shiyanlou/mybin (add path)
   > ~$: echo "PATH=$PATH:/home/shiyanlou/mybin" >> .bashrc
  #### search
  1. whereis
  2. locate
  > ~$: locate /etc/sh (find all file or floder start with sh in /etc)
  locate /usr/share/\\*.jpg (find all jpg file in /usr/share)
  3. which
  4. find
  ![](http://i4.buimg.com/567571/133fc05ae2dea9a5.png)
  ![](https://dn-anything-about-doc.qbox.me/linux_base/5-8.png)


  #### system management
  1. chown  
  > ~$: chown owner filename 	(change the owner of file)
  2. file (show the propetry of a file)
  > ~$: file filename
  3. df  
  > ~$: df -h  (check the storage)
  4. dd  
  > ~$: dd if=... (input file is) of=... (output file is) bs=num (block size num+unit{unit：Byte is default ，can be K M G etc} ) count=num（the number of bs）
  #### vim
  1. find && replace
  > :%s/str1/str2/g（equal to :g/str1/s//str2/g） replace all str1 to str2
  #### tmux
  1. install Resurrect          
  > ~$:mkdir ~/.tmux
  > ~$:cd ~/.tmux
  > ~$:git clone https://github.com/tmux-plugins/tmux-resurrect.git
  > ~$:run-shell ~/.tmux/tmux-resurrect/resurrect.tmux
  > ~$:tmux source-file ~/.tmux.conf

  2. install Tmux Continuum
  > ~$:mkdir ~/.tmux
  > ~$:cd ~/.tmux
  > ~$:git clone clone https://github.com/tmux-plugins/tmux-continuum.git
  > ~$:run-shell ~/.tmux/tmux-continuum/continuum.tmux
  > ~$:tmux source-file ~/.tmux.conf

  #### image Tools
  1. jpegoptim (image optimization)
  > jpegoptim file
  2. optipng  (image optimization)
  > optipng -o<0-7> filename #<0-7> is the optimization level

  3. ImageMagick (image tool)

  SYNOPSIS
  >       convert input-file [options] output-file

         command- line.

         convert

                convert between image formats as well as resize an image,  blur,
                crop,  despeckle,  dither,  draw  on, flip, join, re-sample, and
                much more.

         identify

                describes the format and characteristics of one  or  more  image
                files.

         mogrify

                resize  an  image, blur, crop, despeckle, dither, draw on, flip,
                join, re-sample, and much more. Mogrify overwrites the  original
                image file, whereas, convert writes to a different image file.

         composite

                overlaps one image over another.

         montage

                create  a  composite image by combining several separate images.
                The images are tiled on the composite image  optionally  adorned
                with a border, frame, image name, and more.

         compare

                mathematically  and  visually annotate the difference between an
                image and its reconstruction..

         stream

                is a lightweight tool to stream one or more pixel components  of
                the image or portion of the image to your choice of storage for‐
                mats. It writes the pixel components as they are read  from  the
                input image a row at a time making stream desirable when working
                with large images or when you require raw pixel components.

         display

                displays an image or image sequence on any X server.

         animate

                animates an image sequence on any X server.

         import

                saves any visible window on an X server and  outputs  it  as  an
                image  file. You can capture a single window, the entire screen,
                or any rectangular portion of the screen.

         conjure

                interprets and executes scripts written in the Magick  Scripting
                Language (MSL).

  SEE ALSO
         convert(1),  identify(1),  composite(1),  montage(1),  compare(1), dis‐
         play(1), animate(1), import(1), conjure(1), quantize(5), miff(4)

  4. fbida (image viewer)
  > ~$: fbi filename  #view image file in tty
  5. fbgrab (grab image)
  > ~$: fbgrab -h ... -w ... -s ... -f ...
  -f filename -h height -w width -s second
  ####the internet
  1. irssi
  >
  /network add -nick {yournick} Freenode
  /server add -auto -network Freenode irc.freenode.net 6667
  /channel add -auto #channel Freenode password(if the channel require)
  /network add -autosendcmd "/^msg nickserv identify {yourpasswd};wait 2000" freenode
  ####compression and decompression
  1. zip
  > ~$: zip -r (recursion) -x (1-9 compression level ) -q (quite) -e (encryption)-o (output) filename path -x (except) filename
  2. unzip
  > ~$: unzip -q (quit) filename -d (decompression path) path
  > ~$: unzip -l filename (just list the files in the compressed package)
  3. rar
  > ~$: rar a(create) filename path
  > ~$: rar d filename file (delete a file in package)
  > ~$: rar l filename (just list)
  4. unrar
  > ~$: unrar x filename (decompression)
  5. tar
  > ~$: tar -cf filename path (create a package)
  > ~$: tar -czf filename path (create a .tar.gz package)
  > ~$: tar -cjf filename path (create a .tar.bz2 package)
  > ~$: tar -cJf filename path (create a .tar.xz package)
  > ~$: tar -xf filename -C path (decompress file to a specific directory)
  > ~$: tar -tf (view the content of the package)
  >

  ####


  #### others
  1. change default path of terminal
  > ~$: vim ~/.bashrc
  > **add** cd path
  2. git ssh
  > ~$: git config --global user.name "username"
  > ~$: git config --global user.email "user@xx.com"
  > ~$: ssh-keygen -t rsa -C “user@xx.com”
  > ~$: ssh git@github.com
  3. curl
  > ~$: curl -f 'name=@filename' http://img.vim-cn.com/    <br>#upload an image file(or anyother files) to http://img.vim-cn.com
  > ~$: curl -v --data-urlencode 'content@/home/beval/Desktop/filename' -d 'poster=beval' 'syntax=text' http://paste.ubuntu.com/  
> ~$: curl https://api.streamable.com/upload/ -u username:password -F 'name=@filename'
