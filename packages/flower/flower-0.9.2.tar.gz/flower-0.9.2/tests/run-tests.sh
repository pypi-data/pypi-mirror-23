#!/bin/bash
set -e

if [ $TEST_SUITE == 'unit' ] then
    ./run-unit-tests.sh
else
    ./run-integration-tests.sh
fi
