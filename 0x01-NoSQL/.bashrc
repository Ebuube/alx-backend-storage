# MY PERSONAL CONFIGURATION FOR PRODUCTIVITY
# - ONWUTA EBUBE GIDEON -

# Aliases

alias x='chmod +x'	# Grant executable permission to file[s]
alias z='ls -l'	# Long format listing of files in directory
alias s='git status'	# Status of git branch
alias a='git add'	# Stage files
alias d='git pull'	# Pull changes form upstream
alias ci='git commit -m'	# Commit changes to local branch
alias c='git checkout'	# Checkout a branch
alias p='git push'	# Push to an upstream branch
alias compile='gcc -Wall -Werror -Wextra -pedantic -std=gnu89'	# Compile C code
alias compiledbg='gcc -Wall -Werror -Wextra -pedantic -std=gnu89 -ggdb3'	# Compile with debug build

# Run valgrind on compiled C code. Compile the source code with '-gddb3' debug build. Output is saved in a file '~/valgrind-out.txt'
alias leakcheck='valgrind \
	--leak-check=full \
	--show-leak-kinds=all \
	--track-origins=yes \
	--log-file="leackcheck-out.txt"'

alias g='git log --oneline --graph'	# see a graphical repr of a git log
alias b='git branch'	# Create a branch or list branches
alias e='aspell check -l en'	# Run spelling check on an english text
