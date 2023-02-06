#!/bin/bash

LOGFILE=log.txt

PREFIX="python pychatgpt.py --token"
COMMANDS_LIST=()

for file in ./tokens/*; do
  #echo "${file##*/}"
  COMMANDS_LIST+=("$PREFIX ${file##*/}")
done

printf '%s\n' "${COMMANDS_LIST[@]}"

change=`cat ./change_token`

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

writelog "Starting"

while true ; do
  for i in "${!COMMANDS_LIST[@]}"; do
    if [ "$change" = "True" ]; then
        echo "Change to the next token ..."
        sed -i 's/True/False/g' change_token
    fi
    ${COMMANDS_LIST[$i]}
  done

  writelog "Exited with status $?"
  writelog "Restarting"
done
