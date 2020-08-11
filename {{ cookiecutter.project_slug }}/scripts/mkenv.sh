#!/usr/bin/env bash
cd `dirname $(realpath $0)`

function ask_env_vars {
    read -p "TELEGRAM_TOKEN: " $TELEGRAM_TOKEN

    read -p "DEBUG [Y/n]: " $debug_yn
    $DEBUG=True
    if [[ "$debug_yn" == 'n' ]]; then
        $DEBUG=False
    fi
}

function write_dotenv {
    code="\
TELEGRAM_TOKEN=\"$TELEGRAM_TOKEN\"
DEBUG=$DEBUG
"
    echo "$code" > ../.env
}
