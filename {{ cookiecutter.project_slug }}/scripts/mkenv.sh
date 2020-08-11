#!/usr/bin/env bash
cd `dirname $(realpath $0)`

read -p "TELEGRAM_TOKEN: " $TELEGRAM_TOKEN

read -p "DEBUG [Y/n]: " $debug_yn
$DEBUG=True
if [[ "$debug_yn" == 'n' ]]; then
    $DEBUG=False
fi


code="\
TELEGRAM_TOKEN=\"$TELEGRAM_TOKEN\"
DEBUG=$DEBUG
"
echo "$code" > ../.env
