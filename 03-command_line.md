# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> `pwd` - print working directory  
`cd` - change directory  
`cd ..` - move up one directory  
`mkdir` - make directory  
`touch [filename]` - create file in working directory  
`cp [source] [destination]` - copy files to destination  
`cp * [destination]` - copy all files to destination  
`mv [source] [destination]` - move files to destination  
`mv [filename] [new filename]` - changes name of filename  
`rm [source]` - remove file  
`rm -r [source]` - remove directory & all child directories  
`cat [source]` - outputs content of file in terminal  
`sort [source]` - sorts file in alphabetical order  
`uniq [source]` - filters out adjacent, duplicate lines in a file  
`grep 'text' [source]` - 'Global regular expression print'; searches files for lines that match a pattern and returns the results  
`grep -i 'text' [source]` - same as above but case insensitive  
`grep -R 'text' [source]` - searches all files in directory and outputs filenames and lines containing matched results  
`sed s/'text'/'text'/g` - 'Stream editor'; accepts standard input and modifies it based on an expression. Similar to find and replace. Note: if the 'g' is not included, command will only replace the first instance of "text" on a line  
`>` - takes the standard output of the command on the left, and redirects it to the file on the right  
* Example: `echo 'text' > [destination]`  
* Example: `cat [source] > [destination]`

>> `>>` - takes the standard output of the command on the left and appends (adds) it to the file on the right  
* Example: `cat [source] >> [destination]`

>> `<` - takes the standard input from the file on the right and inputs it into the program on the left  
`|` - takes the standard output of the command on the left, and pipes it as standard input to the command on the right


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - list files/folders in current directory  
`ls -a` - list all contents including hidden files  
`ls -l` - list all contents in long format  
`ls -lh` - list all contents in long format with file sizes in human readable format  
`ls -lah` - list all contents including hidden files in long format with file sizes in human readable format  
`ls -t` - order files & directories by time modified  
`ls -Glp` - list all contents in long format with directories displayed with a `/` & different font color.


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -R` - displays subdirectories  
`ls -1` - displays each entry on a separate line  
`ls -c` - displays files by file timestamp  
`ls -x` - display file as rows across the screen  
`ls -og` - displays contents in long format but excludes group & owner name

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The `xargs` command expects input from stdin and executes the provided command over the input.  
Example: `find . -name "*.md" | xargs grep "xargs"`  
* The example above finds all files with the extension .md in the current directory & looks for the specific keyword in each file using the grep command
