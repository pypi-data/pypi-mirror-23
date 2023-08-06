# HH Stats

Utility for a collection of a vacancies stats from [hh.ru](https://hh.ru/) service.

## Features

* vacancies loading from:
    * [hh.ru](https://hh.ru/) service API;
    * JSON files;
* collection of vacancies key skills;
* collection for every vacancy key skill:
    * request frequency;
    * median salary:
        * minimal;
        * maximal;
* vacancies search options:
    * area list (allowed values (in JSON format): https://api.hh.ru/areas);
    * specialization list (allowed values (in JSON format): https://api.hh.ru/specializations);
    * additional search query (it supports a query language: https://hh.ru/article/1175);
    * search fields for the search query (allowed values: `name`, `description`);
    * search vacancies only with a salary;
    * begin of the time period for an analysis (in the ISO 8601 or the human-readable format; see below for details);
    * end of the time period for an analysis (in the ISO 8601 or the human-readable format; see below for details);
    * time increment for an iteration over the time period (in the human-readable format; see below for details);
* automatic conversion of a salary currency;
* automatic separation of unseparated skills;
* support of skills aliases (see below for details);
* output of a collected stats:
    * in a format:
        * raw (a vacancy list in a JSON format; see below for details);
        * CSV;
        * SVG;
    * to:
        * specified file;
        * stdout (only for raw and CSV formats);
        * window via [Matplotlib](http://matplotlib.org/) library (only for SVG format);
* support of a specification of a minimal output value of skills requests frequencies;
* automatic adding of an output file extension, depending on a specified format.

## Installation

```
$ pip install hh-stats
```

## Usage

```
$ hh-stats -v | --version
$ hh-stats -h | --help
$ hh-stats [options]
```

Options:

* `-v`, `--version` &mdash; show the version message and exit;
* `-h`, `--help` &mdash; show this help message and exit;
* `-a AREA [AREA...]`, `--areas AREA [AREA...]` &mdash; vacancies areas (allowed values (in JSON format): https://api.hh.ru/areas; default: `['1']`);
* `-s SPECIALIZATION [SPECIALIZATION...]`, `--specializations SPECIALIZATION [SPECIALIZATION...]` &mdash; vacancies specializations (allowed values (in JSON format): https://api.hh.ru/specializations; default: `['1.221']`);
* `-q QUERY`, `--query QUERY` &mdash; the additional search query (it supports a query language: https://hh.ru/article/1175);
* `-p {name,description} [{name,description}...]`, `--query-properties {name,description} [{name,description}...]` &mdash; search fields for the search query (allowed values: `name`, `description`; default: `['name', 'description']`);
* `-r`, `--salary-required` &mdash; search vacancies only with a salary;
* `-b ANALYSIS_BEGIN`, `--analysis-begin ANALYSIS_BEGIN` &mdash; a begin of the analysis time period in the ISO 8601 or the human-readable format (default: `1 month ago`);
* `-e ANALYSIS_END`, `--analysis-end ANALYSIS_END` &mdash; an end of the analysis time period in the ISO 8601 or the human-readable format (default: `now`);
* `-I ANALYSIS_INCREMENT`, `--analysis-increment ANALYSIS_INCREMENT` &mdash; the analysis time increment in the human-readable format (see below for details);
* `-F REQUEST_FREQUENCY`, `--request-frequency REQUEST_FREQUENCY` &mdash; the maximal request frequency (default: 30);
* `-S PAGE_SIZE`, `--page-size PAGE_SIZE` &mdash; the maximal page size (default: 500);
* `-V VALUE_OF_INTEREST`, `--value-of-interest VALUE_OF_INTEREST` &mdash; the minimal value of an interest (default: 5);
* `-E`, `--error-on-limit` &mdash; throw an error on an exceeding of the search limit (2000 vacancies);
* `-D [SKILLS_DELIMITER...]`, `--skills-delimiters [SKILLS_DELIMITER...]` &mdash; delimiters for unseparated skills (default: `[',', ';']`);
* `-A SKILLS_ALIASES`, `--skills-aliases SKILLS_ALIASES` &mdash; the path to a file with skills aliases in a JSON format (see below for details);
* `-O {num,min,max}`, `--order {num,min,max}` &mdash; the order of stats items (default: `num`);
* `-f {raw,csv,svg} [{raw,csv,svg}...]`, `--format {raw,csv,svg} [{raw,csv,svg}...]` &mdash; the output format (default: `['svg']`);
* `-i INPUT [INPUT...]`, `--inputs INPUT [INPUT...]` &mdash; input paths;
* `-o OUTPUT`, `--output OUTPUT` &mdash; the output path.

## Timestamp format

### ISO 8601 format

```
YYYY-MM-DDTHH:MM:SS±HHMM
```

### Human-readable format

```
± <quantity> <unit> <modifier> <reference point>
```

Units: `year`, `month`, `week`, `day`, `hour`, `minute`, `second`.

Modifiers: `from`, `before`, `after`, `ago`, `prior`, `prev`, `last`, `next`, `previous`, `end of`, `this`, `eod`, `eom`, `eoy`.

Reference points: months, weekdays, `yesterday`, `today`, `now`, `tomorrow`, `noon`, `afternoon`, `lunch`, `morning`, `breakfast`, `dinner`, `evening`, `midnight`, `night`, `tonight`.

E.g.:

```
5 minutes from now
5 minutes ago
1 hour from noon
last week
2 weeks from tomorrow
3 hours from next monday
```

See for details: https://github.com/bear/parsedatetime.

## Human-readable time delta format

E.g. `5 d 12 h 23 m 42 s`.

See for details: https://github.com/wroberts/pytimeparse.

## Skills aliases format

Skills aliases format in the JSON Schema format: [docs/skills_aliases.schema.json](docs/skills_aliases.schema.json).

E.g.: [docs/skills_aliases.example.json](docs/skills_aliases.example.json).

## Vacancy list format

Vacancy list format in the JSON Schema format: [docs/vacancy_list.schema.json](docs/vacancy_list.schema.json).

## Screenshots

![Help message, part 1](screenshots/screenshot_00.00.png)

Help message, part 1

![Help message, part 2](screenshots/screenshot_00.01.png)

Help message, part 2

![Vacancies loading, start](screenshots/screenshot_01.00.png)

Vacancies loading, start

![Vacancies loading, end](screenshots/screenshot_01.01.png)

Vacancies loading, end

![Collection of a stats](screenshots/screenshot_01.02.png)

Collection of a stats

![Stats as a bar plot, order by a skill request frequency](screenshots/screenshot_02.00.png)

Stats as a bar plot, order by a skill request frequency

![Stats as a bar plot, order by a minimal median salary](screenshots/screenshot_02.01.png)

Stats as a bar plot, order by a minimal median salary

![Stats as a bar plot, order by a maximal median salary](screenshots/screenshot_02.02.png)

Stats as a bar plot, order by a maximal median salary

## License

The MIT License (MIT)

Copyright &copy; 2017 thewizardplusplus
