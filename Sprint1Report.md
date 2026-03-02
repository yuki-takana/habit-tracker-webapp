# Sprint 1 Report (2/24/26 - 3/1/2026)

https://youtu.be/KzuMaZWjYDQ 

## What's New (User Facing)
* Feature 1: Added polished user login UI
* Feature 2: Create account (signup) functionality 
* Feature 3: Set up backend app with habit and completion data models
* Feature 4: Basic dashboard showing habits and current streak calculation
* Feature 5: Habit management page where users can add new habits

## Work Summary (Developer Facing)
We built the login and create account feature by implementing the backend logic first, including form handling, credential validation, user creation, and route/view flow, then tested each path to make sure registration, authentication, and error handling were working correctly before touching the visual design. We then expanded into implementing more features, such as the dashboard page to display the habits the user has, as well as a manage habits page for adding habits, where we needed to implement the backend logic as well as create models for managing the habits in the database. The most significant learning for our team was learning how to better split up and divide work so we aren’t overlapping, as we didn’t have a good idea before we started actually working on the project, where we discovered everything that has to be implemented for a feature to work.

## Unfinished Work
While all sprint 1 issues were completed, the following work remains unfinished heading into sprint 2. The UI for the login page is done and polished but the create account (all though working) is not polished and does not match the card style/colors the login has. The manage habits page doesn’t yet display the user’s existing habits or permit editing and deleting them. Additionally, users currently have no way to mark a habit as complete despite the completion model already being in place to support this in sprint 2. Finally, the PostgreSQL database is currently only configured locally, meaning each developer must set it up locally on their machine. Hosting the database remotely is planned for sprint 2 to eliminate this as a setup requirement. 

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/1 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/4 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/5 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/6 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/7 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/9 
* https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/issues/11 

## Incomplete Issues/User Stories
* No incomplete issues for this sprint. All issues opened during Sprint 1 were completed and closed before the sprint deadline.
## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* [login.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/login.html)
* [models.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/models.py)
* [views.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/Backend/views.py )
* [managehabits.html](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/templates/managehabits.html)
* [urls.py](https://github.com/WSU-CPTS322-SP26/HabitTrackerWebApp/blob/main/client/TheDailyNudge/urls.py)

## Retrospective Summary
Here's what went well:
* Making the login page UI fit the app's theme of calm focus as well as getting the login and create account to work. 
* Making sure the core features of the app currently work with a local PostgeSQL database before implementing more features with a remote database.

Here's what we'd like to improve:
* Improve the UI for the create account section.
* Improve the UI for the dashboard and manage habits page.
* Currently there are a few security things hard coded that would have to get changed before making the repo public. Such as in setting.py

Here are changes we plan to implement in the next sprint:
* Security hardcoded passwords turned into templates instead.
* Making sure habits can be edited, such as changing the name/frequency or deleting the habit.
* Implementing a system to display when habits are due and allow users to mark them as complete.
