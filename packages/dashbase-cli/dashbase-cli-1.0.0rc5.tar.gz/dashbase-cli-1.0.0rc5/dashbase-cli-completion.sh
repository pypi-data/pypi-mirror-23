#!/bin/bash
echo 'eval "$(_DASHBASE_CLI_COMPLETE=source dashbase-cli)"' >> ~/.bashrc
eval "$(_DASHBASE_CLI_COMPLETE=source dashbase-cli)"
echo 'eval "$(_DASH_COMPLETE=source dash)"' >> ~/.bashrc
eval "$(_DASH_COMPLETE=source dash)"
echo 'eval "$(_LOGTAIL_COMPLETE=source logtail)"' >> ~/.bashrc
eval "$(_LOGTAIL_COMPLETE=source logtail)"
