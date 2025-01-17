# Different platforms have different names for the systemwide bashrc
if [[ -f /etc/bashrc ]]; then
  source /etc/bashrc
fi
if [[ -f /etc/bash.bashrc ]]; then
  source /etc/bash.bashrc
fi
if [[ -f ~/.bashrc ]]; then
  source ~/.bashrc
fi

# Reset PS1 so pexpect can find it
PS1="$"

# Unset PROMPT_COMMAND, so that it can't change PS1 to something unexpected.
unset PROMPT_COMMAND

bind 'set enable-bracketed-paste off'
