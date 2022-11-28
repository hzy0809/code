#!/bin/bash
nohup jupyter lab --allow-root --notebook-dir='.'> jupyterlab.log 2>&1 &
