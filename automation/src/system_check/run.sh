#!/bin/bash

# script to scrape/parse the report file and
# extract the relevant details and run the
# python script to display the details in a server.

echo "running......"
echo ""

sudo ./lynis audit system --quick

# execute warnings. sudo ./warnings.sh
echo "Generating warnings"
echo ""
echo "warnings are: "
echo ""

sudo cat /var/log/lynis-report.dat | grep warning | sed -e "s/warning\[\]\=//g"
sudo cat /var/log/lynis-report.dat | grep warning | sed -e "s/warning\[\]\=//g" | cat > warnings.txt

echo ""
echo "warnings generated"
echo "output file: warnings.txt"

sudo chmod 755 warnings.txt

#execute suggestions. sudo ./suggestions.sh
echo "Generating suggestions"
echo ""
echo "suggestions are: "
echo ""

sudo cat /var/log/lynis-report.dat | grep suggestion | sed -e "s/suggestion\[\]\=//g"

sudo cat /var/log/lynis-report.dat | grep suggestion | sed -e "s/suggestion\[\]\=//g" | cat > suggestions.txt

echo ""
echo "suggestions generated"
echo "output file: suggestions.txt"

sudo chmod 755 suggestions.txt


# execute packages. sudo ./packages.sh
echo "Generating packages"
echo ""
echo "packages are: "
echo ""

sudo cat /var/log/lynis-report.dat | grep installed_package | sed -e "s/installed_package\[\]\=//g"
sudo cat /var/log/lynis-report.dat | grep installed_package | sed -e "s/installed_package\[\]\=//g" | cat > packages.txt

echo ""
echo "packages generated"
sudo chmod 755 packages.txt


# execute shells. sudo ./shells.sh
echo "Generating avaliable shells"
echo ""
echo "shells are: "
echo ""

sudo cat /var/log/lynis-report.dat | grep available_shell | sed -e "s/available_shell\[\]\=//g"
sudo cat /var/log/lynis-report.dat | grep available_shell | sed -e "s/available_shell\[\]\=//g" | cat > shells.txt

echo ""
echo "shells generated"

echo "output file: shells.txt"

sudo chmod 755 shells.txt
