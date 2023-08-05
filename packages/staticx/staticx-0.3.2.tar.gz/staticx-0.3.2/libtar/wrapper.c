/*
**  Copyright 1998-2003 University of Illinois Board of Trustees
**  Copyright 1998-2003 Mark D. Roth
**  All rights reserved.
**
**  wrapper.c - libtar high-level wrapper code
**
**  Mark D. Roth <roth@uiuc.edu>
**  Campus Information Technologies and Educational Services
**  University of Illinois at Urbana-Champaign
*/

#include <stdio.h>
#include <sys/param.h>
#include <dirent.h>
#include <errno.h>
#include <string.h>
#include <fnmatch.h>
#include "libtar.h"
#include "compat.h"


int
tar_extract_glob(TAR *t, char *globname, char *prefix)
{
	char *filename;
	char buf[MAXPATHLEN];
	int i;

	while ((i = th_read(t)) == 0)
	{
		filename = th_get_pathname(t);
		if (fnmatch(globname, filename, FNM_PATHNAME | FNM_PERIOD))
		{
			if (TH_ISREG(t) && tar_skip_regfile(t))
				return -1;
			continue;
		}
		if (t->options & TAR_VERBOSE)
			th_print_long_ls(t);
		if (prefix != NULL)
			snprintf(buf, sizeof(buf), "%s/%s", prefix, filename);
		else
			strlcpy(buf, filename, sizeof(buf));
		if (tar_extract_file(t, buf) != 0)
			return -1;
	}

	return (i == 1 ? 0 : -1);
}


int
tar_extract_all(TAR *t, char *prefix)
{
	char *filename;
	char buf[MAXPATHLEN];
	int i;

#ifdef DEBUG
	printf("==> tar_extract_all(TAR *t, \"%s\")\n",
	       (prefix ? prefix : "(null)"));
#endif

	while ((i = th_read(t)) == 0)
	{
#ifdef DEBUG
		puts("    tar_extract_all(): calling th_get_pathname()");
#endif
		filename = th_get_pathname(t);
		if (t->options & TAR_VERBOSE)
			th_print_long_ls(t);
		if (prefix != NULL)
			snprintf(buf, sizeof(buf), "%s/%s", prefix, filename);
		else
			strlcpy(buf, filename, sizeof(buf));
#ifdef DEBUG
		printf("    tar_extract_all(): calling tar_extract_file(t, "
		       "\"%s\")\n", buf);
#endif
		if (tar_extract_file(t, buf) != 0)
			return -1;
	}

	return (i == 1 ? 0 : -1);
}


int
tar_append_tree(TAR *t, char *realdir, char *savedir)
{
	char realpath[MAXPATHLEN];
	char savepath[MAXPATHLEN];
	struct dirent *dent;
	DIR *dp;
	struct stat s;

#ifdef DEBUG
	printf("==> tar_append_tree(0x%p, \"%s\", \"%s\")\n",
	       t, realdir, (savedir ? savedir : "[NULL]"));
#endif

	if (tar_append_file(t, realdir, savedir) != 0)
		return -1;

#ifdef DEBUG
	puts("    tar_append_tree(): done with tar_append_file()...");
#endif

	dp = opendir(realdir);
	if (dp == NULL)
	{
		if (errno == ENOTDIR)
			return 0;
		return -1;
	}
	while ((dent = readdir(dp)) != NULL)
	{
		if (strcmp(dent->d_name, ".") == 0 ||
		    strcmp(dent->d_name, "..") == 0)
			continue;

		snprintf(realpath, MAXPATHLEN, "%s/%s", realdir,
			 dent->d_name);
		if (savedir)
			snprintf(savepath, MAXPATHLEN, "%s/%s", savedir,
				 dent->d_name);

		if (lstat(realpath, &s) != 0)
			return -1;

		if (S_ISDIR(s.st_mode))
		{
			if (tar_append_tree(t, realpath,
					    (savedir ? savepath : NULL)) != 0)
				return -1;
			continue;
		}

		if (tar_append_file(t, realpath,
				    (savedir ? savepath : NULL)) != 0)
			return -1;
	}

	closedir(dp);

	return 0;
}


