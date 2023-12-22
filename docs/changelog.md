**Sprint 5**: 12 Dec 2023 - 22 Dec 2023:
- implemented a slice: "User can evaluate objectives"
    - this introducted the Evaluate View
- implemented a slice: "User can archive Learning Journeys"
- refactored UI: moved common view methods to a view template
- finished re-formatting docstring to Google format, removed unnecessary blahblahblah from /src
- broke, fixed and added some unit tests
- performed final system tests manually
- added proper validation to user input
- started migrating the UI from 'pack' geometry manager to 'grid' manager -> deemed not in line with development goals -> aborted

**Sprint 4**: 5 Dec 2023 - 12 Dec 2023:
- implemented a slice: "User can delete objectives"
- implemented a slice: "User can rename objectives"
    - this introduced the Rename Objective View
- other changes: updated architecture description, added user guide, began rewriting docstrings to Google style
- NOTE: started to notice redundancy and need for intermediate refactoring - skipping it might slow down development soon -> this got taken care of in Sprint 5

**Sprint 3**: 28 Nov 2023 - 5 Dec 2023:
- deemed the current User Path hostile for all humans and scrapped it
- re-invented the wheel with a view-based UI:
    - Home View: user can manage their Learning Journeys
    - Manage View: user can manage the selected Learning Journey
- implemented a slice: "User can view a Learning Journey's objectives"
- added a sequence diagram of adding a new objective ; this demonstrates the new UX flow
- other changes: routine refactoring and cleaning, started releases (latest v0.2.0)

**Sprint 2**: 21 Nov 2023 - 28 Nov 2023:
- sketched the first steps of the User Path to create a human-friendly UX flow
- created the second vertical slice: "User can add Objectives to a Learning Journey"
- the above slice brought some additional classes with it: Objective, ObjectiveRepository and ObjectiveService
- added a description of the current state of architecture in the form of a package diagram
- other changes: added pylint and autopep8 for code quality

**Sprint 1**: 14 Nov 2023 - 21 Nov 2023:
- layed foundation for a Repository Pattern architecture with the following classes:
    - entities: LearningJourney
    - repositories: LearningJourneyRepository
    - services: LearningJourneyService
    - ui: UI
- created the first vertical slice: "User can start a Learning Journey"
- added unit tests for "User can start a Learning Journey"
- other changes: initialized Poetry and sqlite3, added coverage reporting, Invoke tasks and changelog

**Sprint 0**: 31 Oct 2023 - 14 Nov 2023
- initial documentation (software requirements specification, README, time log)