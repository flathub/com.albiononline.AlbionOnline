#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <string.h>

static char const* path = "Plugins/x86_64/libSDL2-2.0.so.0";

void *dlopen(const char *filename, int flags) {
  static void* (*orig)(const char *, int) = NULL;
  if (!orig) {
    orig = dlsym(RTLD_NEXT, "dlopen");
  }
  if (filename) {
    char const* found = strstr(filename, path);
    if (found) {
      if (0 == strcmp(found, path)) {
        return NULL;
      }
    }
  }
  return (*orig)(filename, flags);
}
