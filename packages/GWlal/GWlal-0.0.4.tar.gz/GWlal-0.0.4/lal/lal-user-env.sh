# source this file to access LAL
export LAL_PREFIX
LAL_PREFIX="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers"
export PYTHONPATH
PYTHONPATH=`echo "$PYTHONPATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/python2.7/site-packages:||g;'`
PYTHONPATH="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/python2.7/site-packages:$PYTHONPATH"
export MANPATH
MANPATH=`echo "$MANPATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/man:||g;'`
MANPATH="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/man:$MANPATH"
export LAL_DATADIR
LAL_DATADIR="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/lal"
export PATH
PATH=`echo "$PATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/bin:||g;'`
PATH="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/bin:$PATH"
export PKG_CONFIG_PATH
PKG_CONFIG_PATH=`echo "$PKG_CONFIG_PATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/pkgconfig:||g;'`
PKG_CONFIG_PATH="//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/pkgconfig:$PKG_CONFIG_PATH"
