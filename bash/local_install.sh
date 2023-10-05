#!/bin/bash
shopt -s extglob # cp ./!()

if [ $# -eq 0 ]; then
    echo "Usage: $0 <package-name>"
    exit 1
fi

# Make a temp dir and cd there
package_name="$1"

cd $HOME

mkdir -p .temp/
cd .temp/

# Download package and all dependencies
apt download $package_name
dependencies=$(apt-cache depends -i "$package_name" | grep "Depends:" | awk '{print 2}')

for dependency in $dependencies; do
    apt download "$dependency"
done

# Install all of them in .temp/install/
for deb_file in .temp/*.deb; do
    dpkg -x "$deb_file" "install/"
    deb_file=$(echo "$deb_file" | sed 's:.*/::')

    echo "Installed $deb_file"
done

# Make all needed dirs if they dont exist
mkdir -p $HOME/.local/lib/
mkdir -p $HOME/.local/lib64/
mkdir -p $HOME/.local/lib/x86_64-linux-gnu/

# Cd into .temp/install/ and copy all files
# to their corresponding directories
cd install
cp -r ./!(usr) $HOME/.local/  # > /dev/null
cp -r ./usr/!(local) $HOME/.local  # > /dev/null
cp -r ./usr/local/* $HOME/.local  # > /dev/null

# Remove the temp dir
rm -r .temp/

# Add the library paths to .profile
echo "export LD_LIBRARY_PATH=$HOME/.local/lib:$HOME/.local/lib64:$HOME/.local/lib/x86_64-linux-gnu" >> $HOME/.profile