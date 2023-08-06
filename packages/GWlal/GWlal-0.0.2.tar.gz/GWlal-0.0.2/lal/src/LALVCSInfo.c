/*
 * Copyright (C) 2014, 2016 Karl Wette
 * Copyright (C) 2009-2013 Adam Mercer
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or (at
 * your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with with program; see the file COPYING. If not, write to the
 * Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
 * MA 02111-1307 USA
 */

/*
 * LALVCSInfo.c - LAL VCS Information
 */

#include <stdlib.h>
#include <config.h>

#include <lal/LALVCSInfoType.h>

#if defined(HAVE_LIBLAL)
#include <lal/LALVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALFRAME)
#include <lal/LALFrameVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALMETAIO)
#include <lal/LALMetaIOVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALXML)
#include <lal/LALXMLVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALSIMULATION)
#include <lal/LALSimulationVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALBURST)
#include <lal/LALBurstVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALDETCHAR)
#include <lal/LALDetCharVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALINSPIRAL)
#include <lal/LALInspiralVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALPULSAR)
#include <lal/LALPulsarVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALINFERENCE)
#include <lal/LALInferenceVCSInfoHeader.h>
#endif
#if defined(HAVE_LIBLALSTOCHASTIC)
#include <lal/LALStochasticVCSInfoHeader.h>
#endif

#include "LALVCSInfoHeader.h"
#include "LALBuildInfoHeader.h"

/* VCS and build information */
const LALVCSInfo lalVCSInfo = {
  .name = "LAL",
  .version = LAL_VERSION,
  .vcsId = LAL_VCS_ID,
  .vcsDate = LAL_VCS_DATE,
  .vcsBranch = LAL_VCS_BRANCH,
  .vcsTag = LAL_VCS_TAG,
  .vcsAuthor = LAL_VCS_AUTHOR,
  .vcsCommitter = LAL_VCS_COMMITTER,
  .vcsClean = LAL_VCS_CLEAN,
  .vcsStatus = LAL_VCS_STATUS,
  .configureArgs = LAL_CONFIGURE_ARGS,
  .configureDate = LAL_CONFIGURE_DATE,
  .buildDate = LAL_BUILD_DATE,
};

/* Identable VCS and build information */
const LALVCSInfo lalVCSIdentInfo = {
  .name = "$LALName: " "LAL" " $",
  .version = "$LALVersion: " LAL_VERSION " $",
  .vcsId = "$LALVCSId: " LAL_VCS_ID " $",
  .vcsDate = "$LALVCSDate: " LAL_VCS_DATE " $",
  .vcsBranch = "$LALVCSBranch: " LAL_VCS_BRANCH " $",
  .vcsTag = "$LALVCSTag: " LAL_VCS_TAG " $",
  .vcsAuthor = "$LALVCSAuthor: " LAL_VCS_AUTHOR " $",
  .vcsCommitter = "$LALVCSCommitter: " LAL_VCS_COMMITTER " $",
  .vcsClean = "$LALVCSClean: " LAL_VCS_CLEAN " $",
  .vcsStatus = "$LALVCSStatus: " LAL_VCS_STATUS " $",
  .configureArgs = "$LALConfigureArgs: " LAL_CONFIGURE_ARGS " $",
  .configureDate = "$LALConfigureDate: " LAL_CONFIGURE_DATE " $",
  .buildDate = "$LALBuildDate: " LAL_BUILD_DATE " $",
};

/* NULL-terminated list of library and dependencies VCS and build information */
const LALVCSInfoList lalVCSInfoList = {
#if defined(HAVE_LIBLAL)
  &lalVCSInfo,
#endif
#if defined(HAVE_LIBLALFRAME)
  &lalFrameVCSInfo,
#endif
#if defined(HAVE_LIBLALMETAIO)
  &lalMetaIOVCSInfo,
#endif
#if defined(HAVE_LIBLALXML)
  &lalXMLVCSInfo,
#endif
#if defined(HAVE_LIBLALSIMULATION)
  &lalSimulationVCSInfo,
#endif
#if defined(HAVE_LIBLALBURST)
  &lalBurstVCSInfo,
#endif
#if defined(HAVE_LIBLALDETCHAR)
  &lalDetCharVCSInfo,
#endif
#if defined(HAVE_LIBLALINSPIRAL)
  &lalInspiralVCSInfo,
#endif
#if defined(HAVE_LIBLALPULSAR)
  &lalPulsarVCSInfo,
#endif
#if defined(HAVE_LIBLALINFERENCE)
  &lalInferenceVCSInfo,
#endif
#if defined(HAVE_LIBLALSTOCHASTIC)
  &lalStochasticVCSInfo,
#endif
  &lalVCSInfo,
  NULL
};

/*
 * VCS header/library mismatch link check function:
 * This function will successfully link only if the link check functions defined
 * in the included LAL VCS info headers (e.g. LAL_VCS_LINK_CHECK() defined in
 * <lal/LALVCSInfoHeader.h>) are present in the LAL libraries being linked
 * against. A successful link ensures that the LAL headers included by this
 * library are consistent with the LAL libraries linked against by this library.
 */
void LAL_VCS_LINK_CHECK(void)
{
#if LAL_VERSION_DEVEL != 0
#if defined(HAVE_LIBLAL) && LAL_VERSION_DEVEL != 0
  LAL_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALFRAME) && LALFRAME_VERSION_DEVEL != 0
  LALFRAME_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALMETAIO) && LALMETAIO_VERSION_DEVEL != 0
  LALMETAIO_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALXML) && LALXML_VERSION_DEVEL != 0
  LALXML_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALSIMULATION) && LALSIMULATION_VERSION_DEVEL != 0
  LALSIMULATION_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALBURST) && LALBURST_VERSION_DEVEL != 0
  LALBURST_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALDETCHAR) && LALDETCHAR_VERSION_DEVEL != 0
  LALDETCHAR_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALINSPIRAL) && LALINSPIRAL_VERSION_DEVEL != 0
  LALINSPIRAL_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALPULSAR) && LALPULSAR_VERSION_DEVEL != 0
  LALPULSAR_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALINFERENCE) && LALINFERENCE_VERSION_DEVEL != 0
  LALINFERENCE_VCS_LINK_CHECK();
#endif
#if defined(HAVE_LIBLALSTOCHASTIC) && LALSTOCHASTIC_VERSION_DEVEL != 0
  LALSTOCHASTIC_VCS_LINK_CHECK();
#endif
#endif
}
