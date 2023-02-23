#!/bin/zsh

DIR=$(cd `dirname $0` && pwd)

function bold()
{
    echo -e "\033[1m${1}\033[22m"
}

function dim()
{
    echo -e "\033[2m${1}\033[22m"
}

function italic()
{
    echo -e "\033[3m${1}\033[23m"
}

function underline()
{
    echo -e "\033[4m${1}\033[24m"
}

function red()
{
    echo -e "\033[31m${1}\033[39m"
}

function green()
{
    echo -e "\033[32m${1}\033[39m"
}

function yellow()
{
    echo -e "\033[33m${1}\033[39m"
}

function blue()
{
    echo -e "\033[35m${1}\033[39m"
}

function purple()
{
    echo -e "\033[35m${1}\033[39m"
}

function aqua()
{
    echo -e "\033[36m${1}\033[39m"
}

function brightred()
{
    echo -e "\033[91m${1}\033[39m"
}


function log()
{
  green "${1}"
}

function error()
{
  red "error: ${1}"
  exit 2
}

function is_ok()
{
  rc=$1
  if [ ${rc} -ne 0 ]; then
    error "${3}"
  else
    if [[ -n "${2}" ]];then
        log "${2}"
    fi
  fi
}