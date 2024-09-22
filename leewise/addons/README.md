[![Build Status](http://runbot.leewise.com/runbot/badge/flat/7/master.svg)](http://runbot.leewise.com/runbot/repo/git-github-com-leewise-enterprise-7)
[![Tech Doc](http://img.shields.io/badge/14.0-docs-875A7B.svg?style=flat)](http://www.leewise.in/documentation/master)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat)](https://www.leewise.in/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/master-nightly-875A7B.svg?style=flat)](http://nightly.leewise.com/)

Leewise
----

Leewise is a suite of web based open source business apps.

The main Leewise Apps include an <a href="https://www.leewise.in/app/crm">Open Source CRM</a>,
<a href="https://www.leewise.in/app/website">Website Builder</a>,
<a href="https://www.leewise.in/app/ecommerce">eCommerce</a>,
<a href="https://www.leewise.in/app/inventory">Warehouse Management</a>,
<a href="https://www.leewise.in/app/project">Project Management</a>,
<a href="https://www.leewise.in/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.leewise.in/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.leewise.in/app/employees">Human Resources</a>,
<a href="https://www.leewise.in/app/lead-automation">Marketing</a>,
<a href="https://www.leewise.in/app/manufacturing">Manufacturing</a>,
<a href="https://www.leewise.in/app/purchase">Purchase Management</a>,
<a href="https://www.leewise.in/">...</a>

Leewise Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.leewise.in">Open Source ERP</a> when you install several Apps.

Getting started with Leewise
-------------------------

For a standard installation please follow the <a href="https://www.leewise.in/documentation/17.0/administration/install/install.html">Setup instructions</a>
from the documentation.

If you are a developer you may type the following command at your terminal:

    wget -O- https://raw.githubusercontent.com/leewise/leewise/master/setup/setup_dev.py | python

Then follow <a href="https://www.leewise.in/documentation/17.0/developer/howtos.html">the developer tutorials</a>

For Leewise employees
------------------

To add the leewise-dev remote use this command:

    $ ./setup/setup_dev.py setup_git_dev

To fetch leewise merge pull requests refs use this command:

    $ ./setup/setup_dev.py setup_git_review
