PS1="[\u@\h:\W]\$ "
PROMPT_COMMAND='\
echo -ne "\033]0;YOUR_TITLE_HERE\007";\
echo -ne "\033]1;YOUR_MINIMIZED_TITLE_HERE\007"
