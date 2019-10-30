## System hardening and compliance reports using Lynis

###### You must run a Linux/Unix based OS such as Ubuntu, Mac Os or any other Linux distribution.

- Install Lynis on your system by cloning the github repository: https://github.com/CISOfy/lynis

- Install library using the command `sudo pip3 install pandas`, `sudo pip install openpyxl`, `sudo pip install xlsxwriter`.

- Once you have installed Lynis on your system, navigate to the Lynis (which in my case was `/usr/bin`) directory where you will find a bunch of files along with an executable file called Lynis.

- If permission issues arises in the file. Fix it and then proceed.

- Use the bash script (code is given below) to extract relevant information such as warning and suggestions given in the lynis report. create a file called run.sh and copy paste the bash code into that file and type: sudo ./run.sh to run the bash script and make it executable.

- Run the Python script (code is given below) to clean and parse the extracted data and output the relevant information as an excel file.

- If you want to check system and categorize report in one command, you could add alias in `.zshrc` or `.bashrc`

> PS: python script could be stored in home directory for ease.
