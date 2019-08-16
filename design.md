# Design Doc for rework of Count-Count

## Purpose

Finding statistics about users and servers.

### Intended Audience

Discord Users, Idiots.

### Scope

Gathering data about users and servers. Then being able to display
this in a nice format to the users.

## Overview

### Functional Requirements

- count how many messages they have in a server
- get a diagram of how many messages people have in a server
- claim numbers in the global count
- trade numbers
- all server info
- all user info
- repost images that people upload to a server
- user can opt in/out of images being reposted
- configure commands

### Non Functional Requirements

- two threads should not be able to calculate the same thing.

## Implementation

### File Hierarchy

```
start.py
bot.py
commands/
- __init__.py
- fetch.py
- ...
util/
- __init__.py
- paginator.py
- ...
database/
- __init__.py
- ...
```