#!/bin/bash
shopt -s extglob # cp dir/!(...)

# Exit if there are no arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 <package-name|args>"
    exit 1
fi

# Cycle through args
for arg in "$@"; do
    if [ "$arg" = "--help" ]; then
        echo "General usage: $0 <package-name|args>"
        exit 0
    elif [ "$arg" = "--setup" ]; then
        # Create all needed dirs if they dont exist
        mkdir -p "$HOME/.local/lib/"
        mkdir -p "$HOME/.local/lib64/"
        mkdir -p "$HOME/.local/lib/x86_64-linux-gnu/"

        echo "Created library directories..."

        # Add the library path to .profile
        # if --setup is specified
        append_content="$(printf '%s' \
            "export LD_LIBRARY_PATH=" \
            "$HOME/.local/lib:" \
            "$HOME/.local/lib64:" \
            "$HOME/.local/lib/x86_64-linux-gnu")"

        # Append to $HOME/.profile
        # if it isn't already there
        if ! grep -q "$append_content" \
                "$HOME/.profile"; then
            echo "Adding library paths..."
            echo "$append_content" >> "$HOME/.profile"
        else
            echo "Library paths already"\
                 "present, ignoring..."
        fi

        echo "Done."
        exit 0
    fi
done

# Make a temp dir and cd there
package_name="$1"

mkdir -p "$HOME/.temp/"
trap 'rm -r "$HOME"/.temp/' EXIT
cd "$HOME/.temp/" || { echo "Cannot CD into $HOME/.temp, exiting..." && exit 1; }

# Exit if there's no internet connection
if ! ping -c 1 -W 1 "deb.debian.org" > /dev/null 2>&1; then
    echo "You need an active internet connection"
    exit 1
fi

# Download package and all dependencies
apt download "$package_name" || { echo "Error while trying to install package, exiting..." && exit 1; }
dependencies=$(apt-cache depends --recurse -i "$package_name" | grep "Depends:" | awk '{print $2}')

for dependency in $dependencies; do
    apt download "$dependency"
done

# Install all of them in .temp/install/
for deb_file in "$HOME/.temp/"*.deb; do
    dpkg -x "$deb_file" "install/"
    deb_file="${deb_file##*/}"

    echo "Installed $deb_file"
done

# Cd into .temp/install/ and copy all files
# to their corresponding directories
inst_dir="$HOME/.temp/install"

cp -r "$inst_dir"/!(usr) "$HOME/.local/"

if [ -d "$inst_dir/usr/" ]; then
    cp -r "$inst_dir/usr/"!(local) "$HOME/.local/"
fi

if [ -d "$inst_dir/usr/local/" ]; then
    cp -r "$inst_dir/usr/local/"* "$HOME/.local/"
fi
