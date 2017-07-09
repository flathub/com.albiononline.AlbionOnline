#!/bin/sh

available_version="$(cat /app/extra/data/launcher/version.txt)"
home_version="$(cat "${HOME}/.albiononline/launcher/version.txt" 2>/dev/null)"
if [ "${home_version}" != "${available_version}" ]; then
    mkdir -p "${HOME}/.albiononline"
    rm -rf "${HOME}/.albiononline/launcher"
    cp -r /app/extra/data/launcher "${HOME}/.albiononline/"
fi
cd "${HOME}/.albiononline/"
export LD_PRELOAD="${HOME}/.albiononline/game_x64/Albion-Online_Data/Plugins/x86_64/libSDL2-2.0.so.0"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${HOME}/.albiononline/launcher"
exec "${HOME}/.albiononline/launcher/Albion-Online"
