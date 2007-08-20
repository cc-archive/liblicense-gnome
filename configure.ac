# -*- Autoconf -*-
# Creative Commons has made the contents of this file
# available under a CC-GNU-LGPL license:
#
# http://creativecommons.org/licenses/LGPL/2.1/
#
# A copy of the full license can be found as part of this
# distribution in the file COPYING.
# 
# You may use the liblicense software in accordance with the
# terms of that license. You agree that you are solely 
# responsible for your use of the liblicense software and you
# represent and warrant to Creative Commons that your use
# of the liblicense software will comply with the CC-GNU-LGPL.
#
# Copyright 2007, Creative Commons, www.creativecommons.org.
# Copyright 2007, Jason Kivlighn.
# Process this file with autoconf to produce a configure script.
# This file is part of Liblicense.

AC_PREREQ(2.57)
AC_INIT([liblicense-gnome],[0.4],[cc-devel@lists.ibiblio.org])
AM_INIT_AUTOMAKE([dist-bzip2])

# Checks for programs.
AC_PROG_INSTALL
AC_PROG_MAKE_SET
PKG_PROG_PKG_CONFIG

AM_CHECK_PYTHON_HEADERS

##################################################################
# check for liblicense
##################################################################

LIBLICENSE_REQUIRED=0.4

PKG_CHECK_MODULES(LIBLICENSE,[
	liblicense >= $LIBLICENSE_REQUIRED],,)

LICENSE_ICON_DIR=`$PKG_CONFIG --variable=icondir liblicense`
AC_SUBST(LICENSE_ICON_DIR)

##################################################################
# check for pygtk
##################################################################

PYGTK_REQUIRED=2.10

PKG_CHECK_MODULES(PYGTK,[
	pygtk-2.0 >= $PYGTK_REQUIRED],
	[have_pygtk=yes] , [have_pygtk=no])
AC_SUBST(PYGTK_CFLAGS)
AC_SUBST(PYGTK_LIBS)

##################################################################
# check for nautilus-python
##################################################################

NP_REQUIRED=0.4.3

AC_ARG_ENABLE(nautilus, AC_HELP_STRING([--disable-nautilus], [Disable nautilus python extensions.]),[enable_np=$enableval],[enable_np=yes])
if test "x$enable_np" = "xyes"; then
	PKG_CHECK_MODULES(NP,[
		nautilus-python >= $NP_REQUIRED],
		[have_np=yes] , [have_np=no])
	AC_SUBST(NP_CFLAGS)
	AC_SUBST(NP_LIBS)
else
	have_np="no (disabled)"
fi

AM_CONDITIONAL(HAVE_NP, test "$have_np" = "yes")
test "$have_np" = "yes" && AC_DEFINE(HAVE_NP, [], [Define if we have nautilus-python])

AC_CONFIG_FILES([
	Makefile
	src/Makefile
	src/default-content-license
	src/gui_gtk.py
])

AC_OUTPUT
