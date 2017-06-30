#!/bin/sh

if ! [ -x "${HOME}/.albiononline/launcher/Albion-Online" ]; then
  mkdir -p "${HOME}/.albiononline"
  cp -r /app/extra/data/launcher "${HOME}/.albiononline/"
fi
cd "${HOME}/.albiononline/"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${HOME}/.albiononline/launcher"
export LD_PRELOAD="/app/libexec/do_not_load_bad_sdl.so"
exec "${HOME}/.albiononline/launcher/Albion-Online"
