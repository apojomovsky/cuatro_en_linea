#!/usr/bin/env bash
PYTHONPATH=$PYTHONPATH:.:./ python -m unittest discover -s ./tests -p 'test_*.py'
