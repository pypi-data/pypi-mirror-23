# source this file to access LAL
if ( ! ${?LAL_PREFIX} ) setenv LAL_PREFIX
setenv LAL_PREFIX "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers"
if ( ! ${?PYTHONPATH} ) setenv PYTHONPATH
setenv PYTHONPATH `echo "$PYTHONPATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/python2.7/site-packages:||g;'`
setenv PYTHONPATH "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/python2.7/site-packages:$PYTHONPATH"
if ( ! ${?MANPATH} ) setenv MANPATH
setenv MANPATH `echo "$MANPATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/man:||g;'`
setenv MANPATH "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/man:$MANPATH"
if ( ! ${?LAL_DATADIR} ) setenv LAL_DATADIR
setenv LAL_DATADIR "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/share/lal"
if ( ! ${?PATH} ) setenv PATH
setenv PATH `echo "$PATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/bin:||g;'`
setenv PATH "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/bin:$PATH"
if ( ! ${?PKG_CONFIG_PATH} ) setenv PKG_CONFIG_PATH
setenv PKG_CONFIG_PATH `echo "$PKG_CONFIG_PATH" | /bin/sed -e 's|//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/pkgconfig:||g;'`
setenv PKG_CONFIG_PATH "//home/daniel/.virtualenvs/IGRlaptop21/test-lalinstallers/lib/pkgconfig:$PKG_CONFIG_PATH"
