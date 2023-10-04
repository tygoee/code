#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <package-name>"
    exit 1
fi

# Make a temp dir and cd there
package_name="$1"

if [ ! -d .temp/ ]; then
    mkdir .temp/
fi

cd .temp/

# Download package and all dependencies
apt download $package_name
dependencies=$(apt-cache depends -i "$package_name" | grep "Depends:" | awk '{print 2}')

for dependency in $dependencies; do
    apt download "$dependency"
done

# Install all of them in safeinstall/
cd ..
for deb_file in .temp/*.deb; do
    dpkg -x "$deb_file" "./safeinstall"
    deb_file=$(echo "$deb_file" | sed 's:.*/::')
    echo "Installed $deb_file"
done

# Remove the temp dir
rm -r .temp/
