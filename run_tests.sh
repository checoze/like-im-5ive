#!/bin/bash

echo "** Running Unit Tests **"


echo "** Explain **"
coverage -e
coverage -x manage.py test explain --settings=settings.test

echo "** WRITING COVERAGE **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt