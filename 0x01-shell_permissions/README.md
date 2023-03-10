"su betty" to switch user to betty user
"whoami" to view the name of a user
"groups" to view the groups of a user
"chown betty hello" to change the hello file to user betty
"touch hello" to create a new file called hello
"chmod u+x hello"used to add execution to the file hello
"chmod ug+x,o+r" adding execute permission to user,group and read to other user of a file
"chmod ugo+x" adding execute permission to all handlers of the file hello
"chmod 007 hello" given all permissions to others in file hello
"chmod 753 hello" given users all permmissions groups permission to read execute while other permission to write and execute
"chmod --reference=hello elloh" to give elloh the file permission hello
"chmod -R +x */" execute to all directories in a sub directories
"mkdir -m 751 my_dir" to make a folder with permission to 751
