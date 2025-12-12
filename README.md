### Hexlet tests and linter status:
[![Actions Status](https://github.com/andrewsaltanov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/andrewsaltanov/python-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=andrewsaltanov_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=andrewsaltanov_python-project-49)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg)](https://sonarcloud.io/summary/new_code?id=andrewsaltanov_python-project-49)

# Brain Games

**Brain Games** is a collection of five console-based math games designed to train your brain, similar to popular mobile brain-training apps.

Each game asks questions that you need to answer correctly.  
After three correct answers in a row, the game is considered won.  
Any wrong answer ends the game and invites you to try again.


| Game | Description | Launch Command |
| :--- | :--- | :--- |
| **Greeting game** | Welcome message and prompt name. | `brain-games` |
| **Even game** | Answer `yes` if the number is even, otherwise `no`. | `brain-even` |
| **Calculator game** | Evaluate the result of a random expression. | `brain-calc` |
| **GCD game** | Find the greatest common divisor of two numbers. | `brain-gcd` |
| **Progression game** | Find the missing number in an arithmetic progression. | `brain-progression` |
| **Prime game** | Answer `yes` if the number is prime, otherwise `no`. | `brain-prime` |
------------


### Requirements

`Python 3.11+`

`uv`

# Installation

1. Clone this repository to your local machine (`git clone https://github.com/andrewsaltanov/python-project-49.git`)
2. Go to the downloaded folder (`cd python-project-49`)
3. Install package `uv sync`
4. Build package `uv build`
5. Install games as console commands `uv tool install --force dist/brain_games-*.whl`


## Demo Game Brain-Even

[![asciicast](https://asciinema.org/a/mT7FsTUBf2onaFdCP0xapQ24I.svg)](https://asciinema.org/a/mT7FsTUBf2onaFdCP0xapQ24I)

## Demo Game Brain-Calc

[![asciicast](https://asciinema.org/a/87oz2b2KWoaTWMsMM3MEuAjyj.svg)](https://asciinema.org/a/87oz2b2KWoaTWMsMM3MEuAjyj)

## Demo Game Brain-Gcd

[![asciicast](https://asciinema.org/a/P8nPFRYHuK7oWPkDOt9WrS02m.svg)](https://asciinema.org/a/P8nPFRYHuK7oWPkDOt9WrS02m)

## Demo Game Brain-Progression

[![asciicast](https://asciinema.org/a/dYpdW9is8cA2dvK309Mqx4M4I.svg)](https://asciinema.org/a/dYpdW9is8cA2dvK309Mqx4M4I)

## Demo Game Brain-Prime

[![asciicast](https://asciinema.org/a/pTIuA8DBr7peBEzJr4XnxXsV2.svg)](https://asciinema.org/a/pTIuA8DBr7peBEzJr4XnxXsV2)