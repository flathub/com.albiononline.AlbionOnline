#!/bin/sh

set -e

if ! [ -f "${HOME}/.albiononline/launcher/version.txt" ]; then
    mkdir -p "${HOME}/.albiononline"
    cp -r /app/extra/launcher "${HOME}/.albiononline/"
fi

cd "${HOME}/.albiononline"

installed_version="$(cat launcher/version.txt 2>/dev/null | sed -n '/^launcher-linux-full-\(.*\)\r/{;s//\1/;p;q;}')"

IFS=';' read -a uriver <<<"$(get_albion_online_download_uri)"
version=${uriver[1]}
uri=${uriver[0]}

if [ "${version}" != "${installed_version}" ]; then
    curl "${uri}" -o albion-online-setup --stderr - | zenity --progress --text="Downloading update" --pulsate --no-cancel --auto-close
    /app/bin/splitelf albion-online-setup albion-online-setup.zip
    rm -rf data
    unzip albion-online-setup.zip 'data/launcher/*'
    rm -rf launcher
    mv data/launcher .
    rm -rf data
    rm albion-online-setup
    rm albion-online-setup.zip
fi

export LD_PRELOAD="${HOME}/.albiononline/game_x64/Albion-Online_Data/Plugins/x86_64/libSDL2-2.0.so.0"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${HOME}/.albiononline/launcher"
exec "${HOME}/.albiononline/launcher/Albion-Online"
