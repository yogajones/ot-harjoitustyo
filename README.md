This is an intermediate studies project for the Software Development Methods (5 ECTS) course in the Department of Computer Science in University of Helsinki.

# Personal Learning Objective Manager

The purpose of this offline desktop app is to help lifelong learners manage their learning objectives. Take a look at the [Software Requirements Specification](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/software_requirements_specification.md) for a detailed description of features.

Latest release: [v1.0.0](https://github.com/yogajones/ot-harjoitustyo/releases/tag/v1.0.0)

## Documentation:
- [User guide](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/user_guide.md)
- [Software Requirements Specification (SRS)](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/software_requirements_specification.md)
- [Architecture description](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/architecture.md)
- [Changelog](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/changelog.md)
- [Time log](https://github.com/yogajones/ot-harjoitustyo/blob/main/docs/time_log.md)

## How to run the app as a user

Pre-requisites: the app has been tested on Cubbli Linux (Ubuntu-based distro of University of Helsinki), using Python 3.10.

1. Clone the project repository to your computer:

```bash
git clone git@github.com:yogajones/ot-harjoitustyo.git
```

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Initialize the database:
```bash
poetry run invoke build
```

4. Start the application:

```bash
poetry run invoke start
```

## How to generate a test coverage report

The following command will run tests, generate a test coverage report and open it in your default browser:

```bash
poetry run invoke coverage-report
```
